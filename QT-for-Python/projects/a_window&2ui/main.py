import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide6.QtCore import QFile, Slot
from ui_main_window import Ui_main_window
from ui_window import Ui_window_2

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Create central stacked widget to hold both UIs
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create main page
        self.main_page = QMainWindow()
        self.ui_main = Ui_main_window()
        self.ui_main.setupUi(self.main_page)
        
        # Create second page
        self.second_page = QMainWindow()
        self.ui_second = Ui_window_2()
        self.ui_second.setupUi(self.second_page)
        
        # Add pages to stacked widget
        self.central_widget.addWidget(self.main_page)
        self.central_widget.addWidget(self.second_page)

        # Connect the Quit action in second window
        self.ui_second.actionQuit.triggered.connect(QApplication.instance().quit)
        # Connect the Quit action in first window
        self.ui_main.actionQuit.triggered.connect(QApplication.instance().quit)
        
        # Connect buttons
        self.ui_main.pushButton.clicked.connect(self.on_button_1_click)
        self.ui_main.pushButton_2.clicked.connect(self.on_button_2_click)
        self.ui_main.pushButton_3.clicked.connect(self.go_to_second_page)
        
        # Show first page
        self.central_widget.setCurrentIndex(0)
        self.setWindowTitle("Main Window")
    
    @Slot()
    def on_button_1_click(self):
        self.ui_main.lineEdit.setText("Button clicked!")

    @Slot()
    def on_button_2_click(self):
        self.ui_main.lineEdit.clear()
    
    @Slot()
    def go_to_second_page(self):
        self.central_widget.setCurrentIndex(1)
        self.setWindowTitle("Window 2")
    
    @Slot()
    def go_to_main_page(self):
        self.central_widget.setCurrentIndex(0)
        self.setWindowTitle("Main Window")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(664, 380)  # Set initial window size
    window.show()
    sys.exit(app.exec())