from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, Comment
from .forms import OrderForm, CommentForm
from django.contrib import messages

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'store/index.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            messages.success(request, "Buyurtma muvaffaqiyatli yuborildi!")
            return redirect('product_detail', pk=pk)
    else:
        form = OrderForm()
    return render(request, 'store/product.html', {'product': product, 'form': form, 'comments': comments})

def liked_products(request):
    # Foydalanuvchining yoqtirgan mahsulotlari (dummy)
    products = Product.objects.filter(id__in=request.session.get('liked', []))
    return render(request, 'store/liked-products.html', {'products': products})

def ordered_products(request):
    orders = Order.objects.all()
    return render(request, 'store/ordered-products.html', {'orders': orders})

def market(request):
    products = Product.objects.all()
    return render(request, 'store/market.html', {'products': products})

def profil(request):
    # Foydalanuvchi profili (dummy)
    return render(request, 'store/profil.html')

def profil2(request):
    # Foydalanuvchi profili (dummy)
    return render(request, 'store/profil2.html')

def competition(request):
    # Tanlov sahifasi (dummy)
    return render(request, 'store/competition.html')

def admin_page(request):
    # Admin paneli (dummy)
    return render(request, 'store/admin_page.html')

def admin_pagewithdraw(request):
    # Admin to‘lov sahifasi (dummy)
    return render(request, 'store/admin_pagewithdraw.html')

def requests_view(request):
    # So‘rovlar sahifasi (dummy)
    return render(request, 'store/requests.html')

def stats(request):
    # Statistika sahifasi (dummy)
    return render(request, 'store/stats.html')

def changelog(request):
    # O‘zgarishlar tarixi sahifasi (dummy)
    return render(request, 'store/changelog.html')

def widgets(request):
    # Dashboard widgets sahifasi (dummy)
    return render(request, 'store/widgets.html')