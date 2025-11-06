# 1. Importar Biblioteca de conexión
import pyodbc

# 2. Crear funciones 
def consultar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)

        #Parámetro de Entrada
        l_IDEstudiante = int(input("\n\n\tIngrese ID del Estudiante a Consultar: \t"))
        #Crear Cursor
        micursor = conexion.cursor()
        # 1. Ejemplo: Llamar a SP para Consulta la tabla "Estudiantes”
        SENTENCIA_SQL = "{CALL sp_ListadoEstudiantes (?)}"
        micursor.execute(SENTENCIA_SQL,(l_IDEstudiante))
        
        # Obtener los resultados  
        print("\n\n\t\t\tDatos del Estudiante:")
        rows = micursor.fetchall()
        
        #if rows:
        for row in rows:
        ##print(f"\t\t{row.NombreEstudiante}\t{row.ApellidoEstudiante}\t{row.Email}")
            print(row)

        print("\nOk ... Proceso Culminado con Exito: \n")
    finally:
        print("Conexion Cerrada: \n")
    
# Función insertar registros
def insertar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)
        #Crear Cursor
        micursor = conexion.cursor()
        # Ejemplo: Insertar Tabla Estudiantes 1 Registro
        SENTENCIA_SQL = """
        INSERT INTO Estudiantes
        (IDEstudiante,NombreEstudiante,ApellidoEstudiante,Email,Telefono)
        VALUES(?,?,?,?,?)
        """
        #one_record = ('10','Pepe','Muñoz','pepem@gmail.com','2378008')   
        #micursor.execute(SENTENCIA4_SQL, one_record)
        print("\n\t\tINSERTAR NUEVO ESTUDIANTE:\n")  
        ## Ingreso de Informacion
        l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
        l_NombreEstudiante = input("Ingrese Nombre Estudiante: \t")
        l_ApellidoEstudiante = input("Ingrese Apellido Estudiante:\t")
        l_Email = input("Ingrese Email Estudiante: \t")
        l_Telefono = input("Ingrese Telefono Estudiante:\t")   
            
        micursor.execute( SENTENCIA_SQL,(l_IDEstudiante,l_NombreEstudiante,l_ApellidoEstudiante,l_Email,l_Telefono))
        
        #Realizar Commit
        micursor.commit()
        print("\nOk ... Insercion Exitosa: \n")        
    finally:
        conexion.close()
        print("Conexion Cerrada: \n")
    
# Función eliminar registros
def eliminar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)
        
        #Crear Cursor
        micursor = conexion.cursor()
        
        SENTENCIA_SQL = """DELETE FROM Estudiantes
        WHERE IDEstudiante=?"""
        ## Ingreso de Informacion
        print("\n\t Eliminar Registro Estudiante:\n")
        l_IDEstudiante = int(input("Ingrese ID del Estudiante a Elimnar: \t"))
        
        micursor.execute( SENTENCIA_SQL,(l_IDEstudiante))
        micursor.commit()   
        print("Ok ... Eliminacion Exitosa: \n")
    finally:
        conexion.close()
        print("Conexion Cerrada: \n")

    
# Función actualizar registros
def actualizar_registro(conexion):
    try:
        conexion = pyodbc.connect(connection_string)    

        #Crear Cursor
        micursor = conexion.cursor()
        
        SENTENCIA_SQL = """UPDATE Estudiantes
        SET Email = ?
        WHERE IDEstudiante= ?"""
        ## Ingreso de Informacion
        print("\n\t Actualizar Informacion Estudiante:\n")
        l_IDEstudiante = int(input("Ingrese ID del Estudiante: \t"))
        l_Email = input("Ingrese Nuevo E-Mail Estudiante: \t")
        micursor.execute( SENTENCIA_SQL,(l_Email,l_IDEstudiante))
        
        micursor.commit()
        print("\nOk ... Actualización Exitosa: \n")   

    finally:
        conexion.close()
        print("Conexion Cerrada: \n")
        
    
    
# Función mostrar opciones
def mostrar_opciones_crud():
    print ("Opcion 1 : Crear registro")
    print ("Opcion 2 : Consultar registro")
    print ("Opcion 3 : Actualizar registro")
    print ("Opcion 4 : Eliminar registro")
    print ("Opcion 5 : Salir")


# 2. Declarar variables de Conexión
name_server ='UPEAULA-31224'
database ='UDEMYTEST1'
username ='pythonconsultor'
password = 'UDLA'
controlador_odbc='ODBC Driver 17 for SQL Server'

connection_string = f'DRIVER={controlador_odbc};SERVER={name_server};DATABASE={database};UID={username};PWD={password}'


try:
    conexion = pyodbc.connect(connection_string) 
except Exception as e:
    print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)    
# Fin Conexion de BDD
else:  
    1
    while True:
        mostrar_opciones_crud()
        opcion = input("Seleccione una opción 1-5:\t")
        if opcion == '1':
            #crear_registro(conexion)
            insertar_registro(conexion)
        elif opcion == '2':
            #leer_registros(conexion)
            consultar_registro(conexion)
        elif opcion == '3':
            actualizar_registro(conexion)
        elif opcion == '4':
            eliminar_registro(conexion)
        elif opcion == '5':
            print("Saliendo del programa..\n\n.")
            break
        else:
            print("Opción no válida.")  
            conexion.close() 
            break     
    
finally:
    print("Conexion Cerrada: \n")
