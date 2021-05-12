import  csv
from claseorganismos import organismo
class manejadororganismo:
    __listaorganismos=[]
    def __init__(self):
        self.__listaorganismos=[]

    def cargarorganismo(self):
        band=True
        archivo=open('Organismos-del-Estado.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(band==True):
                band=False
            else:
                nom=fila[0].lower()
                dom=fila[1].lower()
                loc=fila[2].lower()
                tel=fila[3].lower()
                unorganismo=organismo(nom,dom,loc,tel)
                self.__listaorganismos.append(unorganismo)
        archivo.close()
    def getorganismo(self):
        return self.__listaorganismos
