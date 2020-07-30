# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image #Libreria PILLOW
import numpy as np    #Libreria NUMPY
import qdarkstyle
from matplotlib import pyplot as plt

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(170, 610, 151, 91))
        self.btn_open.setObjectName("btn_open")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 650, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(710, 610, 151, 91))
        self.btn_save.setObjectName("btn_save")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 620, 171, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 600, 47, 13))
        self.label.setObjectName("label")
        self.pat_im1 = QtWidgets.QLineEdit(self.centralwidget)
        self.pat_im1.setGeometry(QtCore.QRect(10, 570, 511, 20))
        self.pat_im1.setObjectName("pat_im1")
        self.pat_im1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pat_im1_2.setGeometry(QtCore.QRect(540, 570, 511, 20))
        self.pat_im1_2.setObjectName("pat_im1_2")
        self.caja_im1 = QtWidgets.QLabel(self.centralwidget)
        self.caja_im1.setGeometry(QtCore.QRect(10, 50, 512, 511))
        self.caja_im1.setFrameShape(QtWidgets.QFrame.Box)
        self.caja_im1.setText("")
        self.caja_im1.setObjectName("caja_im1")
        self.im_caja_2 = QtWidgets.QLabel(self.centralwidget)
        self.im_caja_2.setGeometry(QtCore.QRect(540, 50, 512, 511))
        self.im_caja_2.setFrameShape(QtWidgets.QFrame.Box)
        self.im_caja_2.setText("")
        self.im_caja_2.setObjectName("im_caja_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 10, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #self.show_dialog()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_open.clicked.connect(self.btn_open_Pressed)
        self.pushButton_2.clicked.connect(self.btn_filtro_Pressed)
        self.btn_save.clicked.connect(self.btn_save_Pressed)
        
    def show_dialog(self):
       roll, done2 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter your roll:')   
        # self.dialog = QtWidgets.QDialog()
        # self.dialog.setWindowTitle(" Factor de Amplificacion")
        # self.dialog.factor= QtWidgets.QDoubleSpinBox(self.centralwidget)
        # self.dialog.factor.setGeometry(QtCore.QRect(10, 570, 511, 20))
        # self.dialog.factor.setObjectName("factor") 
        # #dialog.ui = Form()
        # self.dialog.setTabOrder
        
        # self.dialog.show()
        #sys.exit(self.dialog.exec_())
     

    def btn_open_Pressed(self):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Imagen", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)") # Ask for file
            if fileName: # If the user gives a file
                self.pat_im1.setText(fileName) 
                pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
                pixmap = pixmap.scaled(self.caja_im1.width(), self.caja_im1.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
                self.caja_im1.setPixmap(pixmap) # Set the pixmap onto the label
                self.caja_im1.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center   
                self.im= Image.open(fileName)
    
    def btn_filtro_Pressed(self):
        filtro= self.comboBox.currentText()
        if filtro=="Identidad3x3":
            ker= kerI3
        if filtro=="Plano3x3":
            ker=ker_plano
        if filtro=="Barlett3x3":
            ker=kerB3
        if filtro=="Barlett5x5":
            ker=kerB5
        if filtro=="Barlett7x7":
            ker=kerB7
        if filtro=="Gauss5x5":
           ker=kerG5
        if filtro=="Gauss7X7":
           ker=kerG7
        if filtro=="Laplaceano4v":
          ker=kerLA4v
        if filtro=="Laplaceano8v":
          ker=kerLA8v
        if filtro=="Laplaceano3x3_4V_AMP":
           fact, ok = QtWidgets.QInputDialog.getDouble(self, 'Factor', 'Ingrese factor', 0.2, 0.1, 1, 2)                                                   
           if ok:                                                                                                                             
            ker= kerLAamp(kerLA4v,fact)
        if filtro=="Laplaceano3x3_8V_AMP":
           fact, ok = QtWidgets.QInputDialog.getDouble(self, 'Factor', 'Ingrese factor', 0.2, 0.1, 1, 2)                                                   
           if ok:                                                                                                                             
            ker= kerLAamp(kerLA8v,fact)  
        if filtro=="Sobel-E":
          ker=kerSOBe
        if filtro=="Sobel-SE":
          ker=kerSOBse
        if filtro=="Sobel-S":
          ker=kerSOBs
        if filtro=="Sobel-SO":
          ker=kerSOBso
        if filtro=="Sobel-O":
          ker=kerSOBo
        if filtro=="Sobel-NO":
          ker=kerSOBno
        if filtro=="Sobel-N":
          ker=kerSOBn 
        if filtro=="Laplaceano5x5_0.2":
          ker=kerLA5  
        if filtro=="Laplaceano5x5_0.4":
          ker=kerLA5v   
        if filtro=="Pasabanda Gaussiano":
           ker=kerDG5
         
        self.out= conv_ker(self.im, ker)
        plt.imsave("out.bmp",self.out,cmap="gray")
        self.pat_im1_2.setText("out.bmp") 
        pixmap = QtGui.QPixmap("out.bmp") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.im_caja_2.width(), self.im_caja_2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.im_caja_2.setPixmap(pixmap) # Set the pixmap onto the label
        self.im_caja_2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center  
        
    def btn_save_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar Espectro',"","Bitmaps (*.bmp)")
        plt.imsave(fileName, self.out, cmap="gray")
        
        
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procesamiento por convolucion"))
        self.btn_open.setText(_translate("MainWindow", "Abrir Imagen"))
        self.pushButton_2.setText(_translate("MainWindow", "Filtrar"))
        self.btn_save.setText(_translate("MainWindow", "Guardar Imagen"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Identidad3x3"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Plano3x3"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Barlett3x3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Barlett5x5"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Barlett7x7"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Gauss5x5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Gauss7x7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Laplaceano4v"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Laplaceano8v"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Laplaceano3x3_4V_AMP"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Laplaceano3x3_8V_AMP"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Laplaceano3x3_8V"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Sobel-E"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Sobel-SE"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Sobel-S"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Sobel-SO"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Sobel-O"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Sobel-NO"))
        self.comboBox.setItemText(18, _translate("MainWindow", "Sobel-N"))
        self.comboBox.setItemText(19, _translate("MainWindow", "Pasabanda Gaussiano"))
        self.comboBox.setItemText(20, _translate("MainWindow", "Laplaceano5x5_0.2"))
        self.comboBox.setItemText(21, _translate("MainWindow", "Laplaceano5x5_0.4"))
        self.label.setText(_translate("MainWindow", "Filtro"))
        self.label_2.setText(_translate("MainWindow", "Imagen Original"))
        self.label_3.setText(_translate("MainWindow", "Imagen Filtrada"))


        
#FUNCIONES
def im_to_YIQ(im):
    im_norm= im/256
    mat_a_YIQ= np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    im_yiq= np.dot(im_norm, mat_a_YIQ.T)
    return im_yiq


def conv_ker(im, ker):
    arr= np.asarray(im)
    arr_yiq= im_to_YIQ(arr)
    Y= arr_yiq[:,:,0]
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    cant= ker.shape[0]
    au= int((cant-1)/2)
    nuevo= np.zeros((w+cant-1,h+cant-1))
    aux= np.zeros((cant,cant))
    for x in range(w):
        for y in range (h):
            nuevo[x+au][y+au]= Y[x][y]
    nuevo_y= np.zeros((w,h))
    for x in range(au,w+au):
        for y in range (au, h+au):
            aux= nuevo[x-au:x+au+1,y-au:y+au+1]
            aux_2= aux*ker
            valor= np.sum(aux_2)
            nuevo_y[x-au][y-au]= valor
    nuevo_y[nuevo_y>1]=1
    nuevo_y[nuevo_y<0]=0
    return nuevo_y

def kerLAamp(ker_in, fact):
    ker= kerI3+ker_in*fact
    return ker

#KERNEL
#IDENTIDAD
kerI3= np.zeros((3,3))
kerI3[1][1]=1
#Plano
ker_plano= np.zeros((3,3))
ker_plano+=1/9
#Bartlett3
Bartlett3= np.array((1,2,1))
kerB3= np.dot(Bartlett3.reshape((3,1)), Bartlett3.reshape((1,3)))/16
#Bartlett5
Bartlett5= np.array((1,2,3,2,1))
kerB5= np.dot(Bartlett5.reshape((5,1)), Bartlett5.reshape((1,5)))/81
#Bartlett7
Bartlett7= np.array((1,2,3,4,3,2,1))
kerB7= np.dot(Bartlett7.reshape((7,1)), Bartlett7.reshape((1,7)))/256
#Gauss5
Gauss5= np.array((1,4,6,4,1))
kerG5= np.dot(Gauss5.reshape((5,1)), Gauss5.reshape((1,5)))/256
#Gauss7
Gauss7= np.array((1,6,15,20,15,6,1))
kerG7= np.dot(Gauss7.reshape((7,1)), Gauss7.reshape((1,7)))/4096
#Laplaceano4V
kerLA4v= np.array(((0,-1,0),(-1,4,-1),(0,-1,0)))
#Laplaceano4V02
#kerLA4v02= kerI3+kerLA4v*0.2

#Laplaceano8V
kerLA8v= np.array(((-1,-1,-1),(-1,8,-1),(-1,-1,-1)))
#Sobel
kerSOBe= np.array(((-1,0,1),(-2,0,2),(-1,0,1)))
kerSOBse= np.array(((-2,-1,0),(-1,0,1),(0,1,2)))
kerSOBs= np.rot90(kerSOBe)
kerSOBso= np.rot90(kerSOBse)
kerSOBo= np.rot90(kerSOBs)
kerSOBno= np.rot90(kerSOBso)
kerSOBn= np.rot90(kerSOBo)
kerSOBne= np.rot90(kerSOBno)
#Laplace5x5
kerLA5= np.ones((5,5))*(-1)
kerLA5[2][2]=24
#Laplacev5x5
kerLA5v= np.array(((-1/16,-1/16,-1/16,-1/16,-1/16),(-1/16,1/9,1/9,1/9,-1/16),(-1/16,1/9,1/9,1/9,-1/16),(-1/16,1/9,1/9,1/9,-1/16),(-1/16,-1/16,-1/16,-1/16,-1/16)))
#DiferenciasGaus 5X5
Gaus3= np.array((0,1,2,1,0))
kerG3= np.dot(Gaus3.reshape((5,1)), Gaus3.reshape((1,5)))/16
kerDG5= kerG5-kerG3

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

