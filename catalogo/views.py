from django.shortcuts import render
from django.db.models import Count, Q
from .models import GeneroTextual
import json  # Usaremos JSON para passar dados para o JavaScript


def mostrar_relatorio(request):
    """
    Esta view busca os dados e os envia para o template HTML.
    """

    # 1. DEFINIR O QUE QUEREMOS CONTAR
    categoria_alvo = 'SEQ'
    nome_categoria = "Sequenciação"

    # 2. USAR O DJANGO ORM PARA FAZER A CONSULTA
    dados = GeneroTextual.objects.annotate(
        total_conectores=Count('texto__ocorrenciaconector',
                               filter=Q(texto__ocorrenciaconector__categoria=categoria_alvo))
    ).values('nome', 'total_conectores')

    # 3. PREPARAR OS DADOS PARA O GRÁFICO (Chart.js)
    generos = []
    contagens = []

    for item in dados:
        if item['total_conectores'] is not None:
            generos.append(item['nome'])
            contagens.append(item['total_conectores'])

    # 4. EMPACOTAR OS DADOS PARA O TEMPLATE
    contexto = {
        'titulo_grafico': f'Distribuição de Conectores de "{nome_categoria}"',
        'labels_grafico': json.dumps(generos),  # Converte lista Python para JSON
        'dados_grafico': json.dumps(contagens),  # Converte lista Python para JSON
    }

    # 5. RENDERIZAR O HTML
    # O Django irá procurar por 'catalogo/relatorio.html'
    return render(request, 'catalogo/relatorio.html', contexto)