import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  # Inicializa la interfaz de usuario

    def init_ui(self):
        # Configura el título y tamaño de la ventana
        self.setWindowTitle('Ingresar Clave Secreta')
        self.setGeometry(100, 100, 300, 200)

        # Crea etiquetas y campos de entrada
        self.instrucciones_label = QLabel('Ingresa tu clave secreta:', self)  # Etiqueta de instrucciones
        self.instrucciones_label.setAlignment(Qt.AlignCenter)  # Alinea el texto al centro

        self.clave_input = QLineEdit(self)  # Campo de entrada para la clave
        self.clave_input.setEchoMode(QLineEdit.Password)  # Oculta la entrada con asteriscos para simular una contraseña
        self.clave_input.setPlaceholderText("Clave secreta")  # Texto de marcador de posición para el campo

        # Crea los botones
        self.boton_mostrar = QPushButton('Mostrar Clave', self)  # Botón para mostrar la clave
        self.boton_limpio = QPushButton('Limpiar', self)  # Botón para limpiar el campo

        # Conecta los botones con las funciones correspondientes
        self.boton_mostrar.clicked.connect(self.mostrar_clave)  # Muestra la clave cuando se hace clic en "Mostrar Clave"
        self.boton_limpio.clicked.connect(self.limpiar)  # Limpia el campo cuando se hace clic en "Limpiar"

        # Crea una etiqueta para mostrar los resultados
        self.resultado_label = QLabel('', self)  # Etiqueta vacía para el resultado
        self.resultado_label.setAlignment(Qt.AlignCenter)  # Alinea el texto al centro

        # Establece el diseño vertical
        layout = QVBoxLayout()
        layout.addWidget(self.instrucciones_label)  # Añade la etiqueta de instrucciones
        layout.addWidget(self.clave_input)  # Añade el campo de entrada de la clave
        layout.addWidget(self.boton_mostrar)  # Añade el botón "Mostrar Clave"
        layout.addWidget(self.boton_limpio)  # Añade el botón "Limpiar"
        layout.addWidget(self.resultado_label)  # Añade la etiqueta de resultado

        self.setLayout(layout)  # Aplica el diseño a la ventana principal

    def mostrar_clave(self):
        # Obtiene la clave ingresada
        clave = self.clave_input.text()

        # Verifica si se ingresó una clave
        if clave:
            # Muestra la clave en la etiqueta de resultado y en un cuadro de mensaje
            self.resultado_label.setText(f'Clave ingresada: {clave}')
            QMessageBox.information(self, 'Clave Mostrada', f'Clave ingresada: {clave}')
        else:
            # Si no se ingresó clave, muestra un mensaje de error
            QMessageBox.warning(self, 'Error', 'Por favor, ingresa una clave secreta.')

    def limpiar(self):
        # Limpia el campo de entrada y la etiqueta de resultado
        self.clave_input.clear()
        self.resultado_label.clear()

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = VentanaPrincipal()  # Crea la ventana principal
    ventana.show()  #
