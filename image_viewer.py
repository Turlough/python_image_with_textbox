import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QScrollArea
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image
from PyQt6.QtGui import QFont
from PIL.ImageQt import ImageQt

image_path = r"images\sample_document.tif"


class ImageViewer(QWidget):
    def __init__(self):
        self.label = None
        super().__init__()

    def init_ui(self, pil_image):
        """
        Display the image with a text box
        :param pil_image: A PIL image, already prepared by Pillow
        """

        layout = QVBoxLayout(self)
        self.label = QLabel(self)

        # Set the Pixmap
        q_image = ImageQt(pil_image)
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)

        # Create a scroll area and add the label to it
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.label)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        # Create a text edit
        text_edit = QTextEdit(self)
        text_edit.setFixedHeight(50)
        text_edit.setText('Sample text')
        layout.addWidget(text_edit)

        # Set a larger font size
        font = QFont()
        font.setPointSize(30)  # Set the font size, e.g., 14 points
        text_edit.setFont(font)

        # Set the layout on the application's window
        self.setLayout(layout)


def launch(image):
    # Launch
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.init_ui(image)
    viewer.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    # Prepare PIL version- need to display grayscale for legibility
    image = Image.open(image_path)
    image = image.convert('L')  # Grayscale

    launch(image)
