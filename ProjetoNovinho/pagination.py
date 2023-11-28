from django.core.paginator import Paginator
from django.shortcuts import render

queryset = Produto.objeto.all()
queryset = queryset.filter(preco__get=50)

def listar_produto(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, per_page= 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name= 'lista_produtos.html', context={'page_obj': page_obj})