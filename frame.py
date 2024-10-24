from PyQt5 import QtCore, QtGui, QtWidgets
from rsa import RSA

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 620)

        # Central widget and layout setup
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setSpacing(20)  # Increased spacing between widgets

        # Set gradient background for the main window
        MainWindow.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #E0FFFF, stop:1 #AFEEEE);
        """)

        # Title Text
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText("Demo nhóm 5")
        self.titleLabel.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #4682B4;
            padding: 20px;
            border-radius: 15px;
            background-color: #F0F8FF;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        """)
        self.centralLayout.addWidget(self.titleLabel)

        # Message Input
        self.messageGroup = QtWidgets.QGroupBox("Nhập thông điệp", self.centralwidget)
        self.messageGroup.setStyleSheet("""
            font-size: 18px;
            border: 1px solid #B0E0E6;
            border-radius: 15px;
            padding: 15px;
            background-color: #FFFFFF;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        """)
        self.messageLayout = QtWidgets.QVBoxLayout(self.messageGroup)
        self.messageLayout.setContentsMargins(10, 10, 10, 10)
        
        self.message = QtWidgets.QTextEdit(self.messageGroup)
        self.message.setPlaceholderText("Nhập thông điệp...")
        self.message.setStyleSheet("""
            font-size: 16px;
            padding: 12px;
            border: 1px solid #87CEEB;
            border-radius: 10px;
            background-color: #F8F8FF;
        """)
        self.messageLayout.addWidget(self.message)
        self.centralLayout.addWidget(self.messageGroup)

        # RSA Parameter Output
        self.paramGroup = QtWidgets.QGroupBox("RSA Parameters", self.centralwidget)
        self.paramGroup.setStyleSheet("""
            font-size: 18px;
            border: 1px solid #B0E0E6;
            border-radius: 15px;
            padding: 15px;
            background-color: #FFFFFF;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        """)
        self.paramLayout = QtWidgets.QFormLayout(self.paramGroup)
        self.paramLayout.setContentsMargins(10, 10, 10, 10)

        self.p1 = QtWidgets.QLineEdit(self.paramGroup)
        self.q1 = QtWidgets.QLineEdit(self.paramGroup)
        self.e1 = QtWidgets.QLineEdit(self.paramGroup)
        self.d1 = QtWidgets.QLineEdit(self.paramGroup)
        self.N1 = QtWidgets.QLineEdit(self.paramGroup)

        for param in [self.p1, self.q1, self.e1, self.d1, self.N1]:
            param.setReadOnly(True)
            param.setStyleSheet("""
                font-size: 16px;
                border: 1px solid #87CEEB;
                border-radius: 10px;
                padding: 8px;
                background-color: #F8F8FF;
            """)

        # Add to form layout
        self.paramLayout.addRow("p:", self.p1)
        self.paramLayout.addRow("q:", self.q1)
        self.paramLayout.addRow("e:", self.e1)
        self.paramLayout.addRow("d:", self.d1)
        self.paramLayout.addRow("N:", self.N1)

        self.centralLayout.addWidget(self.paramGroup)

        # Encryption and Decryption Output
        self.encGroup = QtWidgets.QGroupBox("Mã hóa / Giải mã", self.centralwidget)
        self.encGroup.setStyleSheet("""
            font-size: 18px;
            border: 1px solid #B0E0E6;
            border-radius: 15px;
            padding: 15px;
            background-color: #FFFFFF;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        """)
        self.encLayout = QtWidgets.QFormLayout(self.encGroup)
        self.encLayout.setContentsMargins(10, 10, 10, 10)

        self.enc1 = QtWidgets.QTextEdit(self.encGroup)
        self.enc1.setReadOnly(True)
        self.enc1.setPlaceholderText("Encrypted message will appear here...")
        self.enc1.setStyleSheet("""
            font-size: 16px;
            border: 1px solid #87CEEB;
            border-radius: 10px;
            padding: 8px;
            background-color: #F8F8FF;
        """)
        
        self.dec1 = QtWidgets.QLineEdit(self.encGroup)
        self.dec1.setReadOnly(True)
        self.dec1.setStyleSheet("""
            font-size: 16px;
            border: 1px solid #87CEEB;
            border-radius: 10px;
            padding: 8px;
            background-color: #F8F8FF;
        """)
        
        self.encLayout.addRow("Thông điệp sau khi mã hóa:", self.enc1)
        self.encLayout.addRow("Thông điệp sau khi giải mã:", self.dec1)
        
        self.centralLayout.addWidget(self.encGroup)

        # Generate Button
        self.pushButton = QtWidgets.QPushButton("Mã hóa", self.centralwidget)
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #40E0D0;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 15px 30px;
                border-radius: 25px;
                transition: all 0.3s ease;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            }
            QPushButton:hover {
                background-color: #48D1CC;
                transform: scale(1.05);
            }
        """)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMinimumHeight(50)
        self.centralLayout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)

        # Set central widget layout
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.result)

        # Retranslate UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def result(self):
        self.rsa = RSA(keysize=32)
        msg = self.message.toPlainText()

        enc = self.rsa.encrypt(msg)
        dec = self.rsa.decrypt(enc)

        self.enc1.setText(str(enc))
        self.dec1.setText(str(dec))
        self.p1.setText(str(self.rsa.p))
        self.q1.setText(str(self.rsa.q))
        self.d1.setText(str(self.rsa.d))
        self.e1.setText(str(self.rsa.e))
        self.N1.setText(str(self.rsa.N))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Demo nhóm 5")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
