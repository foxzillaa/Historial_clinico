import os
import csv
from datetime import datetime
class HistoriaClinica:
    #Decidi crear una clase para poder encapsular la funcionalidad relacionada con las historias clínicas.
    #De esta manera, el codigo es modular y facil de mantener y entender.
    #Ademas, permite una expansión futura si se desea agregar más funcionalidades relacionadas con las historias clínicas.
    def __init__(self):
        #Inicializo los atributos necesarios para la clase.
        #El archivo de historias clínicas se define como un atributo de la clase.
        #Esto permite que todas las instancias de la clase compartan el mismo archivo.
        #Los pacientes y médicos se definen como diccionarios para facilitar la búsqueda y el acceso a la información.
        self.ARCHIVO_HISTORIAS = "historias_clinicas.csv"
        self.pacientes = {
        '00000000A': ['Luis Martin', 34, '10-06-2024', '17-06-2024'],
        '11111111B': ['Maria Diaz', 41, '17-06-2024', None],
    }
        self.medicos = {
    1234: 'IEP2024',
    5555: 'M4DR1D'
        }

    def consulta_historia_clinica(self, id_paciente):
        #Este metodo permite consultar el historial clinico de un paciente dado su ID.
        #Se utiliza el archivo CSV para almacenar y recuperar la información de las visitas.
        #Si el archivo no existe o no se encuentra, se maneja la excepción y se informa al usuario.
        try: 
            with open(self.ARCHIVO_HISTORIAS, mode = 'r', newline = '') as file:
                
                reader = csv.DictReader(file)
                visitas = [row for row in reader if row['id_paciente'] == id_paciente]
            # Si no se encuentra el paciente, se informa al usuario.
                if not visitas:
                    print(f"No se encontraron registros para el paciente con DNI: {id_paciente}.")
                    return
            # Si se encuentran registros, se imprimen las visitas del paciente.
                print(f"\nHistorial clínico del paciente con ID {id_paciente}:")
                for visita in visitas:
                    print(f"Fecha: {visita['fecha_visita']}, - Notas: {visita['notas']}")
        # Se maneja la excepción si el archivo no existe o no se puede leer.
        except FileNotFoundError:
            print("El archivo de historias clínicas no existe.")
        except Exception as e:
            print(f"Error al consultar historias clinicas: {e}")
            
    def registra_historia_clinica(self, id_medico):
      #Este metodo permite registrar una nueva historia clínica para un paciente.
        try: 
            id_paciente = input("Introduce el ID del paciente: ").strip()
            if id_paciente not in self.pacientes:
                print(f"El paciente con ID {id_paciente} no existe.")
                return False
            notas = input("Introduce las notas de la visita: ").strip()
            fecha_actual = datetime.now().strftime("%d-%m-%Y")
            #Se usa os.path.exists para verificar si el archivo ya existe.
            #Si el archivo no existe o está vacío, se escribe el encabezado.
            #Si el archivo ya existe y tiene contenido, se agrega la nueva historia clínica al final
            escribir_encabezado = not os.path.exists(self.ARCHIVO_HISTORIAS) or os.stat(self.ARCHIVO_HISTORIAS).st_size == 0
            #Se abre el archivo en modo append para agregar la nueva historia clínica.
            #Se utiliza csv.DictWriter para escribir las historias clínicas en formato CSV.
            #Se escribe el encabezado solo si el archivo es nuevo o está vacío.
            with open(self.ARCHIVO_HISTORIAS, mode = 'a', newline = '') as file:
                writer = csv.DictWriter(file, fieldnames = ['id_paciente', 'id_medico', 'fecha_visita', 'notas'])
                if escribir_encabezado:
                    writer.writeheader()
                writer.writerow({
                    'id_paciente': id_paciente,
                    'id_medico': id_medico,
                    'fecha_visita': fecha_actual,
                    'notas': notas
                })
                print("Registro guardado correctamente.")
                return True
        # Si ocurre un error durante el registro, se maneja la excepción y se informa al usuario.      
        except Exception as e:
            print(f"Error al registrar la historia clínica: {e}")
            return False           
    def registra_paciente(self):
        #Este metodo permite registrar un nuevo paciente en el sistema.
        #Se solicita al usuario que ingrese el DNI, nombre y edad del paciente.
        #Se valida que el DNI no exista ya en el sistema y que la edad esté dentro de un rango razonable (0-120 años).
        #Si el registro es exitoso, se guarda la información del paciente en un diccionario.
        #La fecha de registro se almacena
        try:
            dni = input("Introduzca el DNI del paciente: ").strip()
            if dni in self.pacientes:
                print("Error, ya existe un paciente con ese DNI.")
                return
            nombre = input("Introduzca el nombre del paciente: ").strip()
            while True:
                try:
                    edad = int(input("Introduce la edad del paciente (0-120): "))
                    if 0 <= edad <= 120:
                        break
                    print("Error: La edad debe estar entre 0 y 120.")
                except ValueError:
                    print("Error: Por favor, introduce un número válido para la edad.")
            fecha_registro = datetime.now().strftime("%d-%m-%Y")
            self.pacientes[dni] = [nombre, edad, fecha_registro, None]
            print(f"Paciente {nombre} registrado con éxito.")
            return self.pacientes
        # Si ocurre un error durante el registro, se maneja la excepción y se informa al usuario.
        except Exception as e:
            print(f"Error al registrar el paciente: {e}")
            return self.pacientes
    def alta_paciente(self):
        #Este metodo permite dar de alta a un paciente, actualizando su fecha de alta en el sistema.
        #Se solicita al usuario que ingrese el DNI del paciente a dar de alta.
        #Si el paciente no existe, se informa al usuario.
        #Si el paciente ya tiene una fecha de alta, se pregunta al usuario si desea sobreescribirla.
        #Si el usuario confirma, se actualiza la fecha de alta con la fecha actual.
        #La fecha de alta se almacena en formato "dd-mm-YYYY".
        try:
            dni = input("Introduzca el DNI del paciente a dar de alta: ").strip()
            if dni not in self.pacientes: 
                print("Error: Paciente no encontrado.")
                return self.pacientes
    
            if self.pacientes[dni][3] is not None:
                print("Aviso: este paciente ya tenía fecha de alta anteriormente.")
                confirm = input("¿Desea sobreescribir la fecha de alta? (s/n):")
                if confirm != 's':
                    print("Operación cancelada.")
                    return self.pacientes
    
            fecha_alta = datetime.now().strftime("%d-%m-%Y")
            self.pacientes[dni][3] = fecha_alta
            print(f"Paciente {self.pacientes[dni][0]} dado de alta correctamente.")
        except Exception as e:
            print(f"Error al dar de alta al paciente: {e}")
            return self.pacientes
    def consulta_info_paciente(self, id_paciente):
    #Este metodo permite consultar la información de un paciente dado su ID.
    #Se verifica si el ID del paciente existe en el diccionario de pacientes.
    #Si el ID no existe, se informa al usuario.
    #Si el ID existe, se imprime la información del paciente, incluyendo nombre, edad,
    #fecha de ingreso y fecha de alta (si está disponible).
        if id_paciente not in self.pacientes:
            print("Error: No existe ningún paciente con ese DNI.")
            return
        nombre, edad, ingreso, alta = self.pacientes[id_paciente]
        print(f"\nInformación del paciente con ID {id_paciente}: ")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Fecha de ingreso: {ingreso}")
        print(f"Fecha de alta: {alta if alta else 'Pendiente'}")
    def gestion_acceso(self):
    #Este metodo permite gestionar el acceso de los médicos al sistema.
    #Se solicita al usuario que ingrese su ID de médico y contraseña.
    #Se valida que el ID de médico exista en el diccionario de médicos y que la contraseña sea correcta.
    #Si las credenciales son correctas, se concede el acceso.
    #Si las credenciales son incorrectas, se informa al usuario y se le permite reintentar hasta 3 veces.
    #Si se superan los 3 intentos, se informa al usuario que el acceso ha sido denegado.
    #Importante resaltar que este metodo tiene escalabilidad, ya que se pueden agregar mas seguridades en el futuro.
        intentos = 3
        while intentos > 0:
            try:
                id_medico = int(input("Introduzca su ID de médico (4 dígitos): "))
                contraseña = input("Introduzca su contraseña: ")
                if id_medico in self.medicos and self.medicos[id_medico] == contraseña:
                    print("Acceso concedido.")
                    return id_medico
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")
                    else:
                        raise ValueError("Demasiados intentos fallidos. Acceso denegado.")
            except ValueError as e:
                intentos -= 1
                if intentos > 0:
                    print(f"Error: {e}. Le quedan {intentos} intentos.")
                else:
                    raise ValueError("Acceso denegado, demasiados intentos fallidos.")
    def mostrar_menu(self):
    #Diseñamos un menú para que el usuario pueda interactuar con el sistema.
    #El menú muestra las opciones disponibles y permite al usuario seleccionar una opción.
    #Cada opción corresponde a una funcionalidad del sistema, como registrar un paciente, consultar información
        print("\n")
        print("="*30)
        print("  BIENVENIDO AL HOSPITAL")
        print("="*30)
        print("1. Registrar paciente")
        print("2. Consultar información del paciente")
        print("3. Dar de alta paciente")
        print("4. Añadir historia clínica del paciente")
        print("5. Salir")
        print ("\n")
    def ejecutar_opcion(self):
    #Metodo principal que ejecuta el sistema.
    #Gestiona el acceso del médico, muestra el menú y ejecuta las opciones seleccionadas
    #Maneja excepciones para errores de acceso y errores inesperados.
    #Permite al usuario interactuar con el sistema de manera sencilla y clara.
    #Se utiliza un bucle para permitir al usuario seleccionar opciones hasta que decida salir.
    
        try:
            id_medico = self.gestion_acceso()
            while True:
                self.mostrar_menu()
                opcion = input("Seleccione una opción (1-5): ").strip()
                if not opcion.isdigit():
                    print("Error: Por favor, introduzca un caracter valido.")
                    continue
                opcion = int(opcion)
             
                if opcion == 1:
                    self.registra_paciente()
                elif opcion == 2: 
                    dni = input("Introduzca el DNI del paciente: ").strip()
                    if dni in self.pacientes:
                        self.consulta_info_paciente(dni)
                        self.consulta_historia_clinica(dni)
                    else:
                        print("Error: Paciente no encontrado.")
                elif opcion == 3:
                    self.alta_paciente()
                elif opcion == 4:
                    self.registra_historia_clinica(id_medico)
                elif opcion == 5:
                    print("Saliendo del sistema...")
                    break
                    
                else:
                # OPCION NO VALIDA
                    print("Opción no valida. Por favor, elija una opción del 1 al 5.")
        except ValueError as e:
                    print(f"Error de acceso: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")
            # FIN DEL PROGRAMA
        finally:
            print("Gracias por usar el sistema del hospital. ¡Hasta luego!")
if __name__ == "__main__":
    sistema = HistoriaClinica()
    sistema.ejecutar_opcion()