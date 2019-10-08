from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QVBoxLayout


class MainWindow(QWidget):
	_button: QPushButton
	_username: QLineEdit
	_password: QLineEdit
	_welcome = QLineEdit

	def __init__(self):
		super().__init__()

		self._username = QLineEdit('', self)
		self._password = QLineEdit('', self)
		self._button = QPushButton('Login', self)
		self._welcome = QLineEdit('', self)
		layout: QVBoxLayout = QVBoxLayout(self)
		layout.addWidget(self._username)
		layout.addWidget(self._password)
		layout.addWidget(self._button)
		layout.addWidget(self._welcome)
		self.setLayout(layout)
		self._button.setDisabled(True)
		self._password.setEchoMode(QLineEdit.Password)
		self._password.textChanged.connect(self._check_login)
		self._username.textChanged.connect(self._check_login)
		self._button.clicked.connect(self._on_button_click)

	# self._button.pressed.connect(self._check_user_password)

	def _on_button_click(self) -> None:
		self._welcome.setText('Hello ' + self._username.text())

	def _check_login(self):
		user_changed: bool = len(self._username.text()) > 0
		pass_changed: bool = len(self._password.text()) > 0
		self._button.setEnabled(user_changed and pass_changed)


if __name__ == '__main__':
	app: QApplication = QApplication([])

	main_window: MainWindow = MainWindow()
	main_window.show()
	app.exec()
