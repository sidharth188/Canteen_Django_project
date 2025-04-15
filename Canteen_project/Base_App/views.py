from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from Base_App.models import CartItem, Items,ItemList,Feedback, Payment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#def user_login(request):
 #   if request.method == 'POST':
  #      form = AuthenticationForm(data=request.POST)
  #      if form.is_valid():
   #         user = form.get_user()
    #        login(request, user)
     #       return redirect('home')  # Redirect to home page
    #else:
      #  form = AuthenticationForm()
   # return render(request, 'login.html', {'form': form})
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #form = AuthenticationForm(data=request.POST)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
@login_required
def HomeView(request):
       items = Items.objects.all()
       list = ItemList.objects.all()
       review = Feedback.objects.all()
       return render(request,'home.html', {'items': items,'list': list, 'review': review})
def AboutView(request):
     return render(request,'about.html')
@login_required
def MenuView(request):
       items = Items.objects.all()
       list = ItemList.objects.all()
       return render(request, 'menu.html', {'items': items,'list': list})
def BookView(request):
     return render(request,'book.html')
@login_required
def FeedbackView(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        description=request.POST.get('description')
        ratings=request.POST.get('ratings_number')
        if name != '' and description !='' and ratings!=0:
            data=Feedback(User_name=name, description=description, Rating=ratings)
            data.save()

    review = Feedback.objects.all()
    return render(request,'feedback.html', {'review': review})

@login_required
def cartView(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.get_total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"{item.Item_name} quantity updated in your cart.")
    else:
        messages.success(request, f"{item.Item_name} added to your cart.")
    return redirect('menu')  # redirecting back to menu after adding
@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def paymentView(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.get_total() for item in cart_items)
    total_amount_paise = total_amount * 100  # Razorpay needs amount in paisa

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create Razorpay Order
    payment = client.order.create({
        "amount": total_amount_paise,
        "currency": "INR",
        "payment_capture": "1"
    })

    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'razorpay_order_id': payment['id'],
    }

    return render(request, 'payment.html', context)

@csrf_exempt
@login_required
def paymentSuccess(request):
    if request.method == "POST":
        # Here you could save payment details to DB
        CartItem.objects.filter(user=request.user).delete()
        messages.success(request, "Payment successful! Your order is being processed.")
        return redirect('menu')

# views.py
def payment_list(request):
    payments = Payment.objects.all()  # Fetch all payments from the database
    print(payments)  # Print in the server console for debugging
    return render(request, 'payment_list.html', {'payments': payments})
