from rest_framework import serializers
from apps.productos.models import productos, Pedido, Estado
from django.contrib.auth.models import User

class EstadoSerializer(serializers.ModelSerializer):
    estado = serializers.CharField()
    class Meta:
        model = Estado
        fields = ('estado', 'id_estado')

class ProductoSerializer(serializers.ModelSerializer):
    # nombre = serializers.CharField()
    descripcion = serializers.CharField()
    class Meta:
        model = productos
        fields = ('id_producto', 'nombre', 'descripcion', 'precioVenta')

class PedidoSerializer(serializers.ModelSerializer):
    id_ped = serializers.CharField()
    id_prod = ProductoSerializer(many=True, read_only=True)
    estado = serializers.CharField()
    fecha = serializers.DateTimeField()

    class Meta:
        model = Pedido
        fields = ('id_ped', 'id_prod', 'estado', 'fecha')

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('Password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data
        

