import os
import re
import time
import datetime
import math

rootFileFolder = "C:\\Users\\XSSal\\Desktop\\python_Serial_Number_finder\\Mi_Gran_Directorio"
nfiles = 0

def filter_text(text, _f):
    global nfiles    
    pattern = r'N\w{3}-\d{5}'
    find = re.search(pattern, text)
    if find != None:
        print(f'{_f} \t {find.group()}')
        nfiles += 1 

def read_file(ruta, _f):
    _file = open(ruta, "r")
    text = _file.read()
    filter_text(text, _f)
    
def read_folder():
    for _folder, _subfolder, _file in os.walk(rootFileFolder):
        for _f in _file:
            ruta = _folder + "\\" + _f
            read_file(ruta, _f)
            
def main():
    start = time.time()
    print('-' * 20)
    print(f'Fecha de búsqueda: {datetime.date.today()}')
    print(f'ARCHIVO \t SERIAL')
    read_folder()
    print(f'\r')
    print(f'Archivos encontrados: {nfiles}')
    end = time.time()
    print(f'Tiempo de búsqueda: {math.ceil(end - start)} segundos')
    
    print('-' * 20)
    
    
main()