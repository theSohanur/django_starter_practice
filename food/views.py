from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm


def index(request):
    item_list = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse("<h2>Hello, This is item view.</h2>")


def detail(request, item_id):
    item_n = Item.objects.get(pk=item_id)
    context = {
        "item": item_n,
    }

    return render(request, 'food/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/item_form.html', {'form': form})
