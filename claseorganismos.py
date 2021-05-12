
class organismo:
    __nombre=''
    __domicilio=''
    __localidad=''
    __telefono=''
    def __init__(self,nom='',dom='',loc='',tel=''):
        self.__nombre=nom
        self.__domicilio=dom
        self.__localidad=loc
        self.__telefono=tel

    def calcularcantidadexceptuados(self,unmanejadorexceptuado):
        exceptuados=unmanejadorexceptuado.getexceptuados()
        c_ed=0
        c_en=0
        for i in range(len(exceptuados)):
            if exceptuados[i].getorganismo()==self.__nombre:
                if exceptuados[i].getfactor()=='edad':
                    c_ed+=1
                else:
                    c_en+=1
        print('la cantidad de personas exceptuadas por edad de  {} es: {}'.format(self.__nombre,c_ed))
        print('la cantidad de personas exceptuadas por enfermedad preexistente de  {} es: {}'.format(self.__nombre,c_en))
        print()

