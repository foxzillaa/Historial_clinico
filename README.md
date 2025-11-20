# Historial_clinico
Sistema de gestión de historias clínicas desarrollado en Python para administrar la información de pacientes en un entorno hospitalario. El sistema permite registrar pacientes, gestionar altas, consultar información y mantener un historial clínico completo de cada paciente.

Características Principales:
- Sistema de Autenticación: Acceso seguro para personal médico autorizado
- Gestión de Pacientes: Registro y administración de información de pacientes
- Historias Clínicas: Registro y consulta de historiales médicos
- Control de Fechas: Gestión de fechas de ingreso y alta
- Almacenamiento Persistente: Datos guardados en archivo CSV
- Validación de Datos: Verificación de entradas y manejo de errores

Tecnologias utilizadas:
- Python 3.13
- Módulos estándar: os, csv, datetime
- Almacenamiento en archivos CSV
- Programación orientada a objetos

Estructura del proyecto:
historial_clinico.py
├── Clase HistoriaClinica
│   ├── __init__ (Inicialización del sistema)
│   ├── gestion_acceso (Autenticación de médicos)
│   ├── registra_paciente (Registro de nuevos pacientes)
│   ├── consulta_info_paciente (Consulta de información)
│   ├── alta_paciente (Gestión de altas médicas)
│   ├── registra_historia_clinica (Registro de visitas)
│   ├── consulta_historia_clinica (Consulta de historial)
│   ├── mostrar_menu (Interfaz de usuario)
│   └── ejecutar_opcion (Flujo principal)

Manejo de Errores.
El sistema incluye manejo robusto de excepciones para:
- Archivos no encontrados
- Entradas inválidas del usuario
- Errores de formato
- Accesos no autorizados

Flujo de Trabajo:
- Autenticación → Médico ingresa credenciales
- Menú Principal → Selección de operación
- Ejecución → Procesamiento de la opción seleccionada
- Persistencia → Guardado automático de datos
- Navegación → Retorno al menú o salida del sistema

Posibles Mejoras Futuras
- Búsqueda avanzada de pacientes
- Reportes y estadísticas
- Backup automático de datos
- Interfaz web o gráfica
- Encriptación de datos sensibles

Sistema desarrollado con enfoque en:
- Modularidad: Código organizado y mantenible
- Escalabilidad: Fácil expansión de funcionalidades
- Usabilidad: Interfaz intuitiva para el usuario
- Robustez: Manejo completo de errores

NOTA: Este sistema utiliza datos completamente ficticios y está diseñado exclusivamente con fines demostrativos y educativos. No contiene información médica real de ningún paciente.
