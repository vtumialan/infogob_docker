Para iniciar el proyecto debe clonarse, dirigirse a la raiz del mismo y realizar los siguientes pasos, asegurandose tener instalado docker-compose:

Servidor
 - docker-compose build
 - docker-compose up


1.- Endpoint para consultar todas las regiones y sus respectivos urls:

URL: 127.0.0.1:8000/scraping/
Response: 
[
    {
        "description": "CALLAO",
        "token": "yHi2pAH6Bq8=iA",
        "url_regidor": "/regidor/?region=callao&token=yHi2pAH6Bq8=iA"
    },
    {
        "description": "AMAZONAS",
        "token": "bgnkVFt+VRk=nF",
        "url_regidor": "/regidor/?region=amazonas&token=bgnkVFt+VRk=nF"
    },
    {
        "description": "ANCASH",
        "token": "JDCOqBQNWo4=CB",
        "url_regidor": "/regidor/?region=ancash&token=JDCOqBQNWo4=CB"
    },
...
]


2.- Endpoint para consultar Regidor:

URL: 127.0.0.1:8000/regidor/?region=tacna&token=S4kHdJ5t0pI=kJ
Response:
{
    "GOBERNADOR REGIONAL": "JUAN QUISPE TONCONI"
}