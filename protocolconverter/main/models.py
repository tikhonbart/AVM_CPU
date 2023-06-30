from django.db import models


class ModbusSlaveTCP(models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)
    Clients_Count = models.IntegerField()
    Device_Address = models.IntegerField()
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Registers = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusSlaveTCP"


class ModbusikMasterTCP(models.Model):
    Ip = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)
    Read_timeout = models.CharField(max_length=255)
    Pause = models.CharField(max_length=255)
    Station_Address = models.CharField(max_length=255)
    Reconnect = models.IntegerField()
    NumberOfReconnections = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Read_registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Write_registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusikMasterTCP"


class ModbusSlaveRTU(models.Model):
    Port = models.CharField(max_length=255)
    Address = models.IntegerField()
    Speed = models.CharField(max_length=255)
    Parity = models.CharField(max_length=15)
    Stop_bits = models.CharField(max_length=255)
    Data_bits = models.CharField(max_length=255)
    Number_of_reconnections = models.IntegerField()
    Write_messages_in_log = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Count = models.CharField(max_length=255, blank=True)
    Registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Registers_type = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusSlaveRTU"


class ModbusikMasterRTU(models.Model):
    Port = models.CharField(max_length=255)
    Speed = models.CharField(max_length=255)
    Parity = models.CharField(max_length=15)
    Stop_bits = models.CharField(max_length=255)
    Data_bits = models.CharField(max_length=255)
    Number_of_retries = models.IntegerField()
    Read_timeout = models.IntegerField()
    Pause = models.IntegerField()
    Station_Address = models.IntegerField()
    Reconnect = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Registers_Type = models.CharField(max_length=255, default='null', null=True, blank=True)
    Start = models.CharField(max_length=255, default='null', null=True, blank=True)
    Data_Type = models.CharField(max_length=255, default='null', null=True, blank=True)
    Count = models.CharField(max_length=255, default='null', null=True, blank=True)
    Bytes_Order = models.CharField(max_length=255, default='null', null=True, blank=True)
    Period = models.CharField(max_length=255, default='null', null=True, blank=True)
    Filter = models.CharField(max_length=255, default='null', null=True, blank=True)
    Name = models.CharField(max_length=255, default='null', null=True, blank=True)
    Composition = models.CharField(max_length=255, default='null', null=True, blank=True)
    Control = models.CharField(max_length=255, default='null', null=True, blank=True)

    Read_registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Write_registers = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusikMasterRTU"


class IEC_60870_5_104_Slave(models.Model):
    Port = models.CharField(max_length=255)
    AnswerTimeout = models.IntegerField()
    InfoTimeout = models.IntegerField()
    Downtime = models.IntegerField()
    W = models.IntegerField()
    K = models.IntegerField()
    MaxConnectionCount = models.IntegerField()
    QueueSize = models.IntegerField()
    Filter = models.CharField(max_length=255)
    LogLevel = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Name = models.CharField(max_length=255, blank=True)
    ASDU = models.IntegerField(null=True, blank=True)
    Address = models.IntegerField(null=True, blank=True)
    Count = models.IntegerField(null=True, blank=True)
    Type = models.CharField(max_length=255, blank=True)
    Groups = models.CharField(max_length=255, blank=True)
    Cause_of_transmission = models.CharField(max_length=255, blank=True)
    IOA = models.IntegerField(null=True, blank=True)
    Range = models.IntegerField(null=True, blank=True)
    Type_send = models.CharField(max_length=255, blank=True)
    Description = models.CharField(max_length=255, default='null', null=True, blank=True)

    Data = models.CharField(max_length=255, default='null', null=True, blank=True)
    Command = models.CharField(max_length=255, default='null', null=True, blank=True)
    Files = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "IEC_60870_5_104_Slave"


class IEC_60870_5_104_Master(models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)
    Reconnect = models.IntegerField()
    T1 = models.IntegerField()
    T2 = models.IntegerField()
    T3 = models.IntegerField()
    W = models.IntegerField()
    K = models.IntegerField()
    TimeSync = models.CharField(max_length=255)
    TimeSyncFormat = models.CharField(max_length=255)
    TimeShift = models.IntegerField()
    Filter = models.CharField(max_length=255)
    NumberOfReconnections = models.IntegerField()
    SplitIntoParts = models.CharField(max_length=255)
    LogLevel = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Data = models.CharField(max_length=255, default='null', null=True, blank=True)
    Command = models.CharField(max_length=255, default='null', null=True, blank=True)
    Files = models.CharField(max_length=255, default='null', null=True, blank=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True, blank=True)
    Interrogation_periods = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "IEC_60870_5_104_Master"
