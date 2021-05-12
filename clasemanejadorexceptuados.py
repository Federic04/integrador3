import csv
from claseexceptuados import exceptuado
class manejadorexceptuados:
    __listaexceptuados=[]
    def __init__(self):
        self.__listaexceptuados=[]
    def cargarexceptuados(self):
        band=True
        archivo=open('Personal-exceptuado.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if(band==True):
                band=False
            else:
                ap=fila[0].lower()
                nm=fila[1].lower()
                dnei=fila[2].lower()
                ed=int(fila[3])
                dr=fila[4].lower()
                tl=fila[5].lower()
                fac=fila[6].lower()
                org=fila[7].lower()
                unexceptuado=exceptuado(ap,nm,dnei,ed,dr,tl,fac,org)
                self.__listaexceptuados.append(unexceptuado)
        archivo.close()

    def getexceptuados(self):
        return self.__listaexceptuados
    def ordenar(self):
        self.__listaexceptuados.sort()
    def mostrarexceptuados(self,nom_org):
        for i in range(len(self.__listaexceptuados)):
            if self.__listaexceptuados[i].getorganismo()==nom_org:
                if self.__listaexceptuados[i].getedad()<60:
                    self.__listaexceptuados[i].mostrardatos()
