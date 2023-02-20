import requests
from bs4 import BeautifulSoup
from Data.dataGetters import getCarData, getTotalPageCount
from ExcelCreator.dataToExcel import serializeToExcelSheet
from Data.Constants import BAZARAKI_URL, CAR_QUERY

pageCount = getTotalPageCount(requests.get(BAZARAKI_URL + CAR_QUERY))
maxPrice = "price_max=20000"
cars = {}

for i in range(1, pageCount + 1): # 2 now just for testing purposes
    response  = requests.get(BAZARAKI_URL + CAR_QUERY + f"?page={i}" + "&" + maxPrice)
    soup = BeautifulSoup(response.content, "html.parser")
    carsList = soup.find_all('li', {'class': 'announcement-container'})

    for item in carsList:
        cardata = getCarData(item)
        
        if cardata.brand not in cars:
            cars[cardata.brand] = []
        
        cars[cardata.brand].append(cardata)

serializeToExcelSheet(cars)
    

print("\nBAZARAKI HAS BEEN SCRAPPED\n")