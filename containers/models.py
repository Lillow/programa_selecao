from django.db import models


class Container(models.Model):
    cliente = models.CharField(max_length=100)
    numero_container = models.CharField(max_length=11, unique=True)
    tipo = models.CharField(max_length=2, choices=[("20", "20"), ("40", "40")])
    status = models.CharField(
        max_length=5, choices=[("Cheio", "Cheio"), ("Vazio", "Vazio")]
    )
    categoria = models.CharField(
        max_length=12,
        choices=[("Importação", "Importação"), ("Exportação", "Exportação")],
    )

    def __str__(self):
        return f"{self.numero_container} - {self.cliente}"
