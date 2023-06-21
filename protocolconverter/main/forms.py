from django import forms
from .models import *


class GackPath(forms.Form):
    path = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),
                           label="путь до gack файла")

class IEC_Master_Form(forms.ModelForm):
    class Meta:
        model = IEC_60870_5_104_Master
        fields = ['Name_ID', 'IP', 'Port', 'Reconnect', 'T1', 'T2', 'T3', 'W', 'K', 'TimeSync', 'TimeSyncFormat',
                  'TimeShift', 'Filter', 'NumberOfReconnections', 'SplitIntoParts', 'LogLevel', 'Autorun', 'Data',
                  'Command', 'Files', 'Endpoints', 'Interrogation_periods']


class IEC_Slave_Form(forms.ModelForm):
    class Meta:
        model = IEC_60870_5_104_Slave
        fields = ['Name_ID', 'Port', 'Name', 'ASDU', 'Address', 'Count', 'Type', 'Groups', 'Cause_of_transmission',
                  'IOA', 'Range', 'Type_send', 'AnswerTimeout', 'InfoTimeout', 'Downtime', 'W', 'K',
                  'MaxConnectionCount', 'QueueSize', 'Filter', 'LogLevel', 'Autorun', 'Description', 'Data', 'Command',
                  'Files']


class ModbusikMasterRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusikMasterRTU
        fields = ['Name_ID', 'Port', 'Speed', 'Parity', 'Stop_bits', 'Data_bits', 'Number_of_retries', 'Read_timeout',
                  'Pause', 'Station_Address', 'Reconnect', 'Allowed_errors', 'LogLevel', 'Autorun','Registers_Type',
                  'Start', 'Data_Type', 'Count', 'Bytes_Order', 'Period', 'Filter', 'Name', 'Composition', 'Control',
                  'Read_registers', 'Write_registers']


class ModbusSlaveRTU_Form(forms.ModelForm):
    class Meta:
        model = ModbusSlaveRTU
        fields = ['Name_ID', 'Port', 'Address', 'Speed', 'Parity', 'Stop_bits', 'Data_bits', 'Count',
                  'Number_of_reconnections', 'Write_messages_in_log', 'Autorun', 'Registers', 'Registers_type']


class ModbusikMasterTCP_Form(forms.ModelForm):
    class Meta:
        model = ModbusikMasterTCP
        fields = ['Name_ID', 'Ip', 'Port', 'Read_timeout', 'Pause', 'Station_Address', 'Reconnect', 'NumberOfReconnections',
                  'Allowed_errors', 'LogLevel', 'Autorun', 'Read_registers', 'Write_registers', 'Endpoints']


class ModbusSlaveTCP_Form(forms.ModelForm):
    class Meta:
        model = ModbusSlaveTCP
        fields = ['Name_ID', 'IP', 'Port', 'Clients_Count', 'Device_Address', 'Autorun', 'Registers']