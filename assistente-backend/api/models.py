from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "usuario"  # nome exato no banco, minúsculo nesse carai
        managed = False       #  Django vai criar nada qui nao

class Materia(models.Model):
    class Meta:
        db_table = 'materia'

    nome = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Prova(models.Model):
    class Meta:
        db_table = 'prova'

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()

class Trabalho(models.Model):
    class Meta:
        db_table = 'trabalho'

    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    descricao = models.TextField()