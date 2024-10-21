from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('base', views.base, name='base'),
    path('single/<int:id>', views.single, name='single'),
    path('singleblog/<int:id>', views.singleblog, name='singleblog'),
    path('category', views.category, name='category'),
    path('search', views.search, name='search'),
    path('shop', views.shop, name='shop'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('bluefix', views.bluefix, name='bluefix'),
    path('bluescan', views.bluescan, name='bluescan'),
    path('event', views.event, name='event'),
    path('singleevent/<int:id>', views.singleevent, name='singleevent'),
    path('blueflex-endo', views.blueflexEndo, name='blueflex-endo'),



]

