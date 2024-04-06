import sys

from PySide6.QtWidgets import QApplication
from src.client.MainWindow import MainWindow
from src.database.db_manager import db

if __name__ == '__main__':
    db.checkDatabase('src/database/base.sql')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
