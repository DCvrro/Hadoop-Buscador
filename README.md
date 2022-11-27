<em> Tarea 3-SD </em>
  <p align="left">
   <img src="https://img.shields.io/badge/STATUS-TERMINADO-blue">  <img src="https://img.shields.io/badge/LICENSE-FREE-green">
   </p>
   
<h1 align='center'>Tarea 3 <h1>
  <h3> Integrantes: Abel Baulloza y Diego Carrillo .</h3>
  <h3>**Instrucciones y uso**</h3>

📁 Acceso al proyecto

**Descargar el archivo desde el repositorio de github o hacer un clone mediante consola de comandos.**

🛠️ Abre y ejecuta el proyecto.
  
**Antes de trabajar, es necesario estar dentro de la carpeta instalada e ingresar al path**
  ```
  $cd map-reduce-hadoop-main/examples/Wikipedia/Wikipedia
```
**Ejecutar el archivo api_wikipedia.py**

  **Luego, buildear Dickerfile**
```
  $docker build -t hadoop . 
```
**Despues, levantar contenedor**
  ```
  $docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
  ```
  **Si desea utilizar la interfaz grafica de Hadoop para verificar que los siguientes comando a ejecutar se realizaron exitosamente, ingrese a [http://localhost:9870/dfshealth.html#tab-overview](http://localhost:9870/explorer.html#/user/hduser)**
  **Ingresar al contenedor donde esta alojado hadoop**
  ```
  $docker exec -it hadoop .
  ```
  **Crear las carpetas en hadoop, las cuales tendran los documentos extraidos de la api de wikipedia para ser procesados**
  ``` 
  $hdfs dfs -mkdir /user
  $hdfs dfs -mkdir /user/hduser
  $hdfs dfs -mkdir /user/hduser/input 
  ```
  **Copiar las carpetas donde se generaron los documetnos extraidos de la api de wikipedia a la carpeta input creada en hadoop**
  ``` 
    $hdfs dfs -put Wikipedia/Wikipedia/Documentos1 /user/hduser/input
    $hdfs dfs -put Wikipedia/Wikipedia/Documentos2 /user/hduser/input
  ``` 
  **Atribuir todos los permisos a la carpeta hduser de hadoop**
  ``` 
  $sudo chown -R hduser .
  ```
  **Finalmente, ejecutar el siguiente comando para ejecutar MapReduce**
  ```
  $mapred streaming -files mapper.py,prueba.py -input /user/hduser/input/Documentos*/*.txt -output /user/hduser/output -mapper "python mapper.py" -reducer "python prueba.py"
  ```
  **Este comando, ejecuta los archivos mapper.py, prueba.py(reduce), ocupa de input los documentos guardados en las carpetas de hadoop y crea un a carpeta output en    donde se almacenara el output del programa**
 
  **Si se desea observar el output generado por consola, debe ejecutar el siguiente comando**
  ```
  $hdfs dfs -cat /user/hduser/output/*
  ```
  **Ya ejecuta MapReduce, se sale del contenedor de docker y se trabaja en la maquina local**
  **Ahora, para crear archivo json que almacenara el output generado al ejecutar MapReduce, se ejecuta el comando**
  ```
  $cat resultados.txt | python toJson.py 
  ```
  **Este archivo json cumple la funcion de ser una base de datos para el programa**
  
  **Si desea visualizar el archivo json, ejecute el comando**
 ```
  $cat bdd.json 
  ```
  
  **Finalizando, para ejecutar el buscador con indice invertido, se debe ejecutar el siguiente archivo**\
 ```
  $python buscador.py
  ```
  
## Autores

| [<img src="https://www.geekmi.news/__export/1644190196029/sites/debate/img/2022/02/06/zenitsu4.jpg_172596871.jpg" width=115><br><sub>Abel Baulloza</sub>](https://github.com/Dharknight) |  [<img src="https://www.unotv.com/uploads/2020/08/loco-valdes.jpg" width=115><br><sub>Diego Carrillo</sub>](https://github.com/DCvrro) |
| :---: | :---: |
