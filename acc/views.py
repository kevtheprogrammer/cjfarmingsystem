from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import login , logout



from .tokens import email_activation_token
from .models import User
from .userForms import SignUpForm
from acc.userForms import UserEditForm
from farmer.models import FarmPlotModel


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        ctx = {
            'form': self.form_class() ,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False #u need to deactivate account till it is confirmed
            user.save()
            FarmPlotModel.objects.create(name="default",size="1 x 1(acres)",farm_location="default",user=user)
            #send activation email

            this_site = get_current_site(request)
            site = this_site.domain
            subject = 'Activate Your %(site) Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': email_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('We have sent a confirmation link to your email to activate your account\nPlease follow your email and click on the link!'))

            return redirect('account:login')

        return render(request, self.template_name, {'form': form})


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and email_activation_token.check_token(user, token):
            user.is_active = True
            
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, ('Your email has been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')

