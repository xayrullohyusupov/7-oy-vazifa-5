from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.forms import UserCreationForm


def main(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    navbar_info = models.NavbarInfo.objects.all()
    footer_info = models.FooterInfo.objects.all()

    context = {}
    context['banners'] = banners
    context['navbar_info'] = navbar_info
    context['footer_info'] = footer_info

    return render(request, 'index.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})


def createProduct(request):
    context = {}
    context['categorys'] = models.Category.objects.all()
    if request.method == 'POST':
        product = models.Product.objects.create(
            name = request.POST['name'],
            quantity = request.POST['quantity'],
            price = request.POST['price'],
            category_id = request.POST['category_id'], 
            description = request.POST['description']
        )

        images = request.FILES.getlist('images')

        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
    return render(request, 'create_product.html', context)

def delete_product(request, id):
    product = models.Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()


def product_update(request, id):
    product = models.Product.objects.get(id=id)
    context = {}
    context['product'] = product
    context['categorys'] = models.Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST['name']
        product.quantity = request.POST['quantity']
        product.price = request.POST['price']
        product.category_id = request.POST['category_id']
        product.description = request.POST['description']
        product.save()

        images = request.FILES.getlist('images')
        for image in images:
            models.ProductImg.objects.create(
                img = image,
                product = product
            )
    return render(request, 'product_update.html', context)