from django.db import models

# Create your models here.


class Colaborador(models.Model):
    rutt = models.CharField(max_length=10, primary_key=True ,verbose_name='Rut')
    nombree = models.CharField(max_length=50,verbose_name='Nombre')
    fotoo = models.ImageField(upload_to='images/', null=True, blank=True)
    emaill = models.CharField(max_length=20,verbose_name='Email')
    telefonoo = models.IntegerField(max_length=9, verbose_name='Telefono')
    diree = models.CharField(max_length=70, verbose_name='Direccion')
    paiss = models.CharField(max_length=30, verbose_name='Pais')
    contraa = models.CharField(max_length=10, verbose_name='Contraseña')
    def __str__(self):
        return(self.rutt)