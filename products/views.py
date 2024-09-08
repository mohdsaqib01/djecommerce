from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
# Create your views here.
def category_list(request):
    return render(
        request, 
        'products/category_list.html',
        context = {
            'category': Category.objects.all(),
            'form':CategoryForm()
        }
    )

def category_create(request):
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
        messages.success(request,'Category created successfully')
        form.save()
    else:
        messages.error(request,'error creating category')
    return redirect('category_list')

def category_edit(request, slug):
    category = Category.objects.get(slug=slug)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
            return redirect('category_list')
        else:
            messages.error(request, 'Error creating category')
    return render(
        request, "products/category_edit.html",
        context={'form': form}
    )

def category_delete(request, slug):
    category = Category.objects.get(slug=slug)
    category.delete()
    messages.success(request, 'Category deleted successfully')
    return redirect('category_list')

def product_list(request):
    return render(
        request,'products/list.html',
        context={'products': Product.objects.all()}
    )
def product_create(request):
    form= ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.seller =request.user
            product.slug = slugify(product.title)
            product.save()
            messages.success(request,'Product crezted successfully')
            return redirect('product_detail', slug=product.slug)
        else:
            messages.error(request, 'error creating product')
    return render(
        request,'products/add.html',
        context={'form': form}
    )
def product_edit(request, slug):
    product= get_object_or_404(Product, slug= slug)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.Post, request.FILES, instance= product)
        if form.is_valid():
            product=form.save(commit=False)
            product.slug = slugify(product.title)
            product.save()
            messages.success(request,'Product crezted successfully')
            return redirect('product_list', slug=product.slug)
        else:
            messages.error(request, 'error creating product')
    return render(
        request,'products/edit.html',
        context={'form': form}
    )
def product_delete(request, slug):
    product= get_object_or_404(Product, slug= slug)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('product_list')
    
def product_detail(request, slug):
    product= get_object_or_404(Product, slug= slug)
    return render(
         request,'products/detail.html',
        context={'product': product} 
    )
   
def category_product_list(request, category_slug):
    category= get_object_or_404(Category, slug= category_slug)
    return render(
         request,'products/category_wise.html',
        context={'category': category,
                 'products': Product.objects.filter(category=category)} 
    )
def product_wishlist(request):
    return render(
        request, 'products/wishlist.html',
        context={'wishlist': Wishlist.objects.filter(user=request.user)}
    )
@login_required
def wishlist_add(request,slug):
    product = get_object_or_404(Product, slug=slug)
    Wishlist.objects.create(product=product, user=request.user)
    messages.success(request, 'Product added to wishlist')
    # back to same page
    return redirect(request.META.get('HTTP_REFERER'))
@login_required
def wishlist_remove(request,slug):
    product = get_object_or_404(Product, slug=slug)
    Wishlist.objects.filter(product=product, user=request.user).delete()
    messages.success(request, 'Product removed from wishlist')
    # back to same page
    return redirect(request.META.get('HTTP_REFERER'))
   
def search(request):
    pass
