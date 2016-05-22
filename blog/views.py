from django.http import HttpResponse
from rest_framework import permissions
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import DishSerializer
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import generics
from .models import Dish
from .forms import DishForm


# Create your views here.

class DishList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_queryset(self):
        queryset = Dish.objects.all()
        name = self.request.query_params.get('name', None)
        price = self.request.query_params.get('price', None)
        type = self.request.query_params.get('type', None)
        categoryA = self.request.query_params.get('categoryA', None)
        categoryB = self.request.query_params.get('categoryB', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if price is not None:
            queryset = queryset.filter(price=price)
        if type is not None:
            queryset = queryset.filter(type=type)
        if categoryA is not None:
            queryset = queryset.filter(categoryA=categoryA)
        if categoryB is not None:
            queryset = queryset.filter(categoryB=categoryB)

        return queryset


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishCreate(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


# WEBSITE VIEWS---------------------------------------------------------------------------------------------------------


def dish_list(request):
    dishes = Dish.objects.all().order_by('name')
    return render(request, 'blog/dish_list.html', {'dishes': dishes})


def dish_description(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'blog/dish_description.html', {'dish': dish})


def dish_new(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.author = request.user
            dish.published_date = timezone.now()
            dish.save()
            return redirect('dish_description', pk=dish.pk)
    else:
        form = DishForm()
    return render(request, 'blog/dish_edit.html', {'form': form})


def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.author = request.user
            dish.published_date = timezone.now()
            dish.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'blog/dish_edit.html', {'form': form})


def dish_list_type_appetizer(request):
    dish_type_appetizer = Dish.objects.filter(type=1).order_by('name')
    return render(request, "blog/dish_list_type_appetizer.html", {'dish_type_appetizer': dish_type_appetizer})


def dish_list_type_main_course(request):
    dish_type_main_course = Dish.objects.filter(type=2).order_by('name')
    return render(request, "blog/dish_list_type_main_course.html", {'dish_type_main_course': dish_type_main_course})


def dish_list_type_dessert(request):
    dish_type_dessert = Dish.objects.filter(type=3).order_by('name')
    return render(request, "blog/dish_list_type_dessert.html", {'dish_type_dessert': dish_type_dessert})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        dishes = Dish.objects.filter(name__icontains=q).order_by('name')
        return render(request, 'blog/search.html', {'dishes': dishes, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
