from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    """Home page"""
    return render(request, 'home.html')

def view_list(request):
    """list view"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """new list"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
