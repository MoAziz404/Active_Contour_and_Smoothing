# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import ImageView
import Contour
import timeit
import numpy as np
import cv2 as cv
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 731, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_equalize_input_3 = QtWidgets.QLabel(self.tab)
        self.label_equalize_input_3.setGeometry(QtCore.QRect(370, 20, 231, 171))
        self.label_equalize_input_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_equalize_input_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_equalize_input_3.setObjectName("label_equalize_input_3")
        self.pushButton_equalize_1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_equalize_1.setGeometry(QtCore.QRect(80, 60, 140, 70))
        self.pushButton_equalize_1.setObjectName("pushButton_equalize_1")
        self.label_equalize_output_3 = QtWidgets.QLabel(self.tab)
        self.label_equalize_output_3.setGeometry(QtCore.QRect(370, 210, 231, 171))
        self.label_equalize_output_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_equalize_output_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_equalize_output_3.setObjectName("label_equalize_output_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 241, 71))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(120, 310, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_equalize_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_equalize_2.setGeometry(QtCore.QRect(80, 160, 140, 70))
        self.pushButton_equalize_2.setObjectName("pushButton_equalize_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_contour = QtWidgets.QLabel(self.tab_2)
        self.label_contour.setGeometry(QtCore.QRect(100, 0, 511, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_contour.sizePolicy().hasHeightForWidth())
        self.label_contour.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_contour.setFont(font)
        self.label_contour.setMouseTracking(True)
        self.label_contour.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_contour.setFrameShape(QtWidgets.QFrame.Box)
        self.label_contour.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_contour.setLineWidth(0)
        self.label_contour.setMidLineWidth(0)
        self.label_contour.setTextFormat(QtCore.Qt.PlainText)
        self.label_contour.setScaledContents(False)
        self.label_contour.setAlignment(QtCore.Qt.AlignCenter)
        self.label_contour.setObjectName("label_contour")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 70, 214, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.contour_settings_layout_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.contour_settings_layout_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contour_settings_layout_2.sizePolicy().hasHeightForWidth())
        self.contour_settings_layout_2.setSizePolicy(sizePolicy)
        self.contour_settings_layout_2.setMaximumSize(QtCore.QSize(210, 16777215))
        self.contour_settings_layout_2.setObjectName("contour_settings_layout_2")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.contour_settings_layout_2)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.gridLayout_27.addLayout(self.gridLayout_29, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_26 = QtWidgets.QLabel(self.contour_settings_layout_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(55, 0))
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_3.addWidget(self.label_26)
        self.text_alpha = QtWidgets.QLineEdit(self.contour_settings_layout_2)
        self.text_alpha.setObjectName("text_alpha")
        self.horizontalLayout_3.addWidget(self.text_alpha)
        self.gridLayout_27.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_28 = QtWidgets.QLabel(self.contour_settings_layout_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QtCore.QSize(55, 0))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.text_gamma = QtWidgets.QLineEdit(self.contour_settings_layout_2)
        self.text_gamma.setObjectName("text_gamma")
        self.horizontalLayout_5.addWidget(self.text_gamma)
        self.gridLayout_27.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_27 = QtWidgets.QLabel(self.contour_settings_layout_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(55, 0))
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)
        self.text_num_iterations = QtWidgets.QLineEdit(self.contour_settings_layout_2)
        self.text_num_iterations.setObjectName("text_num_iterations")
        self.horizontalLayout_4.addWidget(self.text_num_iterations)
        self.gridLayout_27.addLayout(self.horizontalLayout_4, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_29 = QtWidgets.QLabel(self.contour_settings_layout_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QtCore.QSize(55, 0))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_6.addWidget(self.label_29)
        self.text_beta = QtWidgets.QLineEdit(self.contour_settings_layout_2)
        self.text_beta.setObjectName("text_beta")
        self.horizontalLayout_6.addWidget(self.text_beta)
        self.gridLayout_27.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.radioButton_circle_contour = QtWidgets.QRadioButton(self.contour_settings_layout_2)
        self.radioButton_circle_contour.setObjectName("radioButton_circle_contour")
        self.gridLayout_27.addWidget(self.radioButton_circle_contour, 0, 0, 1, 1)
        self.radioButton_square_contour = QtWidgets.QRadioButton(self.contour_settings_layout_2)
        self.radioButton_square_contour.setObjectName("radioButton_square_contour")
        self.gridLayout_27.addWidget(self.radioButton_square_contour, 1, 0, 1, 1)
        self.gridLayout_25.addWidget(self.contour_settings_layout_2, 0, 0, 1, 1)
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.btn_clear_anchors = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_clear_anchors.setObjectName("btn_clear_anchors")
        self.gridLayout_30.addWidget(self.btn_clear_anchors, 0, 0, 1, 1)
        self.btn_reset_contour = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_reset_contour.setObjectName("btn_reset_contour")
        self.gridLayout_30.addWidget(self.btn_reset_contour, 2, 0, 1, 1)
        self.btn_apply_contour = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_apply_contour.setObjectName("btn_apply_contour")
        self.gridLayout_30.addWidget(self.btn_apply_contour, 1, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_30, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(240, 70, 461, 341))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(-10, 40, 471, 301))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contour_input = ImageView(self.widget)
        self.contour_input.setObjectName("contour_input")
        self.horizontalLayout.addWidget(self.contour_input)
        self.contour_output = ImageView(self.widget)
        self.contour_output.setObjectName("contour_output")
        self.horizontalLayout.addWidget(self.contour_output)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(0, 20, 471, 18))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.contour_input.ui.roiPlot.hide()
        self.contour_input.ui.menuBtn.hide()
        self.contour_input.view.setMenuEnabled(False)
        self.contour_output.ui.roiPlot.hide()
        self.contour_output.ui.menuBtn.hide()
        self.contour_output.view.setMenuEnabled(False)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.contour_input.ui.histogram.hide()
        self.contour_output.ui.histogram.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_equalize_input_3.setText(_translate("MainWindow", "Input Image"))
        self.pushButton_equalize_1.setText(_translate("MainWindow", "Load image"))
        self.label_equalize_output_3.setText(_translate("MainWindow", "Output Image"))
        self.label_3.setText(_translate("MainWindow", "Select Filter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ellipse"))
        self.comboBox.setItemText(2, _translate("MainWindow", "circles"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Canny"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Lines"))
        self.pushButton_equalize_2.setText(_translate("MainWindow", "Superimpose"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detect"))
        self.label_contour.setText(_translate("MainWindow", "Active Contour"))
        self.contour_settings_layout_2.setTitle(_translate("MainWindow", "Contour Settings"))
        self.label_26.setText(_translate("MainWindow", "Alpha"))
        self.label_28.setText(_translate("MainWindow", "Gamma"))
        self.label_27.setText(_translate("MainWindow", "Num_iterations"))
        self.label_29.setText(_translate("MainWindow", "Beta"))
        self.radioButton_circle_contour.setText(_translate("MainWindow", "Circle Contour"))
        self.radioButton_square_contour.setText(_translate("MainWindow", "Square Contour"))
        self.btn_clear_anchors.setText(_translate("MainWindow", "Clear Anchors"))
        self.btn_reset_contour.setText(_translate("MainWindow", "Reset"))
        self.btn_apply_contour.setText(_translate("MainWindow", "Apply contour"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Input_Image"))
        self.label_2.setText(_translate("MainWindow", "Processed Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Snake"))

        self.btn_apply_contour.clicked.connect(self.active_contour)
    def active_contour(self):
            """
            Apply Active Contour Model (Snake) to the given image on a certain shape.
            This algorithm is applied based on Greedy Algorithm
            :return:
            """

            img=cv.imread('./CT head.jpg')
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            
            
            # Get Contour Parameters
            text_alpha = self.text_alpha.text()
            text_beta = self.text_beta.text()
            text_gamma = self.text_gamma.text()
            num_iterations = self.text_num_iterations.text()
            
            if not (text_alpha and text_beta and text_gamma and num_iterations):
                self.show_error_message("Invalid Input!")
                return
            
            try:    
                alpha = float(text_alpha)
                beta = float(text_beta)
                gamma = float(text_gamma)
                num_iterations = int(num_iterations)
            except ValueError:
                self.show_error_message("Invalid Input! Please enter numeric values.")
                return
            
            num_points_circle = 65
            num_xpoints = 180
            num_ypoints = 180
            w_line = 1
            w_edge = 8

            # Initial variables
            contour_x, contour_y, window_coordinates = None, None, None

            # Calculate function run time
            start_time = timeit.default_timer()

            # Greedy Algorithm

            # copy the image because cv2 will edit the original source in the contour
            image_src = np.copy(img)


            if not (self.radioButton_circle_contour.isChecked() or self.radioButton_square_contour.isChecked()):
                self.show_error_message("Please choose an option for radio buttons!")
                return
            # Create Initial Contour and display it on the GUI
            if self.radioButton_square_contour.isChecked():
                contour_x, contour_y, window_coordinates = Contour.create_square_contour(source=image_src,
                                                                                        num_xpoints=num_xpoints,
                                                                                        num_ypoints=num_ypoints)
                # Set parameters with pre-tested values for good performance
                # alpha = 20
                # beta = 0.01
                # gamma = 2
                # num_iterations = 60
                self.text_alpha.setText(str(alpha))
                self.text_beta.setText(str(beta))
                self.text_gamma.setText(str(gamma))
                self.text_num_iterations.setText(str(num_iterations))

            elif self.radioButton_circle_contour.isChecked():
                contour_x, contour_y, window_coordinates = Contour.create_elipse_contour(source=image_src,
                                                                                        num_points=num_points_circle)
                # Set parameters with pre-tested values for good performance
                # alpha = 0.01
                # beta = 0.01
                # gamma = 2
                # num_iterations = 50
                self.text_alpha.setText(str(alpha))
                self.text_beta.setText(str(beta))
                self.text_gamma.setText(str(gamma))
                self.text_num_iterations.setText(str(num_iterations))

            # Display the input image after creating the contour
            src_copy = np.copy(image_src)
            initial_image = self.draw_contour_on_image(src_copy, contour_x, contour_y)
            self.display_image(initial_image, self.contour_input)

            # Calculate External Energy which will be used in each iteration of greedy algorithm
            external_energy = gamma * Contour.calculate_external_energy(image_src, w_line, w_edge)

            # Copy the coordinates to update them in the main loop
            cont_x, cont_y = np.copy(contour_x), np.copy(contour_y)

            # main loop of the greedy algorithm
            for iteration in range(num_iterations):
                # Start Applying Active Contour Algorithm
                cont_x, cont_y = Contour.iterate_contour(source=image_src, contour_x=cont_x, contour_y=cont_y,
                                                        external_energy=external_energy,
                                                        window_coordinates=window_coordinates,
                                                        alpha=alpha, beta=beta)

                # Display the new contour after each iteration
                src_copy = np.copy(image_src)
                processed_image = self.draw_contour_on_image(src_copy, cont_x, cont_y)
                self.display_image(processed_image,self.contour_output)

                # Used to allow the GUI to update ImageView Object without lagging
                QtWidgets.QApplication.processEvents()

            # Function end
            end_time = timeit.default_timer()
    @staticmethod
    def draw_contour_on_image(source, points_x, points_y):
        """
        This function draws a given contour coordinates on the given image

        :param source: image source to draw the contour above it
        :param points_x: list of indices of the contour in x-direction
        :param points_y: list of indices of the contour in y-direction
        :return:
        """

        # Copy the image source to prevent modifying the original image
        src = np.copy(source)

        points = []
        for px, py in zip(points_x, points_y):
            points.append([px, py])

        points = np.array(points, np.int32)
        points = points.reshape((-1, 1, 2))

        image = cv.polylines(src, [points], isClosed=True, color=(0, 255, 0), thickness=2)

        return image
    @staticmethod
    def display_image(source: np.ndarray, widget: pg.ImageView):
        """
        Displays the given image source in the specified ImageView widget

        :param source: image source
        :param widget: ImageView object
        :return: void
        """

        # Copy the original source because cv2 updates the passed parameter
        src = np.copy(source)

        # Rotate the image 90 degree because ImageView is rotated
        src = cv.transpose(src)

        widget.setImage(src)
        widget.view.setRange(xRange=[0, src.shape[0]], yRange=[0, src.shape[1]],
                             padding=0)
        widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        

    def show_error_message(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec_()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()  # Create an instance of QMainWindow
    ui = Ui_MainWindow()  # Create an instance of your UI class
    ui.setupUi(MainWindow)  # Set up the UI on the MainWindow instance
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Execute the application event loop

