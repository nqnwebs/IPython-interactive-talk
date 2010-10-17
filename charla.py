#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
IPython, la interactividad al poder
===================================
**PyConAr 2010**

    :improvisa: Martín Gaitán [*]_ <gaitan@gmail.com>
    :fecha: Viernes 15 de Octubre de 2010
    :licencia: CC-by-sa 2.5 Argentina


.. [*] http://nqnwebs.com

    Controles::

        >>> d()     #para avanzar un bloque/slide
        >>> d(i)     #para ir al ``i``ésimo bloque
        >>> d.again() #para repetir la última
        >>> d.jump(n) #para saltar n bloques (Ej: d.jump(-1) para volver al último bloque mostrado)
        >>> d.reset() #para iniciar de nuevo
"""

# <demo> stop

# <demo> auto
"""
Disclaimer
----------

Todo lo que sigue es culpa de John Lenton:

    
    2010/7/28 John Rowland Lenton <john.lenton@canonical.com>:
    > Hola!
    >
    > Estamos organizando PyConAr. Viste? La conferencia de Python en
    > Argentina (...) te vas a dar cuenta cuando
    > estés acá en Córdoba que podrías haber presentado tu charla, y te vas
    > a sentir muy zonzo.

y de la militancia:

    2010/9/27 Martín Gaitán <gaitan@gmail.com>:
    > Gente, cómo va?
    >
    > Trabajo en una organización que labura en barrios populares de Córdoba
    > Capital (...) Uno de los talleres que tenemos es Serigrafía con jóvenes del
    > barrio...

IPython es inocente (y está buenísimo) 

DISCULPAS POR ANTICIPADO
"""

# <demo> stop

"""
Empecemos ...
-------------

"""

#algunas variables

confesion = "Esta presentación es interactivamente **fea** "
x = 1
mi_tupla = ('a', 3)
pi = 3.141592

#una funcion

def suma(a=2, b=2):
    """ adiciona los parametros """

    return a + b

#e importemos algo
import random


# Los atajos TAB,  <?> y <??>
# Las primeras magias: who/s,  autocall
# %run 
# Las magias también tiene su documentación accesible


# <demo> stop

"""
Nada se pierde 
---------------
"""

# Manipular Outputs: _ __ ___ _n Out[n]
# Manipular Inputs: _i _ii _iii _in In[n]
# No se piede aunque no se imprima: ;
# %hist: La historia contemporánea
# %hist -g  : Historia universal (-g es de *grep*)

# <demo> stop

"""
Ipython interactua con el SO (1/2)
-----------------------------------
"""

# algunos comandos tienen alias en IPython (%alias)

# otros hay que escaparlos con !  (aunque es fácil definir nuevos alias)

# Ejemplo: !ipython -pylab  -> lanzamos ipython en modo pylab, desde ipython!

# !! escapa y captura la salida en una lista inteligente

# <demo> stop


"""
Ipython interactua con el SO (2/2)
-----------------------------------
"""

#también se pueden pasar  variables
pattern = "*.py"

#y crear atajos a directorios con %bookmark


# <demo> stop

"""
Ipython es un intérprete interactivo, no un editor (1/2)
---------------------------------------------------------
"""

# Line-oriented: Está pensado para que juegues con los método de tus objetos
# No es facil editar bloques multilineas. 

# Mejor usar un editor : %edit

# %edit usa el editor que elijamos 

# Veamos ...


# <demo> stop


"""
Ipython es un intérprete, no un editor (2/2)
--------------------------------------------
"""

# %edit es una masa!

# Usar %hist / %edit


# <demo> stop


"""
Logging 
--------
"""

# %logstart : que comience la función

# 

# <demo> stop

"""
Más métodos persistencia
------------------------
"""



# %store <var> /  %store -r   : usa pickle.

# %save -> guardar líneas específicas: %save filename n1-n2 ... 

# macro -> repetir ejecución de lineas: %macro nombre n1-n2 ... 

# <demo> stop


"""
Cronometrar, 
------------------------


"""


# Productoria Deadmatch

numeros = xrange(1000)

from itertools import product

def mi_productoria(seq):
    producto = 1
    for elem in seq:
        producto *= elem
    return producto
      
# <demo> stop


"""
Debugging
-----------
"""

# %pdb

# se ejecuta automáticamente el debugger cuando ocurre una excepción.

# Raise TypeError()

# <demo> stop


"""
Copy & Paste
-----------
"""

# Copiar código de cualquier lado 
# ... and %paste it!

# <demo> stop

"""
Modos especiales para GUI
---------------------------
"""

# Por qué hacen falta?

# Ejemplo: GPEC 

# <demo> stop

"""
Modo Pylab
"""

# Python con sabor a Matlab

"""
x = arange(.0 , 0.26, .001) 
y = 4*exp(-x**2/(0.1)**2) + 9*exp(-(x-0.13)**2/(1e-5))                     #http://goo.gl/LnWc
ylabel('PROGRAMMING\nSKILLS', fontsize='large', rotation='horizontal')
xlabel('BLOOD ALCOHOL CONCENTRATION (%)', fontsize='large')
gcf().subplots_adjust(left=0.25, right=0.95)
gca().set_title('Ballmer Peak', fontsize='x-large')
plot(x, y, 'r')

"""

# <demo> stop

"""
Preguntas
----------
"""

# No más preguntas señor juez


# <demo> stop

"""
Perdón
------
"""

# y gracias
