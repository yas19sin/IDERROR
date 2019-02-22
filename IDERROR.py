import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *

# specifying the location of the Design
form_ui = 'Design/Editor.ui'


class Editor(QMainWindow):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        # Loading in the Design
        self.ui = loadUi(form_ui)

    # Setting up the window form
    def Setup(self):
        # Setting the size to be fixed
        self.ui.setFixedSize(800, 800)
        # adding the the custom editor of QsciScintilla
        self.editor = QsciScintilla()
        # adding text to the ditro
        self.editor.setText("Hello\n")
        self.editor.append("world")
        # this is i am not sure yet but its for the syntax
        self.editor.setLexer(None)
        self.editor.setUtf8(True)  # Set encoding to UTF-8
        # adding font
        self.Font = QFont()
        # adding text size
        self.Font.setPointSize(14)
        # applying font
        self.editor.setFont(self.Font)  # Will be overridden by lexer!
        # adding the editor to te form TODO: figure out how to add the editor to the form here
        self.layout = self.ui.centralWidget().layout()
        #self.ui.addWidget(self.editor)

        # showing ui
        self.ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = Editor()
    myGUI.Setup()

    sys.exit(app.exec_())
