from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order,StaffRequest
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Item






# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    orders_count=orders.count()
    products_count=products.count()
    workers_count=User.objects.all().count()
   
    
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
        
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'products_count':products_count,
        'workers_count':workers_count,
        'orders_count':orders_count
        
    }
    return render(request,'dashboard/index.html',context)


@login_required(login_url='user-login')
def staff(request):
     workers=User.objects.all()
     workers_count=workers.count()
     orders_count=Order.objects.all().count()
     products_count=Product.objects.all().count()
     context={
        'workers':workers, 
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,

     }

     return render(request,'dashboard/staff.html',context)

def staff_detail(request,pk):
    workers=User.objects.get(id=pk)
    context={
        'workers':workers,
    }
    return render(request,'dashboard/staff_detail.html',context)




def make_request(request):
    if request.method == 'POST':
        staff = request.user
        product_id = request.POST.get('product_id')
        request_quantity = int(request.POST.get('request_quantity'))

        product = Product.objects.get(pk=product_id)
        current_quantity = product.quantity

        if (current_quantity - product.minimum_stock) < request_quantity:
            # Request more products from the seller up to a maximum of 20
            max_request_quantity = min(20, request_quantity)
            # Implement the code to send a request to your seller here
            # This could involve sending an email or making an API call to your seller's system
            # Update the product quantity accordingly when you receive the products

            # For demonstration purposes, we'll just update the product quantity directly
            product.quantity += max_request_quantity
            product.save()

        # Create a staff request record
        StaffRequest.objects.create(staff=staff, product=product, request_quantity=request_quantity)

        return redirect('make-request')  # Redirect to the same page after submitting

    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'dashboard/make_request.html', context)





@login_required(login_url='user-login')
def product(request):
    items=Product.objects.all()
    products_count=items.count()
   # items=Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form=ProductForm
    context ={
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
  
    return render(request,'dashboard/product.html',context)


@login_required(login_url='user-login')
def product_delete(request,pk): #pk-primary key
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')


@login_required(login_url='user-login')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)



@login_required(login_url='user-login')
def order(request):
    orders=Order.objects.all()
    orders_count=orders.count()
    workers_count=User.objects.all().count()
    products_count=Product.objects.all().count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request,'dashboard/order.html',context)




def your_view(request):
    low_stock_products = Product.objects.filter(quantity__lt=F('minimum_quantity'))
    context = {
        'low_stock_products': low_stock_products
    }
    return render(request, 'dashboard/notification.html', context)




def dashboard(request):
    low_stock_products = Product.objects.filter(current_stock__lt=F('minimum_stock')).values('name')

    return render(request, 'dashboard/dashboard.html', {'low_stock_products': low_stock_products})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product_list.html', {'products': products})

def item_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    items = Item.objects.filter(product=product)
    return render(request, 'dashboard/item_list.html', {'product': product, 'items': items})



