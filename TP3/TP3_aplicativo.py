from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from PIL import Image #Libreria PILLOW
import numpy as np    #Libreria NUMPY

import matplotlib.pyplot as plt #Libreria Matplotlib
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


        
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('tp3.ui', self) # Load the .ui file
        

        self.show()
        
        
        self.button = self.findChild(QtWidgets.QPushButton, 'procesar') 
        self.button.clicked.connect(self.printButtonPressed)
        self.btn_his = self.findChild(QtWidgets.QPushButton, 'btn_hist')
        self.btn_his.clicked.connect(self.hist_apretado)
        self.cor = self.findChild(QtWidgets.QComboBox, 'correccion')
        self.but_1 = self.findChild(QtWidgets.QPushButton, 'path_im1')
        self.but_1.clicked.connect(self.setImage)
        self.pat1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.pat2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        
        self.ymin_box= self.findChild(QtWidgets.QDoubleSpinBox, 'ymin')
        self.ymax_box= self.findChild(QtWidgets.QDoubleSpinBox, 'ymax')
        self.alfa_box= self.findChild(QtWidgets.QDoubleSpinBox, 'alfa')
        self.show() # Show the GUI
        
    def hist_apretado(self):
        
        im1= Image.open(self.pat1.text())
        a= np.asarray(im1)
        hist_lumin(a)
    
    def printButtonPressed(self):
        
        print('Correcion:' + self.cor.currentText())
        print("Im1:" + self.pat1.text())
        
        im1= Image.open(self.pat1.text())
        a= np.asarray(im1)
        
        if(self.cor.currentText()=="Alfa"):
            im_yiq= im_to_YIQ(a)
            print(self.alfa_box.value())
            im_coef= yiq_coef(im_yiq, self.alfa_box.value(),1)
            pros= im_to_RGB(im_coef)
        if(self.cor.currentText()=="Raiz Cuadrada"):
            pros= func_sqrt(a)
        if(self.cor.currentText()=="Cuadratica"):  
            pros= func_sqr(a)
        if(self.cor.currentText()=="Lineal a trozos"):  
            pros= func_lin_a_trozos(a,self.ymin_box.value(), self.ymax_box.value())

       
        im3= Image.fromarray(pros)
        #plt.imshow(im3)
        #hist_lumin(pros)
        im_con_his(pros)
        
                

            
        
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Imagen 1", "", "Archivos de Imagen (*.png *.jpg *jpeg)") # Ask for file
        if fileName: # If the user gives a file
            self.pat1.setText(fileName) 
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center    
            
      
    def setImage3(self):
        fileName = self.pat2.text()  
        if fileName: # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl_3.width(), self.imageLbl_3.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl_3.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl_3.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center    

        
def im_to_YIQ(im):
    im_norm= im/256
    mat_a_YIQ= np.array([[0.299,0.587,0.114],[0.595716,-0.274453,-0.321263],[0.211456,-0.522591,0.311135]])
    im_yiq= np.dot(im_norm, mat_a_YIQ.T)
    return im_yiq

def yiq_coef(im, alpha, beta):
    coe= [alpha,beta,beta]
    im_yiq_coef= im*coe
    #Clampeo Y
    im_yiq_coef[:,:,0][im_yiq_coef[:,:,0]>1] = 1
    #Clampeo I
    im_yiq_coef[:,:,1][im_yiq_coef[:,:,1]>0.5957] = 0.5957
    im_yiq_coef[:,:,1][im_yiq_coef[:,:,1]<(-0.5957)] = (-0.5957)
    #Clampeo Q
    im_yiq_coef[:,:,2][im_yiq_coef[:,:,2]>0.5226] = 0.5226
    im_yiq_coef[:,:,2][im_yiq_coef[:,:,2]<(-0.5226)] =( -0.5226)
    
    return im_yiq_coef


def im_to_RGB(im):
    mat_a_RGB= np.array([[1,0.9663,0.6210],[1,-0.2721,-0.6474],[1,-1.1070,1.7046]])
    im_RGB= np.dot(im, mat_a_RGB.T)
    im_RGB*= 255
    #Clampeo RGB
    im_RGB[im_RGB>255]= 255
    im_RGB[im_RGB<0]= 0
    
    return im_RGB.astype(np.uint8)
 
def func_sqrt(im):
    im_yiq= im_to_YIQ(im)
    Y= im_yiq[:,:,0]
    Y_sq= np.sqrt(Y)
    im_yiq[:,:,0]= Y_sq
    im_rgb= im_to_RGB(im_yiq)
    return im_rgb

def func_sqr(im):
    im_yiq= im_to_YIQ(im)
    Y= im_yiq[:,:,0]
    Y_sq= np.square(Y)
    im_yiq[:,:,0]= Y_sq
    im_rgb= im_to_RGB(im_yiq)
    return im_rgb

def func_lin_a_trozos(im, Ymin, Ymax):
    yiq= im_to_YIQ(im)
    Y= yiq[:,:,0]
    Y[Y<Ymin]= Ymin
    Y[Y>Ymax]= Ymax
    for x in range(Y.shape[0]):
        for y in range(Y.shape[1]):
            if Y[x,y]>Ymin and Y[x,y]<Ymax:
                Y[x,y]= Y[x,y]/(Ymax-Ymin)-Ymin/(Ymax-Ymin)  
    yiq[:,:,0]= Y
    rgb= im_to_RGB(yiq)
    return rgb
 
def hist_lumin(im_a):
    im_a_yiq= im_to_YIQ(im_a)
    y_im_a= im_a_yiq[:,:,0]
    ax= plt.hist(y_im_a.reshape(y_im_a.size), 10, weights=np.zeros_like(y_im_a.reshape(y_im_a.size)) + 1. /y_im_a.size)
    plt.title("Histograma de Luminancia")
    plt.xlabel("Luminancia")
    plt.ylabel("Frec. Rel. de aparición (%)")
    plt.show
    
def im_con_his(im_a):
    im_a_yiq= im_to_YIQ(im_a)
    y_im_a= im_a_yiq[:,:,0]
    
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(6,6))

    ax.set_aspect('auto')
    ax.set_title('Imagen', fontsize=15)

    ax.imshow(im_a)

    ax2.set_aspect('equal')
    ax2.set_title('Histograma', fontsize=15)

    ax2.hist(y_im_a.reshape(y_im_a.size), 10, weights=np.zeros_like(y_im_a.reshape(y_im_a.size)) + 1. /y_im_a.size)
    ax2.grid()

    plt.show()
    
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application