from django.db import models


class ModbusSlaveTCP(models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)

    Clients_Count = models.IntegerField()
    Device_Address = models.IntegerField()
    Autorun = models.BooleanField()

    def __str__(self):
        return "ModbusSlaveTCP"


class ModbusikMasterTCP(models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255)
    Read_timeout = models.IntegerField()
    Pause = models.IntegerField()
    Station_Address = models.IntegerField()
    Reconnect = models.IntegerField()
    NumberOfReconnections = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.IntegerField()
    Autorun = models.BooleanField()

    def __str__(self):
        return "ModbusikMasterTCP"


class ModbusSlaveRTU(models.Model):
    Port = models.CharField(max_length=255)
    Address = models.IntegerField()
    Speed = models.IntegerField()
    Parity = models.CharField(max_length=15)
    Stop_bits = models.CharField(max_length=255)
    Data_bits = models.IntegerField()
    Count = models.IntegerField()
    Number_of_reconnections = models.IntegerField()
    Write_messages_in_log = models.BooleanField()
    Autorun = models.BooleanField()

    def __str__(self):
        return "ModbusSlaveRTU"


class ModbusikMasterRTU(models.Model):
    Port = models.CharField(max_length=255)
    Speed = models.IntegerField()
    Parity = models.CharField(max_length=15)
    Stop_bits = models.CharField(max_length=255)
    Data_bits = models.IntegerField()
    Number_of_retries = models.IntegerField()
    Read_timeout = models.IntegerField()
    Pause = models.IntegerField()
    Station_Address = models.IntegerField()
    Reconnect = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.CharField(max_length=255)
    Autorun = models.BooleanField()

    def __str__(self):
        return "ModbusikMasterRTU"


class IEC_60870_5_104_Slave(models.Model):
    Port = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    ASDU = models.IntegerField()
    Address = models.IntegerField()
    Count = models.IntegerField()
    Type = models.CharField(max_length=255)
    Groups = models.CharField(max_length=255)
    Cause_of_transmission = models.CharField(max_length=255)
    IOA = models.IntegerField()
    Range = models.IntegerField()
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
    Autorun = models.BooleanField()

    def __str__(self):
        return "IEC_60870_5_104_Slave"


class IEC_60870_5_104_Master(models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=255, verbose_name="Port")
    Reconnect = models.IntegerField(verbose_name="Reconnect")
    T1 = models.IntegerField(verbose_name="T1")
    T2 = models.IntegerField(verbose_name="T2")
    T3 = models.IntegerField(verbose_name="T3")
    W = models.IntegerField(verbose_name="W")
    K = models.IntegerField(verbose_name="K")
    TimeSync = models.BooleanField(verbose_name="TimeSync")
    TimeSyncFormat = models.CharField(max_length=255, verbose_name="TimeSyncFormat")
    TimeShift = models.IntegerField(verbose_name="TimeShift")
    Filter = models.CharField(max_length=255, verbose_name="Filter")
    NumberOfReconnections = models.IntegerField(verbose_name="NumberOfReconnections")
    SplitIntoParts = models.BooleanField(verbose_name="SplitIntoParts")
    LogLevel = models.CharField(max_length=255, verbose_name="LogLevel")
    Autorun = models.BooleanField(verbose_name="Autorun")

    def __str__(self):
        return "IEC_60870_5_104_Master"

