from PIL import Image, ImageDraw, ImageFont
import os
import requests
import textwrap

#entradas de imagen y afirmaciones
print("Bienvenido al generador de imagen con afirmaciones.")

print(""" vamos a elegir la imagen
      si desea descargar una imagen de internet,
      debe ser en formato jpg. Si ya tiene una imagen descargada,1
      asegurese de que esta en la misma carpeta que este script.""")

opciones_de_imagen = input("descargar imagen precione '1'; si usa imagen ya descargada precione '2': ")

#cargamos la imagen segun la opcion elegida
if opciones_de_imagen == '1':
    url = input("ingrese la URL de la imagen: ")
    response = requests.get(url)
    if response.status_code == 200:
        # Guardamos la imagen descargada
        with open('imagen_descargada.jpg', 'wb') as f:
            f.write(response.content)
        imagen = 'imagen_descargada.jpg'
    else:
        print("Error al descargar la imagen.")
        exit()
elif opciones_de_imagen == '2':
    imagen = input("ingrese el nombre de la imagen (con extension): ")
    if not os.path.exists(imagen):
        print("La imagen no existe.")
        exit()
else:
    print("Opción no válida.")
    exit()

# Lista de afirmaciones
print("los textos debem estar separados por punto y coma ';'")
textos = input("escribe aqui tus afirmaiones:")
afirmaciones = [txt.strip() for txt in textos.split(';') if txt.strip()]

#cargamos la imagen
imagen_base = imagen

print("""
    Ahora vamos a elegir la fuente para las afirmaciones.
    lamentablemente posemos muy pocas.
    1. Arial
    2. Times New Roman
    3. Verdana
    4. Calibri
    5. Copper negra
    6. Algerian normal""")
elegir_fuente = input("elige la fuente (número): ")
if elegir_fuente == '1':
    elegir_fuente = "arial.ttf"
elif elegir_fuente == '2':
    elegir_fuente = "times.ttf"
elif elegir_fuente == '3':
    elegir_fuente = "verdana.ttf"
elif elegir_fuente == '4':
    elegir_fuente = "calibri.ttf"
elif elegir_fuente == '5':
    elegir_fuente = "COOPBL.TTF"
elif elegir_fuente == '6':
    elegir_fuente = "ALGER.TTF"
else:
    print("Opción no válida, se usará Arial por defecto.")
    elegir_fuente = "arial.ttf"

print("eligue el color para las letras")
print("""
    1. blanco
    2. negro
    3. rojo
    4. azul
    5. verde
    """)
color_opcion = input("elige el color de las letras: ")
if color_opcion == '1':
    color = "white"
elif color_opcion == '2':
    color = "black"
elif color_opcion == '3':
    color = "red"
elif color_opcion == '4':
    color = "blue"
elif color_opcion == '5':
    color = "green"
else:
    print("Opción no válida, se usará blanco por defecto.")
    color = "white"
#carpeta de salida

print("""color para el contorno?:
      1. blanco
      2. negro
      """)
color_contorno_opcion = input()
if color_contorno_opcion == '1':
    color_contorno = "white"
elif color_contorno_opcion == '2':
    color_contorno = "black"
else:
    print("Opción no válida, se usará negro por defecto.")
    color_contorno = "black"

#la carpeta por si no esta
os.makedirs('imagenes_con_afirmaciones', exist_ok=True)

#procesamos la imagen
for i, afirmacion in enumerate(afirmaciones):
    imagen = Image.open(imagen_base)
    draw = ImageDraw.Draw(imagen)
    ancho_imagen, alto_imagen = imagen.size

    #ajustamos el tamaño y la tipografia
    tamaño_fuente = int(ancho_imagen * 0.05)  # Tamaño de fuente proporcional al ancho de la imagen
    fuente = ImageFont.truetype(elegir_fuente, tamaño_fuente)  # Asegúrate de tener la fuente seleccionada disponible

    # Ajustamos la afirmación para que quepa en la imagen
    max_ancho = int(ancho_imagen * 0.8)  # 80% del ancho de la imagen
    lineas = textwrap.wrap(afirmacion, width=30)  # Ajustamos el ancho de las líneas

    #medimos alto y ajustamos
    alto_total = 0
    for linea in lineas:
        box = draw.textbbox((0, 0), linea, font=fuente)
        alto_total += box[3] - box[1] + 10
    
    y = (alto_imagen - alto_total) // 2  # Centrar verticalmente

    #dibujamos cada linea lo mas centrado posiblre
    for linea in lineas:
        box = draw.textbbox((0, 0), linea, font=fuente)
        ancho_texto = box[2] - box[0]
        x = (ancho_imagen - ancho_texto) // 2

        grosor = 2  # Grosor del borde
        # Dibujar borde alrededor del texto
        for dx in range(-grosor, grosor + 1):
            for dy in range(-grosor, grosor + 1):
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), linea, font=fuente, fill=color_contorno)
        draw.text((x, y), linea, font=fuente, fill=color)
        y += box[3] - box[1] + 10   # Espacio entre líneas

    # Guardamos la imagen con la afirmación
    salida = f"imagenes_con_afirmaciones/{afirmacion}_{i + 1}.jpg"
    imagen.save(salida)
    print(f"Imagen guardada como {salida} en la carpeta 'imagenes_con_afirmaciones'.")
print(" ")
print("Todas las imágenes han sido procesadas y guardadas.")
print("¡Gracias por usar el generador de imágenes con afirmaciones!")

#recuerda si sirve no lo toques jeje si no reinicia o descargas dependencias jeje