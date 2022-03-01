# smartphone_recommendations
Web scrapping software for collecting smartphones prices and characteristics, providing some recommendations based on user necessities.

**Functionality**

This project is in progress. It aims to help people to find the smartphone they wants at the lowest prices. It works by scrapping prices from different vendors web pages, and store them into a csv file named *checkpoint.csv*. Currently it is limited to local vendors such as Claro, Movistar, Tigo and Ktronix (Colombia) 

This repo also contains the service code. This service gives you recommendations based on what you send as parameter, similarly to a pretty basic browser. You can execute it by just running the docker container.

**ALERT:** You need to restore the Postgres database using the *dump-smartphones...* file inside the *db* folder. Also remember to change the environment values in the dockerfile for connecting to the database.

```
docker build -t smartphones .
```

```
docker run smartphone -p 80:80 smartphones
```
and then access to 

http://127.0.0.1/docs

![Api view to run queries](documentation_files/api_view.PNG?raw=true "Api view")

Inside the **GET** dropdown you can see the query options

![Api view to run queries](documentation_files/query_options.PNG?raw=true "Api view")

Is required to send at least one parameter, that way the system can provide a generic recommendation. By sending more parameters, the system will filter them by and return a more specific set recommendations.

Due to the table design, you do not need to be too specific or precise, e.g., If you send *'note 10'* in the value param, the system will search all the models matching it.

```json
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

The system always will return a list of JSON objects, in which every object is a Device. And every device has its own information, i.e., *model*, *vendor*, *brand*, *ram*, *rom*, *last_seen* and *price*.

The results are ordered by price. 

This way you can compare prices from different vendors. 

**Demo**

From today, the palindromic day 22/02/2022, I deployed a demo API on

http://ec2-54-226-113-231.compute-1.amazonaws.com/docs

Please, don't run a lot of requests, it's running on AWS free tier and I'm unemployed :( 

To see what is coming next, check the issues section. 
If you want to contribute, just do a Pull Request. 

**Update** 
I had to block all the ips to accessing the link above because I was getting weird requests,
really boys? Nice try using a VPN, but only the people from you country uses those characteres. 
This is for you, 125.42.224.122, 185.254.196.218
At least, if you want to test your pentesting skills on my service, let me know. 
