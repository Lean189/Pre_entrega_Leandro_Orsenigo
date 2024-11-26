#Pre entrega para coder_leandro orsenigo
Es un proyecto basado en django para la gestion cursos,estudiantes y sus profesores.
En este se incluye la funcion de agrear Curso,Estudiantes y Profesores con sus datos correspondientes


##Estructura del proyecto

-'datosapp/': Donde se encuentran los modelos,vistas,formularios y las plantillas
-'pre_entrega/' : El directorio principal de configuracion de django

## SuperUsuario:
Username = admin
Pass = 1234Lean

## Usuario: (puede ver y agrear coasas a la base de tados)
Username = leandro
Pass = 1234Lean

## Funcionalidad
La app tiene un Inicio/ el cual hereda a el resto de los templates.
por medio del incio se puede ingresar a las diversas pestañas del mismo Curso/Estudiantes/Profesores/Buscar Camada.
en los 3 primeros tiene un formulario que te deja agrear datos de cada uno en la base de datos y en el 'Buscar Camada' realiza la busqueda del curso si existe
en caso de querer probar La funcion Buscar se puede utilizar alguna ya introducida en la base de datos por ejemplo (3232) o agregar un nuevo curso y realizar la busqueda
en caso de querer borrar se usa el SuperUsuario(no se recomienda...)

###