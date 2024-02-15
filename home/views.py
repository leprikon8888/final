from django.shortcuts import render
from .models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, \
    PortfolioBlock, Portfolio


def main_page(request):
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
    context = {
        'service_block': service_block,
        'services': services,
        'aboutblock': aboutblock,
        'about_unit': about_unit,
        'team': team,
        'client': client,
        'shapka': shapka,
        'brand_name': brand_name,
        'face': face,
        'portfolio_block': portfolio_block,
        'portfolio': portfolio,
    }
    return render(request, 'index.html', context=context)