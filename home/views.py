from django.shortcuts import render, get_object_or_404
from .models import Noun, NounCategory
from django.contrib.auth.models import User

# ------------------- Variables
number_of_displayed_word = 6


# ------------------- Home page
def home(request):
    categories = NounCategory.objects.all()
    context = {
        'theme': 'Chose a theme',
        'categories': categories
      }
    return render(request, 'home/index.html', context)


# ------------------- To display default NOUNS. Categories are available only in default owner
#For displaying default without categories
def feminine(request):
    context = index_with_noun_list_owned('Feminin', '2')  #2 is for the default user here. might have to be changed
    return render(request, 'home/index.html', context)

def masculine(request):
    context = index_with_noun_list_owned('Masculin', '2')  #2 is for the default user here. might have to be changed
    return render(request, 'home/index.html', context)

def neutral(request):
    context = index_with_noun_list_owned('Neutral', '2')  #2 is for the default user here. might have to be changed
    return render(request, 'home/index.html', context)

#For displaying default with categories
def go_to_category(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('', category)
    return render(request, 'home/index.html', context)

#For displaying default with categories + gender
def categorie_feminine(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('Feminin', category)
    return render(request, 'home/index.html', context)


def categorie_masculine(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('Masculin', category)
    return render(request, 'home/index.html', context)

def categorie_neutral(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('Neutral', category)
    return render(request, 'home/index.html', context)

# owner='2' is the default owner. It is to display only the default NOUNS
def index_with_gender_and_category(chosen_gender, chosen_category):
    nouns = Noun.objects.filter(owner='2').filter(
      categories__noun_category__contains=chosen_category).filter(
        gender__noun_gender__contains=chosen_gender).order_by(
          '?')[:number_of_displayed_word]

    categories = NounCategory.objects.all()
    context = {
      'nouns': nouns,
      'categories': categories,
      'theme': chosen_category,
    }
    return context

# owner='2' is the default owner. It is to display only the default NOUNS
def index_with_category(chosen_category):
    nouns = Noun.objects.filter(owner='2').filter( 
      categories__noun_category__contains=chosen_category).order_by(
        '?')[:number_of_displayed_word]
    categories = NounCategory.objects.all()
    context = {
      'nouns': nouns,
      'categories': categories,
      'theme': chosen_category,
      'theme_id': chosen_category.id,
    }
    return context

def index_with_noun_list_owned(chosen_gender, set_user):
    nouns = Noun.objects.filter(owner=set_user).filter(
      gender__noun_gender__contains=chosen_gender).order_by(
        '?')[:number_of_displayed_word]
    categories = NounCategory.objects.all()
    context = {
      'nouns': nouns,
      'categories': categories,
      'theme': 'Chose a theme',
    }
    return context

# ------------- To display only owned nouns. The user has to be logged in
def feminine_user(request):
    context = index_with_noun_list_owned('Feminin', request.user)
    return render(request, 'home/index.html', context)

def masculine_user(request):
    context = index_with_noun_list_owned('Masculin', request.user)
    return render(request, 'home/index.html', context)

def neutral_user(request):
    context = index_with_noun_list_owned('Neutral', request.user)
    return render(request, 'home/index.html', context)
