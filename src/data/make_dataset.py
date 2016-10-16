# -*- coding: utf-8 -*-
import requests
from os import path

def main():
    # Download the data on Connecticut pretrial detention as CSV, save to raw data folder

    url = 'https://data.ct.gov/api/views/b674-jy6w/rows.csv?accessType=DOWNLOAD'

    local_path = path.abspath(path.join(path.dirname(__file__),'..', '..', 'data', 'raw'))
    filename = path.join(local_path, 'detention.csv')

    CT_detention = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(CT_detention.content)

if __name__ == '__main__':
    main()
