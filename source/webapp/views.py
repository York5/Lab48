from django.shortcuts import render, get_object_or_404, redirect

# from webapp.forms import GoodForm
from webapp.models import Good, CATEGORY_CHOICES, OTHER
from django.http import Http404


def index_goods_view(request, *args, **kwargs):
    goods = Good.objects.filter(stock__gte=1).order_by('category', 'name')
    return render(request, 'index.html', context={
        'goods': goods,
    })
