from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('',views.indexView.as_view()),
    path('turista',views.TuristaView.as_view()),
    path('turista/<int:turista_id>',views.TuristaDetailView.as_view()),
    path('empresa',views.EmpresaView.as_view()),
    path('servicio',views.ServicioView.as_view()),
    path('servicioempresa/',views.ServicioEmrpesaView.as_view()),
    path('servicioempresa/<int:servicio_empresa_id>',views.ServicioEmrpesaDetailView.as_view()),
    path('paquete/',views.PaqueteView.as_view()),
    path('user/create/',views.CustomUserCreate.as_view()),
    path('token/obtain/', views.ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', views.LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist')
]