# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:12:02 2020

@author: Admin
"""

from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    
     def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi("ventana_principal.ui", self)
        self.setup()
        
     #slot para abrir una nueva ventana
     def setup(self):
         self.boton_ingresar.clicked.connect(self.abrir_ventana_paciente)
         self.boton_clasificar.clicked.connect(self.abrir_ventana_ver_paciente)
         self.boton_editar.clicked.connect(self.abrir_ventana_buscar_paciente)
        
     def abrir_ventana_ver_paciente(self):
            ventana_ver_paciente = VentanaVerPaciente(self)
            #la ventana principal se oculte
            self.hide()
            #la ventana paciente se hace visible
            ventana_ver_paciente.show()  
            
     def abrir_ventana_buscar_paciente(self):
            ventana_buscar_paciente = VentanaBuscarPaciente(self)
            #la ventana principal se oculte
            self.hide()
            #la ventana paciente se hace visible
            ventana_buscar_paciente.show() 
            
         
     def abrir_ventana_paciente(self):
        ventana_paciente = VentanaPaciente(self)
        #la ventana principal se oculte
        self.hide()
        #la ventana paciente se hace visible
        ventana_paciente.show()
        
     
     def recibir_paciente(self, nombre, cedula, edad, genero, peso, estatura, tfg, cac, presion_arterial, cs, nus):
       
        resultado = self.__mi_coordinador.recibirInfoPaciente(nombre, cedula, edad, genero, peso, estatura, tfg, cac, presion_arterial, cs, nus )
        
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(resultado)
        msg.setWindowTitle("Resultado de la operación")
        msg.show()
        
     def recibir_cedula_ver(self, c):
        
        cedula_ver = self.__mi_coordinador.recibirCedulaVer(c)
    
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(cedula_ver)
        msg.setWindowTitle("Diagnostico")
        msg.show()
        
     def recibir_cedula_buscar(self, cedula):
        pass
        
     def asignarControlador(self,controlador):
         self.__mi_coordinador = controlador
        
class VentanaPaciente(QDialog):
    
    def __init__(self, ppal = None):
        super(VentanaPaciente, self).__init__(ppal)
        loadUi("ventana_paciente.ui", self)
        self.__mi_ventana_principal = ppal
        self.setup()
        
    def setup(self):
      
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
    
            
    def opcion_aceptar(self):
        #1 se recuperan los campos
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        edad = self.campo_edad.text()
        peso = self.campo_peso.text() 
        estatura = self.campo_estatura.text()
        genero = self.campo_genero.text()
        tfg = self.campo_tfg.text()
        cac = self.campo_cac.text()
        presion_arterial = self.campo_pa.text()
        cs = self.campo_cs.text()
        nus = self.campo_nus.text()
        
        
        
        #2 se envia la informacion a la ventana principal
        self.__mi_ventana_principal.recibir_paciente(nombre, cedula,edad,peso,estatura,genero,tfg,cac,presion_arterial,cs,nus)
        #3 se muestra la ventana principal y se oculta la actual
        self.__mi_ventana_principal.show()
        self.hide()
        
    def opcion_cancelar(self):
        #en esta opcion simplemente se vuelve a mostrar la principal y se oculta la actual
        self.__mi_ventana_principal.show()
        self.hide()

class VentanaVerPaciente(QDialog):
    def __init__(self, ppal = None):
        super(VentanaVerPaciente, self).__init__(ppal)
        loadUi("ventana_ver_paciente.ui", self)
        self.__mi_ventana_principal = ppal

        self.setup()
        
    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    
    def opcion_aceptar(self):
        #1 se recuperan los campos
        cedula = self.campo_cedula.text()  
        self.__mi_ventana_principal.recibir_cedula_ver(cedula)
   
    
    def opcion_cancelar(self):
        #en esta opcion simplemente se vuelve a mostrar la principal y se oculta la actual
        self.__mi_ventana_principal.show()
        self.hide()
                
class VentanaBuscarPaciente(QDialog):
    def __init__(self, ppal = None):
        super(VentanaBuscarPaciente, self).__init__(ppal)
        loadUi("ventana_buscar_paciente.ui", self)
        self.__mi_ventana_principal = ppal

        self.setup()
        
    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
    
    def opcion_aceptar(self):
        #1 se recuperan los campos
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        
        dosis = int(self.campo_dosis.text())
        
        self.__mi_ventana_principal.recibir_info_medicamento(cedula, nombre,dosis)
        #3 se muestra la ventana principal y se oculta la actual
        self.__mi_ventana_principal.show()
        self.hide()
    
    def opcion_cancelar(self):
        #en esta opcion simplemente se vuelve a mostrar la principal y se oculta la actual
        self.__mi_ventana_principal.show()
        self.hide()        

