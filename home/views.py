from django.shortcuts import render, get_object_or_404
from .models import Noun, NounCategory

##############

number_of_displayed_word = 4
##############
# Create your views here.


def home(request):
    categories = NounCategory.objects.all()
    context = {
        'theme': 'Chose a theme',
        'categories': categories
      }
    return render(request, 'home/index.html', context)


def feminine(request):
    context = index_with_noun_list('Feminin')
    return render(request, 'home/index.html', context)


def masculine(request):
    context = index_with_noun_list('Masculin')
    return render(request, 'home/index.html', context)


def go_to_category(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('', category)
    return render(request, 'home/index.html', context)


def categorie_feminine(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('Feminin', category)
    return render(request, 'home/index.html', context)


def categorie_masculine(request, category_id):
    category = get_object_or_404(NounCategory, id=category_id)
    context = index_with_gender_and_category('Masculin', category)
    return render(request, 'home/index.html', context)


######################
def index_with_gender_and_category(chosen_gender, chosen_category):
    nouns = Noun.objects.filter(
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
    nouns = Noun.objects.filter(
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


def index_with_noun_list(chosen_gender):
    nouns = Noun.objects.filter(
      gender__noun_gender__contains=chosen_gender).order_by(
        '?')[:number_of_displayed_word]
    categories = NounCategory.objects.all()
    context = {
      'nouns': nouns,
      'categories': categories,
      'theme': 'Chose a theme',
    }
    return context
