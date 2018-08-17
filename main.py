from package.main_window import MainWindowClass
from package.setting_tab_widget import SettingsTabWidgetClass
from package.piv_plot import PIVPlot, PIVStartClass
from package.file_window import FileWindowClass
from package.settings_tab import SettingsTab
from package.image_piv_post_tab import PostProcessingTabClass
from PySide2 import QtWidgets, QtCore
from _functools import partial
import numpy as np
import sys


def run_main_window():
    app = QtWidgets.QApplication(sys.argv)

    # setup for the file window to add for the image processing tab
    file_window_frame = QtWidgets.QFrame()
    file_window_class = FileWindowClass(file_window_frame)
    file_window_class.window_setup()

    settings_tab_class = SettingsTab()
    settings_tab_class.setting_widget_setup()

    post_processing_tab_class = PostProcessingTabClass()
    post_processing_tab_class.post_processing_tab_setup()

    settings_tab_widget_class = SettingsTabWidgetClass()
    settings_tab_widget_class.settings_widget_setup()
    settings_tab_widget_class.image_processing_tab_class.image_processing_tab_layout.addWidget(file_window_frame, 1, 0,
                                                                                               1, 1)
    settings_tab_widget_class.settings_tab_widget.insertTab(1, settings_tab_class.settings_tab, "piv")
    settings_tab_widget_class.settings_tab_widget.insertTab(2, post_processing_tab_class.post_processing_tab, "post")
    settings_tab_widget_class.settings_tab_widget.setStyleSheet("background-color: rgb(240, 240, 240);")

    # a max and a min to the file window frame to make it look better
    file_window_frame.setMinimumSize(QtCore.QSize(198, 200))

    # create the widget of the main window
    main_window_widget = QtWidgets.QMainWindow()

    main_window_class = MainWindowClass(main_window_widget)
    main_window_class.main_widget_layout.addWidget(settings_tab_widget_class.settings_tab_widget, 0, 5, 3, 1)
    main_window_class.main_window_setup()

    # create the widget that will hold the plot
    piv_plot_widget = QtWidgets.QWidget()
    piv_plot_class = PIVPlot(piv_plot_widget, main_window_class)

    main_window_class.image_pages.addWidget(piv_plot_widget)

    settings_tab_widget_class.image_processing_tab_class.invert_button.clicked.connect(
        partial(invert_button, piv_plot_class, settings_tab_widget_class))

    # show the widget of the main window
    main_window_widget.show()

    # exit the program only if you trigger the exit action
    main_window_class.quit_action.triggered.connect(partial(sys.exit, partial(app.exec_)))

    # add a file only when the load button is triggered
    main_window_class.load_action.triggered.connect(file_window_class.add_file)

    # add/remove an image when it is added/removed from the list
    (file_window_class.file_list.model()).rowsInserted.connect(
        lambda: file_added(file_window_class, settings_tab_class, piv_plot_class, settings_tab_widget_class,
                           main_window_class))
    (file_window_class.file_list.model()).rowsRemoved.connect(
        lambda: file_removed(file_window_class, piv_plot_class, main_window_class, settings_tab_class,
                             settings_tab_widget_class))

    # change the image to the left/right next image
    main_window_class.left_button.clicked.connect(
        partial(change_image_number_left, piv_plot_class, main_window_class, settings_tab_widget_class))
    main_window_class.right_button.clicked.connect(
        partial(change_image_number_right, piv_plot_class, main_window_class, settings_tab_widget_class))

    # activating the ROI buttons to work when called
    settings_tab_class.select_roi_button.clicked.connect(partial(piv_plot_class.ROI_buttons, True))
    settings_tab_class.reset_roi_button.clicked.connect(partial(piv_plot_class.ROI_buttons, False))

    file_window_class.file_list.drop_signal.connect(partial(file_order_changed, file_window_class, piv_plot_class))

    settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentIndexChanged.connect(
        lambda: change_bit(str(settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText()),
                           piv_plot_class))

    settings_tab_class.dt_line_edit.textEdited.connect(lambda: check_dt_valid(settings_tab_class))

    settings_tab_class.jump_line_edit.textEdited.connect(lambda: jump_changed(settings_tab_class))

    # the piv start class is a class(QThread) that does the piv
    piv_start_class = PIVStartClass()
    settings_tab_class.start_button.clicked.connect(
        lambda: piv_start_class.set_args_start(piv_plot_class.piv_images_list,
                                               int(settings_tab_class.width_combo_box_a.currentText()),
                                               int(settings_tab_class.height_combo_box_a.currentText()),
                                               int(settings_tab_class.width_combo_box_b.currentText()),
                                               int(settings_tab_class.height_combo_box_b.currentText()),
                                               int(settings_tab_class.horizontal_combo_box.currentText()),
                                               int(settings_tab_class.vertical_combo_box.currentText()),
                                               int(settings_tab_class.type_combo_box.currentText()),
                                               settings_tab_class.value_spin_box.value(),
                                               settings_tab_class.scale_spin_box.value(),
                                               settings_tab_class.outer_filter_spin_box.value(),
                                               int(settings_tab_class.jump_line_edit.text()),
                                               float(settings_tab_class.dt_line_edit.text()),
                                               settings_tab_class.interactive_check_box.isTristate(),
                                               piv_plot_class))

    settings_tab_class.stop_button.clicked.connect(lambda: piv_start_class.exit())

    sys.exit(app.exec_())


def file_removed(file_window_class, piv_plot_class, main_window_class, settings_tab_class, settings_tab_widget_class):
    if file_window_class.file_list.count() == 0:
        del (piv_plot_class.piv_images_list[0])
        main_window_class.image_pages.setCurrentIndex(0)
        return 0

    for i in range(0, file_window_class.file_list.count()):
        if piv_plot_class.piv_images_list[i][1] != file_window_class.file_list.item(i).text():
            del (piv_plot_class.piv_images_list[i])
            piv_plot_class.show_plot(0,
                                     settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
            main_window_class.current_image_number.setText("1")
            # change the jump range when the images number changes
            change_jump_max_min(settings_tab_class, piv_plot_class)
            return 0

    if len(piv_plot_class.piv_images_list) - (file_window_class.file_list.count()) > 0:
        del (piv_plot_class.piv_images_list[-1])

        piv_plot_class.show_plot(0, settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        main_window_class.current_image_number.setText("1")

    # change the jump range when the images number changes
    change_jump_max_min(settings_tab_class, piv_plot_class)


# function that add the image that was added to the main widget
def file_added(file_window_class, settings_tab_class, piv_plot_class, settings_tab_widget_class, main_window_class):
    if file_window_class.file_list.item(file_window_class.file_list.count() - 1).text() == '':
        file_window_class.file_Window_class.file_list.takeItem(
            file_window_class.file_list.item(
                file_window_class.file_list.count() - 1))
        return 0

    if file_window_class.file_list.count() == 1:
        main_window_class.image_pages.setCurrentIndex(1)
        piv_plot_class.add_image(file_window_class.last_file,
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        piv_plot_class.show_plot(0, settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        main_window_class.current_image_number.setText("1")

    elif file_window_class.file_list.count() > 1:
        piv_plot_class.add_image(file_window_class.last_file,
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        piv_plot_class.show_plot(file_window_class.file_list.count() - 1,
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        main_window_class.current_image_number.setText(
            str(file_window_class.file_list.count()))

    # change the jump range when the images number changes
    change_jump_max_min(settings_tab_class, piv_plot_class)


# function that changes the max and min of jump
def change_jump_max_min(settings_tab_class, piv_plot_class):
    settings_tab_class.jump_max = len(piv_plot_class.piv_images_list) // 2
    settings_tab_class.jump_min = (-1) * (len(piv_plot_class.piv_images_list) // 2)
    if len(piv_plot_class.piv_images_list) > 1:
        settings_tab_class.jump_line_edit.setText("1")


def jump_changed(settings_tab_class):
    if settings_tab_class.jump_line_edit.text() != "":
        try:
            int(settings_tab_class.jump_line_edit.text())
            is_good = True
        except ValueError:
            settings_tab_class.jump_line_edit.setText("1")
            is_good = False
        if is_good:
            if abs(int(settings_tab_class.jump_line_edit.text())) > settings_tab_class.jump_max or abs(
                    int(settings_tab_class.jump_line_edit.text())) == 0:
                settings_tab_class.jump_line_edit.setText("1")


# function that moves to the next right image
def change_image_number_right(piv_plot_class, main_window_class, settings_tab_widget_class):
    if len(piv_plot_class.piv_images_list) == 0:
        return 0

    if int(main_window_class.current_image_number.text()) == len(piv_plot_class.piv_images_list):
        main_window_class.current_image_number.setText("1")
        piv_plot_class.show_plot(0, settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
    else:
        piv_plot_class.show_plot(int(main_window_class.current_image_number.text()),
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        main_window_class.current_image_number.setText(str(int(main_window_class.current_image_number.text()) + 1))


# function that moves to the next left image
def change_image_number_left(piv_plot_class, main_window_class, settings_tab_widget_class):
    if len(piv_plot_class.piv_images_list) == 0:
        return 0

    if int(main_window_class.current_image_number.text()) == 1:
        main_window_class.current_image_number.setText(str(len(piv_plot_class.piv_images_list)))
        piv_plot_class.show_plot(len(piv_plot_class.piv_images_list) - 1,
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
    else:
        piv_plot_class.show_plot(int(main_window_class.current_image_number.text()) - 2,
                                 settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        main_window_class.current_image_number.setText(str(int(main_window_class.current_image_number.text()) - 1))


def invert_button(piv_plot_class, settings_tab_widget_class):
    for i in range(len(piv_plot_class.piv_images_list)):
        if piv_plot_class.piv_images_list[i][1].lower().endswith(
                ('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
            piv_plot_class.piv_images_list[i][2] = piv_plot_class.invert(
                piv_plot_class.piv_images_list[i][2], False,
                settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
            piv_plot_class.show_plot(i,
                                     settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
        else:
            piv_plot_class.piv_images_list[i][2] = piv_plot_class.invert(
                piv_plot_class.piv_images_list[i][2], True,
                settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())
            piv_plot_class.show_plot(i,
                                     settings_tab_widget_class.image_processing_tab_class.bit_combo_box.currentText())


def file_order_changed(file_window_class, piv_plot_class):
    file_list_list = []
    for i in range(file_window_class.file_list.count()):
        file_list_list.append(file_window_class.file_list.item(i).text())

    piv_plot_class.piv_images_list.sort(key=lambda x: file_list_list.index(x[1]))


def change_bit(bit, piv_plot_class):
    if bit == "8 bit":
        for i in range(len(piv_plot_class.piv_images_list)):
            piv_plot_class.piv_images_list[i][2] = np.uint8(piv_plot_class.piv_images_list[i][2])
    else:
        for i in range(len(piv_plot_class.piv_images_list)):
            piv_plot_class.piv_images_list[i][2] = np.uint16(piv_plot_class.piv_images_list[i][2])


def check_dt_valid(setting_tab_class):
    try:
        float(setting_tab_class.dt_line_edit.text())
    except ValueError:
        if setting_tab_class.dt_line_edit.text() != "":
            setting_tab_class.dt_line_edit.setText("1.00")


def main():
    # run the program
    run_main_window()


if __name__ == '__main__':
    main()
