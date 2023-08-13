import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=preto'

response = requests.get(url) 


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.text
    print(title[9:15])
        
    aux = []
    aux2 = []
    aux3 = []
    aux4 = []
    aux5 = []

    title_divs = soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal')
    for item in title_divs:
        description_name = item.get_text() 
        aux3.append(description_name)


    price_divs = soup.find_all('span', class_='a-price-whole')
    cents_divs = soup.find_all('span', class_='a-price-fraction')
    for price in price_divs:
        description_price = price.get_text()
        aux.append(description_price)
            
    for cent in cents_divs:
        description_cent = cent.get_text()
        aux2.append(description_cent)

    avaliation_divs = soup.find_all('span', 'a-size-base s-underline-text')
    for avaliation in avaliation_divs:
        description_avaliation = avaliation.get_text()
        aux4.append(description_avaliation)

    frete_divs = soup.find_all('span','a-size-base a-color-secondary')
    for frete in frete_divs:
        description_frete = frete.get_text()
        aux5.append(description_frete)


    prices = aux
    all_cents = aux2
    
    all_prices = []
    
    
    for price in prices:
        all_prices.append(price[:-1])
        
        
    full_price = [float(a + '.' + b) for a, b in zip(all_prices, all_cents)]
    
    
    all_prices = full_price[0:40]
    all_products = aux3[0:40]
    all_compras = aux4[0:40]
    all_obs = aux5[0:40]
    
    
    
    
    dataframe = {
        'NomeProduto': all_products,
        'Preco': all_prices,
        'Qtd. Compras': all_compras,
        'Observação': all_obs
    }
    

    df = pd.DataFrame(dataframe)
    
    df.to_excel('output.xlsx', index=True)
    
