import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer, QDate, QTimeZone, QDateTime   # font alignment and time elements


class digitalclock(QWidget):
    def __init__(self):
        super().__init__()

        self.country = QLabel(self)
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.date_label = QLabel(self)
        
        self.is_pakistan = True

        self.toggle_btn = QPushButton("Switch to Canada")



        
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle("CLOCK")
        self.setGeometry(600, 400, 500, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.country)
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.toggle_btn)
 
        self.setLayout(vbox)

        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                     "font-family: 'Courier New';"
                                     "color: #1CFF03;")
        
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 28px;"
                                     "font-family: Arial;"
                                     "color: #7EF37E;")

        self.toggle_btn.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: A9F7CC;
                border: 2px solid #7EF37E;
                border-radius: 8px;
                padding: 6px;
                font-size: 18px;
                font-family: Arial Bold;
            }
            QPushButton:hover {
                background-color: #8AC6A5;
                color: black;
            }
        """)

        self.toggle_btn.clicked.connect(self.toggle_timezone)

                                            
        self.setStyleSheet("background-color: black;")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    
    def toggle_timezone(self):
        self.is_pakistan = not self.is_pakistan
    
        if self.is_pakistan:
            self.toggle_btn.setText("Switch to Canada")
           # self.time_label.setStyleSheet("font-color: 02E1E5")
        else:
            self.toggle_btn.setText("Switch to Pakistan")
    
        self.update_time()
        
    def update_time(self):
        if self.is_pakistan:
            tz = QTimeZone(b"Asia/Karachi")
            self.country.setText("Lahore, Pakistan")
            self.country.setStyleSheet("color: #1CFF03;")
            self.time_label.setStyleSheet("font-size: 150px;"
                                     "font-family: 'Courier New';"
                                     "color: #1CFF03;")
            self.date_label.setStyleSheet("font-size: 28px;"
                                     "font-family: Arial;"
                                     "color: #7EF37E;")
        else:
            self.country.setText("Ottawa, Canada")
            self.country.setStyleSheet("color: #02E1E5;")
            tz = QTimeZone(b"America/Toronto")  # Ottawa
            self.time_label.setStyleSheet("font-size: 150px;"
                                     "font-family: 'Courier New';"
                                     "color: #02E1E5;")
            self.date_label.setStyleSheet("font-size: 28px;"
                                     "font-family: Arial;"
                                     "color: #02E1E5;")
    
        now = QDateTime.currentDateTimeUtc().toTimeZone(tz)
    
        self.time_label.setText(now.toString("hh:mm:ss AP"))
        self.date_label.setText(now.toString("ddd | dd MMM"))

def main():
    app = QApplication(sys.argv)
    window = digitalclock()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    