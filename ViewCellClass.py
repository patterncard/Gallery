import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PIL import *
from PIL.ImageQt import *
import numpy as np

class ViewCellClass(qtw.QFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Seting window to be placed at 0,0 and have size 640x480
        #self.setGeometry(0, 0, 640, 480)
        self.resize(self.sizeHint())
        self.setFrameStyle(qtw.QFrame.Panel | qtw.QFrame.Plain)

        
        #Seting PIL image
        self.pil_image = None

        #Seting window name
        #self.setWindowTitle('ViewCellClass')
        
        #Seting initial image projection
        self.reset_transform()
        
        #Creating canvas [QLabel] showing image, possibly also for
        #drawing selection.
        self.canvas = qtw.QLabel() # SET TO QLabel or QImageLabel

        #Setting QWidget layout manager
        self.hbox = qtw.QHBoxLayout()
        self.hbox.addWidget(self.canvas)
        self.setLayout(self.hbox)
        self.hbox.setContentsMargins(0, 0, 0, 0)

        #Setting event handeling methods for canvas
        self.canvas.wheelEvent = self.handle_wheel_event 
        self.canvas.mousePressEvent = self.handle_mouse_press_event
        self.canvas.mouseMoveEvent = self.handle_mouse_move_event
        self.canvas.mouseReleaseEvent = self.handle_mouse_release_event

        #Showing image
        self.show()
        
        #Setting image to be projected in canvas, for debugging, in releas
        #version call it from outside code.
        self.set_image('cpplogo.png')
        
    def handle_wheel_event(self, event):
        '''Scales oryginal image[pil_image] on wheelEvent'''
        #Seting scale...
        if (event.angleDelta().y() > 0): #Zooming in
            self.scale_at(1.25, event.x(), event.y())
        else: #Zooming out
            self.scale_at(0.8, event.x(), event.y())
        #Redrawing canvas
        self.redraw_image()

    def handle_mouse_press_event(self, event):
        '''
        When lmb pressed, initializes process of image moving, by setting image_move_flag and saving initial mouse coordinates.
        '''
        if event.buttons() & qtc.Qt.LeftButton:
            self.image_move_flag = True
            self.image_move_x = event.x()
            self.image_move_y = event.y()

    def handle_mouse_move_event(self, event):
        '''
        When lmb pressed and mouse moves, "moves" image in given direction, by applying translation.
        '''
        if event.buttons() & qtc.Qt.LeftButton:
            self.translate(event.x() - self.image_move_x ,  event.y() - self.image_move_y)
            self.image_move_x = event.x()
            self.image_move_y = event.y()
            self.redraw_image()

    def handle_mouse_release_event(self, event):
        '''When lmb released, stops the process of image moving, by unsetting image_move_flag'''
        self.image_move_flag = False

    def set_image(self, filename):
        '''Loads image locatet at filename'''

        #Checking if filename is not empty
        if not filename:
            return

        #Loading image
        self.pil_image = Image.open(filename).convert('RGBA')

        #Adjusting image with and height
        self.zoom_fit(self.pil_image.width, self.pil_image.height)

        #Drawing image
        self.draw_image(self.pil_image)

    
    def reset_transform(self):
        '''Resets affine transform'''
        self.mat_affine = np.eye(3)

    def translate(self, offset_x, offset_y):
        '''Sets translation'''
        mat = np.eye(3) 
        mat[0, 2] = float(offset_x)
        mat[1, 2] = float(offset_y)

        self.mat_affine = np.dot(mat, self.mat_affine)

    def scale(self, scale:float):
        '''Sets scale'''
        mat = np.eye(3)
        mat[0, 0] = scale
        mat[1, 1] = scale

        self.mat_affine = np.dot(mat, self.mat_affine)
        
    def scale_at(self, scale:float, cx:float, cy:float):
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


    def draw_image(self, pil_image):
        '''Draws image on canvas [QLabel]'''
        if pil_image == None:
            return

        self.pil_image = pil_image

        # Saving current canvas [QLabel] with and height
        canvas_width = self.canvas.size().width()
        canvas_height = self.canvas.size().height()


        mat_inv = np.linalg.inv(self.mat_affine)

        affine_inv = (mat_inv[0, 0], mat_inv[0, 1], mat_inv[0, 2],
            mat_inv[1, 0], mat_inv[1, 1], mat_inv[1, 2])

        dst = self.pil_image.transform((canvas_width, canvas_height),
                    Image.AFFINE,   
                    affine_inv,     
                    Image.NEAREST
                    )

        im = ImageQt(dst)
        self.canvas.setPixmap(qtg.QPixmap().fromImage(im))
        self.image = im
        self.resize(canvas_width, canvas_height)

    def redraw_image(self):
        '''Redraws image on canvas [QLabel]''' 
        if self.pil_image == None:
            return
        self.draw_image(self.pil_image)

#For debugging, in releas version call it from outside code.
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = ViewCellClass()
    sys.exit(app.exec_())
