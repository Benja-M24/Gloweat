from rest_framework import serializers
from apps.productos.models import productos, Pedido, Estado
from django.contrib.auth.models import User

class EstadoSerializer(serializers.ModelSerializer):
    estado = serializers.CharField()
    class Meta:
        model = Estado
        fields = ('estado', 'id_estado')

class PedidoSerializer(serializers.ModelSerializer):
    id_estado = EstadoSerializer(many=True, read_only=True)
    class Meta:
        model = Pedido
        fields = ('id_ped', 'fecha', 'id_est')

class ProductoSerializer(serializers.ModelSerializer):
    id_producto = serializers.CharField()
    id_ped = PedidoSerializer(many = True, read_only=True)
    descripcion = serializers.CharField()
    class Meta:
        model = productos
        fields = ('id_producto', 'nombre', 'descripcion', 'precioVenta')

class ConsultaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=False, allow_blank=True, max_length=100)
    descripcion = serializers.CharField(style={'base_template': 'textarea.html'})
    precioVenta = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return productos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

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
        

