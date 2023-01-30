import requests
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

file = Path('faixa_cep') # Folder o store the results
file.mkdir(exist_ok=True) # If the folder doesn't exist, this line will create it
qtd_row = 50 # max number of row per requsition
uf_list = ['MG','ES'] # Searched UF, add more at will
data = [] # initializing the empty variable to store the text from HTML


def req_faixa_cep(uf, pagini, pagfim):
    '''This function will post and return the HTML of the desired page'''
    dataload = {'UF': uf, 'qtd_row': qtd_row, 'pagini': pagini, 'pagfim': pagfim}
    try:
        r = requests.post('https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm', data=dataload)
    except requests.exceptions.RequestException as e:
        print('An error has occurred. Please try again later.')
        raise SystemExit(e)

    return r


def num_max_row(uf, start_row, end_row):
    '''Count the max number of registries'''
    page = req_faixa_cep(uf, start_row, end_row)
    soup = BeautifulSoup(page.text, 'html.parser')
    num_max_row = soup.find(string=re.compile('1 a 50 de '))
    if (num_max_row):
        words = num_max_row.strip().split()
        return words[-1]
    else:
        return 0


def get_cep_list(page):
    '''Parse the HTML for all the info for he CEP, and append in a dict list wih their key:value'''
    global id
    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        content = soup.find('div', class_='ctrlcontent')

        table_rows = content.find_all('tr')

        for table_row in table_rows:
            cells = table_row.findAll('td')
            info = {}
            info['id'] = id

            aux = 0
            for cell in cells:
                if (aux == 0):
                    info['Localidade'] = cell.text
                elif (aux == 1):
                    info['Faixa de CEP'] = cell.text
                elif (aux == 2):
                    info['Situação'] = cell.text
                elif (aux == 3):
                    info['Tipo de faixa'] = cell.text
                else:
                    info[aux] = cell.text
                aux += 1

            if (len(info) > 3):
                data.append(info)
                id += 1
            else:
                pass
    except AttributeError:
        return ['Empty list, check the URL, or the desired UF and try again']
    return data


# loop to get all indexes of the uf_list variable
for uf in uf_list:
    id = 0
    start_row = 1
    end_row = 50
    max_row = int(num_max_row(uf, start_row, end_row))
    page = req_faixa_cep(uf, start_row, end_row)

    get_cep_list(page)

    # loop to get all the pages
    while end_row <= max_row:
        start_row = end_row + 1
        end_row += qtd_row
        page = req_faixa_cep(uf, start_row, end_row)

        get_cep_list(page)

    while end_row <= max_row:
        start_row = end_row + 1
        end_row += qtd_row
        page = req_faixa_cep(uf, start_row, end_row)

        get_cep_list(page)

    # creating the json file
    jsonpath = file / ('faixas_de_cep_' + uf + '.jsonl')

    # export the content stored in data variable to the json file
    with open(jsonpath, 'w', encoding='utf8') as fp:
        for item in data:
            fp.write(json.dumps(item, ensure_ascii=False) + '\n')
