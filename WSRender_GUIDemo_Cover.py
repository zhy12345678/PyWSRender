import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtCore import Qt, QRectF
#from your_form import Ui_MainWindow  # This is your converted UI file
from WSRender_GUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.set_image_to_graphicsview("G:\\single\\MIS_show.png", self.graphicsView)
        #self.set_image_to_graphicsview("G:\\single\\MIS_Rea.png", self.graphicsView_2)
        # self.set_image_to_graphicsview("G:\\single\\Cylindrical_show.png", self.graphicsView)
        # self.set_image_to_graphicsview("G:\\single\\Cylindrical_local.png", self.graphicsView_2)
        # self.set_image_to_graphicsview("G:\\single\\articulated.png", self.graphicsView)
        # self.set_image_to_graphicsview("G:\\single\\dual_articulated.png", self.graphicsView_2)

    def set_image_to_graphicsview(self, image_path, graphics_view):
        # Load the image into a QPixmap
        pixmap = QPixmap(image_path)

        # Check if the image is loaded successfully
        if pixmap.isNull():
            print(f"Failed to load image from {image_path}")
            return

        # Scale the pixmap to the size of the graphicsView
        # scaled_pixmap = pixmap.scaled(
        #     graphics_view.size(),
        #     Qt.KeepAspectRatio,
        #     Qt.SmoothTransformation
        # )
        scale_factor = 16
        scaled_pixmap = pixmap.scaled(
            graphics_view.size() * scale_factor,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        # Create a QGraphicsScene and add the scaled pixmap to it
        scene = QGraphicsScene()
        scene.addPixmap(scaled_pixmap)

        # Set the QGraphicsScene to the QGraphicsView
        graphics_view.setScene(scene)
        graphics_view.setSceneRect(
            QRectF(scaled_pixmap.rect()))  # Convert QRect to QRectF and set scene size to pixmap size


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
