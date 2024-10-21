from containers.models import Container
from django.db import models


class Movement(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    tipo_movimentacao = models.CharField(
        max_length=20,
        choices=[
            ("Embarque", "Embarque"),
            ("Descarga", "Descarga"),
            ("Gate In", "Gate In"),
            ("Gate Out", "Gate Out"),
            ("Reposicionamento", "Reposicionamento"),
            ("Pesagem", "Pesagem"),
            ("Scanner", "Scanner"),
        ],
    )
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()

    def __str__(self):
        return f"{self.tipo_movimentacao} - {self.container.numero_conteiner}"
