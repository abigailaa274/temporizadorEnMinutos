#Requiere paquete para sonido:
# sudo apt install sox

import time
import os

# Pedimos al usuario la cantidad de minutos.
minutos = int(input("¿Cuántos minutos quieres temporizar? "))

# Convertimos los minutos a segundos.
segundos_restantes = minutos * 60

# Repetimos mientras quede tiempo.
while segundos_restantes > 0:

    # Divmod divide un número y devuelve:
    # 1. El cociente (minutos completos).
    # 2. El resto (segundos sobrantes).
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    # Mostramos el tiempo con dos dígitos por unidad.
    # Por ejemplo: 03:07 significa 3 minutos y 7 segundos.
    #\r (carriage return): mueve el cursor al comienzo de la línea actual, sin borrar su contenido. end="": evita que print() salte a la línea siguiente. - Al imprimir el nuevo tiempo, los caracteres anteriores se sobrescriben. Si el nuevo texto fuera más corto, podrían quedar caracteres sobrantes al final.
    print(f"\rTiempo restante: {minutos:02d}:{segundos:02d}", end="")

    # Esperamos un segundo.
    time.sleep(1)

    # Restamos un segundo al tiempo restante.
    segundos_restantes -= 1

# Cuando termina el bucle, mostramos el mensaje final.
print("\rTiempo restante: 00:00")
print("¡Tiempo terminado!")

# Reproducimos un tono de alarma durante 2 segundos.
os.system("play -n synth 2 sine 880")
