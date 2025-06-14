from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "usuario"  # nome exato no banco, minúsculo
        managed = False       # não deixar o Django tentar criar a tabela

