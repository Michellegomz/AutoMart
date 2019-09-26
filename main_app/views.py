from django.shortcuts import render

def index(request):
    return render(request, 'index.html', 
    {'autos' : autos})
 #   nombreAuto = "vw Jetta"
  #  modelo = 2018
   #color = "Gris"

    #dict = {'auto_nombre' : nombreAuto,
     #      'auto_modelo' : modelo,
      #     'auto_precio' : precio,
       #    'auto_color' : color}

    #return render(request, 'index.html', dict)

class Auto:
    def __init__(self, nombre, precio, modelo, color):
        self.nombre = nombre
        self.precio = precio
        self.modelo = modelo
        self.color = color

autos = [
    Auto('VW Jetta', 145000, 2018, 'Gris'),
    Auto('Lexus', 256000, 2017, 'Rojo'),
    Auto('Futura', 0, 1954, 'Aqua'),
    Auto('Porche', 250000, 2010,'Azul')

]

   