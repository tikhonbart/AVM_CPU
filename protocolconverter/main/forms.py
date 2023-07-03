from django import forms
from .models import *
from django.core.validators import RegexValidator

# маска IP
ip_address_validator = RegexValidator(regex=r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',
                                      message='Введите правильный IP-адрес')


class GackPath(forms.Form):
    path = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
                           label="путь до gack файла")


class IEC_Master_Form(forms.ModelForm):
    # IP валидатор
    IP = forms.CharField(validators=[ip_address_validator])

    class Meta:
        model = IEC_60870_5_104_Master
        fields = ['Name_ID', 'IP', 'Port', 'Reconnect', 'T1', 'T2', 'T3', 'W', 'K', 'TimeSync', 'TimeSyncFormat',
                  'TimeShift', 'Filter', 'NumberOfReconnections', 'SplitIntoParts', 'LogLevel', 'Autorun']


class IEC_Slave_Form(forms.ModelForm):
    class Meta:
        model = IEC_60870_5_104_Slave
        fields = ['Name_ID', 'Port', 'AnswerTimeout', 'InfoTimeout', 'Downtime', 'W', 'K',
                  'MaxConnectionCount', 'QueueSize', 'Filter', 'LogLevel', 'Autorun']


class ModbusikMasterRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusikMasterRTU
        fields = ['Name_ID', 'Port', 'Speed', 'Parity', 'Stop_bits', 'Data_bits', 'Number_of_retries', 'Read_timeout',
                  'Pause', 'Station_Address', 'Reconnect', 'Allowed_errors', 'LogLevel', 'Autorun']


class ModbusSlaveRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusSlaveRTU
        fields = ['Name_ID', 'Port', 'Address', 'Speed', 'Parity', 'Stop_bits', 'Data_bits',
                  'Number_of_reconnections', 'Write_messages_in_log', 'Autorun']


class ModbusikMasterTCP_Form(forms.ModelForm):
    # IP валидатор
    Ip = forms.CharField(validators=[ip_address_validator])

    class Meta:
        model = ModbusikMasterTCP
        fields = ['Name_ID', 'Ip', 'Port', 'Read_timeout', 'Pause', 'Station_Address', 'Reconnect',
                  'NumberOfReconnections', 'Allowed_errors', 'LogLevel', 'Autorun']


class ModbusSlaveTCP_Form(forms.ModelForm):
    # IP валидатор
    IP = forms.CharField(validators=[ip_address_validator])

    class Meta:
        model = ModbusSlaveTCP
        fields = ['Name_ID', 'IP', 'Port', 'Clients_Count', 'Device_Address', 'Autorun']
