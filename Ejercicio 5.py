import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class PersonaWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Datos de una Persona")  # Título de la ventana
        layout = QVBoxLayout()  # Crea un layout vertical

        self.caracteristicas = []  # Lista para almacenar los campos de características

        # Lista de características específicas que se van a pedir al usuario
        caracteristicas_especificas = [
            "Altura (cm)", "Peso (kg)", "Color de cabello", "Color de ojos", "Tono de piel",
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración"
        ]

        # Crear campos de entrada para cada característica
        for i, caracteristica in enumerate(caracteristicas_especificas, start=1):
            label = QLabel(f"{i}. {caracteristica}", self)  # Crea una etiqueta para la característica
            layout.addWidget(label)  # Añade la etiqueta al layout

            campo = QLineEdit(self)  # Crea un campo de entrada
            campo.setPlaceholderText(f"Ingrese {caracteristica}")  # Establece un texto de ayuda
            layout.addWidget(campo)  # Añade el campo al layout

            self.caracteristicas.append(campo)  # Guarda el campo en la lista de características

        # Botón para mostrar los datos ingresados
        self.boton_mostrar = QPushButton("Mostrar Datos", self)
        self.boton_mostrar.clicked.connect(self.mostrar_datos)  # Conecta el clic del botón a la función 'mostrar_datos'
        layout.addWidget(self.boton_mostrar)  # Añade el botón al layout

        # Botón para limpiar los campos de entrada
        self.boton_limpiar = QPushButton("Limpiar Campos", self)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)  # Conecta el clic del botón a la función 'limpiar_campos'
        layout.addWidget(self.boton_limpiar)  # Añade el botón al layout

        self.setLayout(layout)  # Establece el layout de la ventana

    def mostrar_datos(self):
        # Lista de nombres de las características para mostrar
        caracteristicas_especificas = [
            "Altura", "Peso", "Color de cabello", "Color de ojos", "Tono de piel",
            "Personalidad", "Habilidades", "Emociones predominantes", "Nivel de estrés", "Capacidad de concentración"
        ]

        datos = []  # Lista para almacenar los datos ingresados
        # Recorre los campos de entrada y sus nombres correspondientes
        for idx, (campo, nombre) in enumerate(zip(self.caracteristicas, caracteristicas_especificas), start=1):
            valor = campo.text()  # Obtiene el texto del campo
            if not valor:  # Verifica si el campo está vacío
                QMessageBox.warning(self, 'Error', f'Por favor, complete el campo: {nombre}.')  # Muestra advertencia
                return  # Sale de la función si hay un campo vacío
            datos.append(f"{nombre}: {valor}")  # Añade el valor a la lista de datos

        # Muestra un cuadro de información con los datos ingresados
        QMessageBox.information(self, "Datos de la Persona", "\n".join(datos))

    def limpiar_campos(self):
        # Limpia todos los campos de entrada
        for campo in self.caracteristicas:
            campo.clear()  # Limpia el contenido de cada campo

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = PersonaWindow()  # Crea la ventana principal
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Inicia el ciclo de eventos
