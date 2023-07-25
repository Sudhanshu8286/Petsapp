from django.http import HttpResponse
from django.shortcuts import render
from .models import Pet
from django.http import Http404
from django.db.models import Q

# Create your views here.

def pet_list(request):
    pets_data = Pet.objects.all() #query
    data = {'pets_d':pets_data}
    return render(request, 'petsapp/list.html',data)


def pet_detail(request,pk):
    query = Pet.objects.filter(id=pk)
    if query.exists() and query.count() == 1:
        instance = query.first()

    else:
        return Http404("Pet data does not Exists")
    context ={
        'data':instance
    }

    return render(request,'petsapp/detail.html',context)    


def dog_list(request):
    dog_data = Pet.objects.filter(animal_type='D')
    all_dog_data ={
        'objects':dog_data
    }

    return render(request,'petsapp/dog-list.html',all_dog_data)



def cat_list(request):
    cat_data = Pet.objects.filter(animal_type='C')
    all_cat_data ={
        'cat':cat_data
    }

    return render(request,'petsapp/cat-list.html',all_cat_data)


def search_product(request):
    if request.method == "GET":
        searched_data = request.GET.get('search')
        if (len(searched_data)==0):
            return Http404("No Such Data")
        
        else:
            # result = Pet.objects.filter(name___icontains=searched_data) it will give you only name search

            query = (Q(name__icontains=searched_data) | Q(species__icontains=searched_data)|
            Q(breed__icontains=searched_data))
            result = Pet.objects.filter(query)
            context = {
                'objects':result
            }

            return render (request,'petsapp/search.html',context)
        
    else:
        return HttpResponse("Invalid Method")        