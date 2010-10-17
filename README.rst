IPython, la interactividad al poder
===================================
**PyConAr 2010**

    :improvisa: Martín Gaitán [*]_ <gaitan@gmail.com>
    :fecha: Viernes 15 de Octubre de 2010
    :licencia: CC-by-sa 2.5 Argentina


.. [*] http://nqnwebs.com


Cómo ejecutar la charla
------------------------

Esta presentación interactiva usa una clase incluída en IPython, ``IPyhton.demo.CleanDemo``
que importa el módulo ``charla.py`` y con un simple marcado permite secuenciar 
bloques interactivos. 

Para lanzar la presentación ejecute::

    $ ipython alpoder.py


Controles
---------

.. code-block:: pycon

    >>> d()     #para mostrar el bloque/slide actual e incremetar +1 el cursor
    >>> d(i)     #para ir al ``i``ésimo bloque (sin cambiar el cursor)
    >>> d.again() #para repetir el último bloque mostrado
    >>> d.jump(n) #para mover el cursor n bloques (Ej: d.jump(-1) para volver al último bloque mostrado)
    >>> d.reset() #para mover el cursor al inicio.


Repositorio
------------

http://github.com/nqnwebs/IPython-interactive-talk




