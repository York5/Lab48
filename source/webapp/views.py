from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import GoodForm
from webapp.models import Good, CATEGORY_CHOICES, OTHER
from django.http import Http404


def index_goods_view(request, *args, **kwargs):
    goods = Good.objects.filter(stock__gte=1).order_by('name', 'category')
    return render(request, 'index.html', context={
        'goods': goods,
    })


def single_good_view(request, pk):
    try:
        good = get_object_or_404(Good, pk=pk)
    except Good.DoesNotExist:
        raise Http404
    return render(request, 'good.html', context={
        'good': good
    })


def good_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = GoodForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = GoodForm(data=request.POST)
        if form.is_valid():
            good = Good.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                stock=form.cleaned_data['stock'],
                price=form.cleaned_data['price'])
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})