from django.shortcuts import render

# Create your views here.
def get_food_list(request):
    return render(request, 'food/food_list.html')