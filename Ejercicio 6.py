import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QVBoxLayout, QPushButton, QMessageBox

class TiendaComponentesWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Tienda de Componentes de Computadora")  # Título de la ventana
        layout = QVBoxLayout()  # Crea un layout vertical

        # Etiqueta que indica al usuario que seleccione un componente
        self.label = QLabel("Selecciona un componente de computadora:", self)
        layout.addWidget(self.label)  # Añade la etiqueta al layout

        # ComboBox para seleccionar un componente de computadora
        self.combo_box = QComboBox(self)
        componentes_pc = ["CPU", "RAM", "Tarjeta Gráfica", "Disco Duro", "Placa Base"]  # Lista de componentes
        self.combo_box.addItems(componentes_pc)  # Añade los componentes al combo box
        layout.addWidget(self.combo_box)  # Añade el combo box al layout

        # SpinBox para seleccionar la cantidad de unidades
        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(1, 6)  # Establece el rango de unidades (1 a 6)
        self.spin_box.setSuffix(" unidades")  # Añade un sufijo al valor (ej. " unidades")
        layout.addWidget(self.spin_box)  # Añade el spin box al layout

        # Botón para agregar el componente al carrito
        self.boton = QPushButton("Agregar al Carrito", self)
        self.boton.clicked.connect(self.mostrar_seleccion)  # Conecta el clic del botón a la función 'mostrar_seleccion'
        layout.addWidget(self.boton)  # Añade el botón al layout

        self.setLayout(layout)  # Establece el layout de la ventana

    def mostrar_seleccion(self):
        # Obtiene el componente seleccionado y la cantidad elegida
        componente_seleccionado = self.combo_box.currentText()
        cantidad_seleccionada = self.spin_box.value()

        # Muestra el resultado en un cuadro de mensaje
        QMessageBox.information(self, "Carrito", f"Has agregado {cantidad_seleccionada} unidad(es) de {componente_seleccionado} al carrito.")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Crea la aplicación
    ventana = TiendaComponentesWindow()  # Crea la ventana principal
    ventana.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Inicia el ciclo de eventos
