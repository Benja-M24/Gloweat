from django.db import models

class categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',max_length=100, blank=False, null=False) 

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'  

    def __str__(self):
        return self.nombre  

class productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    #img = models.CharField(max_length=500, blank=False, null=False)
    precioVenta = models.DecimalField(max_digits=9, decimal_places=2)
    id_cate = models.ForeignKey(categorias, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField('Estado de producción',max_length=100, blank=False, null=False) 

    def __str__(self):
        return self.estado
    
class Pedido(models.Model):
    id_ped = models.AutoField(primary_key=True)
    id_prod = models.ForeignKey(productos, on_delete = models.CASCADE)
    fecha = models.DateField( blank=False, null=False)
    id_est = models.ForeignKey(Estado, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'