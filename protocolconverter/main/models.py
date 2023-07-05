from django.db import models


class ChoicesMixin:
    TrueFalse_Choice = (
        ('true', 'yes'),
        ('false', 'no')
    )
    Loglevel_Choice = (
        ('Trace', 'Trace'),
        ('Debug', 'Debug'),
        ('Info', 'Info'),
        ('Warn', 'Warn'),
        ('Error', 'Error'),
        ('Off', 'Off')
    )
    Speed_Choice = (
        ('s1200', '1200'),
        ('s2400', '2400'),
        ('s4800', '4800'),
        ('s9600', '9600'),
        ('s19200', '19200'),
        ('s38400', '38400'),
        ('s57600', '57600'),
        ('s115200', '115200')
    )
    Partity_Choice = (
        ('None', 'None'),
        ('Odd', 'Odd'),
        ('Even', 'Even'),
        ('Mark', 'Mark'),
        ('Space', 'Space')
    )
    StopBits_Choice = (
        ('One', 'One'),
        ('One5', 'One5'),
        ('Two', 'Two')
    )
    DataBits_Choice = (
        ('Seven', '7'),
        ('Eight', '8')
    )
    FilterChoice = (
        ('None', 'None'),
        ('Partial', 'Partial'),
        ('Full', 'Full')
    )
    TimeSyncFormatChoice = (
        ('UTC', 'UTC'),
        ('Localtime', 'Localtime')
    )


class ModbusSlaveTCP(ChoicesMixin, models.Model):
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=20)
    Clients_Count = models.IntegerField()
    Device_Address = models.IntegerField()
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Registers = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusSlaveTCP"


class ModbusikMasterTCP(ChoicesMixin, models.Model):

    Ip = models.CharField(max_length=15)
    Port = models.CharField(max_length=20)
    Read_timeout = models.CharField(max_length=20)
    Pause = models.CharField(max_length=20)
    Station_Address = models.CharField(max_length=20)
    Reconnect = models.IntegerField()
    NumberOfReconnections = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.CharField(max_length=20, choices=ChoicesMixin.Loglevel_Choice)
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Read_registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Write_registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusikMasterTCP"


class ModbusSlaveRTU(ChoicesMixin, models.Model):

    Port = models.CharField(max_length=20)
    Address = models.IntegerField()
    Speed = models.CharField(max_length=20, choices=ChoicesMixin.Speed_Choice)
    Parity = models.CharField(max_length=20, choices=ChoicesMixin.Partity_Choice)
    Stop_bits = models.CharField(max_length=20, choices=ChoicesMixin.StopBits_Choice)
    Data_bits = models.CharField(max_length=20, choices=ChoicesMixin.DataBits_Choice)
    Number_of_reconnections = models.IntegerField()
    Write_messages_in_log = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Count = models.CharField(max_length=255, blank=True)
    Registers = models.CharField(max_length=255, default='null', null=True, blank=True)
    Registers_type = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "ModbusSlaveRTU"


class ModbusikMasterRTU(ChoicesMixin, models.Model):

    Port = models.CharField(max_length=20)
    Speed = models.CharField(max_length=20, choices=ChoicesMixin.Speed_Choice)
    Parity = models.CharField(max_length=20, choices=ChoicesMixin.Partity_Choice)
    Stop_bits = models.CharField(max_length=20, choices=ChoicesMixin.StopBits_Choice)
    Data_bits = models.CharField(max_length=20, choices=ChoicesMixin.DataBits_Choice)
    Number_of_retries = models.IntegerField()
    Read_timeout = models.IntegerField()
    Pause = models.IntegerField()
    Station_Address = models.IntegerField()
    Reconnect = models.IntegerField()
    Allowed_errors = models.IntegerField()
    LogLevel = models.CharField(max_length=20, choices=ChoicesMixin.Loglevel_Choice)
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

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


class IEC_60870_5_104_Slave(ChoicesMixin, models.Model):
    Port = models.CharField(max_length=20)
    AnswerTimeout = models.IntegerField()
    InfoTimeout = models.IntegerField()
    Downtime = models.IntegerField()
    W = models.IntegerField()
    K = models.IntegerField()
    MaxConnectionCount = models.IntegerField()
    QueueSize = models.IntegerField()
    Filter = models.CharField(max_length=20, choices=ChoicesMixin.FilterChoice)
    LogLevel = models.CharField(max_length=20, choices=ChoicesMixin.Loglevel_Choice)
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

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


class IEC_60870_5_104_Master(ChoicesMixin, models.Model):

    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=20)
    Reconnect = models.IntegerField()
    T1 = models.IntegerField()
    T2 = models.IntegerField()
    T3 = models.IntegerField()
    W = models.IntegerField()
    K = models.IntegerField()
    TimeSync = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)
    TimeSyncFormat = models.CharField(max_length=20, choices=ChoicesMixin.TimeSyncFormatChoice)
    TimeShift = models.IntegerField()
    Filter = models.CharField(max_length=20, choices=ChoicesMixin.FilterChoice)
    NumberOfReconnections = models.IntegerField()
    SplitIntoParts = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)
    LogLevel = models.CharField(max_length=20, choices=ChoicesMixin.Loglevel_Choice)
    Autorun = models.CharField(max_length=20, choices=ChoicesMixin.TrueFalse_Choice)

    Name_ID = models.CharField(max_length=255, default='null', null=True)
    Sector = models.CharField(max_length=255, default='null', null=True, blank=True)
    Data = models.CharField(max_length=255, default='null', null=True, blank=True)
    Command = models.CharField(max_length=255, default='null', null=True, blank=True)
    Files = models.CharField(max_length=255, default='null', null=True, blank=True)
    Endpoints = models.CharField(max_length=255, default='null', null=True, blank=True)
    Interrogation_periods = models.CharField(max_length=255, default='null', null=True, blank=True)

    def __str__(self):
        return "IEC_60870_5_104_Master"
