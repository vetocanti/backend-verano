from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.clave}: {self.valor}"