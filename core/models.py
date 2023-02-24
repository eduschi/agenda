from django.db import models
from django.contrib.auth.models import User

#


class Evento(models.Model):
    #cria a tabela
    titulo = models.CharField(max_length=100)
    #caracters maximo
    descricao = models.TextField(blank=True, null=True)
    #pode ser em branco ou nulo
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    #customizar o nome
    data_criacao = models.DateTimeField(auto_now=True)
    #auto preenche com a funçao now()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #chave estrangeira para separar por usuario, on_delete se apagar o usuario exclui os eventos

    class Meta:
        #parametro para o nome da tabela no banco de dados ser evento
        db_table = 'evento'

    def __str__(self):
        #muda o nome do objeto para o titulo
        return self.titulo

