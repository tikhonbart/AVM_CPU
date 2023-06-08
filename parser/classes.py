class ModbusSlaveTCP:
    def __init__(self,IP,Port,Clients_Count,Device_Address,Autorun):
        self.IP = IP
        self.Port = Port
        #self.Registers
        self.Clients_Count = Clients_Count
        self.Device_Address = Device_Address
        self.Autorun = Autorun
    def change_registers(self,val):
        self.Registers = val
    

class ModbusikMasterTCP:
    def init(self, Ip, Port, Read_timeout, Pause, Station_Address,
                 Reconnect, NumberOfReconnections,
                 Allowed_errors, LogLevel, Autorun):
        self.Ip = Ip
        self.Port = Port
        self.Read_timeout = Read_timeout
        self.Pause = Pause
        self.Station_Address = Station_Address
        self.Reconnect = Reconnect
        self.NumberOfReconnections = NumberOfReconnections
        self.Allowed_errors = Allowed_errors
        self.LogLevel = LogLevel
        self.Autorun = Autorun
        # self.Read_Registers
        # self.Write_Registers
        # self.Endpoints
    def change_registers_read(self,val):
        self.Read_Registers = val
    def change_registers_write(self,val):
        self.Write_Registers = val
    def change_endpoints(self,val):
        self.Endpoints = val

class ModbusSlaveRTU:
    def __init__(self,Port,Address,Speed,Parity, Stop_bits, Data_bits,
                 Count, Number_of_reconnections, Write_messages_in_log, 
                 Autorun) -> None:
        self.Port = Port
        self.Address = Address
        self.Speed = Speed
        self.Parity = Parity
        self.Stop_bits = Stop_bits
        self.Data_bits = Data_bits
        # self.Registers
        # self.Registers_type
        # self.Address_r
        self.Count = Count
        self.Number_of_reconnections = Number_of_reconnections
        self.Write_messages_in_log = Write_messages_in_log
        self.Autorun = Autorun
    def change_registers(self,val):
        self.Registers = val
    def change_Registers_type(self,val):
        self.Registers_type = val
    def change_Address_r(self,val):
        self.Address_r = val

class ModbusikMasterRTU:
    def __init__(self,Port, Speed, Parity, Stop_bits, Data_bits, Number_of_retries, 
                 Read_timeout, Pause, Station_Address, Reconnect, 
                 Allowed_errors, LogLevel, Autorun) -> None:
        self.Port = Port
        self.Speed = Speed
        self.Parity = Parity
        self.Stop_bits = Stop_bits
        self.Data_bits = Data_bits
        self.Number_of_retries = Number_of_retries
        self.Read_timeout = Read_timeout
        self.Pause = Pause
        self.Station_Address = Station_Address
        # self.Read_Registers
        # self.Write_Registers
        self.Reconnect = Reconnect
        self.Allowed_errors = Allowed_errors
        self.LogLevel = LogLevel
        self.Autorun= Autorun
    def change_registers_read(self,val):
        self.Read_Registers = val
    def change_registers_write(self,val):
        self.Write_Registers = val

class IEC_60870_5_104_Slave:
    def __init__(self, Port, Name, ASDU, Address,Count,Type,Groups, 
                 Cause_of_transmission, IOA,Range,Type_send,AnswerTimeout,
                 InfoTimeout,Downtime,W,K,MaxConnectionCount,QueueSize,
                 Filter,LogLevel,Autorun) -> None:
        self.Port = Port
        self.Name = Name
        self.ASDU = ASDU
        self.Address = Address
        self.Count = Count
        self.Type = Type
        self.Groups = Groups
        self.Cause_of_transmission = Cause_of_transmission
        # self.Data
        self.IOA = IOA
        self.Range = Range
        self.Type_send = Type_send
        # self.Command
        # self.Files
        self.AnswerTimeout = AnswerTimeout
        self.InfoTimeout = InfoTimeout
        self.Downtime = Downtime
        self.W = W
        self.K = K
        self.MaxConnectionCount = MaxConnectionCount
        self.QueueSize = QueueSize
        self.Filter = Filter
        self.LogLevel = LogLevel
        self.Autorun = Autorun
    def change_Data(self,val):
        self.Data = val
    def change_Command(self,val):
        self.Command = val
    def change_Files(self,val):
        self.Files = val

class IEC_60870_5_104_Master:
    def __init__(self,IP,Port,Reconnect,T1,T2,T3,W,K,TimeSync,TimeSyncFormat,
                 TimeShift,Filter,NumberOfReconnections,SplitIntoParts,
                 LogLevel,Autorun) -> None:
        self.IP = IP
        self.Port = Port
        # self.Data
        # self.Command
        # self.Interrogation_periods
        # self.Files
        # self.Endpoints
        self.Reconnect = Reconnect
        self.T1 = T1
        self.T2 = T2
        self.T3 = T3
        self.W = W
        self.K = K
        self.TimeSync = TimeSync
        self.TimeSyncFormat = TimeSyncFormat
        self.TimeShift = TimeShift
        self.Filter = Filter
        self.NumberOfReconnections = NumberOfReconnections
        self.SplitIntoParts = SplitIntoParts
        self.LogLevel = LogLevel
        self.Autorun = Autorun
    def change_Data(self,val):
        self.Data = val
    def change_Command(self,val):
        self.Command = val
    def change_Files(self,val):
        self.Files = val
    def change_Interrogation_periods(self,val):
        self.Interrogation_periods = val
    def change_Endpoints(self,val):
        self.Endpoints = val
