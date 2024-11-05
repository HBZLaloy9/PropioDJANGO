from django.db import models

class Genero(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)

    class Meta:
        db_table = 'Generos'


class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=0)
    is_active = models.BooleanField(default=True)  # Estado activo del usuario
    is_online = models.BooleanField(default=False)  # Estado en línea del usuario

    class Meta:
        db_table = 'Usuarios'
