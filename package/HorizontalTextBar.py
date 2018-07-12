from PySide2 import QtWidgets, QtCore


# the class is to make the text of the tabs of the settings be horizontal
class HorizontalTextBar(QtWidgets.QTabBar):
    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        option = QtWidgets.QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, option)
            painter.drawText(self.tabRect(index),
                             QtCore.Qt.AlignCenter | QtCore.Qt.TextDontClip,
                             self.tabText(index))

    def tabSizeHint(self, index):
        size = QtWidgets.QTabBar.tabSizeHint(self, index)
        if size.width() < size.height():
            size.transpose()
        return size
