from PySide2 import QtWidgets, QtCore
from openpiv import tools
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# i am still not putting the navigation tool bar because of some bugs
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# i needed to call QWidget and super to add the tool bar of matplotlib
class PIVPlot(QtWidgets.QWidget):
    def __init__(self, parent=QtWidgets.QWidget):
        super(PIVPlot, self).__init__(parent)
        self.figure = Figure()

        # the canvas is where the graph and the tool bar is
        self.piv_canvas = FigureCanvas(self.figure)

        self.piv_tool_bar = NavigationToolbar(self.piv_canvas, self)
        self.piv_tool_bar.hide()

        # the piv_images_list is where the images are saved
        self.piv_images_list = []
        self.ax = self.figure.add_subplot(111)

        self.canvas_layout = QtWidgets.QGridLayout(parent)
        self.canvas_layout.addWidget(self.piv_canvas)

    # function that shows the chosen image
    def show_plot(self, image_number):
        self.ax.clear()

        self.ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)

        self.piv_canvas.draw()

    # function to add an image
    def add_image(self, image_path, bit):
        if bit == "8 bit":
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint8(tools.imread(image_path))])
        else:
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint16(tools.imread(image_path))])

    # the function that does the piv itself
    def start_piv(self, width, height, horizontal, vertical, sn_type, sn_value, scale, outer_filter, jump):
        pass

    @staticmethod
    def invert(img_read, is_bmp, bit):
        invert_img = img_read
        if is_bmp:
            # for i in range(len(img_read)):
            # for j in range(len(img_read[i])):
            invert_img = 255 - img_read
        else:
            #for i in range(len(img_read)):
            #    for j in range(len(img_read[i])):
            invert_img = 1.0 - img_read # it's not 0.255
        if bit == "8 bit":
            return np.uint8(invert_img)
        else:
            return np.uint16(invert_img)

    def ROI_buttons(self, is_select):
        if is_select:
            self.piv_tool_bar.release_zoom(self.piv_tool_bar.zoom)
            self.piv_tool_bar.zoom()
        else:
            self.piv_tool_bar.home()
            self.piv_tool_bar.zoom()


if __name__ == '__main__':
    # run the application (it does nothing)
    import sys

    app = QtWidgets.QApplication(sys.argv)
    piv_plot_class = PIVPlot(QtWidgets.QWidget())

    sys.exit(app.exec_())
