from __init__ import *
from PIL import Image
from PIL import *
from PIL.ImageQt import *
from PIL import ImageEnhance
import numpy as np
import cv2
from adjust_photo import AdjustImage


class ViewCellClass(QFrame):
    received_exposure = pyqtSignal([float])
    recived_apply = pyqtSignal([bool])
    recived_clear = pyqtSignal([bool])
    imgchange = pyqtSignal(str)
    path = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Seting window to be placed at 0,0 and have size 640x480
        #self.setGeometry(0, 0, 640, 480)
        self.resize(self.sizeHint())
        self.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
        self.imgchange.connect(self.set_image)

        self.popMenu = QMenu()
        action = QAction('save', self)
        action.triggered.connect(self.save)
        self.popMenu.addAction(action)
        self.popMenu.addSeparator()
        action = QAction('brightness', self)
        action.triggered.connect(self.brightness)
        self.popMenu.addAction(action)
        
        # Seting PIL image
        self.raw_image = None
        self.original_image = None
        self.processed_image = None

        # Seting window name
        # self.setWindowTitle('ViewCellClass')

        # Seting initial image projection
        self.reset_transform()

        # Creating canvas [QLabel] showing image, possibly also for
        # drawing selection.
        self.canvas = QLabel()  # SET TO QLabel or QImageLabel

        # Setting QWidget layout manager
        self.hbox = QHBoxLayout()

        self.received_exposure.connect(self.adjustExposure)
        self.recived_apply.connect(self.applyChanges)
        self.recived_clear.connect(self.clearChanges)

        self.hbox.addWidget(self.canvas)
        self.setLayout(self.hbox)
        self.hbox.setContentsMargins(0, 0, 0, 0)

        # Setting event handeling methods for canvas
        self.canvas.wheelEvent = self.handle_wheel_event
        self.canvas.mousePressEvent = self.handle_mouse_press_event
        self.canvas.mouseMoveEvent = self.handle_mouse_move_event
        self.canvas.mouseReleaseEvent = self.handle_mouse_release_event

        # Showing image
        self.show()

        # Setting image to be projected in canvas, for debugging, in releas
        # version call it from outside code.
        #self.set_image("empty_slot.png")

    def handle_wheel_event(self, event):
        '''Scales oryginal image[pil_image] on wheelEvent'''
        # Seting scale...
        if (event.angleDelta().y() > 0):  # Zooming in
            self.scale_at(1.25, event.x(), event.y())
        else:  # Zooming out
            self.scale_at(0.8, event.x(), event.y())
        # Redrawing canvas
        self.redraw_image()

    def handle_mouse_press_event(self, event):
        '''
        When lmb pressed, initializes process of image moving, by setting image_move_flag and saving initial mouse coordinates.
        '''
        if event.buttons() & Qt.LeftButton:
            self.image_move_flag = True
            self.image_move_x = event.x()
            self.image_move_y = event.y()

    def handle_mouse_move_event(self, event):
        '''
        When lmb pressed and mouse moves, "moves" image in given direction, by applying translation.
        '''
        if event.buttons() & Qt.LeftButton:
            self.translate(event.x() - self.image_move_x,
                           event.y() - self.image_move_y)
            self.image_move_x = event.x()
            self.image_move_y = event.y()
            self.redraw_image()

    def handle_mouse_release_event(self, event):
        '''When lmb released, stops the process of image moving, by unsetting image_move_flag'''
        self.image_move_flag = False

    def set_image(self, filename):
        '''Loads image locatet at filename'''
        self.path = filename
        # Checking if filename is not empty
        if not filename:
            return

        # Loading image
        self.raw_image = Image.open(filename).convert('RGBA')
        self.original_image = self.raw_image
        self.processed_image = self.raw_image

        # Adjusting image with and height
        self.zoom_fit(self.original_image.width, self.original_image.height)

        # Drawing image
        self.draw_image(self.original_image)

    def reset_transform(self):
        '''Resets affine transform'''
        self.mat_affine = np.eye(3)

    def translate(self, offset_x, offset_y):
        '''Sets translation'''
        mat = np.eye(3)
        mat[0, 2] = float(offset_x)
        mat[1, 2] = float(offset_y)

        self.mat_affine = np.dot(mat, self.mat_affine)

    def scale(self, scale: float):
        '''Sets scale'''
        mat = np.eye(3)
        mat[0, 0] = scale
        mat[1, 1] = scale

        self.mat_affine = np.dot(mat, self.mat_affine)

    def scale_at(self, scale: float, cx: float, cy: float):
        '''Sets scale with given cx, cy coordinates'''
        self.translate(-cx, -cy)
        self.scale(scale)
        self.translate(cx, cy)

    def zoom_fit(self, image_width, image_height):
        '''Adjusts oryginal image[pil_image] size to fit canvas[QLabel]'''

        canvas_width = self.canvas.size().width()
        canvas_height = self.canvas.size().height()

        if (image_width * image_height <= 0) or (canvas_width * canvas_height <= 0):
            return

        self.reset_transform()

        scale = 1.0
        offsetx = 0.0
        offsety = 0.0

        if (canvas_width * image_height) > (image_width * canvas_height):
            scale = canvas_height / image_height
            offsetx = (canvas_width - image_width * scale) / 2
        else:
            scale = canvas_width / image_width
            offsety = (canvas_height - image_height * scale) / 2

        self.scale(scale)
        self.translate(offsetx, offsety)

    def draw_image(self, image):
        '''Draws image on canvas [QLabel]'''
        if image == None:
            return

        # self.pil_image = pil_image

        # Saving current canvas [QLabel] with and height
        canvas_width = self.canvas.size().width()
        canvas_height = self.canvas.size().height()

        mat_inv = np.linalg.inv(self.mat_affine)

        affine_inv = (mat_inv[0, 0], mat_inv[0, 1], mat_inv[0, 2],
                      mat_inv[1, 0], mat_inv[1, 1], mat_inv[1, 2])

        dst = image.transform((canvas_width, canvas_height),
                              Image.AFFINE,
                              affine_inv,
                              Image.NEAREST
                              )

        im = ImageQt(dst)
        self.canvas.setPixmap(QPixmap().fromImage(im))
        self.image = im
        self.resize(canvas_width, canvas_height)

    def redraw_image(self):
        '''Redraws image on canvas [QLabel]'''
        if self.original_image == None:
            return
        self.draw_image(self.original_image)

    def adjustExposure(self, exposure):
        enhancer = ImageEnhance.Brightness(self.original_image)
        enhanced = enhancer.enhance(exposure)
        self.processed_image = enhanced
        self.draw_image(self.processed_image)

    def applyChanges(self, apply):
        self.original_image = self.processed_image

    def clearChanges(self, clear):
        self.original_image = self.raw_image
        self.redraw_image()

    def on_context_menu(self, point):
        self.popMenu.exec_(self.mapToGlobal(point))
    
    def brightness(self):
        self.nextWindow = AdjustImage()
        self.nextWindow.exposure_signal.connect(self.adjustExposure)
        self.nextWindow.apply_signal.connect(self.applyChanges)
        self.nextWindow.clear_signal.connect(self.clearChanges)

    def save(self):
        fileName, selectedFilter = QFileDialog.getSaveFileName(self, "Save as", self.path, "images (*.jpg *.jpeg *.png);;All Files (*.*)")
        self.original_image.save(fileName)

# For debugging, in releas version call it from outside code.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ViewCellClass()
    sys.exit(app.exec_())
