from seoanalyzer import analyze
from datetime import date
import json
import csv

# Requisição API SEO / Formatação JSON
output = analyze('https://santander.com.br/', 'https://www.santander.com.br/sitemap.xml')
output_to_json = json.dumps(output)

formated_output = json.loads(output_to_json)
indice_csv = formated_output['pages']

# Abre arquivo CSV para leitura
myFile = open('base.csv', 'a', newline='')

# Criando var a ser lida no CSV
csvwriter = csv.writer(myFile)

# Correndo o Json, e ajustes na base bruta
count = 0
for num, out in enumerate(indice_csv):
    indice_csv[num]['Data'] = date.today()
    indice_csv[num]['url'] = indice_csv[num]['url'].replace('http://www.', 'https://')
    if count == 0:
        header = out.keys()
        #csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(out.values())

myFile.close()

# https://www.python.org/success-stories/python-seo-link-analyzer/