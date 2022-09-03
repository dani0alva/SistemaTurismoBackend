from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class TuristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turista
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ServicioEmpresaSerializer(serializers.ModelSerializer):

    #servicio_id = serializers.PrimaryKeyRelatedField(queryset=Servicio.objects.all(), many=True)
    #empresa_id = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all(), many=True)

    class Meta:
        model = ServicioEmpresa
        fields = ['servicio_empresa_id','servicio_id','empresa_id','servicio_empresa_dur','servicio_empresa_img','servicio_empresa_pre','servicio_empresa_des']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['servicio_empresa_img'] = instance.servicio_empresa_img.url
       
        serializerServicio = ServicioSerializer(instance.servicio_id)
        serializerEmpresa = EmpresaSerializer(instance.empresa_id)
        representation['Empresa'] = serializerEmpresa.data
        representation['Servicios'] = serializerServicio.data

        return representation

class ServicioEmpresaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioEmpresa
        fields = ['servicio_empresa_id','servicio_id','empresa_id','servicio_empresa_dur','servicio_empresa_img','servicio_empresa_img_det_1','servicio_empresa_img_det_2','servicio_empresa_img_det_3','servicio_empresa_pre','servicio_empresa_des','servicio_empresa_des2']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['servicio_empresa_img'] = instance.servicio_empresa_img.url
        representation['servicio_empresa_img_det_1'] = instance.servicio_empresa_img_det_1.url
        representation['servicio_empresa_img_det_2'] = instance.servicio_empresa_img_det_2.url
        representation['servicio_empresa_img_det_3'] = instance.servicio_empresa_img_det_3.url

        serializerServicio = ServicioSerializer(instance.servicio_id)
        representation['Servicios'] = serializerServicio.data
        serializerEmpresa = EmpresaSerializer(instance.empresa_id)
        representation['Empresa'] = serializerEmpresa.data

        return representation

class PaqueteSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        #fields = ['servicio_empresa_id','paquete_pre','paquete_cant_ser']
        fields = '__all__'


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['id'] = user.id
        token['name'] = user.username
        # ...

        return token

