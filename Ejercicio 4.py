import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class MascotasWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Datos de Mascotas")
        layout = QVBoxLayout()  # Crea un layout vertical

        # Lista para almacenar los campos de entrada (nombre, especie, edad) de cada mascota
        self.mascotas = []

        # Bucle para generar los campos de entrada de tres mascotas
        for i in range(1, 4):
            layout.addWidget(QLabel(f"Mascota {i}"))  # Añade una etiqueta que indica el número de la mascota

            # Campo para ingresar el nombre de la mascota
            nombre = QLineEdit(self)
            nombre.setPlaceholderText(f"Nombre de la mascota {i}")  # Texto de ayuda dentro del campo
            layout.addWidget(nombre)

            # Campo para ingresar la especie de la mascota
            especie = QLineEdit(self)
            especie.setPlaceholderText(f"Especie de la mascota {i}")
            layout.addWidget(especie)

            # Campo para ingresar la edad de la mascota
            edad = QLineEdit(self)
            edad.setPlaceholderText(f"Edad de la mascota {i}")
            layout.addWidget(edad)

            # Almacena los campos de entrada en la lista 'mascotas' como una tupla
            self.mascotas.append((nombre, especie, edad))

        # Botón para mostrar los datos ingresados
        self.boton_mostrar = QPushButton("Mostrar Datos", self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)  # Conecta el clic del botón con la función 'mostrar_datos'
        layout.addWidget(self.boton_mostrar)

        # Botón para limpiar todos los campos de entrada
        self.boton_limpiar = QPushButton("Limpiar Campos", self)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)  # Conecta el clic del botón con la función 'limpiar_campos'
        layout.addWidget(self.boton_limpiar)

        # Establece el layout de la ventana
        self.setLayout(layout)

    # Función para mostrar los datos de las mascotas ingresadas
    def mostrar_datos(self):
        datos = []  # Lista para almacenar los datos de todas las mascotas

        # Bucle para recorrer cada mascota (nombre, especie, edad)
        for idx, (nombre, especie, edad) in enumerate(self.mascotas, start=1):
            nombre_text = nombre.text()  # Obtiene el texto ingresado en el campo 'nombre'
            especie_text = especie.text()  # Obtiene el texto ingresado en el campo 'especie'
            edad_text = edad.text()  # Obtiene el texto ingresado en el campo 'edad'

            # Verifica que todos los campos tengan datos
            if not nombre_text or not especie_text or not edad_text:
                QMessageBox.warning(self, 'Error', f'Por favor, completa todos los datos de la Mascota {idx}.')
                return  # Si falta algún dato, muestra una advertencia y sale de la función

            # Si los datos están completos, los añade a la lista 'datos'
            datos.append(f"Mascota {idx}:\nNombre: {nombre_text}\nEspecie: {especie_text}\nEdad: {edad_text}\n---")

        # Muestra los datos en un mensaje emergente
        QMessageBox.information(self, "Datos de Mascotas", "\n".join(datos))

    # Función para limpiar todos los campos de entrada

