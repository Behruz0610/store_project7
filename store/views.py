from django.shortcuts import render

def home(request):
    # Agar index.html bosh sahifa bo'lsa:
    return render(request, 'index.html')

# Qo'shimcha viewlar
def market(request):
    return render(request, 'market.html')

def product(request):
    return render(request, 'product.html')

def admin_page(request):
    return render(request, 'admin_page.html')

# Kerakli boshqa viewlar ham shu tarzda qo'shilishi mumkin.
