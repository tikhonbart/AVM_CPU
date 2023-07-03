import zipfile

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from main.forms import *
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

'''Константы'''
ARR = ['ModbusikMasterTCP', 'ModbusSlaveRTU', 'ModbusSlaveTCP', 'ModbusikMasterRTU', 'IEC-60870-5-104-Slave',
       'IEC-60870-5-104-Master-#2', 'IEC-60870-5-104-Master']  # Список необходимых элементов


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
    IEC_60870_5_104_Master.objects.all().delete()
    IEC_60870_5_104_Slave.objects.all().delete()
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


'''Распаковка gack-файла'''
def unpack_zip(file_path, file_name):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        with zip_ref.open(file_name) as f:
            xml_content = ET.parse(f)

    print(xml_content)
    return xml_content


# запись из xml-файла в базу данных
def write_into_db(path):
    path = path.replace('\\', '/')
    parsing = unpack_zip(path, 'xsystem.xml')
    json = read_xml(parsing)
    ModbusikMasterTCP_arr = json['ModbusikMasterTCP']
    ModbusSlaveTCP_arr = json['ModbusSlaveTCP']
    IEC_60870_5_104_Slave_arr = json['IEC-60870-5-104-Slave']
    IEC_60870_5_104_Master_2_arr = json['IEC-60870-5-104-Master-#2']
    IEC_60870_5_104_Master_arr = json['IEC-60870-5-104-Master']
    ModbusikMasterRTU_arr = json['ModbusikMasterRTU']
    ModbusSlaveRTU_arr = json['ModbusSlaveRTU']
    # print('here')
    for item in ModbusSlaveRTU_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            ModbusSlaveRTU.objects.create(**val)
    for item in ModbusikMasterRTU_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            # print(val)
            ModbusikMasterRTU.objects.create(**val)
    for item in IEC_60870_5_104_Master_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Master.objects.create(**val)
    for item in IEC_60870_5_104_Master_2_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Master.objects.create(**val)
    for item in IEC_60870_5_104_Slave_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            IEC_60870_5_104_Slave.objects.create(**val)
    for item in ModbusSlaveTCP_arr:
        for key, val in item.items():
            val['Name_ID'] = key
            ModbusSlaveTCP.objects.create(**val)
    for item in ModbusikMasterTCP_arr:
        for key, val in item.items():
            ModbusikMasterTCP.objects.create(**val)


''' обработка gack файла '''


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
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            cut1 = group7.get('name')
                                            cut1 = cut1.replace(" ", "_")
                                            gr5[cut1] = group7.get('val')
                                cut = group5.get('name')
                                cut = cut.replace(" ", "_")
                                gr5[cut] = group5.get('val')
                                result1 = {}
                                gr5["Sector"] = "root"
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
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            cut1 = group7.get('name')
                                            cut1 = cut1.replace(" ", "_")
                                            gr5[cut1] = group7.get('val')

                                cut = group5.get('name')
                                cut = cut.replace(" ", "_")
                                gr5[cut] = group5.get('val')
                                gr5["Sector"] = "BS_AG"
                                result1 = {}
                                result1[group4.attrib['tag']] = gr5
                                if result1 not in result[group4.attrib['type']]:
                                    result[group4.attrib['type']].append(result1)
                                # result[group4.attrib['tag']] = gr5

    return result


'''Сохранение изменений в xml-файл'''


def write_GACSECTOR(path):
    tree = ET.parse(path)
    root = tree.getroot()

    json = get_data_from_database()
    root1 = {}
    BS_AG = {}
    for i in json:
        for k1, v1 in i.items():
            for k2, v2 in v1.items():
                if k2 == "Sector" and v2 == "root":
                    root1[k1] = v1
                elif k2 == "Sector" and v2 == "BS_AG":
                    BS_AG[k1] = v1

    print(BS_AG)
    for group1 in root.findall('GACSECTOR'):
        for group2 in group1:
            '''Ищем root'''
            if len(group2.attrib) > 0 and group2.attrib['name'] == 'root':
                '''Проходим по сегменту Blocks'''
                for group3 in group2.findall('Blocks'):
                    for group4 in group3:
                        '''Ищем необходимые элементы, записанные в константе'''
                        if len(group4.attrib) > 0 and group4.attrib['tag'] in root1.keys():
                            for group5 in group4:

                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            cut = group7.get('name')
                                            cut1 = cut.replace(" ", "_")
                                            fr = group7.get('val')

                                            ffr = root1[group4.attrib['tag']]
                                            fr1 = ffr[cut1]
                                            cut1 = cut.replace("_", " ")
                                            group5.set('val', str(fr1))
                                            tree.write(path)

                                cut = group5.get('name')
                                cut1 = cut.replace(" ", "_")
                                fr = group5.get('val')

                                ffr = root1[group4.attrib['tag']]

                                fr1 = ffr[cut1]

                                cut1 = cut.replace("_", " ")
                                group5.set('val', str(fr1))
                                tree.write(path)

            '''Ищем BS_AG'''
            if len(group2.attrib) > 0 and group2.attrib['name'] == 'BS_AG':
                '''Проходим по сегменту Blocks'''
                for group3 in group2.findall('Blocks'):
                    for group4 in group3:
                        '''Ищем необходимые элементы, записанные в константе'''
                        if len(group4.attrib) > 0 and group4.attrib['type'] in BS_AG.keys():
                            '''Формируем результат'''
                            for group5 in group4:
                                if group5.findall('Struct'):
                                    for group6 in group5.findall('Struct'):
                                        for group7 in group6:
                                            cut = group7.get('name')
                                            cut1 = cut.replace(" ", "_")
                                            fr = group7.get('val')
                                            ffr = BS_AG[group4.attrib['tag']]
                                            fr1 = ffr[cut1]
                                            cut1 = cut.replace("_", " ")
                                            group5.set('val', str(fr1))
                                            tree.write(path)
                                cut = group5.get('name')
                                cut1 = cut.replace(" ", "_")
                                fr = group5.get('val')
                                print(group4.attrib['tag'])
                                ffr = BS_AG[group4.attrib['tag']]
                                fr1 = ffr[cut1]
                                cut1 = cut.replace("_", " ")
                                group5.set('val', str(fr1))
                                tree.write(path)
    tree.write(path)


def get_data_from_database():
    IEC_Master = IEC_60870_5_104_Master.objects.all()
    IEC_Slave = IEC_60870_5_104_Slave.objects.all()
    ModSlaveRTU = ModbusSlaveRTU.objects.all()
    ModSlaveTCP = ModbusSlaveTCP.objects.all()
    ModMasterRTU = ModbusikMasterRTU.objects.all()
    ModMasterTCP = ModbusikMasterTCP.objects.all()
    form1 = {}
    form2 = {}
    form3 = {}
    form4 = {}
    form5 = {}
    form6 = {}

    for i in range(len(IEC_Master)):
        form1[IEC_Master[i].Name_ID] = {
            'Name_ID': IEC_Master[i].Name_ID, 'Sector': IEC_Master[i].Sector, 'IP': IEC_Master[i].IP,
            'Port': IEC_Master[i].Port
            , 'Reconnect': IEC_Master[i].Reconnect, 'T1': IEC_Master[i].T1, 'T2': IEC_Master[i].T2,
            'T3': IEC_Master[i].T3,
            'W': IEC_Master[i].W, 'K': IEC_Master[i].K, 'TimeSync': IEC_Master[i].TimeSync,
            'TimeSyncFormat': IEC_Master[i].TimeSyncFormat,
            'TimeShift': IEC_Master[i].TimeShift, 'Filter': IEC_Master[i].Filter,
            'NumberOfReconnections': IEC_Master[i].NumberOfReconnections,
            'SplitIntoParts': IEC_Master[i].SplitIntoParts, 'LogLevel': IEC_Master[i].LogLevel,
            'Autorun': IEC_Master[i].Autorun,
            'Data': IEC_Master[i].Data, 'Command': IEC_Master[i].Command, 'Files': IEC_Master[i].Files,
            'Endpoints': IEC_Master[i].Endpoints,
            'Interrogation_periods': IEC_Master[i].Interrogation_periods
        }
        # получаем список полей модели
    for i in range(len(IEC_Slave)):
            # переписываем код с IEC_Master на IEC_Slave и с другими полями
            form2[IEC_Slave[i].Name_ID] = {
                'Name_ID': IEC_Slave[i].Name_ID, 'Sector': IEC_Slave[i].Sector, 'Port': IEC_Slave[i].Port,
                'Name': IEC_Slave[
                    i].Name, 'ASDU': IEC_Slave[i].ASDU, 'Address': IEC_Slave[i].Address, 'Count': IEC_Slave[i].Count,
                'Type':
                    IEC_Slave[i].Type,
                'Groups': IEC_Slave[i].Groups, 'Cause_of_transmission': IEC_Slave[i].Cause_of_transmission,
                'IOA': IEC_Slave[
                    i].IOA, 'Range': IEC_Slave[i].Range, 'Type_send': IEC_Slave[i].Type_send,
                'AnswerTimeout': IEC_Slave[
                    i].AnswerTimeout,
                'InfoTimeout': IEC_Slave[i].InfoTimeout, 'Downtime': IEC_Slave[i].Downtime, 'W': IEC_Slave[i].W,
                'K': IEC_Slave[
                    i].K, 'MaxConnectionCount': IEC_Slave[i].MaxConnectionCount, 'QueueSize': IEC_Slave[i].QueueSize,
                'Filter':
                    IEC_Slave[i].Filter,
                'LogLevel': IEC_Slave[i].LogLevel, 'Autorun': IEC_Slave[i].Autorun, 'Description': IEC_Slave[
                    i].Description, 'Data': IEC_Slave[i].Data, 'Command': IEC_Slave[i].Command,
                'Files': IEC_Slave[i].Files
            }
    #
    for i in range(len(ModMasterRTU)):
        form3[ModMasterRTU[i].Name_ID] = {
            'Name_ID': ModMasterRTU[i].Name_ID, 'Sector': ModMasterRTU[i].Sector, 'Port': ModMasterRTU[i].Port,
            'Speed': ModMasterRTU[i].Speed, 'Parity': ModMasterRTU[i].Parity, 'Stop_bits': ModMasterRTU[i].Stop_bits,
            'Data_bits': ModMasterRTU[i].Data_bits,
            'Number_of_retries': ModMasterRTU[i].Number_of_retries, 'Read_timeout': ModMasterRTU[i].Read_timeout,
            'Pause': ModMasterRTU[i].Pause, 'Station_Address': ModMasterRTU[i].Station_Address,
            'Reconnect': ModMasterRTU[i].Reconnect, 'Allowed_errors': ModMasterRTU[i].Allowed_errors,
            'LogLevel': ModMasterRTU[i].LogLevel, 'Autorun': ModMasterRTU[i].Autorun,
            'Registers_Type': ModMasterRTU[i].Registers_Type, 'Start': ModMasterRTU[i].Start,
            'Data_Type': ModMasterRTU[i].Data_Type, 'Count': ModMasterRTU[i].Count,
            'Bytes_Order': ModMasterRTU[i].Bytes_Order, 'Period': ModMasterRTU[i].Period,
            'Filter': ModMasterRTU[i].Filter, 'Name': ModMasterRTU[i].Name, 'Composition': ModMasterRTU[i].Composition,
            'Control': ModMasterRTU[i].Control,
            'Read_registers': ModMasterRTU[i].Read_registers, 'Write_registers': ModMasterRTU[i].Write_registers}
    #
    for i in range(len(ModMasterTCP)):
        form4[ModMasterTCP[i].Name_ID] = {
            'Name_ID': ModMasterTCP[i].Name_ID, 'Sector': ModMasterTCP[i].Sector, 'Ip': ModMasterTCP[i].Ip,
            'Port': ModMasterTCP[i].Port, 'Read_timeout': ModMasterTCP[i].Read_timeout, 'Pause': ModMasterTCP[i].Pause,
            'Station_Address': ModMasterTCP[i].Station_Address,
            'Reconnect': ModMasterTCP[i].Reconnect, 'NumberOfReconnections': ModMasterTCP[i].NumberOfReconnections,
            'Allowed_errors': ModMasterTCP[i].Allowed_errors, 'LogLevel': ModMasterTCP[i].LogLevel,
            'Autorun': ModMasterTCP[i].Autorun,
            'Read_registers': ModMasterTCP[i].Read_registers, 'Write_registers': ModMasterTCP[i].Write_registers,
            'Endpoints': ModMasterTCP[i].Endpoints
        }
    #
    for i in range(len(ModSlaveRTU)):
        form5[ModSlaveRTU[i].Name_ID] = {
            'Name_ID': ModSlaveRTU[i].Name_ID, 'Sector': ModSlaveRTU[i].Sector, 'Port': ModSlaveRTU[i].Port,
            'Address': ModSlaveRTU[i].Address, 'Speed': ModSlaveRTU[i].Speed, 'Parity': ModSlaveRTU[i].Parity,
            'Stop_bits': ModSlaveRTU[i].Stop_bits,
            'Data_bits': ModSlaveRTU[i].Data_bits, 'Count': ModSlaveRTU[i].Count,
            'Number_of_reconnections': ModSlaveRTU[i].Number_of_reconnections,
            'Write_messages_in_log': ModSlaveRTU[i].Write_messages_in_log,
            'Autorun': ModSlaveRTU[i].Autorun, 'Registers': ModSlaveRTU[i].Registers,
            'Registers_type': ModSlaveRTU[i].Registers_type}
    #
    for i in range(len(ModSlaveTCP)):
        # переписываем код с IEC_Master на ModSlaveTCP и с другими полями
        form6[ModSlaveTCP[i].Name_ID] = {
            'Name_ID': ModSlaveTCP[i].Name_ID, 'IP': ModSlaveTCP[i].IP, 'Port': ModSlaveTCP[i].Port, 'Clients_Count':
                ModSlaveTCP[i].Clients_Count, 'Device_Address': ModSlaveTCP[i].Device_Address,
            'Autorun': ModSlaveTCP[i].Autorun, 'Registers': ModSlaveTCP[i].Registers}

    form_res = [form1, form2, form3, form4, form5, form6]
    return form_res


'''Функция считывающая XML файл'''


def read_xml(tree):
    result = {'ModbusikMasterTCP': [], 'ModbusSlaveRTU': [], 'ModbusSlaveTCP': [], 'ModbusikMasterRTU': [],
              'IEC-60870-5-104-Slave': [], 'IEC-60870-5-104-Master-#2': [], 'IEC-60870-5-104-Master': []}
    try:

        root = tree.getroot()
        '''Проходим по сегменту GACSECTOR'''
        result = read_GACSECTOR(root, result)
        return (result)
    except BaseException:
        print("Возникла ошибка при чтении")


# обработка неправильной адресации
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


# главная страница
def index(request):
    if request.method == "POST":
        path = GackPath(request.POST)
        if path.is_valid():
            try:
                IEC_60870_5_104_Master.objects.all().delete()
                IEC_60870_5_104_Slave.objects.all().delete()
                ModbusikMasterTCP.objects.all().delete()
                ModbusikMasterRTU.objects.all().delete()
                ModbusSlaveTCP.objects.all().delete()
                ModbusSlaveRTU.objects.all().delete()

                write_into_db(list(path.cleaned_data.values())[0])

                request.session['mypath'] = list(path.cleaned_data.values())[0]
                return redirect('/main/controllerInfo/')
            except Exception as e:
                print(e)
                messages.error(request, "неверный путь!")
    else:
        path = GackPath()
    return render(request, "main/index.html", {"path": path})


"""
def categories(request):
    return HttpResponse("<h1>fasdfasdf</h1>")
"""


# обработчик окна с выводом информации из gack файла
def viewBlocks(request):

    object_list = [ModbusSlaveTCP.objects.first(), ModbusikMasterTCP.objects.first(),
                   ModbusSlaveRTU.objects.first(), ModbusikMasterRTU.objects.first(),
                   IEC_60870_5_104_Slave.objects.first(), IEC_60870_5_104_Master.objects.first()]

    object_list = [x for x in object_list if x is not None]

    nameModel = request.GET.get('item')
    success_message = None

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
                if form.is_valid():
                    form.save()

                    #write_GACSECTOR(request.session.get('mypath'))

                    success_message = 'данные изменены!'
                    # return redirect(reverse('blockview') + f'?item={nameModel}')
            except OverflowError:
                # Обработка ошибки OverflowError
                form.add_error(None, 'Произошла ошибка с переполнением')
        else:
            form = form_class(instance=current_model)
    else:
        form = None

    context = {
        "object_list": object_list,
        "form": form,
        "nameModel": nameModel,
        'success_message': success_message
    }
    # список информации о блоках
    return render(request, "main/mainpage.html", context)
