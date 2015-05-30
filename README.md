class: center, middle <!-- for title in the center of the slide -->
name: primera-diapo

# Tests automáticos en Python

### Una introducción para principantes (python-vigo, 21/05/2015)

Francisco Puga

fran.puga (at) gmail.com

https://twitter.com/fpuga

http://conocimientoabierto.es

???

python -m SimpleHTTPServer 8000

---


# Objetivos

* Qué es un test automático y porqué debería escribirlos
* Mi primer test automático en python

.footnote[

*Aviso* : Que las transpas tenga _bullets_ y afirmaciones no significa que sean verdades absolutas. Cada caso será distinto.

]
---

# ¿Porqué hacer tests?

Cuando se hace un cambio se comprueban (_testean_) dos cosas:

* el cambio añade la funcionalidad deseada
* el cambio no rompe nada (regression test)

---

# Tests manuales

Si sólo queremos probar el cambio actual, según el caso desde:

* Recargar la pestaña del navegador y hacer click
* Compilar, levantar la aplicación, loguearse, ...

Si tenemos que probar que no hemos roto nada...

---

# ¿Por qué hacer tests automáticos?

## Las razones de "internet"

* [Porqué ahorran tiempo y dinero](https://www.atlassian.com/test-automation)
* [Porqué lo dice stackoverflow](http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort?page=1&tab=votes#tab-top)
* [Should I write unit tests? Yes and I’ll tell you why](Should I write unit tests? Yes and I’ll tell you why)

---

# ¿Por qué hacer tests automáticos?

* Porqué incrementan la *confianza*
* Porqué incrementan la *velocidad*

---

# Confianza

* ... en que puedo cambiar algo sin romper nada -> Mejor diseño
* ... en que lo que se despliega funciona -> Dormir mejor
* ... en que puedes parar de escribir código (si haces tdd)

# Velocidad

* ... al desarrollar. Sin esperas para levantar la aplicación
* ... al desarrollar. Sin "clicks" hasta llegar a lo que hay que probar
* ... _time to market_. Despliegues más regulares al haber ciclos de testing/qa menores

---

# Una definición "extendida" para tests unitarios

* Funcionan contra una mínima funcionalidad. Usualmente un único método
* Todo test debe ser independiente de otro test
* Son rápidos
* El test prueba por si mismo ser correcto o no. Sin intervención humana
* El código que prueban está aislado del resto del código (no tocan la base de datos, ni el sistema de archivos, ni ...)

Que un test no sea así, no quiere decir que sea malo, sólo que según algunas definiciones no será unitario

---

# Conceptos

.left-column[
* tests automáticos

* unit test

* regression test

* [acceptance test](http://agiletesting.blogspot.com.es/2006/04/should-acceptance-tests-be-included-in.html)

* end-to-end test

* functional test

* ...

]



.right-column[

* [mocks](http://agiletesting.blogspot.com.es/2006/12/mock-testing-examples-and-resources.html) y [stubs](http://martinfowler.com/articles/mocksArentStubs.html)

* integration test

* [tdd](http://martinfowler.com/articles/is-tdd-dead/)

* bdd

* performance test

* [pyramid test](http://martinfowler.com/bliki/TestPyramid.html)

* ...
]

---

Cuando empiezas con tests pueden pasar dos cosas:

* que empieces a hacerlos con el primer tutorial que encuentres
* que abras tantas pestañas en el navegador que acabes bloqueado

---

# Un par de consejos al *empezar* a hacer tests

* Menos leer y más programar
* Cuando aparezca un bug _sencillo_ haz un test antes de resolverlo. Cuando el test esté correcto el bug estará resuelto y tendrás un test de regresión.
* No obsesionarse con que el test sea unitario
* Que todo el equipo tenga la mismas motivaciones y _definiciones_

---

# Librería estándar. unittest

Llamada en sus orígenes PyUnit en honor al JUnit de Beck y Gamma, lleva desde python 2.1 en la librería estándar con el nombre de unittest. En python 2.7 y 3.2 hubo muchas mejoras que fueron portadas a versiones anteriores bajo el nombre de unittest2

```python
# -*- coding: utf-8 -*-
# test_1.py

import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):

    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()
```

---

## Importar la librería

```python
# -*- coding: utf-8 -*-

*import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):

    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()
```

---

## Clases que hereden de unittest.TestCase

```python
# -*- coding: utf-8 -*-

import unittest

def suma(a, b):
    return a + b

*class ExampleTest(unittest.TestCase):

    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()
```

---

## Métodos cuyo nombre empiece por 'test'

```python
# -*- coding: utf-8 -*-

import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):

*    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()
```

---

## _Asertar_ la condición a comprobar

```python
# -*- coding: utf-8 -*-

import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):

    def testMethod(self):
        actual = suma(1,2)
        expected = 3
*        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

if __name__ == '__main__':
    unittest.main()
```

---

## Código para ejecutar desde consola

```python
# -*- coding: utf-8 -*-

import unittest

def suma(a, b):
    return a + b

class ExampleTest(unittest.TestCase):

    def testMethod(self):
        actual = suma(1,2)
        expected = 3
        self.assertEqual(expected, actual, 'suma(1,2) no es igual a 3')

*if __name__ == '__main__':
*    unittest.main()
```

---

# Normas

* Extender unittest.TestCase
* Los nombres de métodos deben comenzar con 'test'. Los que no se llamen así no se ejecutaran.
* Que todo el equipo use la misma nomenclatura. (No es una norma pero debería serlo)

---

# Convenciones

* Usar nombres largos para los nombres de los métodos porque saldrán en el mensaje de error
* Usar 'Test' como prefijo o sufijo del nombre de la clase
* Usar 'test' como prefijo del nombre del fichero (algunas utilidades usan este patrón por defecto para descubrir tests)
* Usar 'tests' como nombre del directorio donde pondremos los tests (_nose_ busca en este directorio por defecto)
---

```python
# -*- coding: utf-8 -*-
# test_2.py

import unittest

def division(a, b):
    return a / b

class Example2Test(unittest.TestCase):
    def testMethod(self):
        actual = division(6, 2)
        expected = 3
        self.assertEqual(expected, actual, 'I should study maths')

    def test_that_fails(self):
        actual = division(6, 2)
        expected = -99
        self.assertEqual(expected, actual, 'I must study maths')

    def test_with_a_not_expected_error(self):
        actual = division(1, 0)
        expected = 0
        self.assertEqual(expected, actual, 'Are you serious')

    def esto_no_es_un_test(self):
        actual = division(1.0, 2)
        expected = 0.5
        self.assertEqual(expected, actual, 'division(1.0, 2) no es igual a 0.5')

if __name__ == '__main__':
    unittest.main()
```
---

# Ejemplo de ejecución de tests

* 1 correcto, 1 falla, y otro tiene una excepción

```bash
$ python test_2.py
.FE
======================================================================
ERROR: test_with_a_not_expected_error (__main__.Example)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_3.py", line 20, in test_with_a_not_expected_error
      actual = division(1, 0)
        File "test_3.py", line 6, in division
	    return a / b
	    ZeroDivisionError: integer division or modulo by zero

======================================================================
FAIL: test_that_fails (__main__.Example)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_3.py", line 17, in test_that_fails
      self.assertEqual(expected, actual, 'I must study maths')
      AssertionError: I must study maths

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1, errors=1)
```

---

# Ejecutar tests desde consola

Cuando tenemos muchos tests...

```bash
$ python pythonvigo/tests/test_1.py
[...]

$ python pythonvigo/tests/test_2.py
[...]

$ python python -m pythonvigo.tests.all.test_everything_is_working
[...]

$ ...
```

tenemos que automatizar la forma de ejecutarlos

---

# Ejecutar tests por código

```python
# run_all_tests.py
import unittest

import test_1
import test_2

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_1)
suite.addTests(loader.loadTestsFromModule(test_2))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
```

---

# Ejecutar tests con _discover_

[discover](https://pypi.python.org/pypi/discover) Una utilidad para _automatizar_ la ejecutación de los _tests automáticos_.

```bash
$ pip install discover
$ python -m discover -s tests/
```

Aunque llegados a este punto seguramente nose, py.test o el método que recomiende tu framework de desarrollo si usas uno, son opciones más interesantes.

---

# Métodos assert

* assertAlmostEqual(first, second, places=7, msg=None): Comprueba que los objetos pasados como parámetros sean iguales hasta el séptimo decimal (o el número de decimales indicado por places).
* assertEqual(first, second, msg=None): Comprueba que los objetos pasados como parámetros sean iguales.
* assertFalse(expr, msg=None): Comprueba que la expresión sea falsa.
* assertNotAlmostEqual(first, second, places=7, msg=None): Comprueba que los objetos pasados como parámetros no sean iguales hasta el séptimo decimal (o hasta el número de decimales indicado por places).
* assertNotEqual(first, second, msg=None): Comprueba que los objetos pasados como parámetros no sean iguales.
* assertRaises(excClass, callableObj, args, kwargs): Comprueba que al llamar al objeto callableObj con los parámetros definidos por args y kwargs se lanza una excepción de tipo excClass.
* assertTrue(expr, msg=None): Comprueba que la expresión sea cierta.
* assert_(expr, msg=None): Comprueba que la expresión sea cierta.

---

# Métodos fail

* fail(msg=None): Falla inmediatamente.
* failIf(expr, msg=None): Falla si la expresión es cierta.
* failIfAlmostEqual(first, second, places=7, msg=None): Falla si los objetos pasados como parámetros son iguales hasta el séptimo decimal (o hasta el número de decimales indicado por places).
* failIfEqual(first, second, msg=None): Falla si los objetos pasados como parámetros son iguales.
* failUnless(expr, msg=None): Falla a menos que la expresión sea cierta.
* failUnlessAlmostEqual(first, second, places=7, msg=None): Falla a menos que los objetos pasados como parámetros sean iguales hasta el séptimo decimal (o hasta el número de decimales indicado por places).
* failUnlessEqual(first, second, msg=None): Falla a menos que los objetos pasados como parámetros sean iguales.
* failUnlessRaises(excClass, callableObj, args, kwargs): Falla a menos que al llamar al objeto callableObj con los parámetros definidos por args y kwargs se lance una excepción de tipo excClass.

---

# setUp y tearDown

* *setUp*: Se ejecuta antes de cada test
* *tearDown*: Se ejecuta después de cada test

```python
import unittest

from mymodule import MyClass

class MyTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.myclass = MyClass()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.myclass.close()

    def testTrue(self):
        result = self.myclass.method()
        self.asssertTrue(result)
```

---

# setUpClass tearDowClass

Se ejecutan una vez por clase

```python
import unittest

from mymodule import MyClass

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()

   def testTrue(self):
        result = self._connection.doSomething()
        self.asssertTrue(result)
```

---

# doctest

```python
# -*- coding: utf-8 -*-

import unittest

def division(a, b):
    '''
    Divides a with b

    >>> division(6, 2)
    3

    >>> division(10, 2)
    99
    '''
    return a / b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```
---

# Referencias y tutoriales

* [Introduction to unittest](http://www.voidspace.org.uk/python/articles/introduction-to-unittest.shtml)
* Dive Into Python: [Unit testing](http://www.diveintopython3.net/unit-testing.html) y [Refactoring](http://www.diveintopython3.net/refactoring.html)
* [The Hitchhiker’s Guide to Python!](http://docs.python-guide.org/en/latest/writing/tests/)
* [unittest – Automated testing framework - Python Module of the Week](unittest – Automated testing framework)
---

template: primera-diapo
