from bs4 import BeautifulSoup
import requests as rq

#colores para la terminal: 
ROJO = '\033[31m'
VERDE = '\033[32m'
AZUL = '\033[34m'
NEGRITA = '\033[1m'
RESET = '\033[0m'

peliWeb = rq.get("https://pelispp.com/inicio/")
soup = BeautifulSoup(peliWeb.text,'html.parser')

#funcion de ordenamiento de listas
def ordenar(list1,list2,list3):
    listG = []
    count = 0
    for i in list1:
        listG.append([i])
    for i in list2:
        listG[count].append(i)
        count += 1
    count = 0 #reseteando conta
    for i in list3:
        listG[count].append(i)
        count += 1

    return listG

#funcion de calificacion 
def calificacion(href):
    listCalification = []
    for n in href:
        soupFunc = BeautifulSoup(rq.get(n).text,'html.parser')
        print(f'{ROJO}{n}{RESET}',f"\n{VERDE}[+]{RESET}{NEGRITA}scraping correcto{RESET}\n")
        eCalification = soupFunc.find_all('strong',string="IMDb:")
        for x in eCalification:
            listCalification.append(x.parent.text.strip())
    return listCalification

#primera pagina
#retorna lista de lista con 3 elementos o matriz "3xn" n: numeron de peliculas en la lista top 
def topPelisUno():
    #seleccionanddo el contenedor de las peliculas
    boxListTop = soup.find('div',class_='list-movie')
    
    #creando sopa dos
    listLink = str(boxListTop)
    soup2 = BeautifulSoup(listLink,'html.parser')
    
    #lista de nombre
    listName = soup2.select('div.col>div.card>a>div.card-body>h2')
    listTag = []
    for tag in listName:
        listTag.append(tag.text)

    #lista de href
    listAnclas = soup2.select('div.col>div.card>a')
    listHref = []
    for link in listAnclas:
        listHref.append(f'https://pelispp.com{link.attrs['href']}')

    cList = calificacion(listHref)
    
    #aplicando funcion de ord
    topPelis = ordenar(listTag,listHref,cList)

    return topPelis

p = topPelisUno()

count = 0
for i in p: 
    print(f"{VERDE}[+]{RESET}nombre: ",p[count][0])
    print(f"{VERDE}[+]{RESET}link: ",p[count][1])
    print(f"{VERDE}[+]{RESET}calificacion: ",p[count][2],f"\n{"·"*30}\n")

    count += 1

#for i in p:
#    print(f"[+]nombre: {p[0]}")
#    print(f"[+]link: {p[1]}")
#    print(f"[+]calificacion: {p[2]}")
