from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Property
from .forms import ContactForm

def home(request):
    return render(request, 'imoveis/home.html')

def property_list(request):
    properties = Property.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'imoveis/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    form = ContactForm()

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
        'form': form
    })

def development_list(request):
    # Placeholder for developments - will be implemented later
    return render(request, 'imoveis/development_list.html')
