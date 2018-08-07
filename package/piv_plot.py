from PySide2 import QtWidgets, QtCore
from openpiv import tools
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector, Rectangle
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

        # self.zoom_ax = self.figure.add_subplot(221)
        # self.zoom_ax.axis('off')
        self.xy_zoom = [[None, None], [None, None]]

        self.zoom_rectangle = None

        self.cid = None
        self.bit = '8 bit'
        self.current_image = 1

        self.canvas_layout = QtWidgets.QGridLayout(parent)
        self.canvas_layout.addWidget(self.piv_canvas)

    # function that shows the chosen image
    def show_plot(self, image_number, bit):
        self.ax.clear()
        self.bit = bit
        self.current_image = image_number
        if self.bit == "8 bit":
            self.ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            self.ax.axis('off')

            # self.zoom_ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            # self.zoom_ax.axis('off')
            # if self.xy_zoom[0][0] != None:
            # self.zoom_ax.set_xlim(self.xy_zoom[0][0], self.xy_zoom[0][1])
            # self.zoom_ax.set_ylim(self.xy_zoom[1][0], self.xy_zoom[1][1])
        else:
            self.ax.imshow(np.uint16(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            self.ax.axis('off')
            # self.zoom_ax.imshow(np.uint16(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            # self.zoom_ax.axis('off')
            # if self.xy_zoom[0][0] != None:
            # self.zoom_ax.set_xlim(self.xy_zoom[0][0], self.xy_zoom[0][1])
            # self.zoom_ax.set_ylim(self.xy_zoom[1][0], self.xy_zoom[1][1])

            self.ax.add_patch(self.zoom_rectangle)

        if self.xy_zoom[0][0] == 0 and self.xy_zoom[0][1] == len(self.piv_images_list[0][2][0]) and self.xy_zoom[1][
            0] == 0 and self.xy_zoom[1][1] == len(self.piv_images_list[0][2]):
            self.zoom_rectangle = Rectangle((self.xy_zoom[0][0], self.xy_zoom[1][0]),
                                            abs(self.xy_zoom[0][1] - self.xy_zoom[0][0]),
                                            abs(self.xy_zoom[1][1] - self.xy_zoom[1][0]), facecolor='none', alpha=0.1,
                                            edgecolor='none', linewidth=1, fill=False)

        elif not self.xy_zoom[0][0] == None:
            self.zoom_rectangle = Rectangle((self.xy_zoom[0][0], self.xy_zoom[1][0]),
                                            abs(self.xy_zoom[0][1] - self.xy_zoom[0][0]),
                                            abs(self.xy_zoom[1][1] - self.xy_zoom[1][0]), facecolor='gray', alpha=0.6,
                                            linestyle='--', edgecolor='white', linewidth=2, fill=True)
            self.ax.add_patch(self.zoom_rectangle)

        self.piv_canvas.draw()

    # function to add an image
    def add_image(self, image_path, bit):
        self.bit = bit
        if self.bit == "8 bit":
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint8(tools.imread(image_path))])
        else:
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint16(tools.imread(image_path))])

    @staticmethod
    def invert(img_read, is_bmp, bit):
        if is_bmp:
            # for i in range(len(img_read)):
            # for j in range(len(img_read[i])):
            img_read = 255 - img_read
        else:
            # for i in range(len(img_read)):
            #    for j in range(len(img_read[i])):
            img_read = 1.0 - img_read  # it's not 0.255
        if bit == "8 bit":
            return np.uint8(img_read)
        else:
            return np.uint16(img_read)

    def ROI_buttons(self, is_select):
        if is_select:
            self.rs = RectangleSelector(self.ax, self.zoom, drawtype='box', useblit=False, button=[1],
                                        spancoords='pixels', interactive=False,
                                        rectprops=dict(facecolor='gray', alpha=0.6, linestyle='--', edgecolor='white',
                                                       linewidth=2))
        else:
            # i made it that if self.xy_zoom[0][0] == None than it will go back to regula
            self.xy_zoom[0][0] = 0
            self.xy_zoom[0][1] = len(self.piv_images_list[0][2][0])
            self.xy_zoom[1][0] = 0
            self.xy_zoom[1][1] = len(self.piv_images_list[0][2])
            self.show_plot(self.current_image, self.bit)

    def zoom(self, click_point, release_point):
        x1, y1 = click_point.xdata, click_point.ydata
        x2, y2 = release_point.xdata, release_point.ydata
        self.xy_zoom[0][0] = x1
        self.xy_zoom[0][1] = x2
        self.xy_zoom[1][0] = y1
        self.xy_zoom[1][1] = y2
        self.rs = None
        self.show_plot(self.current_image, self.bit)

    # the function that does the piv itself
    def start_piv(self, width_a, height_a, width_b, height_b, horizontal, vertical, sn_type, sn_value, scale,
                  outer_filter, jump):
        pass


if __name__ == '__main__':
    # run the application (it does nothing)
    import sys

    app = QtWidgets.QApplication(sys.argv)
    piv_plot_class = PIVPlot(QtWidgets.QWidget())

    sys.exit(app.exec_())
