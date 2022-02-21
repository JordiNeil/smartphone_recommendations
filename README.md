# smartphone_recommendations
Web scrapping software for collecting smartphones prices and characteristics and giving some recommendations based on user necessities

**Functionality**

This projects in progress. It aims to help people to find the smartphone they wants at the lowest prices. It works by scrapping prices from different vendors web pages, now it's limited to Claro, Movistar, Tigo and Ktronix (Colombia) and store them into a csv file named *checkpoint.csv*

This repo also contains the service code. This service give you recommendations based on what you send as parameter, similar to a pretty basic browser. You can execute it just by running the docker container.

**ALERT:** You need to restore the Postgres database using the *dump-smartphones...* file inside the *db* folder. Also remember to change the environment values in the dockerfile for connecting to the database.

```
docker build -t smartphones .
```

```
docker run smartphone -p 80:80 smartphones
```
and then access to 

http://127.0.0.1/docs

![Api view to run queries](https://github.com/JordiNeil/smartphone_recommendations/documentation_files/api_view.PNG?raw=true "Api view")

Inside the **GET** dropdown you can see the query options

![Api view to run queries](https://github.com/JordiNeil/smartphone_recommendations/documentation_files/query_options.PNG?raw=true "Api view")

Is required to send at least one parameter, that way the system can give you any recommendation. If you send more parameters, the system will filter by them and return a more specific recommendation.

Due to the design of the table, you do not need to be too specific or precise, for example.

If you send *'note 10'* in the value param, the system is going to search for all the models that match with it.

```
[
  {
    "model": "note 10 5g",
    "vendor": {
      "name": "movistar",
      "web_page": "descubre.movistar.co/celulares/cambia-tu-celular/"
    },
    "ram": null,
    "rom": null,
    "brand": {
      "brand_name": "xiaomi"
    },
    "last_seen": "2022-02-20",
    "price": "1099889"
  },
  {
    "model": "note 10s",
    "vendor": {
      "name": "movistar",
      "web_page": "descubre.movistar.co/celulares/cambia-tu-celular/"
    },
    "ram": null,
    "rom": null,
    "brand": {
      "brand_name": "xiaomi"
    },
    "last_seen": "2022-02-20",
    "price": "1099889"
  },
  {
    "model": " note 10s gris",
    "vendor": {
      "name": "ktronix",
      "web_page": "ktronix.com/celulares/telefonos-celulares"
    },
    "ram": null,
    "rom": 128,
    "brand": {
      "brand_name": "xiaomi"
    },
    "last_seen": "2022-02-20",
    "price": "1099900"
  },
  {
    "model": " note 10s azul",
    "vendor": {
      "name": "ktronix",
      "web_page": "ktronix.com/celulares/telefonos-celulares"
    },
    "ram": null,
    "rom": 128,
    "brand": {
      "brand_name": "xiaomi"
    },
    "last_seen": "2022-02-20",
    "price": "1099900"
  },
  {
    "model": " note 10s gris",
    "vendor": {
      "name": "ktronix",
      "web_page": "ktronix.com/celulares/telefonos-celulares"
    },
    "ram": null,
    "rom": 128,
    "brand": {
      "brand_name": "xiaomi"
    },
    "last_seen": "2022-02-20",
    "price": "1099900"
  }
]
```

The system always will return a list of JSON objects, every object is a Device. And every device has is own information, like *model*, *vendor*, *brand*, *ram*, *rom*, *last_seen* and *price*.

The results are ordered by price. 

This way you can compare prices from different vendors. 

To see what is coming next, check the issues section. 