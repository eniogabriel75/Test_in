def inverter(texto):
  text_invert = texto [::-1]
  return text_invert

texto = "Me contrata"
text_invert = inverter(texto)
print("Texto original: ", texto)
print("Texto invertido: ", text_invert)