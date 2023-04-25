from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegisterForm,AuthorRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import ListView
from book.models import Book
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = "/user/login/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
        

class AuthorRegisterView(CreateView):
    model = User
    form_class = AuthorRegistrationForm
    template_name = 'user/author_register.html'
    success_url = "/user/login/"    
    
    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_author:
                return '/user/author/dashboard/'
            else:
                return '/user/user/dashboard'
            
class UserDashboardView(ListView):            
 
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    def get(self, request, *args, **kwargs):
        book = Book.objects.all().values('bookImage','bookName','bookAuthor__authorname','bookPrice','id')
        
        return render(request, 'user/user_dashboard.html',{
            'books':book,
        })
    template_name = 'user/user_dashboard.html'
    
class AuthorDashBoardView(ListView):
    
    model = User
    
    def get(self, request, *args, **kwargs):
        book = Book.objects.all().values('id','bookImage','bookName','bookPrice','bookAuthor__authorname','bookCategory__name','bookQuantity','bookDescription','bookStatus')
        
        return render(request, 'user/author_dashboard.html',{
            'books':book,
        })

    
    template_name = 'user/author_dashboard.html'

class Newarrivals(ListView):            
 
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    def get(self, request, *args, **kwargs):
        book = Book.objects.all().values('bookImage','bookName','bookAuthor__authorname','bookPrice','id')
        
        return render(request, 'user/newarrivals.html',{
            'books':book,
        })
    template_name = 'user/newarrivals.html'

class Bestsellers(ListView):            
 
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    def get(self, request, *args, **kwargs):
        book = Book.objects.filter(bookAuthor__authorname='JK Rowling')
        
        return render(request, 'user/bestsellers.html',{
            'books':book,
        })
    template_name = 'user/bestsellers.html'

class Home(ListView):            
 
    model = User
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        
        return super().get_queryset()
    def get(self, request, *args, **kwargs):
        book = Book.objects.all().values('bookImage','bookName','bookAuthor__authorname','bookPrice','id')
        
        return render(request, 'user/homepage.html',{
            'books':book,
        })
    template_name = 'user/homepage.html'


# class Cart(ListView):
#     def get(self,request,*args,**kwargs):
#         return render(request, 'user/cart.html',{})
#     template_name = 'user/cart.html'

class Checkout(ListView):
    def get(self,request,*args,**kwargs):
        return render(request, 'user/checkout.html',{})
    template_name = 'user/checkout.html'

class Contactus(ListView):
    def get(self,request,*args,**kwargs):
        return render(request, 'user/contactus.html',{})
    template_name = 'user/contactus.html'


# def homepage(request):
#     return render(request, 'user/homepage.html') 

def aboutus(request):
    return render(request, 'user/aboutus.html') 


# def tv(request):
#     return render(request, 'user/user_dashboard/tv.html') 

# def movies(request):
#     return render(request, 'user/user_dashboard/movies.html')

# def celebs(request):
#     return render(request, 'user/user_dashboard/celebs.html')

# def user_dashboard(request):
#     return render(request, 'user/user_dashboard.html')


#cart

@login_required(login_url="/user/login")
def cart_add(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.add(book=book)
    return redirect("user_dashboard")


@login_required(login_url="/user/login")
def item_clear(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.remove(book)
    return redirect("cart")


@login_required(login_url="/user/login")
def item_increment(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.add(book=book)
    return redirect("cart")


@login_required(login_url="/user/login")
def item_decrement(request, id):
    cart = Cart(request)
    book = Book.objects.get(id=id)
    cart.decrement(book=book)
    return redirect("cart")


@login_required(login_url="/user/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/user/login")
def cart_detail(request):
    return render(request, 'user/cart.html')    