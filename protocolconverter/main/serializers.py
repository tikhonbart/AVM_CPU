from rest_framework import serializers
from .models import IEC_60870_5_104_Master, IEC_60870_5_104_Slave, ModbusikMasterTCP, ModbusikMasterRTU, ModbusSlaveTCP, \
    ModbusSlaveRTU


class IEC_60870_5_104_Master_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IEC_60870_5_104_Master
        fields = ('Name_ID', 'Sector', 'IP', 'Port', 'Reconnect', 'T1', 'T2', 'T3', 'W', 'K', 'TimeSync', 'TimeSyncFormat',
                  'TimeShift', 'Filter', 'NumberOfReconnections', 'SplitIntoParts', 'LogLevel', 'Autorun', 'Data',
                  'Command', 'Files', 'Endpoints', 'Interrogation_periods')


class IEC_60870_5_104_Slave_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IEC_60870_5_104_Slave
        fields = ('Name_ID','Sector', 'Port', 'Name', 'ASDU', 'Address', 'Count', 'Type', 'Groups', 'Cause_of_transmission',
                  'IOA', 'Range', 'Type_send', 'AnswerTimeout', 'InfoTimeout', 'Downtime', 'W', 'K',
                  'MaxConnectionCount', 'QueueSize', 'Filter', 'LogLevel', 'Autorun', 'Description', 'Data', 'Command',
                  'Files')


class ModbusikMasterTCP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModbusikMasterTCP
        fields = ('Name_ID', 'Sector', 'Ip', 'Port', 'Read_timeout', 'Pause', 'Station_Address', 'Reconnect', 'NumberOfReconnections',
                  'Allowed_errors', 'LogLevel', 'Autorun', 'Read_registers', 'Write_registers', 'Endpoints')


class ModbusikMasterRTU_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModbusikMasterRTU
        fields = ('Name_ID', 'Sector', 'Port', 'Speed', 'Parity', 'Stop_bits', 'Data_bits', 'Number_of_retries', 'Read_timeout',
                  'Pause', 'Station_Address', 'Reconnect', 'Allowed_errors', 'LogLevel', 'Autorun','Registers_Type',
                  'Start', 'Data_Type', 'Count', 'Bytes_Order', 'Period', 'Filter', 'Name', 'Composition', 'Control',
                  'Read_registers', 'Write_registers')


class ModbusSlaveTCP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModbusSlaveTCP
        fields = ('Name_ID', 'Sector', 'IP', 'Port', 'Clients_Count', 'Device_Address', 'Autorun', 'Registers')


class ModbusSlaveRTU_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ModbusSlaveRTU
        fields = ('Name_ID', 'Sector', 'Port', 'Address', 'Speed', 'Parity', 'Stop_bits', 'Data_bits', 'Count',
                  'Number_of_reconnections', 'Write_messages_in_log', 'Autorun', 'Registers', 'Registers_type')
