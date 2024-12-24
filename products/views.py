from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from products.forms import ProductForm
from django.db.models import Count, Q
from django.utils.safestring import mark_safe

# Create your views here.
def main(request):
    user = request.user
    products = Product.objects.filter(
        author__in=user.following.all()).order_by('-created_at')
    context = {"products":products}
    return render(request, "products/main.html",context)


def products(request):
    sort_by = request.GET.get('sort_by', 'date_desc')  # 기본값 'date_desc'

    if sort_by == 'popularity':
        products = Product.objects.annotate(
            like_count=Count('like_user')).order_by('-like_count')
    elif sort_by == 'newest':
        products = Product.objects.all().order_by('-created_at')
    elif sort_by == 'priceAsc':
        products = Product.objects.all().order_by('price')
    elif sort_by == 'priceDesc':
        products = Product.objects.all().order_by('-price')
    else:
        products = Product.objects.all()

    context = {"products": products, 'sort_by': sort_by}
    return render(request, "products/products.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.GET.get("redirected") != "true" and request.user != product.author:
        product.see_count += 1
        product.save()
    total_likes = product.like_user.count()
    user = get_object_or_404(get_user_model(), pk=product.author_id)
    context = {
        "product":product,
        "total_likes":total_likes,
        "user":user,}
    return render(request, "products/product_detail.html", context)


@require_http_methods(["GET","POST"])
def create(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.author = request.user
                product.save()
                return redirect(f"/products/{product.pk}/?redirected=true")
        else:
            form = ProductForm()
            context = {"form":form}
            return render(request, "products/create.html", context)
    else:
        return redirect("accounts:login")
    

@login_required
@require_http_methods(["GET","POST"])
def update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect(f"/products/{product.pk}/?redirected=true")
    else:
        form = ProductForm(instance=product)
    context = {"product":product}
    return render(request, "products/update.html", context)


@login_required
@require_http_methods(["POST"])
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.author:
        product.delete()
        return redirect("products:products")
    return redirect("product_detail", pk)


@require_http_methods(["POST"])
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if request.user != product.author:
            if request.user in product.like_user.all():
                product.like_user.remove(request.user)
            else:
                product.like_user.add(request.user)
        else:
            messages.error(request, "본인의 물품은 찜할 수 없습니다.")
        return redirect(f"/products/{product.pk}/?redirected=true")
    else:
        return redirect("accounts:login")


def search(request):
    query = request.GET.get('q')
    results = Product.objects.all()

    if query:
        results = Product.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        )
        for product in results:
            product.title = mark_safe(
                product.title.replace(query, f"<mark>{query}</mark>"))
            product.content = mark_safe(
                product.content.replace(query, f"<mark>{query}</mark>"))
            
    context = {'query': query, 'results': results}

    return render(request, 'products/search.html', context)
