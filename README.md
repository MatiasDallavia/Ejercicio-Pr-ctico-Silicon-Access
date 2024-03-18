<!-- Description -->

## Descripción

Servicio backend para el monitoréo de la entrada y salida de vehiculos dentro de una urbanización privada

<hr />

### 🔧 Tecnologías usadas:

- <img alt='Django' src='https://img.shields.io/badge/Django-100000?style=for-the-badge&logo=Django&logoColor=white&labelColor=092e20&color=D9E7E1'/>

- <img alt='Postgresql' src='https://img.shields.io/badge/PostgresQL-100000?style=for-the-badge&logo=Postgresql&logoColor=white&labelColor=0064a5&color=D9E7E1'/>
- <img alt='Docker' src='https://img.shields.io/badge/Docker-100000?style=for-the-badge&logo=Docker&logoColor=white&labelColor=0db7ed&color=D9E7E1'/>

<hr />

### 💻Requisitos

- [docker-compose](https://docs.docker.com/get-docker/)

<hr />

### 🚀 Instalación

1. Clonar el ropositorio
   ```sh
   git clone https://github.com/MatiasDallavia/Ejercicio-Practico-Silicon-Access.git
   ```
2. Construir y correr los contendores

   ```sh
   docker-compose up --build -d
   ```

<hr>

### API Endopoints

| Endpoint                                        | Método HTTP    | Método CRUD         | Resultado                                           |
| ----------------------------------------------- | -------------- | ------------------ | -------------------------------------------------- |
| `users`                                         | POST           | CREATE             | Crea un nuevo usuario                              |
| `users/auth-token/`                             | POST           | CREATE             | Crea el token de autenticación                     |
| `areas/`                                        | POST/GET       | CREATE/READ        | Crea o recupera todas las áreas de un usuario      |
| `areas/<int:area_pk>/`                          | PUT/GET/DELETE | UPDATE/READ/DELETE | Actualiza, recupera o borra un área específica     |
| `areas/<int:area_pk>/vehicles/`                 | POST/GET       | CREATE/READ        | Crea o recupera todos los vehículos de un área     |
| `areas/<int:area_pk>/vehicles/<int:vehicle_pk>` | PUT/GET/DELETE | UPDATE/READ/DELETE | Actualiza, recupera o borra un vehículo específico |

<br/>

La colección de requests se puede encontrar dentro de la carpeta root como:
```
Ejercicio_Práctico_Colleción.postman_collection.json
```

<hr/>

# Autenticacíon


Primero se tiene que crear un usuario en el siguiente endpoint:

```
localhost:8000/api/users
```

Con un payload con esta estructura:

```
{
    "username": "myUsername",
    "password": "myPassword",
    "email": "email@gmail.com",
    "first_name": "first_name",
    "last_name" : "last_name"
}
```

Posteriormente se crea el token de autenticación en:

```
localhost:8000/api/users/auth-token/
```

```
{
    "username": "myUsername",
    "password": "myPassword"
}
```

El token que devuelva habilitará las demás peticiones. Para eso se deberá almacenar en una variable llamada 'authToken' dentro de la colección de Postman:

```
authToken : Token 34227bfbc9e300eaa3da3d3ef52854d37a996332
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
