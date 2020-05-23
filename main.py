#TODOITS - Javascript
#Crear tareas
#Revisar tareas
#Modificar tarea 
#Eliminar tarea
#CRUD Create - Read - Update  Delete 
opcion = " "
tarea = " "

def opciones():
  print("A. Ingresar una nueva tarea")
  print("B. Mostrar las tareas pendientes")
  print("C. Modificar tareas disponibles")
  print("D. Eliminar las tareas")
  print("E. Salir del programa")
  opcion = input("Ingrese aquí la opción deseada: ")
  return opcion
  

opcion = opciones()
while (opcion != "E" ):
  if(opcion == "A"):
    tarea = input("Ingrese su tarea: ")
    print("Se guardo su tarea con exito")
    opcion = opciones()
  
  elif(opcion == "B"):
    print("Tareas pendientes")
    print("1. "+ tarea)
    opcion = opciones()
  
  elif(opcion == "C"):
    tarea = input("Ingrese su nueva tarea")
    print("Se modifico la tarea con exito")
    opcion = opciones()
  
  elif(opcion == "D"):
    tarea = " "
    print("Se elimino la tarea con exito")
    opcion = opciones()
  

