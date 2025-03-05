import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

directorio_principal = os.path.dirname(__file__)

try:
    from ctypes import windll  # Código solo válido en windows
    identificador_de_aplicacion = 'desarrollo_interfaces.unidad_6.hola_mundo.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(identificador_de_aplicacion)
except ImportError:
    pass


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("PySide6 executable")

        layout = QVBoxLayout()

        label = QLabel("Hola mundo!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("Cerrar")
        button.setIcon(QIcon(os.path.join(directorio_principal, "iconos", "cerrar.png")))
        button.pressed.connect(self.close)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(directorio_principal, "iconos", "mano.ico")))
window = MainWindow()
window.show()

app.exec()