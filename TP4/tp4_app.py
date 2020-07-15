# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image #Libreria PILLOW
import numpy as np    #Libreria NUMPY
import qdarkstyle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Transformada de Fourier")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_gen_esp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_esp.setGeometry(QtCore.QRect(340, 150, 121, 41))
        self.btn_gen_esp.setObjectName("btn_gen_esp")
        self.btn_open_im = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_im.setGeometry(QtCore.QRect(20, 420, 121, 31))
        self.btn_open_im.setObjectName("btn_open_im")
        self.im_caja = QtWidgets.QLabel(self.centralwidget)
        self.im_caja.setGeometry(QtCore.QRect(20, 50, 300, 300))
        self.im_caja.setFrameShape(QtWidgets.QFrame.Box)
        self.im_caja.setText("")
        self.im_caja.setObjectName("im_caja")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 360, 301, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_gen_im = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_im.setGeometry(QtCore.QRect(340, 230, 121, 41))
        self.btn_gen_im.setObjectName("btn_gen_im")
        self.esp_caja = QtWidgets.QLabel(self.centralwidget)
        self.esp_caja.setGeometry(QtCore.QRect(480, 50, 300, 300))
        self.esp_caja.setFrameShape(QtWidgets.QFrame.Box)
        self.esp_caja.setText("")
        self.esp_caja.setObjectName("esp_caja")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 360, 301, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btn_open_esp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_esp.setGeometry(QtCore.QRect(480, 420, 121, 31))
        self.btn_open_esp.setObjectName("btn_open_esp")
        self.save_im = QtWidgets.QPushButton(self.centralwidget)
        self.save_im.setGeometry(QtCore.QRect(200, 420, 121, 31))
        self.save_im.setObjectName("save_im")
        self.btn_save_esp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_esp.setGeometry(QtCore.QRect(660, 420, 121, 31))
        self.btn_save_esp.setObjectName("btn_save_esp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.btn_open_esp.clicked.connect(self.btn_open_esp_Pressed)
        self.btn_open_im.clicked.connect(self.btn_open_im_Pressed)
        self.btn_gen_esp.clicked.connect(self.btn_gen_esp_Pressed)
        self.btn_gen_im.clicked.connect(self.btn_gen_im_Pressed)
        self.save_im.clicked.connect(self.btn_save_im_Pressed)
        self.btn_save_esp.clicked.connect(self.btn_save_esp_Pressed)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def btn_open_im_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Imagen", "", "Archivos de Imagen (*.png *.jpg *.jpeg *.bmp)") # Ask for file
        if fileName: # If the user gives a file
            self.lineEdit.setText(fileName) 
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.im_caja.width(), self.im_caja.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.im_caja.setPixmap(pixmap) # Set the pixmap onto the label
            self.im_caja.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center   
            self.im= Image.open(self.lineEdit.text())
            
    def btn_open_esp_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Espectro", "", "Archivos de Imagen (*.bmp)") # Ask for file
        if fileName: # If the user gives a file
            self.lineEdit_2.setText(fileName) 
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.esp_caja.width(), self.esp_caja.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.esp_caja.setPixmap(pixmap) # Set the pixmap onto the label
            self.esp_caja.setAlignment(QtCore.Qt.AlignCenter) # Align the label to 
            self.esp= Image.open(self.lineEdit_2.text())
    
    def btn_gen_esp_Pressed(self):
        #im= Image.open(self.lineEdit.text())
        a= np.asarray(self.im)
        espect, self.Fase, self.norm= generar_espectro(a, 100)
        espect.save("pro.bmp")
        self.esp= espect
        self.lineEdit_2.setText("pro.bmp") 
        pixmap = QtGui.QPixmap("pro.bmp") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.esp_caja.width(), self.esp_caja.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.esp_caja.setPixmap(pixmap) # Set the pixmap onto the label
        self.esp_caja.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center  
    
    def btn_gen_im_Pressed(self):
        #esp= Image.open(self.lineEdit_2.text())
        a= np.asarray(self.esp)
        im_re= reconstruir_im(a, 100, self.Fase, self.norm)
        
        im_re.save("res.bmp")
        self.im= im_re
        pixmap = QtGui.QPixmap("res.bmp") # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.im_caja.width(), self.im_caja.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.im_caja.setPixmap(pixmap) # Set the pixmap onto the label
        self.im_caja.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center  
        
    def btn_save_im_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar Imagen',"","Bitmaps (*.bmp)")
        self.im.save(fileName)
        #pixmap.save(&file, "PNG");
         #file = open(name, 'w')
    def btn_save_esp_Pressed(self):
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar Espectro',"","Bitmaps (*.bmp)")
        self.esp.save(fileName)
                
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transformada de Fourier"))
        self.btn_gen_esp.setText(_translate("MainWindow", "Generar Espectro-->"))
        self.btn_open_im.setText(_translate("MainWindow", "Abrir Imagen"))
        self.btn_gen_im.setText(_translate("MainWindow", "<--Generar Imagen"))
        self.btn_open_esp.setText(_translate("MainWindow", "Abrir Espectro"))
        self.save_im.setText(_translate("MainWindow", "Guardar Imagen"))
        self.btn_save_esp.setText(_translate("MainWindow", "Guardar Espectro"))
        self.label.setText(_translate("MainWindow", "Imagen"))
        self.label_2.setText(_translate("MainWindow", "Espectro"))

def generar_espectro(im, fact):
    im_array= np.asarray(im)
    im_yiq= im_to_YIQ(im_array)
    Y= im_yiq[:,:,0]
    F = np.fft.fft2(Y)
    F_shift = np.fft.fftshift(F)
    Fa= np.angle(F_shift)
    Mod = np.abs(F_shift)
    Pro_crudo =np.log(Mod/fact+1)
    Pro= Pro_crudo/Pro_crudo.max()
    pro_yiq= np.zeros(im_yiq.shape)
    pro_yiq[:,:,0]= Pro
    pro_rgb= im_to_RGB(pro_yiq)
    return Image.fromarray(pro_rgb), Fa, Pro_crudo.max()

def reconstruir_im(im, fact, Fa, norm):
    im_array= np.asarray(im) 
    im_yiq= im_to_YIQ(im_array)
    Mod_log= im_yiq[:,:,0]*norm
    Mod= (np.exp(Mod_log)-1)*fact
    
    Re= Mod*np.cos(Fa)
    Im= Mod*np.sin(Fa)
    pro= np.zeros( Mod_log.shape, dtype="complex128")
    pro.real= Re
    pro.imag= Im
    f_I= np.fft.ifftshift(pro)
    I = np.fft.ifft2(f_I)
    Y= np.abs(I)
    # Y_nuevo[Y_nuevo<0.01]=0
    # Y_nuevo[Y_nuevo>0.99]=1
    pro_yiq= np.zeros(im_array.shape)
    pro_yiq[:,:,0]= Y
    pro_rgb= im_to_RGB(pro_yiq)
    return Image.fromarray(pro_rgb)

def im_to_YIQ(im):
    im_norm= im/256
    mat_a_YIQ= np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    im_yiq= np.dot(im_norm, mat_a_YIQ.T)
    return im_yiq

def im_to_RGB(im):
    mat_a_RGB= np.array([[1,0.9663,0.6210],[1,-0.2721,-0.6474],[1,-1.1070,1.7046]])
    im_RGB= np.dot(im, mat_a_RGB.T)
    im_RGB*= 255
    #Clampeo RGB
    im_RGB[im_RGB>255]= 255
    im_RGB[im_RGB<0]= 0
    
    return im_RGB.astype(np.uint8)

if __name__== "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    MainWindow= QtWidgets.QMainWindow()
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # or in new API
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
