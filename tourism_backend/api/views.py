
from tkinter.messagebox import RETRY
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from datetime import datetime


class indexView(APIView):
    def get(self,request):
        context = {
            'status' : True,
            'content' : 'API activo'
        }

        return Response(context)

class TuristaView(APIView):
    def get(self,request):
        data = Turista.objects.all()
        serializerData = TuristaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class TuristaDetailView(APIView):
    def get(self,request,turista_id):
        data = Turista.objects.get(pk=turista_id)
        serializerData = TuristaSerializer(data)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)


class EmpresaView(APIView):
    def get(self, request):
        data = Empresa.objects.all()
        serializerData = EmpresaSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }
        
        return Response(context)

class ServicioView(APIView):
    def get(self, request):
        data = Servicio.objects.all()
        serializerData = ServicioSerializer(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

class ServicioEmrpesaView(APIView):
    def get(self, request):
        data = ServicioEmpresa.objects.all()
        serializerData = ServicioEmpresaSerializer(data,many=True)
        
        context = {
            
            'content':serializerData.data
        }

        return Response(serializerData.data)

class ServicioEmrpesaDetailView(APIView):
    def get(self,request,servicio_empresa_id):
        data = ServicioEmpresa.objects.get(pk=servicio_empresa_id)
        serializerData = ServicioEmpresaDetailSerializer(data)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        print("--",serializer)
        print("--",request.data)

        #guardarTurista = Turista.objects.get(usuario = request.data)
 
        if serializer.is_valid():
            user = serializer.save()
            if(request.data['registro']==0):
                guardarTurista = Turista(usuario_id=user,turista_pais=request.data['pais'],turista_ciu=request.data['ciudad'],
                turista_nroDoc=request.data['nroDoc'],turista_doc=request.data['tipoDoc'],turista_tel=request.data['telefono'],
                turista_sex=request.data['sexo'],turista_fech_cre = datetime.today()
                ).save()
            else:
                guardarEmpres = Empresa(empresa_usuario_id=user,empresa_ruc=request.data['ruc'],empresa_mail=request.data['email'],empresa_rs=request.data['razon_social'],empresa_ubi=request.data['direccion'],empresa_tel=request.data['telefono'],
                empresa_web=request.data['paginaweb'],empresa_fech_cre = datetime.today()
                ).save()
            

            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaqueteView(APIView):
 

    def get(self,request):
        data = Paquete.objects.all()
        serializerData = PaqueteSerializerPOST(data,many=True)

        context = {
            'ok':True,
            'content':serializerData.data
        }

        return Response(context)

    def post(self,request):
        serializerData = PaqueteSerializerPOST(data=request.data)

        if serializerData.is_valid():
            try:
                
                serializerData.save()

                context = {
                    'ok':True,
                    'content':serializerData.data
                }

                return Response(data=context,status=status.HTTP_200_OK)
                
            except Exception as error:
                return Response(data={'message':'error en el servidor'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data={'message':'data es invalida'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
     
            


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
