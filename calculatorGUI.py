import PyQt6.QtWidgets as wid
from sys import argv
from calc_server import recieve

class MainWindow(wid.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Calculator")
        self.label = wid.QLabel("")
        
        self.algo = ""
        self.clearButton = wid.QPushButton("Clear")
        self.clearButton.clicked.connect(self.clear)

        self.deleteButton = wid.QPushButton("Delete")
        self.deleteButton.setShortcut("backspace")
        self.deleteButton.clicked.connect(self.delete)

        buttonOne = wid.QPushButton("1")
        buttonOne.setShortcut("1")
        buttonOne.clicked.connect(lambda: self.clicked_button(buttonOne.text()))
        buttonTwo = wid.QPushButton("2")
        buttonTwo.setShortcut("2")
        buttonTwo.clicked.connect(lambda: self.clicked_button(buttonTwo.text()))
        buttonThree = wid.QPushButton("3")
        buttonThree.setShortcut("3")
        buttonThree.clicked.connect(lambda: self.clicked_button(buttonThree.text()))
        buttonPlus = wid.QPushButton("+")
        buttonPlus.setShortcut("+")
        buttonPlus.clicked.connect(lambda: self.clicked_button(buttonPlus.text()))
        buttonFour = wid.QPushButton("4")
        buttonFour.setShortcut("4")
        buttonFour.clicked.connect(lambda: self.clicked_button(buttonFour.text()))
        buttonFive = wid.QPushButton("5")
        buttonFive.setShortcut("5")
        buttonFive.clicked.connect(lambda: self.clicked_button(buttonFive.text()))
        buttonSix = wid.QPushButton("6")
        buttonSix.setShortcut("6")
        buttonSix.clicked.connect(lambda: self.clicked_button(buttonSix.text()))
        buttonSub = wid.QPushButton("-")
        buttonSub.setShortcut("-")
        buttonSub.clicked.connect(lambda: self.clicked_button(buttonSub.text()))
        buttonSeven = wid.QPushButton("7")
        buttonSeven.setShortcut("7")
        buttonSeven.clicked.connect(lambda: self.clicked_button(buttonSeven.text()))
        buttonEight = wid.QPushButton("8")
        buttonEight.setShortcut("8")
        buttonEight.clicked.connect(lambda: self.clicked_button(buttonEight.text()))
        buttonNine = wid.QPushButton("9")
        buttonNine.setShortcut("9")
        buttonNine.clicked.connect(lambda: self.clicked_button(buttonNine.text()))
        buttonMul = wid.QPushButton("*")
        buttonMul.setShortcut("*")
        buttonMul.clicked.connect(lambda: self.clicked_button(buttonMul.text()))
        buttonZero = wid.QPushButton("0")
        buttonZero.setShortcut("0")
        buttonZero.clicked.connect(lambda: self.clicked_button(buttonZero.text()))
        buttonDot = wid.QPushButton(".")
        buttonDot.setShortcut(".")
        buttonDot.clicked.connect(lambda: self.clicked_button(buttonDot.text()))
        buttonEqual = wid.QPushButton("=")
        buttonEqual.setShortcut("return")
        buttonEqual.clicked.connect(self.equal)
        buttonDiv = wid.QPushButton("/")
        buttonDiv.setShortcut("/")
        buttonDiv.clicked.connect(lambda: self.clicked_button(buttonDiv.text()))
        buttonLeftParen = wid.QPushButton("(")
        buttonLeftParen.setShortcut("(")
        buttonLeftParen.clicked.connect(lambda: self.clicked_button(buttonLeftParen.text()))
        buttonRightParen = wid.QPushButton(")")
        buttonRightParen.setShortcut(")")
        buttonRightParen.clicked.connect(lambda: self.clicked_button(buttonRightParen.text()))

        grid = wid.QGridLayout()
        grid.addWidget(buttonLeftParen, 0, 0)
        grid.addWidget(buttonRightParen, 0, 1)
        grid.addWidget(self.deleteButton, 0, 2)
        grid.addWidget(self.clearButton, 0, 3)
        grid.addWidget(buttonOne, 1, 0)
        grid.addWidget(buttonTwo, 1, 1)
        grid.addWidget(buttonThree, 1, 2)
        grid.addWidget(buttonPlus, 1, 3)
        grid.addWidget(buttonFour, 2, 0)
        grid.addWidget(buttonFive, 2, 1)
        grid.addWidget(buttonSix, 2, 2)
        grid.addWidget(buttonSub, 2, 3)
        grid.addWidget(buttonSeven, 3, 0)
        grid.addWidget(buttonEight, 3, 1)
        grid.addWidget(buttonNine, 3, 2)
        grid.addWidget(buttonMul, 3, 3)
        grid.addWidget(buttonZero, 4, 0)
        grid.addWidget(buttonDot, 4, 1)
        grid.addWidget(buttonEqual, 4, 2)
        grid.addWidget(buttonDiv, 4, 3)
        
        vbox = wid.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(grid)
        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

    def clicked_button(self, button):
        self.algo += button
        self.label.setText(self.algo)
    
    def equal(self):
        self.label.setText(str(recieve(self.algo)))
        self.algo = ""
    
    def clear(self):
        self.label.setText("")
        self.algo = ""
    
    def delete(self):
        self.algo = self.algo[:len(self.algo)-1]
        self.label.setText(self.algo)


def main():
    app = wid.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()