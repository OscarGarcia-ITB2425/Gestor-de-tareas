
---

### **Proyecto 2: Gestor de Tareas por Línea de Comandos**
Un programa en Python para gestionar tareas desde la terminal. Incluye funcionalidades para añadir, listar, marcar como completadas y eliminar tareas. Ideal para aprender a trabajar con archivos y organizar datos.

#### Archivos del proyecto:
1. **`gestor_tareas.py`**: Código principal.
2. **`README.md`**: Instrucciones de uso.
3. **`tareas.txt`**: Archivo de almacenamiento de las tareas.

#### Código principal (`gestor_tareas.py`):
```python
import os

ARCHIVO_TAREAS = "tareas.txt"

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r") as file:
        return [linea.strip() for linea in file.readlines()]

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as file:
        for tarea in tareas:
            file.write(tarea + "\n")

def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea(tarea):
    tareas = cargar_tareas()
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea añadida con éxito.")

def eliminar_tarea(indice):
    tareas = cargar_tareas()
    try:
        tarea_eliminada = tareas.pop(indice - 1)
        guardar_tareas(tareas)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    except IndexError:
        print("Índice no válido.")

def menu():
    while True:
        print("\nGestor de Tareas")
        print("1. Listar tareas")
        print("2. Añadir tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_tareas()
        elif opcion == "2":
            tarea = input("Escribe la nueva tarea: ")
            agregar_tarea(tarea)
        elif opcion == "3":
            listar_tareas()
            indice = int(input("Número de la tarea a eliminar: "))
            eliminar_tarea(indice)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
