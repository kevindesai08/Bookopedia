from django.db import models
# Create your models here.
#django orm object relational mapping

class Author(models.Model):
    authorname = models.CharField(max_length=30)
    #authorid= models.IntegerField(max_length=9)

    def __str__(self):
        return self.authorname
    
    class Meta:
        db_table= 'authors'

class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    description= models.CharField(max_length=1000,null=True)
    
    class Meta:
        db_table = 'categories'
        
    def __str__(self):
        return self.name

class Book(models.Model):
    #we dont have to provide id explicitly
    bookAuthor = models.ForeignKey(Author,on_delete=models.CASCADE,max_length=30,null=True)
    bookCategory = models.ForeignKey(Category,on_delete=models.CASCADE,max_length=100,null=True)
    bookName = models.CharField(max_length=100)
    bookPrice = models.FloatField()
    bookQuantity  = models.IntegerField(null=True)
    bookDescription = models.CharField(max_length=1000,null=True)
    bookStatus = models.BooleanField(default=True)
    bookImage = models.ImageField(upload_to='images/',null=True,blank=True)
    #if you dont provide table name in meta class product.product
    
    def __str__(self):
        return self.bookName
        
    
    class Meta:
        db_table = 'books'
    
            
            
        
    
            
    
    
