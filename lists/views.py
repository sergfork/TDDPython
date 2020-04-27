from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.forms import ItemForm
from lists.models import Item, List


# Create your views here.
def home_page(request):
    """Home page"""
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    """list view"""
    list_ = List.objects.get(id=list_id)
    # error = None
    form = ItemForm()
    if request.method == 'POST':
        # try:
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
        # item.full_clean()
        # item.save()
        #     return  redirect(list_)
        # except ValidationError:
        #     error = "You can't have an empty item"
    #
    # form = ItemForm()
    return render(request, 'list.html', {'list': list_, "form": form})


def new_list(request):
    """new list"""
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
    # list_ = List.objects.create()
    # item = Item(text=request.POST['text'], list=list_)
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # return redirect(list_)
