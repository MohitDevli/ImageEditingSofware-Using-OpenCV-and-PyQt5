import sys
from PyQt5.QtCore import center
from PyQt5.QtGui import QPixmap, QImage, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox, QVBoxLayout , QFileDialog , QLineEdit, QWidget, QLabel, QGridLayout, QPushButton
import cv2


class Main():
    
    def windowSetup(self):
        self.app=QApplication(sys.argv)
        
        
        self.win1=QWidget()
        self.FormatWin= QWidget()
        self.win2 = QWidget()
        
        """ Win1 and Win2 Window """
        
        self.win1.setWindowTitle("CV-GUI")
        self.win2.setWindowTitle("CV-GUI")
        self.win1.setGeometry(0, self.app.desktop().screen().height()/2, self.app.desktop().screen().width()/4, self.app.desktop().screen().height()-100)
        self.win2.setGeometry(self.app.desktop().screen().width(), self.app.desktop().screen().height()/2, self.app.desktop().screen().width()/4, self.app.desktop().screen().height()-100)
        
        """ File Window """
        
        self.fileWin = QWidget()
        self.fileWin.setWindowTitle("Choose File")
        self.fileWin.setGeometry(self.app.desktop().screen().width()/4, self.app.desktop().screen().height()/4, self.app.desktop().screen().width()/2, self.app.desktop().screen().height()/2)
        
        """ Format Window """
        self.FormatWin.setWindowTitle("CV-GUI")
        
        
        chooseLabel= QLabel(self.fileWin)
        chooseLabel.setText("ChooseImage")
        chooseLabel.move(50,20)
        
        self.chooseFilePathEdit=QLineEdit(self.fileWin)
        self.chooseFilePathEdit.resize(self.fileWin.width()/2, 30)
        self.chooseFilePathEdit.move(self.fileWin.width()/4,15)
        
        
        chooseButton = QPushButton(self.fileWin)
        chooseButton.clicked.connect(self.chooseImage)
        chooseButton.setText("Choose..")
        chooseButton.move(self.fileWin.width()-100 ,15)
        
        
        openButton = QPushButton(self.fileWin)
        openButton.clicked.connect(lambda:self.openEditor())
        openButton.setText("Confirm")
        openButton.move(self.fileWin.width()/2 - openButton.width()/2 ,self.fileWin.height()-100)
            
        self.fileWin.show()
        
        
        ########################################################
        
        self.ImageFormatTranformLabel = QLabel(self.win1)
        self.ImageFormatTranformLabel.setText('Channge Image Format:')
        self.ImageFormatTranformLabel.move(0,20)
        
        self.ImageFormatTranformButton = QPushButton(self.win1)
        self.ImageFormatTranformButton.setText("Channge Image Format")
        self.ImageFormatTranformButton.move(self.ImageFormatTranformButton.width()*2-30,15)
        self.ImageFormatTranformButton.clicked.connect(self.ImageFormat)
    
        ##################################################
        
        scaleLabel = QLabel(self.win1)
        scaleLabel.setText("Scale Image: ")
        scaleLabel.move(0,70)
        
        self.width= QLineEdit(self.win1)
        self.width.move(self.win1.width()/4,70)
        self.width.resize(70,20)
        
        xLabel = QLabel(self.win1)
        xLabel.setText("x")
        xLabel.move(self.width.width()*2+18,70)        
        
        self.height= QLineEdit(self.win1)
        self.height.move(self.win1.width()/2,70)
        self.height.resize(70,20)
        
        whLabel = QLabel(self.win1)
        whLabel.setText("wxh")
        whLabel.move(self.height.width()*3+32,70)                
        
        
        goBtn= QPushButton(self.win1)
        goBtn.setText('Go')
        goBtn.clicked.connect(self.scaleImg)
        goBtn.move(self.win1.width()-60,65)   
        goBtn.resize(30,30)
        
        
        
        
        sys.exit(self.app.exec_())    
    
    def chooseImage(self):
        self.fileDialog=QFileDialog(self.fileWin)
        fileName=self.fileDialog.getOpenFileName(self.fileDialog, "Choose Image File.", "", "Images (*.png *.jpg *.jpeg *.jpe *.jp2 *.tiff *.tif *.sr *.ras *.pbm *.pgm *.ppm)")
        self.imageName=fileName[0]
        self.chooseFilePathEdit.setText(self.imageName)
        
       
        
    def openEditor(self):
        
        try:
            self.fileWin.destroy()
            self.win1.show()
            self.win2.show()
            
            namedWindow=cv2.namedWindow(self.chooseFilePathEdit.text(), cv2.WINDOW_NORMAL)
            self.image = cv2.imread(self.chooseFilePathEdit.text())
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
        except:
            fileNameMismatchError=QMessageBox(self.fileWin)
            fileNameMismatchError.setIcon(QMessageBox.Critical)
            fileNameMismatchError.setText("Error : An Error Occured. Please check the ImageFIleName \n\nTip: Image Path in InputBox is Diffrent, then the path of Image you selected. You can make an another try.")
                
    
    def scaleImg(self):
        width= int(self.width.text())
        height= int(self.height.text())
        cv2.destroyAllWindows()
        self.image = cv2.resize(self.image, (width, height))
        cv2.imshow(self.chooseFilePathEdit.text(),self.image)
               
    def ImageFormat(self):
        self.FormatWin.setGeometry(self.win1.width() , self.win1.pos().y(), 400,200)
        
        grid = QGridLayout(self.FormatWin)
        self.FormatWin.setLayout(grid)
        
        bgr2gray = QPushButton(self.FormatWin)
        bgr2gray.setText("BGR2Gray")
        bgr2gray.clicked.connect(self.BGR2GRAY)
        grid.addWidget(bgr2gray)
        
        
        
        bgr2ghls = QPushButton(self.FormatWin)
        bgr2ghls.setText("BGR2HLS")
        bgr2ghls.clicked.connect(self.BGR2HLS)
        grid.addWidget(bgr2ghls)
         
         
        bgr2ghsv = QPushButton(self.FormatWin)
        bgr2ghsv.setText("BGR2HSV")
        bgr2ghsv.clicked.connect(self.BGR2HSV)
        grid.addWidget(bgr2ghsv)
         
        
        bgr2glab = QPushButton(self.FormatWin)
        bgr2glab.setText("BGR2LAB")
        bgr2glab.clicked.connect(self.BGR2LAB)
        grid.addWidget(bgr2glab)
             
        bgr2gluv = QPushButton(self.FormatWin)
        bgr2gluv.setText("BGR2LUB")
        bgr2gluv.clicked.connect(self.BGR2LUV)
        grid.addWidget(bgr2gluv)
        
        bgr2rgb = QPushButton(self.FormatWin)
        bgr2rgb.setText("BGR2RGB")
        bgr2rgb.clicked.connect(self.BGR2RGB)
        grid.addWidget(bgr2rgb)
         
        bgr2rgba = QPushButton(self.FormatWin)
        bgr2rgba.setText("BGR2RGBA")
        bgr2rgba.clicked.connect(self.BGR2RGBA)
        grid.addWidget(bgr2rgba)
         
        bgr2xyz = QPushButton(self.FormatWin)
        bgr2xyz.setText("BGR2XYZ")
        bgr2xyz.clicked.connect(self.BGR2XYZ)
        grid.addWidget(bgr2xyz)        
        
        bgr2yuv = QPushButton(self.FormatWin)
        bgr2yuv.setText("BGR2YUV")
        bgr2yuv.clicked.connect(self.BGR2YUV)
        grid.addWidget(bgr2yuv)  
        
        
        resetFormatBtn=QPushButton(self.FormatWin)
        resetFormatBtn.setText("Reset")
        resetFormatBtn.clicked.connect(self.ResetFormat)
        grid.addWidget(resetFormatBtn)
        
    
        self.FormatWin.show()
        
    
    
    
    
    
    def ResetFormat(self):
        self.image = cv2.imread(self.chooseFilePathEdit.text())
        cv2.destroyAllWindows()
        cv2.imshow(self.chooseFilePathEdit.text(), self.image)        
    
       
    def BGR2GRAY(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()
            
    
    #cv2.COLOR_BGR2HLS
    def BGR2HLS(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HLS)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()
            
            
    #cv2.COLOR_BGR2HSV
    def BGR2HSV(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()
            
    #cv2.COLOR_BGR2LAB
    def BGR2LAB(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()    
    
    #cv2.COLOR_BGR2LUV
    def BGR2LUV(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2LUV)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()      
    
    #cv2.COLOR_BGR2RGB
    def BGR2RGB(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()          
    
    #cv2.COLOR_BGR2RGBA
    def BGR2RGBA(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()          
    
    
    #cv2.COLOR_BGR2XYZ
    def BGR2XYZ(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2XYZ)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()          
      
    #cv2.COLOR_BGR2YUV
    def BGR2YUV(self):
        try:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2YUV)
            cv2.destroyAllWindows()
            cv2.imshow(self.chooseFilePathEdit.text(), self.image)    
        except:
            messageBox=QMessageBox()
            messageBox.setIcon(QMessageBox.Critical)
            messageBox.setText("The Action cannot be done at this Time.")
            messageBox.setWindowTitle("Error..")
            messageBox.exec_()          
     
    
    
if __name__=="__main__":
    Main().windowSetup()

  
