from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('books/',views.getAllbooks,name='getbooks'),
    path('addbook/',views.addbooks),
    #path('deleteproduct/',views.deleteProduct),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('updatebook/<int:id>',views.updatebook),
    path('addbookwithform/',views.addbookWithForm),
    path('bookdetail/<int:id>,',views.getbookDetail,name='bookdetail'),
    path('update/<int:id>',views.updatebookWithForm,name ="updatebook"),
    
    
    path('addcategory/',views.addCategory,name='addcategory'),
    path('getcategories/',views.getAllCategories,name='getcategories'),
    path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),
    path('updatecategory/<int:id>',views.updateCategory,name='updatecategory'),


    path('addauthor/',views.addAuthor,name='addauthor'),
    path('getauthors/',views.getAllAuthors,name='getauthors'),
    path('deleteauthors/<int:id>',views.deleteAuthor,name='deleteauthor'),
    path('updateauthor/<int:id>',views.updateAuthor,name='updateauthor'),
    
    
    
    
]