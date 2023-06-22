from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from main.forms import *
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *


# метод для обработки запросов
def write_into_db(request):
    pass


# обработка неправильной адресации
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# главная страница
def index(request):
    if request.method == "POST":
        path = GackPath(request.POST)
        if path.is_valid():
            try:
                mypath = main(list(path.cleaned_data.values())[0])
                query_param = "&".join(f"mypath={item}" for item in mypath)
                url = reverse('blockview') + f"?{query_param}"
                return HttpResponseRedirect(url)
            except Exception:
                messages.error(request, "неверный путь!")
    else:
        path = GackPath()
    return render(request, "main/index.html", {"path": path})


''' обработка gack файла '''

'''Константы'''
ARR = ['ModbusSlaveRTU', 'ModbusSlaveTCP', 'ModbusikMasterRTU', 'ModbusikMasterTCP',
       'FunBetta', 'SQLiteConnection', 'aPeriodicalTable']  # Список необходимых элементов


def read_GACSECTOR(root, result):
    for group1 in root.findall('GACSECTOR'):
        for group2 in group1:
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
                                # print(group5.attrib)
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            # print(group7.attrib)
                                            gr5[group7.get('name')] = group7.get('val')
                                gr5[group5.get('name')] = group5.get('val')
                                result[group4.attrib['tag']] = gr5
    return result


'''Функция считывающая XML файл'''


def read_xml(path):
    result = {}
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        '''Проходим по сегменту GACSECTOR'''
        result = read_GACSECTOR(root, result)
        return (result)
    except BaseException:
        print("Возникла ошибка при чтении")


def main(path):
    parsing = read_xml(path)

    keys_list = list(parsing.keys())
    values_list = list(parsing.values())

    pairs = list(zip(keys_list, values_list))

    dannlist = []
    for i in pairs:
        dannlist.append(i[0])
        keys_list = list(i[1].keys())
        values_list = list(i[1].values())
        pairs = list(zip(keys_list, values_list))
        for j in pairs:
            dannlist.append(list(j))
    return dannlist


"""
def categories(request):
    return HttpResponse("<h1>fasdfasdf</h1>")
"""


# обработчик окна с выводом информации из gack файла
def viewBlocks(request):
    listInfo = request.GET.getlist('mypath', None)
    if listInfo is None:
        # Обработка, если значение mypath не найдено
        pass
    else:
        object_list = [ModbusSlaveTCP.objects.first(), ModbusikMasterTCP.objects.first(),
                       ModbusSlaveRTU.objects.first(), ModbusikMasterRTU.objects.first(),
                       IEC_60870_5_104_Slave.objects.first(), IEC_60870_5_104_Master.objects.first()]

        object_list = [x for x in object_list if x is not None]

        context = {
            "list": listInfo,
            "object_list": object_list
        }
        # список информации о блоках
        return render(request, "main/mainpage.html", context)


def edit_my_model(request, nameModel):
    object_list = [ModbusSlaveTCP.objects.first(), ModbusikMasterTCP.objects.first(),
                   ModbusSlaveRTU.objects.first(), ModbusikMasterRTU.objects.first(),
                   IEC_60870_5_104_Slave.objects.first(), IEC_60870_5_104_Master.objects.first()]

    object_list = [x for x in object_list if x is not None]

    model_form_mapping = {
        "IEC_60870_5_104_Master": (IEC_Master_Form, IEC_60870_5_104_Master),
        "IEC_60870_5_104_Slave": (IEC_Slave_Form, IEC_60870_5_104_Slave),
        "ModbusikMasterRTU": (ModbusikMasterRTU_Form, ModbusikMasterRTU),
        "ModbusSlaveRTU": (ModbusSlaveRTU_Form, ModbusSlaveRTU),
        "ModbusikMasterTCP": (ModbusikMasterTCP_Form, ModbusikMasterTCP),
        "ModbusSlaveTCP": (ModbusSlaveTCP_Form, ModbusSlaveTCP),
    }

    if nameModel in model_form_mapping:
        form_class, model_class = model_form_mapping[nameModel]
        current_model = model_class.objects.first()

        if request.method == "POST":
            form = form_class(request.POST, instance=current_model)
            try:
                form.save()
                return redirect("blockview")
            except:
                form.add_error(None, 'ошибка сохранения')
        else:
            form = form_class(instance=current_model)
    else:
        form = None

    context = {
        "form": form,
        "object_list": object_list
    }
    return render(request, 'main/mainpage.html', context)
