import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from lesson_33.python_calculator.calc_controller import PyCalcCtrl
from lesson_33.python_calculator.calc_eval import evaluate


class PyCalcUi(QMainWindow):

    def __init__(self):
        """View initializer."""
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setFixedSize(250, 250)

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display."""
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'CE': (0, 0),
                   'C': (0, 1),
                   '(': (0, 2),
                   ')': (0, 3),
                   '7': (1, 0),
                   '8': (1, 1),
                   '9': (1, 2),
                   '/': (1, 3),
                   '4': (2, 0),
                   '5': (2, 1),
                   '6': (2, 2),
                   '*': (2, 3),
                   '1': (3, 0),
                   '2': (3, 1),
                   '3': (3, 2),
                   '-': (3, 3),
                   '0': (4, 0),
                   '^': (4, 1),
                   '=': (4, 2),
                   '+': (4, 3),
                   }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(35, 35)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    @property
    def displayText(self):
        """Get display's text."""
        return self.display.text()

    @displayText.setter
    def displayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def clearDisplay(self):
        """Clear the display."""
        self.displayText = ''

    def clearLast(self):
        self.displayText = self.displayText[:-1]
        self.display.setFocus()


def main():
    """Main function."""
    py_calc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = evaluate
    PyCalcCtrl(model=model, view=view)
    sys.exit(py_calc.exec_())


if __name__ == '__main__':
    main()
