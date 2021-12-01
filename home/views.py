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


# For displaying default without categories
def gender(request, clicked_gender):
    context = index_with_noun_list_owned(clicked_gender, '2')
    return render(request, 'home/index.html', context)


# For displaying default with categories
def go_to_category(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('', category)
    return render(request, 'home/index.html', context)


# For displaying default with categories + gender
def categorie_gender(request, category_id, clicked_gender):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category(clicked_gender, category)
    return render(request, 'home/index.html', context)


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


# To display only owned nouns. The user has to be logged in
def user_gender(request, clicked_gender):
    context = index_with_noun_list_owned(clicked_gender, request.user)
    return render(request, 'home/index.html', context)

