from manejadorCamas import manejadorCamas
from manejadorMedicamentos import manejadorMed

if __name__ == '__main__':
    controlC = manejadorCamas()
    controlM = manejadorMed()
    controlC.leerArchivoCamas()             # lectura de archivo camas.csv
    controlM.leerArchivoMedicamentos()      # lectura de archivo medicamentos.csv
    print('----------------------------------------')
    opcion = input('1 - Dar alta a paciente\n2 - Listar pacientes por diagnóstico\n0 - SALIR\nOpción: ')
    while opcion != '0':
        print('----------------------------------------\n')
        if opcion == '1':       # alta y datos del paciente
            paciente = input('Ingrese Apellido y nombre del paciente (separados por una coma): ')
            indice = controlC.buscar(paciente)
            if indice != -1:
                if not controlC.darAlta(indice):
                    print('\n--- DATOS DEL PACIENTE ---')
                    idCama = controlC.obtenerIdCama(indice)
                    print(controlC.mostrarPaciente(indice))
                    print('MEDICAMENTO / MONODROGA          PRESENTACION    CANTIDAD    PRECIO')
                    total = controlM.mostrarMedicamentoPaciente(idCama)
                    print('Total adecuado:{:>52}\n'.format(total))
            else:
                input('Paciente no encontrado.\nNOTA: Recuerde respetas mayúsculas y separar el apellido y el nombre con una coma.\nPresione enter para volver al menú.\n')
        elif opcion == '2':
            diagnostico = input('Ingrese un diagnóstico (debe comenzar con mayúscula): ')
            controlC.buscarPorDiagnostico(diagnostico)
        else:
            input('ERROR - Ingrese una opción válida.\nPresione enter para volver al menú.\n')
        print('----------------------------------------')
        opcion = input('1 - Dar alta a paciente\n2 - Listar pacientes por diagnóstico\n0 - SALIR\nOpción: ')
