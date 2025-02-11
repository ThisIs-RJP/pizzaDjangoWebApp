from django.shortcuts               import *
from django.http                    import *
from templates.forms                import *
from templates.models               import *
from django.core.cache              import *
from django.contrib                 import messages
from django.contrib.auth.forms      import UserCreationForm, AuthenticationForm
from django.contrib.auth            import *
from django.contrib.auth            import login, authenticate
from django.contrib.auth.views      import LoginView
from django.urls                    import reverse_lazy
from django.views                   import generic
from django.contrib.auth.decorators import login_required

# Create your views here.

go_to_delivery = 0
pizza = 0

def index(request):
    # Pizza.objects.all().delete() ## Deleting everything from testing
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'make-account.html', {'form': form})

class UserLoginView(LoginView):
    template_name='login.html'

def profile(request):
    orders = Pizza.objects.all().filter(author=request.user)

    return render(request, 'profile.html', {'orders' : orders})

def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url='index') #redirect when user is not logged in
def order(request):
    global go_to_delivery
    global pizza

    if request.method == 'POST':
        toppings = request.POST.getlist("toppings")
        form     = PizzaForm(request.POST)

        if form.is_valid():
            pizza          = form.save(commit=False)
            pizza.author   = request.user
            pizza.toppings = ", ".join(toppings)

            go_to_delivery = 1
            return redirect('delivery')
        else:
            return render(request, 'order.html', {'form': form})

    else:
        form = PizzaForm()

        if form.is_valid():
            toppings       = request.POST.getlist("toppings")
            pizza          = form.save(commit=False)
            pizza.author   = request.user
            pizza.toppings = ", ".join(toppings)

            go_to_delivery = 1
            return redirect('delivery')

    return render(request, 'order.html', {'form': form})

@login_required(login_url='index')
def delivery(request):

    global go_to_delivery
    global pizza

    if go_to_delivery == 1:
        if request.method == 'POST':
            form = DeliveryForm(request.POST)

            if form.is_valid():
                delivery        = form.save(commit=False)
                delivery.author = request.user
                delivery.save()

                go_to_delivery = 0
                pizza.save()

                return redirect("confirmation")
        else:
            form = DeliveryForm()
            if form.is_valid():
                delivery        = form.save(commit=False)
                delivery.author = request.user
                delivery.save()

                go_to_delivery = 0
                pizza.save()

                return redirect("confirmation")
    else:
        return redirect('profile')

    return render(request, 'delivery.html', {'form': form})

def confirmation(request):
    orders   = Pizza.objects.all().filter(author=request.user)
    delivery = Delivery.objects.all().filter(author=request.user)
    
    return render(request, 'confirmation.html', {'orders' : orders, "delivery" : delivery})