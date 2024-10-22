import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QFormLayout, QMessageBox

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Inicializa la interfaz de usuario

    def init_ui(self):
        # Configura el título y el tamaño de la ventana
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)

        # Crea etiquetas y campos de entrada
        self.nombre_label = QLabel('Nombre Completo:', self)  # Etiqueta para el nombre
        self.edad_label = QLabel('Edad:', self)  # Etiqueta para la edad
        self.nombre_input = QLineEdit(self)  # Campo de entrada para el nombre
        self.edad_input = QLineEdit(self)  # Campo de entrada para la edad
        self.resultado_label = QLabel('', self)  # Etiqueta para mostrar el resultado

        # Crea y conecta el botón de actualizar
        self.boton_actualizar = QPushButton('Actualizar', self)  # Botón de actualizar
        self.boton_actualizar.clicked.connect(self.actualizar_datos)  # Conecta el botón con la función `actualizar_datos`

        # Configura el diseño de la ventana con un formulario
        layout = QFormLayout()
        layout.addRow(self.nombre_label, self.nombre_input)  # Añade la etiqueta y el campo del nombre al formulario
        layout.addRow(self.edad_label, self.edad_input)  # Añade la etiqueta y el campo de la edad al formulario
        layout.addRow(self.boton_actualizar, self.resultado_label)  # Añade el botón y el campo del resultado
        self.setLayout(layout)  # Establece el diseño en el widget principal

    def actualizar_datos(self):
        # Obtiene los datos ingresados por el usuario
        nombre = self.nombre_input.text().strip()
        edad = self.edad_input.text().strip()

        # Valida que el nombre no esté vacío
        if not nombre:
            self.show_error("Por favor, ingrese un nombre.")  # Muestra un mensaje de error si el nombre está vacío
            return

        # Valida que la edad sea un número positivo
        if not edad.isdigit() or int(edad) < 0:
            self.show_error("Por favor, ingrese una edad válida (número positivo).")  # Muestra un mensaje de error si la edad no es válida
            return

        # Actualiza la etiqueta del resultado con el nombre y la edad ingresados
        self.resultado_label.setText(f'Nombre Completo: {nombre}\nEdad: {edad}')

    def show_error(self, message):
        # Muestra un cuadro de mensaje de error
        QMessageBox.warning(self, 'Error', message)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = VentanaPrincipal()  # Crea la ventana principal
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos de la aplicación
