# 📜 DESCRIPCIÓN GENERAL
Este script es un generador de imágenes con afirmaciones espirituales o motivacionales. Toma una imagen base (descargada o local), añade frases centradas en estilo y color personalizado, y guarda cada imagen final en una carpeta específica.

Ideal para base de proyectos más estructurados para crear material para redes.

## 🛠️ DEPENDENCIAS
- PIL (Pillow): para manipulación de imágenes.
- requests: para descargar imágenes desde internet.
- os, textwrap: funciones de sistema y formateo de texto.

## 🎯 FLUJO DEL SCRIPT
1. Entrada de datos:
   - Elección de imagen: descargar vía URL o usar imagen local.
   - Ingreso de afirmaciones separadas por punto y coma.
   - Selección de fuente (Arial, Times, Verdana, etc.).
   - Selección de color (blanco, negro, rojo, azul, verde).

2. Procesamiento:
   - Carga de imagen base.
   - Afirmación centrada horizontal y verticalmente.
   - Ajuste automático de líneas con `textwrap`.

3. Salida:
   - Genera imágenes en la carpeta `imagenes_con_afirmaciones`.

## 🖌️ PERSONALIZACIÓN
- Fuentes disponibles (necesitan estar en el sistema):
  Arial, Times New Roman, Verdana, Calibri, Cooper Black, Algerian.
- Color de texto configurable.
- Espaciado vertical automático entre líneas.
- Textos centrados en la imagen.

## 📂 ORGANIZACIÓN DE ARCHIVOS
- Carpeta: `imagenes_con_afirmaciones`
- Archivo generado por afirmación: `afirmacion_i.jpg`, donde i es el número.

## RECOMENDACIONES
- Verifica que las fuentes estén disponibles.
- Considera formatos cuadrados o verticales para redes sociales como Instagram o Pinterest.
