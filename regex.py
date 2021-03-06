# Se importa el módulo (re) para usar regular expressions
import re

def main():
  # El dato se pregunta hasta que se cumpla la expresión
  while True:
    strRFC = input("Ingrese RFC: ")
    # (^) inicia con, ($) termina con. [A-Z][0-9] caracteres de "A a Z" y "0 a 9"
    if (re.search("^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$", strRFC)):
      print("RFC correcto")
      # El ciclo termina cuando se presenta un break
      break
    else:
      print("RFC incorrecto. Intente de nuevo.")