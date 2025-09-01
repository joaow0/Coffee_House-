from django.shortcuts import redirect, render, HttpResponse
from pagina.models import Products, Contacts, Gallery, Testimonials


def home(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        if nome and email and mensagem:
            Contacts.objects.create(nome=nome, email=email, mensagem=mensagem)
            # Opcional: mensagem de sucesso ou redirect
            return redirect('home')
    product = Products.objects.all()
    gallery = Gallery.objects.all()
    contacts = Contacts.objects.all()
    context = {
        'products': product,
        'testimonials': Testimonials.objects.all(),
        'gallery': gallery,
        'contacts': contacts
    }
    return render(request, 'page.html', context)


def about(request):
    return render(request, 'about.html')


def menu(request):
    return render(request, 'menu.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def gallery(request):
    return render(request, 'gallery.html')


def contacts(request):
    return render(request, 'contacts.html')
