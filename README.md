# Demo Microsoft SEAL - Python
Demo del uso de la librería SEAL para criptografía completamente homomórfica (FHE) de Microsoft.
Incluye un fichero de instalación de dependencias junto con una demo denominada scenario.py.

## Instalación
### Docker
1. Instalación de dependencias
~~~
sudo apt-get update
sudo apt-get install git build-essential cmake python3 python3-dev python3-pip
~~~
2. Instalación de docker docker
~~~
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
~~~
3. Clonación del proyecto de SEAL-Python.
~~~
git clone https://github.com/Huelse/SEAL-Python.git
cd SEAL-Python/
~~~
4. Construcción de la imagen a partir del Dockerfile proporcionado y comprobación de su correcta creación.
~~~~
sudo docker build -t seal_python .
sudo docker image ls
~~~~
5. Arrancar el contenedor de docker.
~~~
sudo docker run -it --name container-seal seal_python
~~~
6. Entramos en un contenedor de docker interactivo de lenguaje Python. Para ejecutar la demo debemos seguir los siguientes pasos.
~~~~
import os
os.system('git clone >>> os.system('git clone https://github.com/patriciaOrtuno28/Demo-MicrosoftSEAL-Python.git')
os.chdir('Demo-MicrosoftSEAL-Python')
os.system('apt-get install python3-tk')
os.system('pip3 install simplefhe')
os.system('python3 scenario.py')
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
