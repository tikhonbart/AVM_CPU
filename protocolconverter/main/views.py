from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView

from main.forms import *
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import IEC_60870_5_104_Master, IEC_60870_5_104_Slave, ModbusikMasterTCP, ModbusikMasterRTU, ModbusSlaveTCP, \
    ModbusSlaveRTU
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

# запись из xml-файла в базу данных
def write_into_db(path):
    json = read_xml(path)
    ModbusikMasterTCP_arr = json['ModbusikMasterTCP']
    ModbusSlaveTCP_arr = json['ModbusSlaveTCP']
    IEC_60870_5_104_Slave_arr = json['IEC-60870-5-104-Slave']
    IEC_60870_5_104_Master_2_arr = json['IEC-60870-5-104-Master-#2']
    IEC_60870_5_104_Master_arr = json['IEC-60870-5-104-Master']
    ModbusikMasterRTU_arr = json['ModbusikMasterRTU']
    ModbusSlaveRTU_arr = json['ModbusSlaveRTU']
    print('here')
    for item in ModbusSlaveRTU_arr:
       for key,val in item.items():
           val['Name_ID'] = key
           ModbusSlaveRTU.objects.create(**val)
    for item in ModbusikMasterRTU_arr:
        for key,val in item.items():
            val['Name_ID'] = key
            #print(val)
            ModbusikMasterRTU.objects.create(**val)
    for item in IEC_60870_5_104_Master_arr:
        for key,val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Master.objects.create(**val)
    for item in IEC_60870_5_104_Master_2_arr:
        for key,val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Master.objects.create(**val)
    for item in IEC_60870_5_104_Slave_arr:
        for key,val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Slave.objects.create(**val)
    for item in ModbusSlaveTCP_arr:
        for key,val in item.items():
            val['Name_ID'] = key
            ModbusSlaveTCP.objects.create(**val)
    for item in ModbusikMasterTCP_arr:
        for key,val in item.items():
            ModbusikMasterTCP.objects.create(**val)


'''Методы для получения всех элементов из базы данных'''

class IEC_60870_5_104_Master_View(ListView):
    model = IEC_60870_5_104_Master
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'

class IEC_60870_5_104_Slave_View(ListView):
    model = IEC_60870_5_104_Slave
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'


class ModbusikMasterRTU_View(ListView):
    model = ModbusikMasterRTU
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'


class ModbusSlaveRTU_View(ListView):
    model = ModbusSlaveRTU
    #queryset = ModbusSlaveRTU.Name_ID
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'


class ModbusikMasterTCP_View(ListView):
    model = ModbusikMasterTCP
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'


class ModbusSlaveTCP_View(ListView):
    model = ModbusSlaveTCP
    template_name = 'html/getFromDB.html'
    context_object_name = 'objects'


@api_view(['POST'])
def insert_IEC_60870_5_104_Master(request):
    if request.method == 'POST':
        print('post')
        serializer = IEC_60870_5_104_Master_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_IEC_60870_5_104_Slave(request):
    if request.method == 'POST':
        print('post')
        serializer = IEC_60870_5_104_Slave_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_ModbusikMasterTCP(request):
    if request.method == 'POST':
        print('post')
        serializer = ModbusikMasterTCP_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_ModbusikMasterRTU(request, pk):
    if request.method == 'POST':
        print('post')
        serializer = ModbusikMasterRTU_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_ModbusSlaveTCP(request, pk):
    if request.method == 'POST':
        print('post')
        serializer = ModbusSlaveTCP_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_ModbusSlaveRTU(request, pk):
    if request.method == 'POST':
        print('post')
        serializer = ModbusSlaveRTU_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''Удаление всех данных из базы данных'''
@api_view(['DELETE'])
def delete_db(request):
    IEC_60870_5_104_Master.objects.all().delete(),
    IEC_60870_5_104_Slave.objects.all().delete(),
    ModbusikMasterTCP.objects.all().delete()
    ModbusikMasterRTU.objects.all().delete()
    ModbusSlaveTCP.objects.all().delete()
    ModbusSlaveRTU.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

'''Удаление определённых элементов из базы данных'''
@api_view(['DELETE'])
def delete_IEC_60870_5_104_Master(request):
    IEC_60870_5_104_Master.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_IEC_60870_5_104_Slave(request):
    IEC_60870_5_104_Slave.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_ModbusikMasterTCP(request):
    ModbusikMasterTCP.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_ModbusikMasterRTU(request):
    ModbusikMasterRTU.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_ModbusSlaveTCP(request):
    ModbusSlaveTCP.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def delete_ModbusSlaveRTU(request):
    ModbusSlaveRTU.objects.all().delete()
    return Response(status=status.HTTP_202_ACCEPTED)

'''Добавление в базу данных из json-файла'''
@api_view(['UPDATE'])
def add_from_json(request):
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
                write_into_db(list(path.cleaned_data.values())[0])
                mypath = main1(list(path.cleaned_data.values())[0])
                #print(mypath)
                query_param = "&".join(f"mypath={item}" for item in mypath)
                url = reverse('blockview') + f"?{query_param}"
                #print(url)

                return HttpResponseRedirect(url)
            except Exception:
                messages.error(request, "неверный путь!")


    else:
        path = GackPath()
    return render(request, "html/index.html", {"path": path})


''' обработка gack файла '''

'''Константы'''
ARR = ['ModbusikMasterTCP', 'ModbusSlaveRTU', 'ModbusSlaveTCP', 'ModbusikMasterRTU', 'IEC-60870-5-104-Slave',
       'IEC-60870-5-104-Master-#2', 'IEC-60870-5-104-Master']


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
                                # print(group5.attrib)
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            # print(group7.attrib)
                                            cut1 = group7.get('name')
                                            cut1= cut1.replace(" ", "_")
                                            gr5[cut1] = group7.get('val')
                                cut = group5.get('name')
                                cut = cut.replace(" ","_")
                                #print(cut)
                                gr5[cut] = group5.get('val')
                                result1 = {}
                                result1[group4.attrib['tag']] = gr5
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
                                # print(group5.attrib)
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            cut1 = group7.get('name')
                                            cut1 = cut1.replace(" ", "_")
                                            gr5[cut1] = group7.get('val')

                                cut = group5.get('name')
                                cut = cut.replace(" ", "_")
                                #print(cut)
                                gr5[cut] = group5.get('val')
                                result1 = {}
                                result1[group4.attrib['tag']] = gr5
                                if result1 not in result[group4.attrib['type']]:
                                    result[group4.attrib['type']].append(result1)
                                # result[group4.attrib['tag']] = gr5

    return result


'''Функция считывающая XML файл'''


def read_xml(path):
    result = {'ModbusikMasterTCP': [], 'ModbusSlaveRTU': [], 'ModbusSlaveTCP': [], 'ModbusikMasterRTU': [],
              'IEC-60870-5-104-Slave': [], 'IEC-60870-5-104-Master-#2': [], 'IEC-60870-5-104-Master': []}
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        '''Проходим по сегменту GACSECTOR'''
        result = read_GACSECTOR(root, result)
        return (result)
    except BaseException:
        print("Возникла ошибка при чтении")


def main1(path):
    parsing = read_xml(path)

    # keys_list = list(parsing.keys())
    # values_list = list(parsing.values())
    #
    # pairs = list(zip(keys_list, values_list))
    #
    # dannlist = []
    # for i in pairs:
    #     dannlist.append(i[0])
    #     keys_list = list(i[1].keys())
    #     values_list = list(i[1].values())
    #     pairs = list(zip(keys_list, values_list))
    #     for j in pairs:
    #         dannlist.append(list(j))
    return parsing


"""
def categories(request):
    return HttpResponse("<h1>fasdfasdf</h1>")
"""


# обработчик окна с выводом информации из gack файла
def viewBlocks(request):
    # listInfo = request.GET.getlist('mypath', None)
    # if listInfo is None:
    #     # Обработка, если значение mypath не найдено
    #     pass
    # else:
    #     # список информации о блоках
    #     return render(request, "html/mainpage.html", {"list": listInfo})

    listInfo = request.GET.getlist('mypath', None)
    if listInfo is None:
        # Обработка, если значение mypath не найдено
        pass
    else:
        # objects_massive.append(IEC_60870_5_104_Master.objects.all())

        IEC_Master = IEC_60870_5_104_Master.objects.all()
        IEC_Slave = IEC_60870_5_104_Slave.objects.all()
        ModSlaveRTU = ModbusSlaveRTU.objects.all()
        ModSlaveTCP = ModbusSlaveTCP.objects.all()
        ModMasterRTU = ModbusikMasterRTU.objects.all()
        ModMasterTCP = ModbusikMasterTCP.objects.all()
        if request.method == "POST":

            print(IEC_Master)
            form = IEC_Master_Form(request.POST, instance=IEC_Master[0])
            try:
                form.save()
                return redirect("blockview")
            except:
                form.add_error(None, 'ошибка сохранения')
        else:
            print(IEC_Master)
            form1 = []
            form2 = []
            form3 = []
            form4 = []
            form5 = []
            form6 = []

            for i in range(len(IEC_Master)):
                form1.append(IEC_Master_Form(instance=IEC_Master[i]))

            for i in range(len(IEC_Slave)):
                form2.append(IEC_Slave_Form(instance=IEC_Slave[i]))

            for i in range(len(ModSlaveRTU)):
                form3.append(ModbusSlaveRTU_Form(instance=ModSlaveRTU[i]))

            for i in range(len(ModSlaveTCP)):
                form4.append(ModbusSlaveTCP_Form(instance=ModSlaveTCP[i]))

            for i in range(len(ModMasterRTU)):
                form5.append(ModbusikMasterRTU_Form(instance=ModMasterRTU[i]))

            for i in range(len(ModMasterTCP)):
                form6.append(ModbusikMasterTCP_Form(instance=ModMasterTCP[i]))

        context = {
            "list": listInfo,
            "form1": form1,
            "form2": form2,
            "form3": form3,
            "form4": form4,
            "form5": form5,
            "form6": form6
        }
        # список информации о блоках
        return render(request, "html/mainpage.html", context)
