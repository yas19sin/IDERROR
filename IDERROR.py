import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

form_ui = 'design/Editor.ui'


class Editor(QMainWindow):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.ui = loadUi(form_ui)

    def Setup(self):
        self.ui.setFixedSize(800, 800)
        self.editor = QsciScintilla()
        self.editor.setText("Hello\n")
        self.editor.append("world")
        self.editor.setLexer(None)
        self.editor.setUtf8(True)  # Set encoding to UTF-8
        self.Font = QFont()
        self.Font.setPointSize(14)
        self.editor.setFont(self.Font)  # Will be overridden by lexer!
        self.layout = self.ui.centralWidget().layout()
        #self.ui.addWidget(self.editor)

        # show ui
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = Editor()
    myGUI.Setup()

    sys.exit(app.exec_())
