class exceptuado:
    __apellido=''
    __nombre=''
    __direccion=''
    __dni=''
    __edad=0
    __telefono=''
    __factor=''
    __organismo=''
    def __init__(self,ap='',nm='',dnei='',ed=0,dr='',tl='',fac='',org=''):
        self.__apellido=ap
        self.__nombre=nm
        self.__direccion=dr
        self.__dni=dnei
        self.__edad=ed
        self.__telefono=tl
        self.__factor=fac
        self.__organismo=org

    def getfactor(self):
        return self.__factor
    def getorganismo(self):
        return self.__organismo
    def getedad(self):
        return self.__edad
    def getapellido(self):
        return self.__apellido
    def mostrardatos(self):
        print('Apellido:{}  Nombre: {}  dni: {}  Edad: {}'.format(self.__apellido,self.__nombre,self.__dni,self.__edad))
    def __lt__(self, otroapellido):
        if self.__apellido<otroapellido.getapellido():
            return True
        else:
            return False

