import django.forms as form
from .models import Book,Category,Author

class BookForm(form.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class CategoryForm(form.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'       

class AuthorForm(form.ModelForm):
    class Meta:
        model = Author
        fields = '__all__' 

