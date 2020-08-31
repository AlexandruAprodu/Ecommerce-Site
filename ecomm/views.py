from django.shortcuts import render
from products.models import Categories, Products
from django.core.mail import send_mail
from django.views.generic.list import ListView


# Create your views here.


def index(request):
    return render(request, 'ecomm/index.html')


def categories(request):
    context1 = Categories.objects.all()
    return render(request, 'ecomm/categories.html', {'context1': context1})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        mail = request.POST['mail']
        subject = request.POST['subject']
        send_mail(
            'Informatii despre produse: ' + message_name,  # subiect
            subject,  # mesaj
            mail,  # from email
            ['testingsiteromania@gmail.com'],  # to email
        )
        return render(request, 'ecomm/contact.html', {'message_name': message_name})
    else:
        return render(request, 'ecomm/contact.html', {'title': 'Contact'})


class SearchView(ListView):
    model = Products
    template_name = 'ecomm/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Products.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('search')
        context['products'] = Products.objects.filter(title__contains=query)
        return context


def about(request):
    return render(request, 'ecomm/about.html')
