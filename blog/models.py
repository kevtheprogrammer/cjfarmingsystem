from django.db import models
from django.db.models.fields import related
from django.urls import reverse

from acc.models import User

class Category(models.Model):
    title  = models.CharField(max_length=9000)
    slug   = models.SlugField( default=None )
    l_updated   = models.DateField( auto_now=True )

    def __str__(self) -> str:
        return f"{self.title}"

class Article(models.Model):
    thumb  = models.ImageField( upload_to='post/thumb/',default="thumb.jpg" )
    title  = models.CharField( max_length=9000,default=None )
    intro  = models.TextField( default=None,verbose_name="introduction",blank = True)
    body   = models.TextField( default=None,verbose_name="content",blank = True )
    v_link = models.TextField( default=None,verbose_name="video link" , blank = True )
    m_link = models.TextField( default=None,verbose_name="music link", blank = True ) 
    s_link = models.TextField( default=None,verbose_name="social link", blank = True )
    cat    = models.ForeignKey( Category,on_delete=models.CASCADE,default=None,verbose_name="category",related_name="category" )
    author = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="author" )
    upload = models.FileField( upload_to="post/upload/", blank=True )
    active = models.BooleanField(default=False) 
    slug   = models.SlugField( default=None )
    stamp  = models.DateField( auto_now_add=True )
    l_updated   = models.DateField( auto_now=True )
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('blog:post-details', args=[self.pk,self.slug])

    def snip(self):
        return f'{self.intro}'[:180]
    class Meta: 
        ordering = ('-stamp',) 

class Comment(models.Model): 
    post = models.ForeignKey(Article,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name    = models.CharField(max_length=80) 
    email   = models.EmailField() 
    body    = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active  = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 