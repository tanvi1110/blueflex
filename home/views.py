from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import CommentEvent, Events, Product,Category,Contact,Blogs,Comment,Testimonials


# Create your views here.
def index(request):
    testimonials = Testimonials.objects.all()
    category=Category.objects.all().order_by('id')
    allBlog = Blogs.objects.all().order_by('id')[: 3]
    allevent = Events.objects.all().order_by('id')[: 3]
    product=Product.objects.all().order_by('id')
    latestproduct = Product.objects.all().order_by('data_added')[: 3]
    return render(request, 'home/index.html',{'category':category,'product':product,'latestproduct':latestproduct, 'testimonials':testimonials,'allBlog':allBlog,'allevent':allevent})

def blog(request):
    allBlog = Blogs.objects.all().order_by('id')
    return render(request, 'home/blog.html',{'allBlog':allBlog})

def singleblog(request, id):
    try:
        myBlog = Blogs.objects.get(id=id)
        allBlog = Blogs.objects.all().order_by('id')[: 2]
        category=Category.objects.all().order_by('id')
        comment=Comment.objects.all().order_by('id')
        Counter=Comment.objects.all().count()
    except:
        return redirect('/404')

    return render(request, 'home/singleblog.html',{'myBlog': myBlog,'category':category,'comment':comment,'Counter':Counter,'allBlog':allBlog})

def single(request,id):
    try:
        singleproduct = Product.objects.get(id=id)
    except:
        return redirect('/404')

    return render(request, 'home/single.html',{'singleproduct': singleproduct})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def services(request):
    return render(request, 'home/services.html')

def base(request):
    return render(request, 'home/base.html')

# def single(request):
#     return render(request, 'home/single.html')

def blueflexEndo(request):
    return render(request, 'home/blueflex-endo.html')

def category(request):
    return render(request, 'home/category.html')

def shop(request):
    product=Product.objects.all().order_by('id')
    return render(request, 'home/shop.html',{'product':product})



def search(request):
    if request.method == 'GET':
        query = str(request.GET.get('searchbar', 'invalid query'))
        print(query)
        products = Product.objects.filter(Q(title__icontains = query))
        if(products.exists()==False):
            products = Product.objects.all()
    return render(request, 'home/search.html',{'products': products})

def testimonials(request):
    return render(request, 'home/testimonials.html')

def bluefix(request):
    return render(request, 'home/bluefix.html')

def bluescan(request):
    return render(request, 'home/bluescan.html')

def event(request):
    events = Events.objects.all().order_by('id')
    return render(request, 'home/event.html',{'events':events})

def singleevent(request, id):
    try:
        myevent = Events.objects.get(id=id)
        allevent = Events.objects.all().order_by('id')[: 2]
        category=Category.objects.all().order_by('id')
        comment=CommentEvent.objects.all().order_by('id')
        Counter=CommentEvent.objects.all().count()
    except:
        return redirect('/404')

    return render(request, 'home/singleevent.html',{'myevent': myevent,'category':category,'comment':comment,'Counter':Counter,'allevent':allevent})

