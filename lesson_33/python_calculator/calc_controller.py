from functools import partial

from lesson_33.python_calculator.calc_eval import ERROR_MSG


class PyCalcCtrl:
    """PyCalc Controller class."""

    def __init__(self, model, view):
        """Controller initializer."""
        self._view = view
        self._evaluate = model
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.displayText)
        self._view.displayText = result

    def _buildExpression(self, sub_exp):
        """Build expression."""

        if self._view.displayText == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText + sub_exp
        self._view.displayText = expression

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C', 'CE'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['CE'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['C'].clicked.connect(self._view.clearLast)


if __name__ == '__main__':
    pass
