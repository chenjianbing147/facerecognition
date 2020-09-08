import sys
import main_ui
from PyQt5.QtWidgets import QApplication, QMainWindow
from display import Display


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = QMainWindow()
    ui = main_ui.Ui_MainWindow()

    ui.setupUi(mainWnd)

    dis = Display(ui, mainWnd)

    mainWnd.show()

    sys.exit(app.exec_())