import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle('Ingresar Cédula y Nombre')
        self.setGeometry(100, 100, 300, 250)  # Establece la posición y el tamaño de la ventana

        # Crear etiquetas para los campos de entrada
        self.cedula_label = QLabel('Número de Cédula:', self)  # Etiqueta para la cédula
        self.nombre_label = QLabel('Nombre Completo:', self)    # Etiqueta para el nombre

        # Etiqueta para mostrar resultados
        self.resultado_label = QLabel('', self)  # Inicialmente vacía
        self.resultado_label.setAlignment(Qt.AlignCenter)  # Alineación centrada

        # Campos de entrada
        self.cedula_input = QLineEdit(self)  # Campo de entrada para la cédula
        self.cedula_input.setPlaceholderText("Número de cédula")  # Texto de ayuda
        self.nombre_input = QLineEdit(self)  # Campo de entrada para el nombre
        self.nombre_input.setPlaceholderText("Nombre completo")  # Texto de ayuda

        # Botón para mostrar los datos ingresados
        self.boton_mostrar = QPushButton('Mostrar Datos', self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)  # Conecta el clic del botón a la función 'mostrar_datos'

        # Botón para limpiar los campos de entrada
        self.boton_limpiar = QPushButton('Limpiar Campos', self)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)  # Conecta el clic del botón a la función 'limpiar_campos'

        # Disposición de la interfaz usando un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.cedula_label)  # Añade la etiqueta de cédula al layout
        layout.addWidget(self.cedula_input)  # Añade el campo de entrada de cédula
        layout.addWidget(self.nombre_label)  # Añade la etiqueta de nombre
        layout.addWidget(self.nombre_input)  # Añade el campo de entrada de nombre
        layout.addWidget(self.boton_mostrar)  # Añade el botón de mostrar datos
        layout.addWidget(self.boton_limpiar)  # Añade el botón de limpiar campos
        layout.addWidget(self.resultado_label)  # Añade la etiqueta de resultado

        self.setLayout(layout)  # Establece el layout de la ventana

    def mostrar_datos(self):
        # Obtiene el texto de los campos de entrada
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        # Verifica que ambos campos tengan datos
        if cedula and nombre:
            # Muestra los datos en la etiqueta de resultado
            self.resultado_label.setText(f'Cédula: {cedula}\nNombre: {nombre}')
        else:
            # Si falta algún dato, muestra un mensaje de advertencia
            QMessageBox.warning(self, 'Error', 'Por favor, ingresa ambos datos.')

    def limpiar_campos(self):
        # Limpia los campos de entrada y el resultado
        self.cedula_input.clear()  # Limpia el campo de cédula
        self.nombre_input.clear()  # Limpia el campo de nombre
        self.resultado_label.clear()  # Limpia la etiqueta de resultado

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = VentanaPrincipal()  # Crea la ventana principal
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Inicia el ciclo de eventos

