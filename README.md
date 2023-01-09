# Demo Microsoft SEAL - Python
Demo del uso de la librería SEAL para criptografía completamente homomórfica (FHE) de Microsoft.
Incluye un fichero de instalación de dependencias junto con una demo denominada scenario.py.

## Modo de uso

1. Introducir un dígito entero en el cuadro de texto y pulsar `Añadir`.
2. Repetir la operación para todos los dígitos a los que queramos aplicar la fórmula. Se irán concatenando en una lista.
3. Pulse `Encriptar` cuando haya introducido todos los valores que desee.
4. Pulse `Desencriptar` para obtener el resultado de `x**3 - 3x + 1` por cada dato individual introducido.

## Instalación
### Docker
1. Instalación de docker (Opcional): Linux
~~~
./installDocker.sh
~~~
2. Construcción de la imagen Docker a partir del Dockerfile
~~~
sudo docker build -t seal_python .
~~~
3. Arrancar el contenedor de docker
~~~
sudo docker run -it --name seal seal_python
~~~
4. Acceder al contenedor de docker
~~~~
sudo docker exec -it seal /bin/bash
~~~~
5. Ejecutar la demo
~~~~
cd SEAL-Python/
python3 scenario.py
~~~~


### Linux
1. Clonación del proyecto
~~~~
git clone https://github.com/patriciaOrtuno28/Demo-MicrosoftSEAL-Python.git
cd Demo-MicrosoftSEAL-Python/
~~~~
2. Ejecutar fichero automatizado de instalación de dependencias
~~~~
python3 install_simplefhe.py
~~~~
3. Ejecutar la demo en el directorio correspondiente
~~~~
cd SEAL-Python/
python3 scenario.py
~~~~
