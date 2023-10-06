from django.shortcuts import render, reverse
from django.http import HttpResponse
import copy


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def menu_views(request):
    context = {
        'menu': DATA,
    }
    return render(request, 'calculator/menu.html', context)

def recipe_views(request):
    recipe_copy = DATA.get(request.path.replace('/',''))
    if recipe_copy:
        servings = request.GET.get("servings")
        if not servings:
            servings=1
        recipe = copy.deepcopy(recipe_copy)
        for i in recipe:
            recipe[i] = recipe[i] * int(servings)
    else:
         recipe = recipe_copy

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)