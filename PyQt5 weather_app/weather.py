import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QRadioButton, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QPixmap # font designing, image designing
from PyQt5.QtCore import Qt, QTime, QTimer   # font alignment
import requests
from datetime import datetime, timezone

class weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.updated_label = QLabel(self)
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setMinimumSize(500, 650)
    
        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.setContentsMargins(30, 30, 30, 30)
    
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addStretch()
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.updated_label)

        vbox.addStretch()
    
        self.setLayout(vbox)
    
        for widget in [
            self.city_label,
            self.city_input,
            self.temperature_label,
            self.emoji_label,
            self.description_label,
            self.updated_label
        ]:
            widget.setAlignment(Qt.AlignCenter)

     
        self.updated_label.setObjectName("updated_label")
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
    
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: white;
            }
    
            QLabel {
                font-family: Segoe UI;
            }
    
            QLabel#city_label {
                font-size: 34px;
                font-weight: bold;
                color: #38bdf8;
            }
    
            QLineEdit#city_input {
                font-size: 28px;
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #334155;
                background-color: #020617;
                color: white;
            }
    
            QPushButton#get_weather_button {
                font-size: 24px;
                padding: 12px;
                border-radius: 12px;
                background-color: #38bdf8;
                color: black;
                font-weight: bold;
            }
    
            QPushButton#get_weather_button:hover {
                background-color: #0ea5e9;
            }
    
            QPushButton#get_weather_button:disabled {
                background-color: #64748b;
            }
    
            QLabel#temperature_label {
                font-size: 80px;
                font-weight: bold;
            }
    
            QLabel#emoji_label {
                font-size: 110px;
            }
    
            QLabel#description_label {
                font-size: 36px;
                color: #cbd5f5;
            }

            QLabel#updated_label {
                font-size: 18px;
                color: #94a3b8;
                font-style: italic;
            }
            """)
    
        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)


    def get_weather(self):
        self.get_weather_button.setEnabled(False)
        self.temperature_label.setText("Loading...")
        self.emoji_label.clear()
        self.description_label.clear()
    
        api = 'dfc872e7f007ef32d0a2f56e7a0bdaef'
        city = self.city_input.text().strip()
    
        if not city:
            self.display_error("Please enter a city name")
            self.get_weather_button.setEnabled(True)
            return
    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            self.display_weather(data)
    
        except requests.exceptions.HTTPError:
            self.display_error("City not found")
    
        except requests.exceptions.ConnectionError:
            self.display_error("No internet connection")
    
        except requests.exceptions.Timeout:
            self.display_error("Request timed out")
    
        except requests.exceptions.RequestException as e:
            self.display_error(str(e))
    
        finally:
            self.get_weather_button.setEnabled(True)
        
        
    
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.updated_label.clear()

    def display_weather(self, data):
        temperature_c = data["main"]["temp"]
        weather_des = data["weather"][0]["description"]
        weather_id = data["weather"][0]['id']
        updated_time = data["dt"]
        
        self.temperature_label.setText(f"{round(temperature_c, 3)}°C")
        
        self.emoji_label.setText(self.weather_emoji(weather_id))
        
        self.description_label.setText(weather_des)

        self.updated_label.setText(self.time_ago(updated_time))

    @staticmethod
    def time_ago(unix_time):
        now = datetime.now(timezone.utc)
        updated_time = datetime.fromtimestamp(unix_time, tz=timezone.utc)
    
        diff = now - updated_time
        seconds = int(diff.total_seconds())
    
        minutes = seconds // 60
        hours = minutes // 60
    
        minutes %= 60
    
        if hours > 0:
            return f"Updated {hours} hour(s), {minutes} minute(s) ago"
        else:
            return f"Updated {minutes} minute(s) ago"


    @staticmethod
    def weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""


        

def main():
    app = QApplication(sys.argv)
    window = weatherapp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
