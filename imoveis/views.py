from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Property, NewsletterSignup, Favorite
from .forms import ContactForm, NewsletterSignupForm

def home(request):
    properties = Property.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'imoveis/home.html', {'properties': properties})

def property_list(request):
    properties = Property.objects.filter(is_available=True)

    # Aplicar filtros
    price_max = request.GET.get('price')
    if price_max:
        try:
            properties = properties.filter(price__lte=float(price_max))
        except ValueError:
            pass

    city = request.GET.get('city')
    if city:
        properties = properties.filter(city__icontains=city)

    rental_type = request.GET.get('rental_type')
    if rental_type in ['compra', 'aluguel']:
        properties = properties.filter(rental_type=rental_type)

    properties = properties.order_by('-created_at')
    return render(request, 'imoveis/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    form = ContactForm()
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, property=property).exists()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.property = property
            contact.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('property_detail', pk=property.pk)

    return render(request, 'imoveis/property_detail.html', {
        'property': property,
        'form': form,
        'is_favorite': is_favorite,
    })

def development_list(request):
    return render(request, 'imoveis/development_list.html')

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Email cadastrado com sucesso! Você receberá nossas novidades em breve.')
            except:
                messages.warning(request, 'Este email já está cadastrado em nossa newsletter.')
            return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'imoveis/home.html', {'newsletter_form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro realizado com sucesso.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'imoveis/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'imoveis/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home')

@login_required
def profile(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('property')
    return render(request, 'imoveis/profile.html', {'favorites': favorites})

@login_required
def toggle_favorite(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        property_id = request.POST.get('property_id')
        property = get_object_or_404(Property, pk=property_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, property=property)
        if not created:
            favorite.delete()
            favorited = False
        else:
            favorited = True
        return JsonResponse({'favorited': favorited})
    return JsonResponse({'error': 'Invalid request'}, status=400)
