Introducción y contexto
Los programas adquieren significado cuando pueden tomar decisiones y repetir acciones. El flujo de control permite a un programa:
Ejecutar distinto código según las condiciones.
Repetir instrucciones usando bucles.
Combinar condiciones lógicas para modelar situaciones reales.
Este proyecto se centra exclusivamente en el flujo de control usando:
if, elif, else
Operadores de comparación
Lógica booleana
Bucles while
Bucles for con range()
Las actividades están adaptadas del proyecto existente "Python - if/else, loops, functions", conservando solo aquellas alineadas con el flujo de control.
Objetivos de aprendizaje
Al final de este proyecto, deberías ser capaz de:
Escribir sentencias condicionales usando if, elif y else.
Usar correctamente operadores de comparación y lógicos.
Controlar la repetición usando bucles while y for.
Razonar sobre los límites de los bucles y los rangos de iteración.
Generar salida formateada usando iteración numérica.
Combinar condiciones y bucles para producir una salida determinista.
Recursos
Resumen general de toda la documentación en español
Python - Flujo de control
La siguiente documentación es la oficial pero se encuentra en inglés
Documentación oficial
Tutorial de Python — Herramientas de flujo de control
https://docs.python.org/3/tutorial/controlflow.html
Tutorial de Python — Más sobre condiciones
https://docs.python.org/3/reference/expressions.html#comparisons
Requisitos generales
Las correcciones se ejecutarán en Ubuntu 20.04 LTS.
Versión de Python utilizada para la corrección: Python 3.8.x.
Todo archivo Python debe comenzar exactamente con:
Todo archivo Python debe:
Ser ejecutable.
Terminar con una nueva línea.
Cumplir con PEP8 (pycodestyle 2.7.x).
No se permiten bibliotecas externas.
No se permiten funciones en este proyecto.
No se permiten imports.
La salida debe coincidir exactamente con el formato esperado.
Tareas
0. Cualquier cosa positiva es mejor que nada negativo
Crea un script que asigne un número entero aleatorio a una variable llamada number. Copia la siguiente línea exactamente como está, después de la línea shebang.
number = __import__('random').randint(-10, 10)
La línea anterior asignará un número entero aleatorio entre -10 y 10 a la variable number. No necesitas enfocarte en esto todavía.
Usando sentencias condicionales, imprime:
<number> is positive si el número es mayor que 0
<number> is zero si el número es igual a 0
<number> is negative si el número es menor que 0
Ejemplo:
spam@camelot:~/$ ./positive_or_negative.py 
-4 is negative
spam@camelot:~/$ ./positive_or_negative.py 
0 is zero
spam@camelot:~/$ ./positive_or_negative.py 
-3 is negative
spam@camelot:~/$ ./positive_or_negative.py 
-10 is negative
spam@camelot:~/$ ./positive_or_negative.py 
10 is positive
Repositorio:
Repositorio GitHub: utec-core-engineering
Directorio: python_fundamentals/control_flow
mkdir -p python_fundamentals/control_flow
cd python_fundamentals/control_flow
nano positive_or_negative.py
chmod +x positive_or_negative.py
./positive_or_negative.py
git add positive_or_negative.py
git add
git init
git add python_fundamentals/control_flow/positive_or_negative.py
git commit -m "Add positive_or_negative.py"
git push origin main
git config --global user.email "tu_correo@example.com"
git config --global user.name "isabelperazzo27"
git add positive_or_negative.py
git commit -m "Add positive_or_negative.py"
git push origin main
git push origin master
git remote add origin https://github.com/isabelperazzo27/utec-core-engineering.git
git push -u origin master
git remote add origin https://github.com/isabelperazzo27/utec-core-engineering.git
git push -u origin master
git remote -v
cd python_fundamentals/control_flow
git init
git remote add origin https://github.com/isabelperazzo27/utec-core-engineering.git
git add positive_or_negative.py
git commit -m "Add positive_or_negative.py"
git push -u origin master
git remote set-url origin https://github.com/isabelperazzo27/utec-core-engineering.git
git push -u origin master
cd ~/python_fundamentals/control_flow
echo "# Python - Control Flow" > README.md
cat positive_or_negative.py
#!/usr/bin/env python3
number = __import__('random').randint(-10, 10)
if number > 0:;     print(f"{number} is positive")
elif number == 0:
else:
chmod +x positive_or_negative.py
git add .
git commit -m "Add positive_or_negative.py and README.md"
git branch -M main
git push -u origin main
cd ~
git init
git remote add origin https://github.com/isabelperazzo27/utec-core-engineering.git
git remote set-url origin https://github.com/isabelperazzo27/utec-core-engineering.git
rm -rf ~/python_fundamentals/control_flow/.git
echo "# utec-core-engineering" > ~/README.md
