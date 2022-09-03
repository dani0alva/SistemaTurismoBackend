
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# TABLA DE SERVICIO
class Servicio(models.Model):

    DESTINO_CHOICES = (
        ('MONTANA','Montaña'),
        ('DESIERTO','Desierto'),
        ('SELVA','Selva')
    )

    CATEGORIA_CHOICES = (
        ('AVENTURA','Aventura'),
        ('VIVENCIAL','Vivencial'),
        ('HC','Historico Cultural'),
        ('NATURALEZA','Naturaleza'),
        ('EXCLUSIVO','Exclusivo'),
        ('GASTRONOMIA','Gastronomia')
    )

    servicio_id = models.AutoField(primary_key=True)
    servicio_nom = models.CharField(max_length=100,verbose_name='Servicio')
    servicio_cat_des = models.CharField(max_length=100,choices=DESTINO_CHOICES,verbose_name='Categoria Destino')
    servicio_cat_exp = models.CharField(max_length=100,choices=CATEGORIA_CHOICES,verbose_name='Categoria Experiencia')
    servicio_dep = models.CharField(max_length=50,verbose_name='Departamento')
    servicio_pro = models.CharField(max_length=50,verbose_name='Provincia')
    servicio_dis = models.CharField(max_length=50,verbose_name='Distrito')
    servicio_ubi = models.CharField(null=True,max_length=50,verbose_name='Ubicacion')
    servicio_fech_cre = models.DateTimeField(null=True,verbose_name='Fecha de creacion')
    servicio_fech_mod = models.DateTimeField(null=True,verbose_name='Fecha de modificacion')
    servicio_est = models.BooleanField(default=True,verbose_name='Estado del servicio')

    class Meta:
        db_table = 'tbl_servicio'

    def __str__(self):
        return str(self.servicio_id)


# TABLA DE TURISTA
class Turista(models.Model):

    DOCUMENTO_CHOICES = (
        ('DNI','DNI'),
        ('PASAPORTE','Pasaporte'),
        ('CARNET','Carnet de Extranjeria'),
        ('LIBRETA','Libreta Electoral')
    )

    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino')
    )

    turista_id = models.AutoField(primary_key=True)
    usuario_id = models.OneToOneField(User,to_field='id',on_delete=models.RESTRICT,db_column='usuario_id',verbose_name='Usuario')
    turista_doc = models.CharField(max_length=25,choices=DOCUMENTO_CHOICES,verbose_name='Tipo Documento')
    turista_nroDoc = models.CharField(max_length=15,unique=True,verbose_name='Nro documento')
    turista_tel = models.CharField(max_length=15,verbose_name='Telefono')
    turista_sex = models.CharField(max_length=50,choices=SEXO_CHOICES,verbose_name='Sexo')
    turista_pais = models.CharField(max_length=50,verbose_name='Pais de origen')
    turista_ciu = models.CharField(max_length=50,verbose_name='Ciudad de Origen')
    turista_fech_cre = models.DateTimeField(null=True,verbose_name='Fecha de creacion')
    turista_fech_mod = models.DateTimeField(null=True,verbose_name='Fecha de modificacion')
    turista_est = models.BooleanField(default=True,verbose_name='Estado del turista')

    class Meta:
        db_table = 'tbl_turista'

    def __str__(self):
        return str(self.usuario_id)


# TABLA DE EMPRESA
class Empresa(models.Model):
    empresa_id = models.AutoField(primary_key=True)
    empresa_usuario_id = models.OneToOneField(User,to_field='id',on_delete=models.RESTRICT,db_column='usuario_id',verbose_name='Usuario')
    empresa_ruc = models.CharField(max_length=15,unique=True,verbose_name='R.U.C.')
    empresa_rs = models.CharField(max_length=100,unique=True,verbose_name='Razon Social')
    empresa_ubi = models.CharField(max_length=200,verbose_name='Ubicacion')
    empresa_tel = models.CharField(max_length=15,verbose_name='Telefono')
    empresa_mail = models.EmailField(max_length=50,unique=True,null=False,verbose_name='Email')
    empresa_pass = models.CharField(max_length=50,verbose_name='Password')
    empresa_web = models.CharField(null=True,max_length=75,verbose_name='Pagina Web')
    empresa_fech_cre = models.DateTimeField(null=True,verbose_name='Fecha de creacion')
    empresa_fech_mod = models.DateTimeField(null=True,verbose_name='Fecha de modificacion')
    empresa_est = models.BooleanField(default=True,verbose_name='Estado de la empresa')

    class Meta:
        db_table = 'tbl_empresa'

    def __str__(self):
        return self.empresa_rs


# TABLA INTERMEDIA SERVICIO - EMPRESA
class ServicioEmpresa(models.Model):
    servicio_empresa_id = models.AutoField(primary_key=True)
    servicio_empresa_est = models.BooleanField(default=True)
    servicio_empresa_des = models.TextField(max_length=500,verbose_name='Descripción')
    servicio_empresa_des2 = models.TextField(max_length=500,verbose_name='Descripción2')
    servicio_empresa_car = models.TextField(max_length=200,verbose_name='Caracteristica',default='')
    servicio_empresa_dur = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Duracion del Servicio')
    servicio_empresa_pre = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Precio')
    servicio_empresa_img = CloudinaryField('image',default='')
    servicio_empresa_img_det_1 = CloudinaryField('image1',default='')
    servicio_empresa_img_det_2 = CloudinaryField('image2',default='')
    servicio_empresa_img_det_3 = CloudinaryField('image3',default='')
 
    servicio_id = models.ForeignKey(
        Servicio,to_field='servicio_id',related_name='servicioEmpresa',
        on_delete=models.RESTRICT,db_column='servicio_id'
    )
    
    empresa_id = models.ForeignKey(
        Empresa,to_field='empresa_id',related_name='servicioEmpresa',
        on_delete=models.RESTRICT,db_column='empresa_id'
    )

    class Meta:
        db_table = 'tbl_servicio_empresa'

    def __str__(self):
        return str(self.servicio_empresa_id)


# TABLA PAGO - EMPRESA
class PagoEmpresa(models.Model):
    pago_empresa_id = models.AutoField(primary_key=True)
    pago_empresa_des = models.CharField(max_length=75,verbose_name='Descripcion')
    pago_empresa_mont = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Monto')
    pago_empresa_com = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='Comision')
    pago_empresa_fech = models.DateTimeField(null=True,verbose_name='Fecha de creacion')
    pago_empresa_nro = models.CharField(max_length=15,unique=True,verbose_name='Nro Comprobante')
    
    servicio_empresa_id = models.ForeignKey(
        ServicioEmpresa,to_field='servicio_empresa_id',related_name='servicio_empresa_pago_empresa',
        on_delete=models.RESTRICT,db_column='servicio_empresa_id'
    )

    class Meta:
        db_table = 'tbl_pago_empresa'

    def __str__(self):
        return self.pago_empresa_nro


# TABLA DE PAQUETE
class Paquete(models.Model):
    paquete_id = models.AutoField(primary_key=True)
    paquete_pre = models.CharField(max_length=20,verbose_name='Precio del paquete')
    paquete_cant_ser = models.IntegerField(default='0')
    paquete_fech_cre = models.DateTimeField( default=datetime.now(), null=True,verbose_name='Fecha de creacion')
    
    servicio_empresa_id = models.ForeignKey(
        ServicioEmpresa,to_field='servicio_empresa_id',related_name='servicioEmpresa',
        on_delete=models.RESTRICT,db_column='servicio_empresa_id'
    )
    
    class Meta:
        db_table = 'tbl_paquete'

    def __str__(self):
        return str(self.paquete_id)


# TABLA DE RESERVA - PAGO
class ReservaPago(models.Model):
    reserva_pago_id = models.AutoField(primary_key=True)
    reserva_pago_pre = models.CharField(max_length=20,verbose_name='Precio del paquete')
    reserva_pago_conf = models.BooleanField(verbose_name='Confirmacion pago')
    reserva_pago_fech = models.DateTimeField(null=True,verbose_name='Fecha de pago')
    
    turista_id = models.ForeignKey(
        Turista,to_field='turista_id',related_name='reservaPagoTurista',
        on_delete=models.RESTRICT,db_column='turista_id'
    )
    
    paquete_id = models.ForeignKey(
        Paquete,to_field='paquete_id',related_name='reservaPagoTurista',
        on_delete=models.RESTRICT,db_column='paquete_id'
    )

    class Meta:
        db_table = 'tbl_reserva_pago'

    def __str__(self):
        return str(self.reserva_pago_id)
