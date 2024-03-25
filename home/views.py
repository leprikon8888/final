from django.shortcuts import render
from django.shortcuts import redirect
from .models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, \
    PortfolioBlock, Portfolio, ContactBlock, Niz
from .forms import FormContactForm
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """ Add extra context data to the template context. """
        context = super().get_context_data(**kwargs)
        service_block = ServiceBlock.objects.filter(is_visible=True)
        services = Service.objects.filter(is_visible=True)
        aboutblock = AboutBlock.objects.filter(is_visible=True)
        about_unit = AboutUnit.objects.filter(is_visible=True)
        team = Team.objects.filter(is_visible=True)
        client = Client.objects.filter(is_visible=True)
        shapka = Shapka.objects.filter(is_visible=True)
        brand_name = BrandName.objects.all()
        face = BrandFace.objects.all()
        portfolio_block = PortfolioBlock.objects.all()
        portfolio = Portfolio.objects.filter(is_visible=True)
        form_contact = FormContactForm()
        contact = ContactBlock.objects.all()
        niz = Niz.objects.all()

        context['service_block'] = service_block
        context['services'] = services
        context['aboutblock'] = aboutblock
        context['about_unit'] = about_unit
        context['team'] = team
        context['client'] = client
        context['shapka'] = shapka
        context['brand_name'] = brand_name
        context['face'] = face
        context['portfolio_block'] = portfolio_block
        context['portfolio'] = portfolio
        context['form_contact'] = form_contact
        context['contact'] = contact
        context['niz'] = niz
        return context

    def post(self, request, *args, **kwargs):
        """ Add extra context data to the template context. """
        form_contact = FormContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            return redirect('home:main_page')
        else:
            return render(request, 'index.html', {'form_contact': form_contact})
