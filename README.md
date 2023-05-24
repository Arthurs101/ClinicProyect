# ClinicProyect2
Proyecto que es un sistema para gestión de centros de salud
# Tecnología empleadas:
- Supabase: Backend
- Python Flask: Backend-front end
- SQLAlchemy
- html
- css

# Comandos
Instalar todas las dependencias del proyecto , se encuentran en el requierements.txt
````sh
pip install -r requirements.txt
````
Ejecutar la app en localhost:
````sh
flask run
````
con esto en la terminal sale el url localhost a ingresar

# Estructura de Folders del proyecto: 

> ## ClinicProyect
>
>>  ## src
>> 
>>> ### static
>>> 
>>>> #### css
>>>>> auth-css
>>>>>> dashboard.css
>>>>>> 
>>>>>> establecimiento.css
>>>>>> 
>>>>>> global.css
>>>>>> 
>>>> #### img
>>>> 
>>>> Aqui se almacenan todas las imagenes requeridas
>>> ### templates
>>> 
>>>> #### auth
>>>>
>>>>>auth.html
>>>>>
>>>>>main.html
>>>>>
>>>>>register.html
>>>>>
>>>> #### dashboard
>>>>
>>>>>dashboard.html
>>>>>        
>>>>establecimiento
>>>>
>>>>>agregarInv.html
>>>>>
>>>>>establecimiento.html 
>>>>>  
>>>> #### inventario
>>>>
>>>>>inventario.html  
>>>>>
>>>> #### medicamentos
>>>>
>>>>>AddHistorial.html
>>>>>
>>>>>medicamento.html
>>>>>
>>>> #### pacientes
>>>>
>>>>>AddPaciente.html
>>>>>
>>>>>paciente-individual.html
>>>>>
>>>>>paciente.html
>>>>>
>>>> base.html
>>>>
>>> app.py
>>> 
>>> config.py
>>>
>>> models.py (deprecated)
>>>
>> .gitattributes
>> .gitignore
>> Procfile
>> README.md
>> requirements.txt
