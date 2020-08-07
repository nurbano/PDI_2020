# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image #Libreria PILLOW
import numpy as np    #Libreria NUMPY
import qdarkstyle
from matplotlib import pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(130, 520, 151, 91))
        self.btn_open.setObjectName("btn_open")
        self.btn_fil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fil.setGeometry(QtCore.QRect(440, 350, 171, 51))
        self.btn_fil.setObjectName("btn_fil")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(780, 520, 151, 91))
        self.btn_save.setObjectName("btn_save")
        self.combo_fil = QtWidgets.QComboBox(self.centralwidget)
        self.combo_fil.setGeometry(QtCore.QRect(440, 430, 171, 21))
        self.combo_fil.setObjectName("combo_fil")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.combo_fil.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 410, 47, 13))
        self.label.setObjectName("label")
        self.pat_im1 = QtWidgets.QLineEdit(self.centralwidget)
        self.pat_im1.setGeometry(QtCore.QRect(10, 460, 401, 51))
        self.pat_im1.setObjectName("pat_im1")
        self.pat_im2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pat_im2.setGeometry(QtCore.QRect(640, 460, 401, 51))
        self.pat_im2.setObjectName("pat_im2")
        self.caja_im1 = QtWidgets.QLabel(self.centralwidget)
        self.caja_im1.setGeometry(QtCore.QRect(10, 50, 400, 400))
        self.caja_im1.setFrameShape(QtWidgets.QFrame.Box)
        self.caja_im1.setText("")
        self.caja_im1.setObjectName("caja_im1")
        self.im_caja_2 = QtWidgets.QLabel(self.centralwidget)
        self.im_caja_2.setGeometry(QtCore.QRect(640, 50, 400, 400))
        self.im_caja_2.setFrameShape(QtWidgets.QFrame.Box)
        self.im_caja_2.setText("")
        self.im_caja_2.setObjectName("im_caja_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 10, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_cop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cop.setGeometry(QtCore.QRect(440, 140, 171, 51))
        self.btn_cop.setObjectName("btn_cop")
        self.combo_tam = QtWidgets.QComboBox(self.centralwidget)
        self.combo_tam.setGeometry(QtCore.QRect(440, 480, 171, 21))
        self.combo_tam.setObjectName("combo_tam")
        self.combo_tam.addItem("")
        self.combo_tam.addItem("")
        self.combo_tam.addItem("")
        self.combo_tam.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 460, 47, 13))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_open.clicked.connect(self.btn_open_Pressed)
        self.btn_fil.clicked.connect(self.btn_filtro_Pressed)
        self.btn_save.clicked.connect(self.btn_save_Pressed)
        self.btn_cop.clicked.connect(self.btn_cop_Pressed)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
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
        filtro= self.combo_fil.currentText()
        tam= self.combo_tam.currentText()
        if tam=="3x3":
            cant= 3
        if tam=="5x5":
            cant= 5
        if tam=="7x7":
            cant= 7    
        
        if filtro=="Erosion":
            self.out= erosion(self.im, cant)
        if filtro=="Dilatacion":
            self.out= dilatacion(self.im, cant)
        if filtro=="Apertura":
            self.out= apertura(self.im, cant)
        if filtro=="Cierre":
            self.out= cierre(self.im, cant) 
        if filtro=="Borde Exterior":
             self.out= borde_ext(self.im, cant) 
        if filtro=="Borde Interior":
             self.out= borde_int(self.im, cant) 
        if filtro=="Mediana":
             self.out= mediana(self.im, cant)      
        if filtro=="Gradiente":
             self.out= gradiente(self.im, cant)      
        if filtro=="Top-hat":
             self.out= tophat(self.im, cant)    
            
        plt.imsave("out.bmp",self.out,cmap="gray")
        self.pat_im2.setText("out.bmp") 
        pixmap = QtGui.QPixmap("out.bmp") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.im_caja_2.width(), self.im_caja_2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.im_caja_2.setPixmap(pixmap) # Set the pixmap onto the label
        self.im_caja_2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center      
      
    def btn_save_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar Imágen',"","Bitmaps (*.bmp)")
        plt.imsave(fileName, self.out, cmap="gray")       
        
    def btn_cop_Pressed(self):    
        self.pat_im1.setText("out.bmp") 
        pixmap = QtGui.QPixmap("out.bmp") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.caja_im1.width(), self.caja_im1.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.caja_im1.setPixmap(pixmap) # Set the pixmap onto the label
        self.caja_im1.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center 
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procesamiento Morfologico"))
        self.btn_open.setText(_translate("MainWindow", "Abrir Imagen"))
        self.btn_fil.setText(_translate("MainWindow", "Filtrar ---->"))
        self.btn_save.setText(_translate("MainWindow", "Guardar Imagen"))
        self.combo_fil.setItemText(0, _translate("MainWindow", "Erosion"))
        self.combo_fil.setItemText(1, _translate("MainWindow", "Dilatacion"))
        self.combo_fil.setItemText(2, _translate("MainWindow", "Apertura"))
        self.combo_fil.setItemText(3, _translate("MainWindow", "Cierre"))
        self.combo_fil.setItemText(4, _translate("MainWindow", "Borde Exterior"))
        self.combo_fil.setItemText(5, _translate("MainWindow", "Borde Interior"))
        self.combo_fil.setItemText(6, _translate("MainWindow", "Mediana"))
        self.combo_fil.setItemText(7, _translate("MainWindow", "Gradiente"))
        self.combo_fil.setItemText(8, _translate("MainWindow", "Top-hat"))
        self.label.setText(_translate("MainWindow", "Filtro"))
        self.label_2.setText(_translate("MainWindow", "Imagen Original"))
        self.label_3.setText(_translate("MainWindow", "Imagen Filtrada"))
        self.btn_cop.setText(_translate("MainWindow", "<---- Copiar"))
        self.combo_tam.setItemText(0, _translate("MainWindow", "3x3"))
        self.combo_tam.setItemText(1, _translate("MainWindow", "5x5"))
        self.combo_tam.setItemText(2, _translate("MainWindow", "7x7"))
        self.combo_tam.setItemText(3, _translate("MainWindow", "9x9"))
        self.label_4.setText(_translate("MainWindow", "Elemento"))

def im_to_YIQ(im):
    im_norm= im/256
    mat_a_YIQ= np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    im_yiq= np.dot(im_norm, mat_a_YIQ.T)
    return im_yiq

def erosion(im, tam):
    ima= np.asarray(im)
    arr_yiq= im_to_YIQ(ima)
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    Y=arr_yiq[:,:,0]
    cant=tam
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
            valor= aux.min()
            nuevo_y[x-au][y-au]= valor
    return nuevo_y

def dilatacion(im, tam):
    ima= np.asarray(im)
    arr_yiq= im_to_YIQ(ima)
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    Y=arr_yiq[:,:,0]
    cant=tam
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
            valor= aux.max()
            nuevo_y[x-au][y-au]= valor
    return nuevo_y

def apertura(im, tam):
    #Erosión
    ima= np.asarray(im)
    arr_yiq= im_to_YIQ(ima)
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    Y=arr_yiq[:,:,0]
    cant=tam
    au= int((cant-1)/2)
    nuevo= np.zeros((w+cant-1,h+cant-1))
    aux= np.zeros((cant,cant))
    
    for x in range(w):
        for y in range (h):
            nuevo[x+au][y+au]= Y[x][y]
    
    y_ero= np.zeros((w+cant-1,h+cant-1))

    for x in range(au,w+au):
        for y in range (au, h+au):
            aux= nuevo[x-au:x+au+1,y-au:y+au+1]
            valor= aux.min()
            y_ero[x][y]= valor
    #Dilatación
    y_dil= np.zeros((w,h))
    for x in range(au,w+au):
        for y in range (au, h+au):
            aux= y_ero[x-au:x+au+1,y-au:y+au+1]
            valor= aux.max()
            y_dil[x-au][y-au]= valor
    return y_dil

def cierre(im, tam):
    #Dilatación
    ima= np.asarray(im)
    arr_yiq= im_to_YIQ(ima)
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    Y=arr_yiq[:,:,0]
    cant=tam
    au= int((cant-1)/2)
    nuevo= np.zeros((w+cant-1,h+cant-1))
    aux= np.zeros((cant,cant))
    for x in range(w):
        for y in range (h):
            nuevo[x+au][y+au]= Y[x][y]
    y_dil= np.zeros((w+cant-1,h+cant-1))

    for x in range(au,w+au):
        for y in range (au, h+au):
            aux= nuevo[x-au:x+au+1,y-au:y+au+1]
            valor= aux.max()
            y_dil[x][y]= valor
    #Erosión
    y_ero= np.zeros((w,h))
    for x in range(au,w+au):
        for y in range (au, h+au):
            aux= y_dil[x-au:x+au+1,y-au:y+au+1]
            valor= aux.max()
            y_ero[x-au][y-au]= valor
    return y_ero

def borde_ext(im, cant):
    y_ori=im_to_YIQ(np.asarray(im))[:,:,0]
    y_dil= dilatacion(im,cant)
    y_borde_ext= y_dil- y_ori
    #Clampeo
    y_borde_ext[y_borde_ext>1]=1
    y_borde_ext[y_borde_ext<0]=0
    return y_borde_ext

def borde_int(im, cant):
    y_ori=im_to_YIQ(np.asarray(im))[:,:,0]
    y_ero= erosion(im,cant)
    y_borde_int= y_ori-y_ero
    #Clampeo
    y_borde_int[y_borde_int>1]=1
    y_borde_int[y_borde_int<0]=0
    return y_borde_int
def mediana(im, tam):
    ima= np.asarray(im)
    arr_yiq= im_to_YIQ(ima)
    w= arr_yiq.shape[0]
    h= arr_yiq.shape[1]
    Y=arr_yiq[:,:,0]
    cant=tam
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
            valor= np.median(aux)
            nuevo_y[x-au][y-au]= valor
    return nuevo_y

def gradiente(im, cant):
    y_dil= dilatacion(im,cant)
    y_ero= erosion(im,cant)
    y_gradiente= y_dil-y_ero
    #Clampeo
    y_gradiente[y_gradiente>1]=1
    y_gradiente[y_gradiente<0]=0
    return y_gradiente

def tophat(im, cant):
    y_ori=im_to_YIQ(np.asarray(im))[:,:,0]
    y_ap= apertura(im,cant)
    y_tophat= y_ori-y_ap
    #Clampeo
    y_tophat[y_tophat>1]=1
    y_tophat[y_tophat<0]=0
    return y_tophat

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

