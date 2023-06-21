from django import forms
from .models import *


class GackPath(forms.Form):
    path = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
                           label="путь до gack файла")


class IEC_Master_Form(forms.ModelForm):
    class Meta:
        model = IEC_60870_5_104_Master
        fields = ['IP', 'Port', 'Reconnect', 'T1', 'T2', 'T3', 'W', 'K',
                  'TimeSync', 'TimeSyncFormat', 'TimeShift', 'Filter',
                  'NumberOfReconnections', 'SplitIntoParts', 'LogLevel', "Autorun"]


class IEC_Slave_Form(forms.ModelForm):
    class Meta:
        model = IEC_60870_5_104_Slave
        fields = ['Port', 'Name', 'ASDU', 'Address', 'Count', 'Type', 'Groups', 'Cause_of_transmission',
                  'IOA', 'Range', 'Type_send', 'AnswerTimeout',
                  'InfoTimeout', 'Downtime', 'W', "K",
                  'MaxConnectionCount', 'QueueSize', 'Filter', 'LogLevel', 'Autorun']


class ModbusikMasterRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusikMasterRTU
        fields = ['Port', 'Speed', 'Parity', 'Stop_bits', 'Data_bits',
                  'Number_of_retries', 'Read_timeout', 'Pause', 'Station_Address', 'Reconnect',
                  'Allowed_errors', 'LogLevel', 'Autorun']


class ModbusSlaveRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusSlaveRTU
        fields = ['Port', 'Address', 'Speed', 'Parity', 'Stop_bits',
                  'Data_bits', 'Count', 'Number_of_reconnections',
                  'Write_messages_in_log', 'Autorun']


class ModbusikMasterTCP_Form(forms.ModelForm):
    class Meta:
        model = ModbusikMasterTCP
        fields = ['IP', 'Port', 'Read_timeout', 'Pause', 'Station_Address',
                  'Reconnect', 'NumberOfReconnections', 'Allowed_errors', 'LogLevel', 'Autorun']


class ModbusSlaveTCP_Form(forms.ModelForm):
    class Meta:
        model = ModbusSlaveTCP
        fields = ['IP', 'Port', 'Clients_Count', 'Device_Address', 'Autorun']
