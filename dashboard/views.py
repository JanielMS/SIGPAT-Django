from django.shortcuts import render
from bens.models import Bem
from movimentacoes.models import Movimentacao
from django.db.models import Count, Sum, Prefetch

def dashboard_view(request):
    """
    View responsável por exibir o painel principal do sistema, com indicadores e gráficos.
    """
    total_bens = Bem.objects.count()
    total_movimentacoes = Movimentacao.objects.count()
    
    # Quantidade de bens por status
    bens_por_status = Bem.objects.values('status').annotate(total=Count('status'))
    
    # Quantidade de bens por categoria (opcional, se quiser mais detalhes no dashboard)
    bens_por_categoria = Bem.objects.values('categoria__nome').annotate(total=Count('categoria'))
    
    # Quantidade de bens por departamento (opcional, se quiser mais detalhes no dashboard)
    bens_por_departamento = Bem.objects.values('departamento__nome').annotate(total=Count('departamento'))
    
    # Últimas movimentações
    ultimas_movimentacoes = Movimentacao.objects.select_related('bem').order_by('-data_movimentacao')[:5]
    
    # Total de valor dos bens por categoria (pode ser útil para gráfico de valor total)
    valor_total_bens = Bem.objects.aggregate(total_valor=Sum('valor'))
    
    # Passando os dados para o contexto
    context = {
        'total_bens': total_bens,
        'total_movimentacoes': total_movimentacoes,
        'bens_por_status': bens_por_status,
        'bens_por_categoria': bens_por_categoria,
        'bens_por_departamento': bens_por_departamento,
        'ultimas_movimentacoes': ultimas_movimentacoes,
        'valor_total_bens': valor_total_bens['total_valor'],
    }
    return render(request, 'dashboard/dashboard.html', context)
