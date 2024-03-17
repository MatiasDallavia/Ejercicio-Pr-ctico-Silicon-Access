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

### API

| Endpoint                                        | HTTP Method    | CRUD Method             | Devuelve                                            |
| ----------------------------------------------- | -------------- | ----------------------- | --------------------------------------------------- |
| `users`                                         | POST           | CREATE                  | Crea un nuevo usuario                               |
| `users/auth-token/`                             | POST           | CREATE                  | Crea el token de autenticación                      |
| `areas/`                                        | POST/GET       | CREATE/RETRIEVE         | Crea o recupera todas las áreas de un usuario       |
| `areas/<int:area_pk>/`                          | PUT/GET/DELETE | UPDATE/RETRIEVE/DELETES | Actualiza, recupera o borra una área especifica     |
| `areas/<int:area_pk>/vehicles/`                 | POST/GET       | CREATE/RETRIEVE         | Crea o recupera todas los vehiculos de un área      |
| `areas/<int:area_pk>/vehicles/<int:vehicle_pk>` | PUT/GET/DELETE | UPDATE/RETRIEVE/DELETES | Actualiza, recupera o borra una vehiculo especifica |

# Autenticacíon

Primero se tiene que crear un usuario en el siguiente endpoint:

```
localhost:8000/users
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
localhost:8000/users/auth-token/
```

```
{
    "username": "myUsername",
    "password": "myPassword"
}
```

El token que devuelva habilitará el resto de los endpoints. Cada petición deberá tener una cabezera "Authorization" con el token devuelto. Por ejemplo: 


```
Authorization : Token 34227bfbc9e300eaa3da3d3ef52854d37a996332
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>
