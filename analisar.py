import os
import django
import matplotlib.pyplot as plt
from django.db.models import Count,Q

# --- Configuração para rodar o script "fora" do Django ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_analise.settings')
django.setup()
# ---------------------------------------------------------

# Importe seus modelos DEPOIS do setup()
from catalogo.models import GeneroTextual, OcorrenciaConector

def gerar_grafico():
    print("Iniciando análise...")

    # 1. DEFINIR O QUE QUEREMOS CONTAR
    # Mude aqui para 'REF' (Referenciação) ou 'SUB' (Substituição) se quiser
    categoria_alvo = 'SEQ'
    nome_categoria = dict(OcorrenciaConector.CATEGORIAS)[categoria_alvo]

    # 2. USAR O DJANGO ORM PARA FAZER A CONSULTA
    # "Para cada Gênero, conte quantas Ocorrências da 'categoria_alvo' existem"
    dados = GeneroTextual.objects.annotate(
        total_conectores=Count('texto__ocorrenciaconector',
                               filter=Q(texto__ocorrenciaconector__categoria=categoria_alvo))
    ).values('nome', 'total_conectores')

    # 3. PREPARAR OS DADOS PARA O MATPLOTLIB
    generos = []
    contagens = []

    for item in dados:
        if item['total_conectores'] is not None:
            generos.append(item['nome'])
            contagens.append(item['total_conectores'])

    print(f"Dados encontrados: {list(zip(generos, contagens))}")

    # 4. USAR O MATPLOTLIB PARA VISUALIZAR
    plt.figure(figsize=(10, 6)) # Define o tamanho da imagem
    plt.bar(generos, contagens, color=['blue', 'green', 'red']) # Cria o gráfico de barras

    plt.title(f'Distribuição de Conectores de "{nome_categoria}"')
    plt.xlabel('Gênero Textual (Contexto)')
    plt.ylabel('Quantidade de Ocorrências')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 5. SALVAR O GRÁFICO
    nome_arquivo = f'grafico_{categoria_alvo}.png'
    plt.savefig(nome_arquivo)
    print(f"Gráfico salvo como '{nome_arquivo}'!")

# Executa a função
if __name__ == "__main__":
    gerar_grafico()