# SIEMFAP-Sistema-Inteligente-de-Ecoturismo-y-Monitoreo-de-Fauna-en-reas-Protegidas-

nombre del equipo: Byte Warrios


El turismo de naturaleza y conservación es una gran oportunidad para ayudar a la recuperación económica post-pandemia nuestro modelo de IA basado en VGG16, puede ser adaptado para ofrecer herramientas que impulsen el ecoturismo responsable en áreas protegidas, parques nacionales y reservas naturales.


Problematica

Este plan se centra en un problema grave que pone en riesgo tanto la Bio-diversidad de vida en Venezuela como el bienestar de las comunidades que dependen del sector turistico para subsistir, Venezuela, hogar de una increíble diversidad biológica, está perdiendo especies valiosas a un ritmo alarmante debido a la destrucción de bosques, la caza ilegal, la contaminación y el cambio climático, Si no tomamos medidas inmediatas, podríamos perder para siempre especies únicas e irremplazables, esenciales para el equilibrio natural y parte fundamental de nuestra herencia.

Solución

Este proyecto no solo revitaliza el turismo ecológico, sino que también proporciona una herramienta valiosa para la conservación y monitoreo de especies en peligro en Venezuela. Al combinar la tecnología de IA con una interfaz interactiva, se generan beneficios económicos y ambientales, ayudando a un sector debilitado por la situacion actual del pais y que fue agraviado por la pandemia, dejandolos sin ingresos y trabajadores, en consecuencia muchas personas quedaron desempleadas por lo que promoveremos
un turismo sostenible y respetuoso con la biodiversidad.

Funcionamiento:

 El monitoreo y seguimientos de la fauna silvestre atravez de la clasificacion y registros de los usuarios adentro de zonas de preservacion natural para darle a los trabajadores o turistas informacion en su celular enfocada a la fauna que les rodea y cuales son los ultimos lugares en los que se percibieron ejemplares alrededor de ellos.

 Para ejercutar el proyecto:

  1. Habre el libro de jupyter "proyecto" en colab.
  2. Descarga el modelo que estara en un enlace a mi drive "clasificador_sierra_nevada_v1.h5". Sube el modelo a tu drive.
  3. Descarga el archivo app25_SN.py y subelo a tu drive.
  4. En el libro de "proyecto" ejecuta desde la parte que esta debajo de la matriz de confusion del modelo, donde tendras que instalar en tu colab lo necesario para ejecutar el archivo.
![image](https://github.com/user-attachments/assets/0914c66d-dcdb-4440-9c14-af0ba854967a)
  5. ejecuta las demas celdas de codigo para que tengas lo necesario para poder habrir el servidor y ejecutar la pagina.
  6. El codigo final se mantendra ejecutando y cuando lo cierres de cerrara la pagina.
![image](https://github.com/user-attachments/assets/00c1e132-6e3b-42de-b25e-9084bcaa3d5e)
  7. Ingresa al link que te aparece en el codigo penultimo para ingresar a la pagina.
![image](https://github.com/user-attachments/assets/5c3b899c-c00c-4b51-96c9-fc268c75b888)


  MODELO:

Nuestro modelo entrenado con una base de datos, elegida cuidadosamente con caracteristicas especificas de animales en peligro de extincion, enfoncandonos en la fauna venezolana especificamente en el parque nacional Sierre Nevada por el momento(de encontrarse imagenes de otros animales se podria realizar una futura actualizacion). 
 Entrenado con: aproximadamente 200 imagenes por categoria.
 ![image](https://github.com/user-attachments/assets/687fb79d-643b-4c5b-92c3-fb7215fd2019)
 
 Lista de categorias:
    'Chiguire',                # 0
    'Coati Andino',            # 1
    'Condor',                  # 2
    'Conejo del paramo',       # 3
    'Jaguar',                  # 4
    'Jicotea',                 # 5
    'La curraca',              # 6
    'La lapa',                 # 7
    'Leopardo andino',         # 8
    'Mono araña',             # 9
    'Mono nocturno',           # 10
    'Oso andino',              # 11
    'Oso hormiguero gigante',  # 12
    'Pato de torrente',        # 13
    'Paují de yelmo',         # 14
    'Pava andina',             # 15
    'Puma',                    # 16
    'Tonina',                  # 17
    'Tortuga carey',           # 18
    'Venado andino',           # 19

    
 RESULTADOS:
 Obtuvimos los siguientes resultados con la aplicacion del modelo:
![image](https://github.com/user-attachments/assets/bbc50160-ecd4-4ea8-a5da-7d654a675983)

medidas de presicion:
![image](https://github.com/user-attachments/assets/116143de-383e-4d98-a959-0827c309a3f9)

  
 
**Tecnologias utilizadas**
TensorFlow/Keras, Streamlit


modelo de aprendizaje profundo basado en VGG16 para clasificación de imágenes.

Integrantes proyecto:
Trino Alejandro Carrisales Colmenares ##trinitocarrizo365@gmail.com

Eliezer Josué Ballestero Silva ##eliezerjosue26@gmail.com
Ivan Antonio lesmes ceballo ##ivanlesmes10@gmail.com

Sergio Andres De Los Santos Bonive ##sergiodelossantos5d@gmail.com
Jobciel Gabdiel Mendoza Cordero ##jobcielmendozacordero@gmail.com
