from django.db import models
#from datetime import date

class categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',max_length=100, blank=False, null=False) 
    #estado = models.BooleanField('Categoria Activada/Categoria no Activada', default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'  

    def __str__(self):
        return self.nombre  

class productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    #img = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    precioVenta = models.DecimalField(max_digits=9, decimal_places=2)
    #fecha = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False, default=date.today)
    id_cate = models.ForeignKey(categorias, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre