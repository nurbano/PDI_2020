from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from PIL import Image #Libreria PILLOW
import numpy as np    #Libreria NUMPY
import matplotlib.pyplot as plt #Libreria Matplotlib

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('tp2.ui', self) # Load the .ui file
        self.button = self.findChild(QtWidgets.QPushButton, 'procesar') # Find the button
        self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        self.metodo = self.findChild(QtWidgets.QComboBox, 'metodo')
        self.operacion = self.findChild(QtWidgets.QComboBox, 'comboBox_2')
        self.but_1 = self.findChild(QtWidgets.QPushButton, 'path_im1')
        self.but_1.clicked.connect(self.setImage)
        self.but_2 = self.findChild(QtWidgets.QPushButton, 'path_im2')
        self.but_2.clicked.connect(self.setImage2)
        self.pat1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit')
        self.pat2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.pat3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.show() # Show the GUI
        
    def printButtonPressed(self):
        # This is executed when the button is pressed
        print('Operación:' + self.operacion.currentText())
        print('Metodo:' + self.metodo.currentText())
        print("Im1:" + self.pat1.text())
        print("Im2:" + self.pat2.text())
        pat_im1= self.pat2.text()
        im1= Image.open(self.pat1.text())
        im2= Image.open(self.pat2.text())
        ima = im1.resize((350, 350)) 
        imb = im2.resize((350, 350)) 
        a= np.asarray(ima)
        b= np.asarray(imb)
        if(self.operacion.currentText()=="Suma"):
            if(self.metodo.currentText()=="RGB Promediado"):
                pros= sum_rgb_prom(a,b)
            if(self.metodo.currentText()=="RGB Clampeado"):
                pros= sum_rgb_clamp(a,b)
            if(self.metodo.currentText()=="YIQ Promediado"):
                pros= sum_yiq_prom(a,b)
            if(self.metodo.currentText()=="YIQ Clampeado"):
                pros= sum_yiq_clamp(a,b)
            if(self.metodo.currentText()=="If Darker/ If lighter"):
                pros= sum_ifligther(a,b)
        if(self.operacion.currentText()=="Resta"):
            if(self.metodo.currentText()=="RGB Promediado"):
                pros= res_rgb_prom(a,b)
            if(self.metodo.currentText()=="RGB Clampeado"):
                pros= res_rgb_clamp(a,b)
            if(self.metodo.currentText()=="YIQ Promediado"):
                pros= res_yiq_prom(a,b)
            if(self.metodo.currentText()=="YIQ Clampeado"):
                pros= res_yiq_clamp(a,b)
            if(self.metodo.currentText()=="If Darker/ If lighter"):
                pros= res_ifdarker(a,b)
                
                
                
                
                
                
                
        im3= Image.fromarray(pros)
        im3.save(pat_im1[0:-4]+"_procesado.jpg")
        self.pat3.setText(pat_im1[0:-4]+"_procesado.jpg")
        self.setImage3()
                

            
        
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Imagen 1", "", "Archivos de Imagen (*.png *.jpg *jpeg)") # Ask for file
        if fileName: # If the user gives a file
            self.pat1.setText(fileName) 
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center    
            
    def setImage2(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Seleccionar Imagen 2", "", "Archivos de Imagen (*.png *.jpg *jpeg)") # Ask for file
        if fileName: # If the user gives a file
            self.pat2.setText(fileName)   
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl_2.width(), self.imageLbl_2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl_2.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl_2.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
    
    def setImage3(self):
        fileName = self.pat3.text()  
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
 
def show_two_im(a, b, text):
    im1= Image.fromarray(a)
    im2= Image.fromarray(b)
    plt.subplot(121), plt.imshow(im1)
    plt.title("Original")

    plt.subplot(122), plt.imshow(im2)
    plt.title(text)

def sum_rgb_clamp(a1, a2):
    sum_rgb_clamp= np.zeros(a1.shape, dtype="int16")
    sum_rgb_clamp+=a1
    sum_rgb_clamp+=a2
    sum_rgb_clamp[sum_rgb_clamp>255]=255
    return sum_rgb_clamp.astype(np.uint8)

def sum_rgb_prom(a1,a2):
    sum_rgb_prom= a1*0.5 +a2*0.5
    return sum_rgb_prom.astype(np.uint8)

def sum_yiq_clamp(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2)
    #SUMO
    sum_yiq_clam= np.zeros(a1_yiq.shape)
    sum_yiq_clam[:,:,0]= a1_yiq[:,:,0] +a2_yiq[:,:,0]
    sum_yiq_clam[sum_yiq_clam[:,:,0]>1]=1
    sum_yiq_clam[:,:,1]= (a1_yiq[:,:,0]*a1_yiq[:,:,1] +a2_yiq[:,:,0]*a2_yiq[:,:,1])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    sum_yiq_clam[:,:,2]= (a1_yiq[:,:,0]*a1_yiq[:,:,2] +a2_yiq[:,:,0]*a2_yiq[:,:,2])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    #Clampeo los valores YIQ
    sum_yiq_clam[sum_yiq_clam[:,:,0]>1]=1
    sum_yiq_clam[sum_yiq_clam[:,:,1]>0.5957]=0.5957
    sum_yiq_clam[sum_yiq_clam[:,:,1]<-0.5957]=-0.5957
    sum_yiq_clam[sum_yiq_clam[:,:,2]>0.5226]=0.5226
    sum_yiq_clam[sum_yiq_clam[:,:,2]<-0.5226]=-0.5226
    sum_yiq_clamp_rgb= im_to_RGB(sum_yiq_clam)
    return sum_yiq_clamp_rgb.astype(np.uint8)

def sum_yiq_prom(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2)
    #SUMO
    sum_yiq_prom= np.zeros(a1_yiq.shape)
    sum_yiq_prom[:,:,0]= a1_yiq[:,:,0]*0.5 +a2_yiq[:,:,0]*0.5
    sum_yiq_prom[:,:,1]= (a1_yiq[:,:,0]*a1_yiq[:,:,1] +a2_yiq[:,:,0]*a2_yiq[:,:,1])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    sum_yiq_prom[:,:,2]= (a1_yiq[:,:,0]*a1_yiq[:,:,2] +a2_yiq[:,:,0]*a2_yiq[:,:,2])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    #Clampeo los valores YIQ
    sum_yiq_prom[sum_yiq_prom[:,:,0]>1]=1
    sum_yiq_prom[sum_yiq_prom[:,:,1]>0.5957]=0.5957
    sum_yiq_prom[sum_yiq_prom[:,:,1]<-0.5957]=-0.5957
    sum_yiq_prom[sum_yiq_prom[:,:,2]>0.5226]=0.5226
    sum_yiq_prom[sum_yiq_prom[:,:,2]<-0.5226]=-0.5226
    #Vuelvo al espacio RGB
    sum_yiq_prom_rgb= im_to_RGB(sum_yiq_prom)
    #Convierto de float a uint8 para poder representar la imagen
    return sum_yiq_prom_rgb.astype(np.uint8)

def sum_ifligther(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2)
    #Sumo
    sum_yiq_ifligther= np.zeros(a1_yiq.shape)
    for x in range(sum_yiq_ifligther.shape[0]):
        for y in range(sum_yiq_ifligther.shape[1]):
            if a1_yiq[x,y,0]>=a2_yiq[x,y,0]:
                sum_yiq_ifligther[x,y,0]=  a1_yiq[x,y,0]
                sum_yiq_ifligther[x,y,1]=  a1_yiq[x,y,1]
                sum_yiq_ifligther[x,y,2]=  a1_yiq[x,y,2]
            else:
                sum_yiq_ifligther[x,y,0]=  a2_yiq[x,y,0]
                sum_yiq_ifligther[x,y,1]=  a2_yiq[x,y,1]
                sum_yiq_ifligther[x,y,2]=  a2_yiq[x,y,2]

    #Clampeo los valores YIQ
    sum_yiq_ifligther[sum_yiq_ifligther[:,:,0]>1]=1
    sum_yiq_ifligther[sum_yiq_ifligther[:,:,1]>0.5957]=0.5957
    sum_yiq_ifligther[sum_yiq_ifligther[:,:,1]<-0.5957]=-0.5957
    sum_yiq_ifligther[sum_yiq_ifligther[:,:,2]>0.5226]=0.5226
    sum_yiq_ifligther[sum_yiq_ifligther[:,:,2]<-0.5226]=-0.5226
    #Vuelvo al espacio RGB
    sum_yiq_ifligther_rgb= im_to_RGB(sum_yiq_ifligther)
    #Grafico
    return sum_yiq_ifligther_rgb.astype(np.uint8) 

def res_rgb_clamp(a1, a2):
    #Cuasi Resta RGB clampeada
    res_rgb_clamp= np.zeros(a1.shape, dtype="int16")
    res_rgb_clamp+=a1
    res_rgb_clamp-=a2
    #Clampeo
    res_rgb_clamp[res_rgb_clamp<0]=0
    
    return res_rgb_clamp.astype("uint8")

def res_rgb_prom(a1, a2):
    #Cuasi resta promediada
    res_rgb_prom= np.zeros(a1.shape, dtype="int16")
    res_rgb_prom= a1*0.5-a2*0.5 +128
    #Clampeo
    res_rgb_prom[res_rgb_prom<0]=0
    
    return res_rgb_prom.astype("uint8")

def res_yiq_clamp(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2)
    #Cuasi resta YIQ clampeada
    res_yiq_clam= np.zeros(a1.shape, dtype="float64")
    res_yiq_clam+= a1_yiq
    res_yiq_clam-= a2_yiq
    #Clampeo valores YIQ
    res_yiq_clam[res_yiq_clam[:,:,0]>1]=1
    res_yiq_clam[res_yiq_clam[:,:,1]>0.5957]=0.5957
    res_yiq_clam[res_yiq_clam[:,:,1]<-0.5957]=-0.5957
    res_yiq_clam[res_yiq_clam[:,:,2]>0.5226]=0.5226
    res_yiq_clam[res_yiq_clam[:,:,2]<-0.5226]=-0.5226
    #Vuelvo al espacio RGB
    res_yiq_clam_rgb_bytes= im_to_RGB(res_yiq_clam)
    
    return res_yiq_clam_rgb_bytes.astype("uint8")
   
def res_yiq_prom(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2)   
    #Cuasi resta YIQ promediada
    res_yiq_prom= np.zeros(a1.shape, dtype="float64")
    res_yiq_prom[:,:,0]= a1_yiq[:,:,0]*0.5 -a2_yiq[:,:,0]*0.5 + 0.5
    res_yiq_prom[res_yiq_prom[:,:,0]>1]=1
    res_yiq_prom[:,:,1]= (a1_yiq[:,:,0]*a1_yiq[:,:,1] -a2_yiq[:,:,0]*a2_yiq[:,:,1])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    res_yiq_prom[:,:,2]= (a1_yiq[:,:,0]*a1_yiq[:,:,2] -a2_yiq[:,:,0]*a2_yiq[:,:,2])/(a1_yiq[:,:,0] +a2_yiq[:,:,0])
    #Clampeo los valores YIQ
    res_yiq_prom[res_yiq_prom[:,:,0]>1]=1
    res_yiq_prom[res_yiq_prom[:,:,1]>0.5957]=0.5957
    res_yiq_prom[res_yiq_prom[:,:,1]<-0.5957]=-0.5957
    res_yiq_prom[res_yiq_prom[:,:,2]>0.5226]=0.5226
    res_yiq_prom[res_yiq_prom[:,:,2]<-0.5226]=-0.5226
    #Vuelvo al espacio RGB
    res_yiq_prom_rgb_bytes= im_to_RGB(res_yiq_prom)
    
    return res_yiq_prom_rgb_bytes.astype("uint8")

def res_ifdarker(a1, a2):
    a1_yiq= im_to_YIQ(a1)
    a2_yiq= im_to_YIQ(a2) 
    #Cuasi resta YIQ if darker
    res_yiq_ifdarker= np.zeros(a1.shape, dtype="float64")
    for x in range(res_yiq_ifdarker.shape[0]):
        for y in range(res_yiq_ifdarker.shape[1]):
            if a1_yiq[x,y,0]<a2_yiq[x,y,0]:
                res_yiq_ifdarker[x,y,0]=  a1_yiq[x,y,0]
                res_yiq_ifdarker[x,y,1]=  a1_yiq[x,y,1]
                res_yiq_ifdarker[x,y,2]=  a1_yiq[x,y,2]
            else:
                res_yiq_ifdarker[x,y,0]=  a2_yiq[x,y,0]
                res_yiq_ifdarker[x,y,1]=  a2_yiq[x,y,1]
                res_yiq_ifdarker[x,y,2]=  a2_yiq[x,y,2]
    #Clampeo los valores YIQ
    res_yiq_ifdarker[res_yiq_ifdarker[:,:,0]>1]=1
    res_yiq_ifdarker[res_yiq_ifdarker[:,:,1]>0.5957]=0.5957
    res_yiq_ifdarker[res_yiq_ifdarker[:,:,1]<-0.5957]=-0.5957
    res_yiq_ifdarker[res_yiq_ifdarker[:,:,2]>0.5226]=0.5226
    res_yiq_ifdarker[res_yiq_ifdarker[:,:,2]<-0.5226]=-0.5226
    #Vuelvo al espacio RGB
    res_yiq_ifdarker_rgb_bytes= im_to_RGB(res_yiq_ifdarker)
    return res_yiq_ifdarker_rgb_bytes.astype("uint8")
 
def show_three_im(a, b, c, text):
    im1= Image.fromarray(a)
    im2= Image.fromarray(b)
    im3= Image.fromarray(c)
    plt.subplot(131), plt.imshow(im1)
    plt.title("Original 1")

    plt.subplot(132), plt.imshow(im2)
    plt.title("Original 2")
    
    plt.subplot(133), plt.imshow(im3)
    plt.title(text)
    
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application