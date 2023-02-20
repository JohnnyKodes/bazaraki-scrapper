from Data.carData import CarData
from Data.Constants import BAZARAKI_URL, NO_DATA_FOUND
from bs4 import BeautifulSoup
import re

def extractYear(s) -> str:
    match = re.search(r'\b\d{4}\b', s)
    year = match.group() if match is not None else NO_DATA_FOUND
    return year
    
def getTotalPageCount(response):
    return int(BeautifulSoup(response.content, "html.parser").find('ul', {'class': 'number-list'}).find_all('li')[-1].get_text())    
    
def getCarData(item) -> CarData:
    brand = NO_DATA_FOUND
    type = NO_DATA_FOUND
    breadCrumbs = item.find('div', {'class' : 'announcement-block__breadcrumbs'}).find_all('span')
    if breadCrumbs is not None:
        brand = breadCrumbs[0].get_text().strip()
        type = breadCrumbs[1].get_text().strip()
     
    price = item.find("meta", {"itemprop": "price"}).get("content")
    year = extractYear(item.find("meta", attrs={"itemprop": "name"}).get("content").strip())
    
    fuelType = NO_DATA_FOUND
    gearBox = NO_DATA_FOUND
    mileage = NO_DATA_FOUND
    carDescription = item.find('div', {'class': 'announcement-block__description'})
    if carDescription:
        carDescription = carDescription.get_text().strip().split(',')
        mileage = carDescription[0].strip()
        gearBox = carDescription[1].strip()
        fuelType = carDescription[2].strip()
        
    url = BAZARAKI_URL + item.find('a').get('href')

    return CarData(
        brand=brand,
        type=type,
        price=price,
        year=year,
        fuelType=fuelType,
        gearBox=gearBox,
        mileage=mileage,
        url=url
    )