from django.contrib import admin

from .models import Category, CommentEvent, Events, Product, Blogs, Comment, Testimonials, Contact 
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Blogs)
admin.site.register(Comment)
admin.site.register(Testimonials)
admin.site.register(Contact)
admin.site.register(Events)
admin.site.register(CommentEvent)
