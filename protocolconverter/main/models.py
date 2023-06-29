from django.db import models


class ModbusSlaveTCP(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)
    Clients_Count = models.IntegerField()
    Device_Address = models.IntegerField()
    Autorun = models.CharField(max_length=255)

    Registers = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID


class ModbusikMasterTCP(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
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

    Read_registers = models.CharField(max_length=255, default='null', null=True)
    Write_registers = models.CharField(max_length=255, default='null', null=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID


class ModbusSlaveRTU(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
    Port = models.CharField(max_length=255)
    Address = models.IntegerField()
    Speed = models.CharField(max_length=255)
    Parity = models.CharField(max_length=15)
    Stop_bits = models.CharField(max_length=255)
    Data_bits = models.CharField(max_length=255)
    Count = models.CharField(max_length=255)
    Number_of_reconnections = models.IntegerField()
    Write_messages_in_log = models.CharField(max_length=255)
    Autorun = models.CharField(max_length=255)

    Registers = models.CharField(max_length=255, default='null', null=True)
    Registers_type = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID


class ModbusikMasterRTU(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
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

    Registers_Type = models.CharField(max_length=255, default='null', null=True)
    Start = models.CharField(max_length=255, default='null', null=True)
    Data_Type = models.CharField(max_length=255, default='null', null=True)
    Count = models.CharField(max_length=255, default='null', null=True)
    Bytes_Order = models.CharField(max_length=255, default='null', null=True)
    Period = models.CharField(max_length=255, default='null', null=True)
    Filter = models.CharField(max_length=255, default='null', null=True)
    Name = models.CharField(max_length=255, default='null', null=True)
    Composition = models.CharField(max_length=255, default='null', null=True)
    Control = models.CharField(max_length=255, default='null', null=True)

    Read_registers = models.CharField(max_length=255, default='null', null=True)
    Write_registers = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID


class IEC_60870_5_104_Slave(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
    Port = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    ASDU = models.IntegerField()
    Address = models.IntegerField()
    Count = models.IntegerField()
    Type = models.CharField(max_length=255)
    Groups = models.CharField(max_length=255)
    Cause_of_transmission = models.CharField(max_length=255)
    IOA = models.IntegerField(null=True)
    Range = models.IntegerField(null=True)
    Type_send = models.CharField(max_length=255)
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

    Description = models.CharField(max_length=255, default='null', null=True)

    Data = models.CharField(max_length=255, default='null', null=True)
    Command = models.CharField(max_length=255, default='null', null=True)
    Files = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID


class IEC_60870_5_104_Master(models.Model):
    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True)
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

    Data = models.CharField(max_length=255, default='null', null=True)
    Command = models.CharField(max_length=255, default='null', null=True)
    Files = models.CharField(max_length=255, default='null', null=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True)
    Interrogation_periods = models.CharField(max_length=255, default='null', null=True)

    def __str__(self):
        return self.Name_ID
