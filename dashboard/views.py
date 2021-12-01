from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Item
from .forms import ItemForm, NounForm
from home.models import Noun, Gender, NounCategory
from django.contrib.auth.models import User


# Functions items and nouns
def dashboard(request):
    context = {
        'owned_items': owned_todo_list(request.user),
        'owned_nouns': owned_nouns_list(request.user),
        }
    return render(request, 'dashboard/dashboard.html', context)


# Functions related to todo list
def owned_todo_list(set_user):
    items = Item.objects.filter(owner=set_user).all().order_by('done', 'name')
    return items


def todo_dashboard(request):
    context = {
        'owned_items': owned_todo_list(request.user),
        'owned_nouns': owned_nouns_list(request.user),
        'show_todo': 'show'
        }
    return render(request, 'dashboard/dashboard.html', context)


def add_todo_item(request):
    '''
    This function does not use from forms.py "ItemForm" for learning purpose
    "ItemForm" will be used for editing the Items
    However, this function is a good example how to edit without using form 
    and understand the CRUD process
    '''
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        owner = request.user
        Item.objects.create(name=name, done=done, owner=owner)
        return redirect('todo_dashboard')
    return render(request, 'dashboard/add_todo_item.html')


def edit_todo_item(request, item_id):
    '''
    In this function "ItemForm" from forms.py
    it was not in add_todo_item for learning purpose
    Here it is to have a second example of how to interact with data
    '''
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_dashboard')

    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_todo_item.html', context)


def toggle_todo_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('todo_dashboard')


def delete_todo_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('todo_dashboard')


# Function related to noun list
def owned_nouns_list(set_user):
    owned_nouns = Noun.objects.filter(owner=set_user).all()
    return owned_nouns


def noun_dashboard(request):
    context = {
        'owned_items': owned_todo_list(request.user),
        'owned_nouns': owned_nouns_list(request.user),
        'show_nouns': 'show'
        }
    return render(request, 'dashboard/dashboard.html', context)


def add_noun(request):  
    '''
    This function uses a form in forms.py
    '''
    if request.method == 'POST':
        form = NounForm(request.POST)
        if form.is_valid():
                noun = form.save(commit=False)
                noun.owner = request.user
                noun.save()
    form = NounForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_noun.html', context)


def edit_noun(request, noun_id):
    noun = get_object_or_404(Noun, id=noun_id)
    if request.method == 'POST':
        form = NounForm(request.POST, instance=noun)
        if form.is_valid():
                noun = form.save(commit=False)
                noun.owner = request.user
                noun.save()
                return redirect('noun_dashboard')
    form = NounForm(instance=noun)
    context = {
        'form': form
    }
    return render(request, 'dashboard/edit_noun.html', context)


def delete_noun(request, noun_id):
    noun = get_object_or_404(Noun, id=noun_id)
    noun.delete()
    return redirect('noun_dashboard')