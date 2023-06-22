# Proyecto Django y Aplicación Flask

Este proyecto consta de una aplicación Django y una aplicación Flask que se comunican entre sí a través de una red de Docker. A continuación, se proporciona una guía para ejecutar y utilizar ambas aplicaciones.

## Ejecución de los contenedores

Para lanzar los contenedores, se debe ejecutar el siguiente comando:

```
docker-compose --env-file django_project/django_project/.env up

```

Aquí se pasan las variables de entorno necesarias para la configuración del proyecto Django.

## Proyecto Django

El proyecto Django incluye 4 modelos: Productos, Clientes, Órdenes y Categorías. Se construyó utilizando Django Rest Framework y se implementó un sistema de autenticación basado en tokens utilizando la biblioteca djoser. La base de datos utilizada es PostgreSQL.

El proyecto Django está disponible en la siguiente dirección: [http://127.0.0.1:8000](http://127.0.0.1:8000/).

La documentación de la API fue generada utilizando drf-yasg y se puede acceder a ella en la siguiente dirección: [http://127.0.0.1:8000/doc/](http://127.0.0.1:8000/doc/).

Para ejecutar las pruebas, se debe utilizar el siguiente comando:

```
python manage.py test --keepdb apps.api

```

## Obtención de token de autenticación

Ya existe un usuario registrado con las siguientes credenciales: username=admin y password=010203.

Para obtener un token de autenticación, se puede utilizar el siguiente comando curl:

```
curl --location '<http://127.0.0.1:8000/auth/token/login>' \\
--header 'Content-Type: application/json' \\
--data '{
    "password": "010203",
    "username": "admin"
}'

```

Esto retornará un token de autenticación en el siguiente formato:

```
{
    "auth_token": "fb4d4c424bf503a4901609055afdb5ceaa8b042a"
}

```

## Endpoints autenticados

Todos los endpoints, excepto el endpoint de `/categories`, requieren autenticación. Para acceder a un endpoint autenticado, se debe incluir el token en los headers de la solicitud.

Por ejemplo, para agregar un nuevo producto, se puede utilizar el siguiente comando curl:

```
curl --location '<http://127.0.0.1:8000/products/>' \\
--header 'Authorization: Token fb4d4c424bf503a4901609055afdb5ceaa8b042a' \\
--header 'Content-Type: application/json' \\
--data '{
  "name": "Vino A",
  "price": 2000,
  "category": 2
}'

```

## Aplicación Flask

La aplicación Flask se conecta al endpoint `/categories` de la aplicación Django utilizando HTTP (circuit break). Para realizar una solicitud GET a dicho endpoint, se utiliza la biblioteca `requests` y se maneja el circuit breaker mediante la biblioteca `circuitbreaker`.
Está disponible en el siguiente enlace http://127.0.0.1:8080

Por ejemplo, para agregar un nueva categoría, se puede utilizar el siguiente comando curl:

```
curl --location 'http://127.0.0.1:8080/categories' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Categoria 102"
}'
```