from django.urls import path, include
from .views import *
from .views import lista_resultados_economicos
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name='inicio'),
    path('acciones/', lista_acciones, name='lista_acciones'),
    path('compras/', lista_compras, name='lista_compras'),
    path('resultados/', lista_resultados_economicos, name='lista_resultados'),
    path('ceos/', lista_ceos, name='lista_ceos'),
    path("etfs/",lista_etf, name='lista_etfs'),
    path('lista_bkn/', lista_bkn, name='lista_bkn'),
    
    

    #---------------------------------------------------------------------------
    #URLS para FORMULARIOS CRUDS sección "Create"
    #---------------------------------------------------------------------------

    path('agregar/', agregar_accion, name='agregar_accion'),#formulario para agregar acciones 
    path('agregar-ceo/', agregar_ceo, name='agregar_ceo'), #formulario para agregar ceos
    path('agregar-resultado/', agregar_resultado, name='agregar_resultado'), #formulario para agregar resultados economicos
    path('agregar_etf/',agregar_etf, name='agregar_etf'), # formulario para agregar etf
    path('agregar_bkn/', agregar_bkn, name='agregar_bkn'), # formulario para agregar breaking news

#------------------------------------------------------------------------------
#URLS Para CRUDS : sección "Update y Deletes"
#-------------------------------------------------------------------------------

    path('acciones/updateAccion/<int:id_accion>/',updateAccion, name='update_accion'), #url para hacer un update de las acciones a monitorear, permite editar cualquier campo, simbolo, descripcion, fecha de fundacion
    path('acciones/deleteAccion/<int:id_accion>/', deleteAccion, name='deleteAccion'), #url para hacer un borrar las acciones a monitorear
    path('editar-ceo/<int:ceo_id>/',editar_ceo, name='editar_ceo'), #url para editar informacion financiera de empresas
    path('eliminar-ceo/<int:id_ceo>/',eliminar_ceo, name='eliminar_ceo'), #url para borrar informacion financiera de empresas
    path('editar-etf/<int:etf_id>/', editar_etf, name='editar_etf'), # url para editar etf
    path('eliminar-etf/<int:etf_id>/', eliminar_etf, name='eliminar_etf'), #url para eliminar etf
    path('editar_bkn/<int:bkn_id>/', editar_bkn, name='editar_bkn'), # URL para editar una BKN específica
    path('borrar_bkn/<int:bkn_id>/', borrar_bkn, name='borrar_bkn'),  # URL para borrar una BKN específica

#------------------------------------------------------------------

    path('federico_secondo/',federico_secondo, name='federico_secondo'), # url para el hablar sobre mi solicitado en la pauta
  
#--------------------------------------------------------------------

# url para el log in

    path('login/',login_request, name='login'),
    path('logout/',LogoutView.as_view(template_name="acciones/logout.html"), name='logout'),
    path('register/', register, name="register"),
    

    

]




    

    