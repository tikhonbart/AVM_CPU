import zipfile
import shutil
import xml.etree.ElementTree as ET
import pyon
import pyonr
import json

'''Константы'''
ARR = ['ModbusikMasterTCP','ModbusSlaveRTU', 'ModbusSlaveTCP', 'ModbusikMasterRTU', 'IEC-60870-5-104-Slave','IEC-60870-5-104-Master-#2','IEC-60870-5-104-Master']  # Список необходимых элементов

'''Функция, производящая распаковку Gack-файла'''
def unpack_zip(file_path, output_dir):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)



def read_GACSECTOR(root, result):
    for group1 in root.findall('GACSECTOR'):
            for group2 in group1:
                '''Ищем root'''
                if len(group2.attrib) > 0 and group2.attrib['name'] == 'root':
                     '''Проходим по сегменту Blocks'''
                     for group3 in group2.findall('Blocks'):
                        for group4 in group3:
                            '''Ищем необходимые элементы, записанные в константе'''
                            if len(group4.attrib) > 0 and group4.attrib['type'] in ARR:
                                '''Формируем результат'''
                                gr5 = {}
                                for group5 in group4:
                                    #print(group5.attrib)
                                    if group5.findall('Struct'):
                                        for group6 in group5.findall('Struct'):
                                            for group7 in group6:
                                                #print(group7.attrib)
                                                gr5[group7.get('name')] = group7.get('val')

                                    gr5[group5.get('name')] = group5.get('val')
                                    result1 = {}
                                    result1[group4.attrib['tag']] = gr5
                                    #print(result1)
                                    if result1 not in result[group4.attrib['type']]:
                                        result[group4.attrib['type']].append(result1)
                                    # result[group4.attrib['tag']] = gr5
                
                '''Ищем BS_AG'''
                if len(group2.attrib) > 0 and group2.attrib['name'] == 'BS_AG':
                    '''Проходим по сегменту Blocks'''
                    for group3 in group2.findall('Blocks'):
                        for group4 in group3:
                            '''Ищем необходимые элементы, записанные в константе'''
                            if len(group4.attrib) > 0 and group4.attrib['type'] in ARR:
                                '''Формируем результат'''
                                gr5 = {}
                                for group5 in group4:
                                    #print(group5.attrib)
                                    if group5.findall('Struct'):
                                        for group6 in group5.findall('Struct'):
                                            for group7 in group6:
                                                #print(group7.attrib)
                                                gr5[group7.get('name')] = group7.get('val')

                                    gr5[group5.get('name')] = group5.get('val')
                                    result1 = {}
                                    result1[group4.attrib['tag']] = gr5
                                    #print(result1)
                                    if result1 not in result[group4.attrib['type']]:
                                        result[group4.attrib['type']].append(result1)
                                    # result[group4.attrib['tag']] = gr5

    
    return result
def read_SHELLSECTOR(path):
    pass

def read_GackLog(path):
    pass



'''Функция считывающая XML файл'''
def read_xml(path):
    result = {'ModbusikMasterTCP':[],'ModbusSlaveRTU':[], 'ModbusSlaveTCP':[], 'ModbusikMasterRTU':[], 'IEC-60870-5-104-Slave':[],'IEC-60870-5-104-Master-#2':[],'IEC-60870-5-104-Master':[]}
    # result = {}
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        '''Проходим по сегменту GACSECTOR'''
        result = read_GACSECTOR(root, result)
        return(result) 
    except BaseException:
        print("Возникла ошибка при чтении")


def unzip_and_parse():
    # Пример использования

    # Указываем пути до файла и путь до папки для резудьтата
    file_path = 'C:/Users/igor_/Sonica-shared/dtc-test#2.Gack'
    output_dir = 'res'

    #Вызываем необходимые функции для парсера
    unpack_zip(file_path, output_dir)
    parsing = read_xml('res/xsystem.xml')

    '''Сохраняем в формате PYON'''
    with open('res/result.pyon', "w", encoding="utf-8") as file:
        json.dump(parsing, file,indent=4)
        

    '''Сохраняем в формате JSON'''
    fileJSON = 'res/result.json'
    with open('res/result.json', "w", encoding="utf-8") as file1:
        json.dump(parsing, file1,indent=4)
