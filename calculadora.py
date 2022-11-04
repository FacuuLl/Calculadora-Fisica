import matplotlib.pyplot as plt

G = 9.8
def main():
    print("1_Tiro Vertical\n2_Movimiento Plano\n3_Tiro Oblicuo.")
    ejecicio = input("\nQue ejercicio quiere hacer: ")

    if ejecicio == "1":
        tiro_vertical()
    elif ejecicio == "2":
        movimiento_plano()
    elif ejecicio == "3":
        tiro_oblicuo()
    else:
        print("\nIngrese la posicion de un ejercicio valido")

def tiro_oblicuo():
    import cmath
    import math
    v0 = float(input("Ingrese la velocidad inicial: "))
    ang_out = float(input("Ingrese el angulo de salida: "))
    x0 = float(input("Ingrese la pocicion inicial en x: "))
    y0 = float(input("Ingrese la pocicion inicial en y: "))

    v0x = v0*cmath.cos(math.radians(ang_out))
    v0y = v0*cmath.sin(math.radians(ang_out))    

    t = -abs(v0y)/-abs(G)
    xmax = x0+v0x*(t*2)
    hmax = y0+v0y*t+0.5*-abs(G)*t**2 
    print(f"La altura maxima es de {hmax}\nLa distancia maxima q alcanza es de {xmax}\nEl tiempo que tarda en recorrer esa distancia es de {t}")

def movimiento_plano():
    friccion = input("Hay friccion en la simulacion?: ")
    masa = float(input("Ingrese la masa del objeto: "))
    fuerza = float(input("Ingrese la fuerza: "))
    peso = masa*G


    if friccion.lower() == "s":
        ue = float(input("Ingrese el mu estatico: "))
        ud = float(input("Ingrese el mu dinamico: "))
        ffe = peso*ue
        ffd = peso*ud
        if ffe < fuerza:
            print(f"El objeto se mueve a {(fuerza-ffd)/masa}m/s2")
        else:
            print(f"Se necesitan {ffe}N para mover el objeto")
    else:
        if fuerza != 0:
            print(f"El objeto se mueve a {fuerza/masa}m/s2")
        else:
                print("Se necesita una fuerza mayor a 0 para mover el objeto.")

def tiro_vertical():
    print("\n1_Velocidad Inicial\n2_Altura maxima\n3_Tiempo en Caer")
    datos = input("\nQue datos desea ingresar: ")
    if datos == "1":
        v0 = float(input("\nIngrese la velocidad inicial: "))
        hmax = (v0**2)/(2*G)
        t = v0/G
    elif datos == "2":
        hmax = float(input("\nIngrese la altura maxima: "))
        v0 = (2*G*hmax)**(1./2.)
        t = v0/G
    elif datos == "3":
        t = float(input("Cuanto tiempo tarda en car el objeto"))
        v0 = G*(t/2)
        hmax = (v0**2)/(2*G)
        t = t/2
    else:print("\nIngrese una respuesta valida")
    print(f"\nLa altura maxima es de {hmax}m\nLa velocidad Inicial es de {v0}m/s2\nEl tiempo que tarda en llegar a la altura maxima {t}s\nEl tiempo que tarda en caer el objeto es de {t*2}s")

    t = int((v0/G)*2)
    h = lambda time : v0*time+(0.5*-abs(G))*time**2
    x, y = [], []
    for i in range(t+1):
        x.append(i)
        y.append(h(i))
    x.append((v0/G)*2)
    y.append(0)
    plt.xlabel("Tiempo(s)")
    plt.ylabel("Altira(m)")
    plt.grid()
    plt.plot(x, y)
    plt.show()

main()