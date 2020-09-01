# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp7.ui'
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
        self.btn_mues = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mues.setGeometry(QtCore.QRect(440, 350, 171, 51))
        self.btn_mues.setObjectName("btn_mues")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(780, 520, 151, 91))
        self.btn_save.setObjectName("btn_save")
        self.combo_mues = QtWidgets.QComboBox(self.centralwidget)
        self.combo_mues.setGeometry(QtCore.QRect(440, 430, 171, 21))
        self.combo_mues.setObjectName("combo_mues")
        self.combo_mues.addItem("")
        self.combo_mues.addItem("")
        self.combo_mues.addItem("")
        self.combo_mues.addItem("")
        self.combo_mues.addItem("")
        self.combo_mues.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 410, 101, 16))
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
        self.combo_cuan = QtWidgets.QComboBox(self.centralwidget)
        self.combo_cuan.setGeometry(QtCore.QRect(440, 220, 171, 21))
        self.combo_cuan.setObjectName("combo_cuan")
        self.combo_cuan.addItem("")
        self.combo_cuan.addItem("")
        self.combo_cuan.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 200, 131, 16))
        self.label_4.setObjectName("label_4")
        self.spinbox_gris = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_gris.setGeometry(QtCore.QRect(440, 270, 42, 22))
        self.spinbox_gris.setObjectName("spinbox_gris")
        self.spinbox_gris.setMinimum(2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 250, 131, 16))
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(429, 339, 191, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(4)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 130, 191, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(4)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.btn_open.raise_()
        self.btn_mues.raise_()
        self.btn_save.raise_()
        self.combo_mues.raise_()
        self.label.raise_()
        self.pat_im1.raise_()
        self.pat_im2.raise_()
        self.caja_im1.raise_()
        self.im_caja_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btn_cop.raise_()
        self.combo_cuan.raise_()
        self.label_4.raise_()
        self.spinbox_gris.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btn_open.clicked.connect(self.btn_open_Pressed)
        self.btn_mues.clicked.connect(self.btn_mues_Pressed)
        self.btn_cop.clicked.connect(self.btn_cuan_Pressed)
        self.btn_save.clicked.connect(self.btn_save_Pressed)
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
    
    def btn_mues_Pressed(self):
            muestreo= self.combo_mues.currentText()
            if muestreo=="Downsampling X2 Constante":
                self.out= submuestreo(self.im)
            if muestreo=="Downsampling X2 Bilineal":
                self.out= subm_bilineal(self.im)
            if muestreo=="Downsampling X2 Bicubico":
                self.out= subm_bicubico(self.im)   
            if muestreo=="Upsampling X2 Constante":
                self.out= supermuestreo(self.im)
            if muestreo=="Upsampling X2  Bilineal":
                self.out= superm_bilineal(self.im)
            if muestreo=="Upsampling X2  Bicubico":
                self.out= superm_bicubico(self.im)       
            plt.imsave("out.bmp",self.out,cmap="gray")
            self.pat_im2.setText("out.bmp") 
            pixmap = QtGui.QPixmap("out.bmp") # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.im_caja_2.width(), self.im_caja_2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.im_caja_2.setPixmap(pixmap) # Set the pixmap onto the label
            self.im_caja_2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center      
    
    def btn_cuan_Pressed(self):
            cuanti= self.combo_cuan.currentText()
            niv= self.spinbox_gris.value()
            if cuanti=="Uniforme":
                self.out= cuan_uniforme(self.im, niv)
            if cuanti=="Dithering Aleatorio":
                self.out= dit_aleatorio(self.im, niv)
            if cuanti=="Difusion del Error":
                self.out= dif_error(self.im, niv)  
            
            plt.imsave("out.bmp",self.out,cmap="gray")
            self.pat_im2.setText("out.bmp") 
            pixmap = QtGui.QPixmap("out.bmp") # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.im_caja_2.width(), self.im_caja_2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.im_caja_2.setPixmap(pixmap) # Set the pixmap onto the label
            self.im_caja_2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center              
    def btn_save_Pressed(self):
      fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar Imágen',"","Bitmaps (*.bmp)")
      plt.imsave(fileName, self.out, cmap="gray") 
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "Abrir Imagen"))
        self.btn_mues.setText(_translate("MainWindow", "Muestrear --->"))
        self.btn_save.setText(_translate("MainWindow", "Guardar Imagen"))
        self.combo_mues.setItemText(0, _translate("MainWindow", "Downsampling X2 Constante"))
        self.combo_mues.setItemText(1, _translate("MainWindow", "Downsampling X2 Bilineal"))
        self.combo_mues.setItemText(2, _translate("MainWindow", "Downsampling X2 Bicubico"))
        self.combo_mues.setItemText(3, _translate("MainWindow", "Upsampling X2 Constante"))
        self.combo_mues.setItemText(4, _translate("MainWindow", "Upsampling X2  Bilineal"))
        self.combo_mues.setItemText(5, _translate("MainWindow", "Upsampling X2  Bicubico"))
        self.label.setText(_translate("MainWindow", "Muestreo"))
        self.label_2.setText(_translate("MainWindow", "Imagen Original"))
        self.label_3.setText(_translate("MainWindow", "Imagen Procesada"))
        self.btn_cop.setText(_translate("MainWindow", "Cuantizar --->"))
        self.combo_cuan.setItemText(0, _translate("MainWindow", "Uniforme"))
        self.combo_cuan.setItemText(1, _translate("MainWindow", "Dithering Aleatorio"))
        self.combo_cuan.setItemText(2, _translate("MainWindow", "Difusion del Error"))
        self.label_4.setText(_translate("MainWindow", "Cuantizacion"))
        self.label_5.setText(_translate("MainWindow", "Cantidad de Nivel de Gris"))

def im_to_YIQ(im):
    im_norm= im/256
    mat_a_YIQ= np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    im_yiq= np.dot(im_norm, mat_a_YIQ.T)
    return im_yiq

kernel= np.array((-1/8, 5/8, 5/8, -1/8))
kernel2= np.dot(kernel.reshape((4,1)),kernel.reshape((1,4)))

def submuestreo(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an/2)+1,int(al/2)+1))
              
    for x in range(0,an,1):
        for y in range(0,al,1):
            aux= Y[x:x+2, y:y+2]
            out[int(x/2),int(y/2)]=aux[0,0]
    return out

def subm_bilineal(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an/2)+1,int(al/2)+1))
    for x in range(0,an,1):
        for y in range(0,al,1):
            aux= Y[x:x+2, y:y+2]
            out[int(x/2),int(y/2)]=aux.sum()/4
    return out

def subm_bicubico(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an/2)+1,int(al/2)+1))
    for x in range(0,an-1,1):
        for y in range(0,al-1,1):
            aux= Y[x-1:x+3, y-1:y+3]
            if(aux.shape[0]>3):
                if(aux.shape[1]>3):
                    aux_x=aux*kernel2
                    valor=aux_x.sum()
                    if valor>1:
                        valor=1
                    out[int(x/2),int(y/2)]=valor
    return out

def supermuestreo(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an*2),int(al*2)))

    for x in range(0,an,1):
        for y in range(0,al,1):
            aux= Y[x, y]
            out[2*x:2*x+2,2*y:2*y+2]=aux
    return out

def superm_bilineal(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an*2)-1,int(al*2)-1))
    for x in range(0,an-1,1):
        for y in range(0,al-1,1):

            aux= Y[x:x+2, y:y+2]
            out[2*x,2*y]= aux[0,0]
            out[2*x+1,2*y]= (aux[0,0]+aux[1,0])/2
            out[2*x,2*y+1]= (aux[0,0]+aux[0,1])/2
            out[2*x+1,2*y+1]= (aux[0,0]+aux[1,0]+ aux[0,0]+aux[0,1])/4
    return out

def superm_bicubico(im1):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    out= np.zeros((int(an*2)-1,int(al*2)-1))
    for x in range(0,an-1,1):
        for y in range(0,al-1,1):

            aux= Y[x-1:x+3, y-1:y+3]
            if(aux.shape[0]==4):
                if(aux.shape[1]==4):
                    out[2*x,2*y]= aux[1,1]
                    out[2*x,2*y+1]= np.sum(aux[1,:]*kernel)
                    out[2*x+1,2*y]= np.sum(aux[:,1]*kernel)
                    out[2*x+1,2*y+1]= np.sum(aux*kernel2)
    out[out>1]=1
    out[out<0]=0
    return out


def cuan_uniforme(im1,niv):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    aux= np.zeros((an,al))
    for x in range(0,an):
        for y in range(0,al):
            for i in range(0,niv):
                if Y[x,y]>i/niv and Y[x,y]<i+1/niv:
                    aux[x,y]= i/niv
    return aux

def dit_aleatorio(im1,niv):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    aux= np.zeros((an,al))
    for x in range(0,an):
        for y in range(0,al):
            rand= np.random.rand(niv,1)
            ran= np.sort(rand.reshape(niv,))
            ran[0]=0

            for i in range(0,niv-1):

                if Y[x,y]>=ran[i] and Y[x,y]<ran[i+1]:
                    aux[x,y]= ran[i]
                if Y[x,y]>=ran[niv-1]:
                    aux[x,y]= 1
    return aux

def dif_error(im1,niv):
    ima= np.asarray(im1)
    im_yiq= im_to_YIQ(ima)
    Y= im_yiq[:,:,0]
    an= Y.shape[0]
    al= Y.shape[1]
    aux= np.zeros((an,al))
    niveles= np.arange(0,1+1/niv,step=1/niv)
    for x in range(0,an):
        error=0
        for y in range(0,al):

            for i in range(0,niv-1):
                if Y[x,y]>=niveles[i]+error and Y[x,y]<niveles[i+1]+error:
                    aux[x,y]=niveles[i]
                if Y[x,y]>=niveles[i+1]+error:
                    aux[x,y]=1
                error= error+aux[x,y]-Y[x,y]   
    return aux
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

