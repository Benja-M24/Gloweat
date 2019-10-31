from django.db import models
from datetime import date

class Usuario(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 200, blank = False, null = False)
    edad = models.DateField( auto_now = False , auto_now_add = False, blank = False, null = False, default = date.today)
    email = models.EmailField(max_length = 254)
    passw = models.CharField(max_length = 20, blank = False, null = False)

class Meta:
    verbose_name= "Usuario"
    verbose_name_plural = "Usuarios"

#def __str__(self):return self.apellidos