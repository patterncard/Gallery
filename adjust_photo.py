from PyQt5.QtWidgets import QPushButton, QSlider
from __init__ import *


class AdjustImage(QWidget):

    exposure_signal = pyqtSignal([float])
    apply_signal = pyqtSignal([bool])
    clear_signal = pyqtSignal([bool])

    def __init__(self):
        super(AdjustImage, self).__init__()
        hbox = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(20)
        self.slider.setValue(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMaximumWidth(400)
        self.slider.setMinimumHeight(60)
        self.slider.move(0, 50)

        self.slider.valueChanged.connect(self.updateExposureValue)

        self.name = QLabel('Exposure', self.slider)
        self.name.move(170, 0)

        self.label = QLabel('1.0', self)
        self.label.setMinimumWidth(20)

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.button = QPushButton('Apply', self)
        self.button.pressed.connect(lambda: self.apply_signal.emit(True))
        self.button.move(115, 200)

        self.button = QPushButton('Clear', self)
        self.button.pressed.connect(lambda: self.clear_signal.emit(True))
        self.button.pressed.connect(self.resetSlider)
        self.button.move(215, 200)

    def updateExposureValue(self, value):
        exposure_value = value/10
        self.label.setText(str(exposure_value))
        self.exposure_signal.emit(exposure_value)

    def resetSlider(self):
        self.slider.setValue(10)
