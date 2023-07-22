from django.contrib.auth.models import Group

def agregar_permiso_context(request):
    agregar_permiso = False  # Valor predeterminado en caso de que el usuario no tenga permiso
    if request.user.is_authenticated:  # Verificar si el usuario está autenticado
        es_grupo1 = request.user.groups.filter(name='grupo1').exists()
        if es_grupo1:
            grupo_1 = Group.objects.get(name='grupo1')
            agregar_permiso = grupo_1.permissions.filter(codename='add_vehiculo').exists()
    return {'agregar_permiso': agregar_permiso}

