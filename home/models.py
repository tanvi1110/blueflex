from django.db import models
from django.db.models.fields import NullBooleanField
from django.template.defaultfilters import default, slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='products' ,on_delete=models.CASCADE)
    
    productimg = models.ImageField(upload_to='image')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    data_added = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=50, default=slugify(title))

    def __str__(self):
        return self.title



    

class Blogs(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=True)
    docimage=models.ImageField(upload_to='image')
    descimage=models.ImageField(upload_to='image')
    desc=models.TextField()
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    # image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=True)
    blog = models.ForeignKey(Blogs,related_name="comments",on_delete=models.CASCADE)

    

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    designation=models.CharField(max_length=50)
    tesimg = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    subject=models.TextField()
    message=models.TextField()

class Events(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=True)
   
    descimage=models.ImageField(upload_to='image',default="")
    descimage2=models.ImageField(upload_to='image',default="")
    descimage3=models.ImageField(upload_to='image',default="")
    

    desc=models.TextField()
    
    def __str__(self):
        return self.title

class CommentEvent(models.Model):
    # image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    desc=models.TextField()
    date=models.DateField(auto_now=False, auto_now_add=True)
    blog = models.ForeignKey(Events,related_name="commentsevents",on_delete=models.CASCADE)
