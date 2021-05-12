from clasemanejadorexceptuados import manejadorexceptuados
from clasemanejadororganismos import manejadororganismo
if __name__ == '__main__':
    unmanejadorexceptuado=manejadorexceptuados()
    unmanejadororganismo=manejadororganismo()
    unmanejadorexceptuado.cargarexceptuados()
    unmanejadororganismo.cargarorganismo()
    organismos=unmanejadororganismo.getorganismo()
    for i in range(len(organismos)):
        organismos[i].calcularcantidadexceptuados(unmanejadorexceptuado)
    print()
    unmanejadorexceptuado.ordenar()
    n_org=input('\n ingrese el nombre de algun organismo:')
    unmanejadorexceptuado.mostrarexceptuados(n_org)
