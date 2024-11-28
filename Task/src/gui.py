
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, QDialog, QLineEdit, QFormLayout, QSpinBox

from db_operations import get_all_tasks, add_task

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Management Application")
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()

        self.add_task_button = QPushButton("Добавить задачу")
        self.add_task_button.clicked.connect(self.show_add_task_dialog)
        self.layout.addWidget(self.add_task_button)

        self.task_table = QTableWidget()
        self.task_table.setColumnCount(5)
        self.task_table.setHorizontalHeaderLabels(["ID", "Название", "Сложность", "Автор", "Комментарий"])
        self.layout.addWidget(self.task_table)

        self.load_tasks_button = QPushButton("Отобразить задачу")
        self.load_tasks_button.clicked.connect(self.load_tasks)
        self.layout.addWidget(self.load_tasks_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def show_add_task_dialog(self):
        dialog = AddTaskDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            title, difficulty, author, comnt = dialog.get_task_data()
            self.handle_add_task(title, difficulty, author, comnt)
            
    def handle_add_task(self, title, difficulty, author="", comnt=""):
        add_task(title, difficulty, author, comnt)
        QMessageBox.information(self, "Успех", "Задача успешно создана!")
    
    def load_tasks(self):
        tasks = get_all_tasks()
        self.task_table.setRowCount(len(tasks))
        for i, task in enumerate(tasks):
            self.task_table.setItem(i, 0, QTableWidgetItem(str(task[0])))
            self.task_table.setItem(i, 1, QTableWidgetItem(task[1]))
            self.task_table.setItem(i, 2, QTableWidgetItem(str(task[2])))
            self.task_table.setItem(i, 3, QTableWidgetItem(str(task[3])))
            self.task_table.setItem(i, 4, QTableWidgetItem(str(task[4])))

class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить новую задачу")

        layout = QFormLayout(self)

        self.title_input = QLineEdit(self)
        self.difficulty_input = QSpinBox(self)
        self.difficulty_input.setRange(1, 5)
        self.author_input = QLineEdit(self)
        self.comnt_input = QLineEdit(self)

        layout.addRow("Название задачи:", self.title_input)
        layout.addRow("Сложность (1-5):", self.difficulty_input)
        layout.addRow("Автор задачи:", self.author_input)
        layout.addRow("Комментарий:", self.comnt_input)

        self.button_box = QPushButton("Добавить", self)
        self.button_box.clicked.connect(self.accept)
        layout.addWidget(self.button_box)
    
    def get_task_data(self):
        return self.title_input.text(), self.difficulty_input.value(), self.author_input.text(), self.comnt_input.text()