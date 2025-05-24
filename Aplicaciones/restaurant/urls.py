from django.urls import path
from Aplicaciones.restaurant.views import menu_views, bebidas_views, ubicacion_views, almuerzos_views
from django.contrib.auth import views as auth_views #se importa vistas de django y particularmente la de auth y se declara como auth_view
from .views.login_views import CustomLoginForm #viene de la clase de views login


urlpatterns = [
    #menus
    path('', menu_views.inicio, name='inicio'),
    path('menu/', menu_views.todo_menu, name='lista_menu'),
    path('crear_menu/', menu_views.crear_menu, name='nuevo_menu'),
    path('eliminar_menu/<int:id>', menu_views.eliminar_menu, name='menu_borrado'),
    path('tabla_menu/', menu_views.tabla_menu, name='lista_menus'),
    path('modificar_menu/<int:id>', menu_views.modificar_menu, name='menu_modificado'),
    
    #bebidas
    path('bebidas/', bebidas_views.todo_bebidas, name='lista_bebidas'),
    path('tabla_bebidas/', bebidas_views.tabla_bebidas, name='tabla_bebidas'),
    path('eliminar_bebida/<int:id>', bebidas_views.eliminar_bebida, name='bebida_eliminada'),
    path('crear_bebida/', bebidas_views.crear_bebida, name='nueva_bebida'),
    path('modificar_bebida/<int:id>', bebidas_views.modificar_bebida, name='bebida_modificada'),
    
    #almuerzos
    path('almuerzos/', almuerzos_views.almuerEjec, name='almuerzodia'),
    path('tabla_almuerzos/', almuerzos_views.tabla_almuerzo, name='tabla_almuerzo'),
    path('eliminar_almuerzo/<int:id>', almuerzos_views.eliminar_almuerzo, name='almuerzo_eliminado'),
    path('crear_almuerzo/', almuerzos_views.crear_almuerzo, name='nuevo_almuerzo'),
    path('modificar_almuerzo/<int:id>', almuerzos_views.editar_almuerzo, name='almuerzo_modificado'),
    
    
    #autenticacion
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html", authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
    
    path('contacto/', ubicacion_views.latia, name="latia"),
    path('latia/', ubicacion_views.contacto, name="contacto"),
    path('ubicacion/', ubicacion_views.ubicacion, name="ubicacion"),
]
