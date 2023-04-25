from django.shortcuts import render,redirect
from .models import Book,Category,Author
from django.http import HttpResponse
from .forms import CategoryForm,BookForm,AuthorForm
from django.conf import settings

# Create your views here.

#forbooks

def getAllbooks(request):
    
    #select * from books
    books = Book.objects.all().values('id','bookName','bookPrice','bookAuthor__authorname','bookCategory__name','bookQuantity','bookDescription','bookStatus','bookImage')
    #books = book.objects.all().values_list('pName','pPrice','pQty')
    #books = book.objects.all().values('pName','pPrice','pQty')
    #fetch single object
    #book =book.objects.get(id=1)
    #price greater thn....
    #__ django orm lookups
    #books  = book.objects.filter(pPrice__gte = 800).values()
    #books  = book.objects.filter(pPrice__lte = 800).values()
    #books = book.objects.filter(pName__startswith='i').values()
    #books = book.objects.filter(pName__icontains='P').values()
    #orderby
    #books = book.objects.all().order_by('-pName').values()
    print(books)
    return render(request,'book/allbook.html',{'books':books})

def addbooks(request):
    #add book
    #bookdict ={'pName':'mouse2','pPrice':100,'pQty':10,'pDesc':'mouse for laptop','pStatus':True,'pColor':'black'}
    book = Book(bookName ="mouse pad",bookPrice=100,bookQuantity=10,bookDescription="mouse pad for laptop",bookStatus=True)
    #book = book(bookdict)
    book.save()
    print("Book added")
    return render(request,'book/addbook.html')


def deletebook(request,id):
    #delete book
    #id = 1
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('author_dashboard')
    #return render(request,'book/deletebook.html')
    
def updatebook(request,id):
    #update book
    #id = 1
    
    book = Book.objects.get(id=id)
    book.bookName = "lenovo laptop"
    book.bookPrice = 500000
    book.save()
    
    # book = book.objects.get(id=id)
    # book.pName = "mouse"
    # book.save()
    return HttpResponse("book updated")
    #return render(request,'book/updatebook.html')
    
def getbookDetail(request,id):
    book=Book.objects.get(id=id)
    bookdetail= Book.objects.all().values()    
    return render(request,'book/bookdetail.html',{'book':book,'books':bookdetail})
    
def addbookWithForm(request):
    
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,'user/author_dashboard.html')    
            
        
    return render(request,'book/addbookwithform.html',{'form':form})    
        
    
    # if request.method == "POST":
    #     pName = request.POST['pName']
        
            
def updatebookWithForm(request,id):
    book = Book.objects.get(id=id)
    form = BookForm()  
    print("Post....")
    form = BookForm(request.POST or None,instance=book)
    if form.is_valid():
        form.save()
        return redirect('author_dashboard')
    return render(request,'book/updatebookwithform.html',{'form':form})

#forcategories

def addCategory(request):
    form = CategoryForm()
    if request.method =="POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('getcategories')
    return render(request,'book/addcategory.html',{'form':form})

def getAllCategories(request):
    categories = Category.objects.all().values()
    return render(request,'book/allcategories.html',{'categories':categories})
                
   
def deleteCategory(request,id):
    
    cat = Category.objects.get(id=id)
    cat.delete()
    return redirect('getcategories')
        
    
def updateCategory(request,id):
    cat = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None,instance=cat)
    if form.is_valid():
        cat.save()
        return redirect('getcategories')
    
    return render(request,'book/updatecategory.html',{'form':form})


def addAuthor(request):
    form = AuthorForm()
    if request.method =="POST":
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('getauthors')
    return render(request,'book/addauthor.html',{'form':form})

def getAllAuthors(request):
    authors = Author.objects.all().values()
    return render(request,'book/allauthors.html',{'authors':authors})
                
   
def deleteAuthor(request,id):
    
    auth = Author.objects.get(id=id)
    auth.delete()
    return redirect('getauthors')
        
    
def updateAuthor(request,id):
    auth = Author.objects.get(id=id)
    form = AuthorForm(request.POST or None,instance=auth)
    if form.is_valid():
        auth.save()
        return redirect('getauthors')
    
    return render(request,'book/updateauthor.html',{'form':form})