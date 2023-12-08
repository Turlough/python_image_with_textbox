import sys


from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PIL import Image, ImageQt
from PyQt6.QtGui import QFont

image_path = r"images\sample_document.jpg"


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Vertical layout
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        # Prepare PIL version- need to display grayscale for legibility
        pil_image = Image.open(image_path)
        self.q_image = ImageQt.ImageQt(pil_image)
        # Set the QPixmap
        self.pixmap = QPixmap(image_path)
        self.label.setPixmap(self.pixmap)

        # Create a scroll area and add the label to it
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.label)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        # Create a text edit for notes
        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedHeight(50)
        self.text_edit.setText('Sample text')
        layout.addWidget(self.text_edit)

        # Set a larger font size
        font = QFont()
        font.setPointSize(30)  # Set the font size, e.g., 14 points
        self.text_edit.setFont(font)

        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
