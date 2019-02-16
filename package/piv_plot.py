import matplotlib.pyplot as plt
import numpy as np
from PySide2 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# i am still not putting the navigation tool bar because of some bugs
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector, Rectangle
from openpiv import tools
from openpiv.filters import replace_outliers
from openpiv.process import extended_search_area_piv, get_coordinates, get_field_shape
from openpiv.validation import sig2noise_val
from package.openpiv_savevec import save_openpiv_vec


# i needed to call QWidget and super to add the tool bar of matplotlib
class PIVPlot(QtWidgets.QWidget):
    def __init__(self, parent=QtWidgets.QWidget, main_class=None):
        super(PIVPlot, self).__init__(parent)
        self.figure = Figure()
        self.figure.patch.set_facecolor((0.94117647, 0.94117647, 0.94117647))

        # the canvas is where the graph and the tool bar is
        self.piv_canvas = FigureCanvas(self.figure)

        self.piv_tool_bar = NavigationToolbar(self.piv_canvas, self)
        self.piv_tool_bar.hide()

        self.main_class = main_class
        # the piv_images_list is where the images are saved
        self.piv_images_list = []

        # the list where the results of the piv are saved
        self.piv_results_list = []
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
    def show_plot(self, image_number, bit, change_number=False):
        self.ax.clear()
        self.bit = bit
        self.current_image = image_number

        """
        if self.bit == "8 bit":
            if self.piv_images_list[image_number][3]:
                self.ax.quiver(self.piv_images_list[image_number][3][0],
                               max(self.piv_images_list[image_number][3][1].flatten()) -
                               self.piv_images_list[image_number][3][1],
                               self.piv_images_list[image_number][3][2], self.piv_images_list[image_number][3][3],
                               color='b', pivot='middle')
                self.ax.quiver(self.piv_images_list[image_number][3][0][self.piv_images_list[image_number][3][4]],
                               max(self.piv_images_list[image_number][3][1][
                                       self.piv_images_list[image_number][3][4]].flatten()) -
                               self.piv_images_list[image_number][3][1][self.piv_images_list[image_number][3][4]],
                               self.piv_images_list[image_number][3][2][self.piv_images_list[image_number][3][4]],
                               self.piv_images_list[image_number][3][3][self.piv_images_list[image_number][3][4]],
                               color='r',
                               pivot='middle')

            self.ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            self.ax.axis('off')
        
            self.zoom_ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
            self.zoom_ax.axis('off')
            if self.xy_zoom[0][0] != None:
            self.zoom_ax.set_xlim(self.xy_zoom[0][0], self.xy_zoom[0][1])
            self.zoom_ax.set_ylim(self.xy_zoom[1][0], self.xy_zoom[1][1])
            """

            # try:
            #     self.ax.quiver(self.piv_images_list[image_number][3][0][self.piv_images_list[image_number][3][4]],
            #                    max(self.piv_images_list[image_number][3][1][
            #                            self.piv_images_list[image_number][3][4]].flatten()) -
            #                    self.piv_images_list[image_number][3][1][self.piv_images_list[image_number][3][4]],
            #                    self.piv_images_list[image_number][3][2][self.piv_images_list[image_number][3][4]],
            #                    self.piv_images_list[image_number][3][3][self.piv_images_list[image_number][3][4]],
            #                    color='r',
            #                    pivot='middle')
            # except ValueError:
            #     self.ax.quiver(self.piv_images_list[image_number][3][0][self.piv_images_list[image_number][3][4]],
            #                    0 -
            #                    self.piv_images_list[image_number][3][1][self.piv_images_list[image_number][3][4]],
            #                    self.piv_images_list[image_number][3][2][self.piv_images_list[image_number][3][4]],
            #                    self.piv_images_list[image_number][3][3][self.piv_images_list[image_number][3][4]],
            #                    color='r',
            #                    pivot='middle')

        if self.bit == "8 bit":
            self.ax.imshow(np.uint8(self.piv_images_list[image_number][2]), cmap=plt.get_cmap('gray'), origin="upper")
        else:
            self.ax.imshow(np.uint16(self.piv_images_list[image_number][2]), cmap=plt.get_cmap('gray'), origin="upper")
        self.ax.axis('off')

        if self.piv_images_list[image_number][3]:

            self.ax.quiver(self.piv_images_list[image_number][3][0],
                           self.piv_images_list[image_number][3][1],
                           self.piv_images_list[image_number][3][2], 
                           self.piv_images_list[image_number][3][3],
                           color='y', pivot='middle')



        """
        self.zoom_ax.imshow(np.uint16(self.piv_images_list[image_number][2]), cmap=plt.cm.gray)
        self.zoom_ax.axis('off')
        if self.xy_zoom[0][0] != None:
        self.zoom_ax.set_xlim(self.xy_zoom[0][0], self.xy_zoom[0][1])
        self.zoom_ax.set_ylim(self.xy_zoom[1][0], self.xy_zoom[1][1])
        """

        if self.xy_zoom[0][0] == 0 and self.xy_zoom[0][1] == len(self.piv_images_list[0][2][0]) and self.xy_zoom[1][
            0] == 0 and self.xy_zoom[1][1] == len(self.piv_images_list[0][2]):
            self.zoom_rectangle = Rectangle((self.xy_zoom[0][0], self.xy_zoom[1][0]),
                                            abs(self.xy_zoom[0][1] - self.xy_zoom[0][0]),
                                            abs(self.xy_zoom[1][1] - self.xy_zoom[1][0]), facecolor='none',
                                            alpha=0.1,
                                            edgecolor='none', linewidth=1, fill=False)

        elif not self.xy_zoom[0][0] == None:
            self.zoom_rectangle = Rectangle((self.xy_zoom[0][0], self.xy_zoom[1][0]),
                                            abs(self.xy_zoom[0][1] - self.xy_zoom[0][0]),
                                            abs(self.xy_zoom[1][1] - self.xy_zoom[1][0]), facecolor='none',
                                            alpha=0.6,
                                            linestyle='-', edgecolor='white', linewidth=2, fill=True)
            self.ax.add_patch(self.zoom_rectangle)
        if change_number:
            self.main_class.current_image_number.setText(str(image_number + 1))
        self.piv_canvas.draw()

    # function to add an image
    def add_image(self, image_path, bit):
        self.bit = bit
        if self.bit == "8 bit":
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint8(tools.imread(image_path)), None, None])
        else:
            self.piv_images_list.append(
                [image_path, QtCore.QFileInfo(image_path).fileName(), np.uint16(tools.imread(image_path)), None, None])

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
                                        rectprops=dict(alpha=0.6, linestyle='-', edgecolor='white',
                                                       linewidth=2))
        else:
            self.xy_zoom[0][0] = 0  # top left / x1
            self.xy_zoom[0][1] = len(self.piv_images_list[0][2][0])  # top right / x2
            self.xy_zoom[1][0] = 0  # bottom left/ y1
            self.xy_zoom[1][1] = len(self.piv_images_list[0][2])  # bottom right/ y2
            self.reset_piv()
        self.show_plot(self.current_image, self.bit)

    def zoom(self, click_point, release_point):
        x1, y1 = click_point.xdata, click_point.ydata
        x2, y2 = release_point.xdata, release_point.ydata
        self.xy_zoom[0][0] = min([x1, x2])
        self.xy_zoom[0][1] = max([x1, x2])
        self.xy_zoom[1][0] = min([y1, y2])
        self.xy_zoom[1][1] = max([y1, y2])
        self.rs = None
        self.show_plot(self.current_image, self.bit)

    def reset_piv(self):
        for i in range(len(self.piv_images_list)):
            self.piv_images_list[i][3] = None


class PIVStartClass(QtCore.QThread):
    piv_finished_signal = QtCore.Signal()
    piv_stop_signal = QtCore.Signal()

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.frame_a = None
        self.frame_b = None
        self.dt = None
        self.winsize = None
        self.overlap = None
        self.searchsize = None
        self.sig2noise = None
        self.mask = None
        self.x = None
        self.y = None
        self.u = None
        self.v = None
        self.piv = None
        self.scale = None
        self.jump = None
        self.frames_list = []
        self.is_to_stop = False
        self.error_message = None

    def __del__(self):
        self.wait()

    def set_args_start(self, frames_list, width_a, height_a, width_b, height_b, horizontal, vertical, sn_type, sn_value,
                       scale, outer_filter, jump, dt, is_interactive, error_message, piv):
        self.frames_list = frames_list
        if len(self.frames_list) < 2:
            error_message.setText("you must choose at list two images to run the piv")
            error_message.exec()
        self.overlap = horizontal
        self.winsize = width_a
        self.searchsize = width_b
        self.dt = dt
        self.piv = piv
        self.scale = scale
        self.jump = jump
        self.error_message = error_message
        self.start()

    # running the piv process
    def run(self):
        self.is_to_stop = False
        self.piv.piv_results_list = []

        for i in range(0, len(self.frames_list) - 1, abs(self.jump)):
            if self.piv.xy_zoom[0][0]:
                try:
                    frame_a = self.frames_list[i][2][int(self.frames_list[i][2].shape[1] - self.piv.xy_zoom[1][1]): int(
                        self.frames_list[i][2].shape[1] - self.piv.xy_zoom[1][0]),
                              int(self.piv.xy_zoom[0][0]): int(
                                  self.piv.xy_zoom[0][1])]

                    frame_b = self.frames_list[i + 1][2][
                              int(self.frames_list[i + 1][2].shape[1] - self.piv.xy_zoom[1][1]): int(
                                  self.frames_list[i + 1][2].shape[1] - self.piv.xy_zoom[1][0]),
                              int(self.piv.xy_zoom[0][0]): int(
                                  self.piv.xy_zoom[0][1])]
                except ValueError:
                    frame_a = self.frames_list[i][2][int(self.frames_list[i][2].shape[1] - self.piv.xy_zoom[1][0]): int(
                        self.frames_list[i][2].shape[1] - self.piv.xy_zoom[1][1]),
                              int(self.piv.xy_zoom[0][0]): int(
                                  self.piv.xy_zoom[0][1])]

                    frame_b = self.frames_list[i + 1][2][
                              int(self.frames_list[i + 1][2].shape[1] - self.piv.xy_zoom[1][0]): int(
                                  self.frames_list[i + 1][2].shape[1] - self.piv.xy_zoom[1][1]),
                              int(self.piv.xy_zoom[0][0]): int(
                                  self.piv.xy_zoom[0][1])]

            else:
                frame_a = self.frames_list[i][2]

                frame_b = self.frames_list[i + 1][2]

            try:
                self.u, self.v, self.sig2noise = extended_search_area_piv(frame_a.astype(np.int32),
                                                                          frame_b.astype(
                                                                              np.int32),
                                                                          window_size=self.winsize,
                                                                          overlap=self.overlap,
                                                                          dt=self.dt, search_area_size=self.searchsize,
                                                                          sig2noise_method='peak2peak')
                self.x, self.y = get_coordinates(image_size=frame_a.shape, window_size=self.winsize,
                                                 overlap=self.overlap)
                self.u, self.v, self.mask = sig2noise_val(self.u, self.v, self.sig2noise, threshold=1.0)
                self.u, self.v = replace_outliers(self.u, self.v, method='localmean', max_iter=10, kernel_size=2)
                # self.x, self.y, self.u, self.v = uniform(self.x, self.y, self.u, self.v, scaling_factor=5)

                if self.piv.xy_zoom[0][0]:
                    self.x += int(self.piv.xy_zoom[0][0])
                    self.y += int(self.piv.xy_zoom[1][0])

                # self.u *= -1.0 # alex: this wasn't correct
                self.y = np.max(self.y) - self.y
                # self.v = -self.v 

            except ValueError:
                if self.searchsize < self.winsize:
                    self.error_message.setText("the search size cannot be smaller than the window size")
                elif self.overlap > self.winsize:
                    self.error_message.setText("Overlap has to be smaller than the window_size")
                else:
                    self.error_message.setText("ROI window to small")
                
                self.error_message.exec()
                break
            self.piv.piv_results_list.append([self.x, self.y, self.u, self.v, self.mask])
            self.piv.piv_images_list[i][3] = self.piv.piv_results_list[i // abs(self.jump)]
            data = np.zeros((len(np.ravel(self.u)), 5))
            res_list = [np.ravel(self.x), np.ravel(self.y), np.ravel(self.u), np.ravel(self.v), np.ravel(self.mask)]
            for j in range(0, 4):
                for k in range(len(res_list[j])):
                    data[k][j] = res_list[j][k]
            self.piv.piv_images_list[i][4] = data
            # save_openpiv_vec(self.piv.piv_images_list[i][1].split('.')[0], data, 'pix', 'dt',
            #                  len(data[0]), len(data))
            self.piv.show_plot(i, self.piv.bit, True)

            if i == len(self.frames_list) - 2 and self.jump == 1:
                self.piv.piv_results_list.append([self.x, self.y, self.u, self.v, self.mask])
                self.piv.piv_images_list[i + 1][3] = self.piv.piv_results_list[i + 1]
                self.piv.piv_images_list[i + 1][4] = data
                self.piv.show_plot(i + 1, self.piv.bit, True)

            if self.is_to_stop:
                break

        self.piv_finished_signal.emit()


if __name__ == '__main__':
    # run the application (it does nothing)
    import sys

    app = QtWidgets.QApplication(sys.argv)
    piv_plot_class = PIVPlot(QtWidgets.QWidget())

    sys.exit(app.exec_())
