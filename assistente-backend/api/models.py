from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "usuario"  # nome exato no banco, minúsculo nesse carai
        managed = False       #  Django vai criar nada qui nao

