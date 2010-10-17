IPython, la interactividad al poder
===================================
**PyConAr 2010**

    :improvisa: Martín Gaitán [*]_ <gaitan@gmail.com>
    :fecha: Viernes 15 de Octubre de 2010
    :licencia: CC-by-sa 2.5 Argentina


.. [*] http://nqnwebs.com


Cómo ejecutar la charla
=======================

Esta presentación interactiva usa una clase incluída en IPython, ``IPyhton.demo.CleanDemo``
que importa el módulo ``charla.py`` y con un simple marcado permite secuenciar 
bloques interactivos. 

Para lanzar la presentación ejecute

$ ipython alpoder.py


Controles
==========

>>> d()     #para avanzar un bloque/slide
>>> d(i)     #para ir al ``i``ésimo bloque
>>> d.again() #para repetir la última
>>> d.jump(n) #para saltar n bloques (Ej: d.jump(-1) para volver al último bloque mostrado)
>>> d.reset() #para iniciar de nuevo


Repositorio
===========
http://github.com/nqnwebs/IPython-interactive-talk




