from django.db import models

# Entidade 1: O Contexto
class GeneroTextual(models.Model):
    nome = models.CharField(max_length=100) # Ex: "Notícia", "Artigo de Opinião"

    def __str__(self):
        return self.nome

# Entidade 2: O Texto
class Texto(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    # A relação (chave estrangeira) que liga o Texto ao seu Gênero
    genero = models.ForeignKey(GeneroTextual, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# Entidade 3: O Elemento Categorizado
class OcorrenciaConector(models.Model):
    # Tipos de conectores (conforme o conteúdo da aula)
    CATEGORIAS = [
        ('REF', 'Referenciação'), # Ex: "este", "aquele", "ele"
        ('SUB', 'Substituição'), # Ex: "fazer o mesmo"
        ('SEQ', 'Sequenciação'),   # Ex: "portanto", "mas", "além disso"
        # Você pode adicionar mais categorias
    ]

    palavra = models.CharField(max_length=50) # Ex: "portanto"
    categoria = models.CharField(max_length=3, choices=CATEGORIAS)
    # A relação que liga esta ocorrência ao texto onde ela apareceu
    texto = models.ForeignKey(Texto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.palavra} ({self.get_categoria_display()}) em '{self.texto.titulo}'"