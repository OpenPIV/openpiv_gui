from PySide2 import QtWidgets
from openpiv import tools

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# i am still not putting the navigation tool bar becuse of some bugs
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# i needed to call QWidget and super to add the tool bar of matplotlib
class PIVPlot(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PIVPlot, self).__init__(parent)
        self.figure = Figure()

        # the canves is where the grath and the tool bar is
        self.piv_canves = FigureCanvas(self.figure)
        # self.piv_tool_bar = NavigationToolbar(self.piv_canves, self)

        # the piv_images_list is where the images are saved
        self.piv_images_list = []
        self.ax = self.figure.add_subplot(111)

        self.canvas_layout = QtWidgets.QGridLayout(parent)
        # self.canvas_layout.addWidget(self.piv_tool_bar)
        self.canvas_layout.addWidget(self.piv_canves)
        # self.piv_tool_bar.toolitems = [t for t in NavigationToolbar.toolitems if
        #                                t[0] in ['Home', 'Zoom', 'Save']]

    # function that showes the choosen image
    def show_plot(self, image_number):
        self.ax.clear()

        self.ax.imshow(tools.imread(self.piv_images_list[image_number]), cmap=plt.cm.gray)

        self.piv_canves.draw()

    # function to add an image
    def add_image(self, image_path):
        self.piv_images_list.append(image_path)

    def start_piv(self, width, height, horizontal, vertical, sn_type, sn_value, scale, outer_filter, jump):
        pass

if __name__ == '__main__':
    # run the application (it does nothing)
    import sys

    app = QtWidgets.QApplication(sys.argv)
    piv_plot_class = PIVPlot(QtWidgets.QWidget())

    sys.exit(app.exec_())
