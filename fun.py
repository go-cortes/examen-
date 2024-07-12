from random import randrange 
from numpy import sum
import csv

# rellenar la lista con diccionario de empleados y sus respectivos sueldos brutos 
# los sueldos van desde los 300.000 hasta los 2.500.000

def generar_sueldos(lista):
    for i in range (10):

        nom='empleado'+str(i+1)
        sueldo=randrange(300.000,2.500000)
        d={'nombre':nom,'sueldo':sueldo}
        lista.append(d)

        def menu():
            m="""bienvenido
            ********************
            [1]clasificar sueldos
            [2]ver estadisticas de los sueldos
            [3]exportar reporte de sueldos
            [4]salir
            -->"""
        print(m,end="")

        def validar_op():
            while True:
                try:
                       op = int(input())
                    if op>=1 and op=<=4:
                        return op
                        else:
                            raise ValueError
                            except:
        print(seleccione una opcion valida.-->,end="")

                                def clasificar_empleados(lista):
                                    bajos = []
                                    medios = []
                                    alto = []
                                    for trabajador in lista:
                                    if trabajador["sueldo"]<=300.000:
                                        bajos.append(trabajador)
                                    elif trabajador["sueldo"]<=2.500000
                                    medios.append(trabajador)
                                    else:
                                        altos.append(trabajador)

                                        print("empleados con sueldo menor a 800.000:")
                                        print()

                                    for e in bajos: 
                                    print(f"{e["nombre"]}:${e["sueldo"]:,.0f}")  
                                    print("**********************************") 

                                    print("empleados con sueldo entre $800.000 y 2.000.000:") 
                                    print()
                                    for e in medios:
                                        print(f"{e["nombre"]}:${e["sueldo"]:,.0f}")
                                        print("**********************************")

                                        print("empleados con sueldo mayor a 2.000.000:")
                                        print()

                                        for e in altos:
                                            print(f"{e["nombre"]}:${e["sueldo"]:,.0f}")

                                            def sueldo_bajo(lista):
                                                bajo = lista[0]
                                                for empleado in lista:
                                                if alto["sueldo"]<empleado["sueldo"]:
                                                    alto = empleado
                                                    return alto

                                                    def imprimir_estadisticas(lista):
                                                        print(f"sueldo mas bajo:{sueldo_bajo(lista)}")
                                                        print(f"sueldo mas alto:{sueldo_alto(lista)}")

                                                        listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
                                                        suma = sum(listar_sueldos)
                                                        promedio = suma/10
                                                        print(f"sueldo promedio:{promedio:,.0f}")

                                                        def report_sueldos(lista):
                                                            reporte = []
                                                            for trabajador in lista:
                                                                sueldo_bruto=trabajador["sueldo"]
                                                                afp = int(sueldo_bruto*0,12)
                                                                salud = int(sueldo_bruto*0,7)
                                                                sueldo_liquido = sueldo_bruto-afp-salud

                                                                a={"nombre":trabajador["nombre"],"sueldo_bruto":sueldo_bruto"afp":afp,"salud":salud,"sueldo_liquido":sueldo_liquido}
                                                                reporte.append(a)

                                                                nombre_campos=["nombre","sueldo_bruto","afp","salud","sueldo_liquido"]
                                                                with open ('reporte sueldos.csv','w',newline = "") as archivo:
                                                                    escritor.writeheader()
                                                                    escritor.writerows(reporte)


                                        

