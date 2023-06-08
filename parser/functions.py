import classes
import json
'''Распаковывает json'''
def unpack_json(json_get):
    mass = []
    with open(json_get, 'r', encoding='utf-8') as f: #открыли файл с данными
        text = json.load(f) #загнали все, что получилось в переменную
    for k,v in text.items():
        for j in v:
            for k1,v1 in j.items():
                match k:
                    case "IEC_60870_5_104_Master":
                        mass.append(create_IEC_60870_5_104_Master(v1))
                        break

                    case "IEC_60870_5_104_Slave":
                        mass.append(create_IEC_60870_5_104_Slave(v1))
                        break
                    case "ModbusikMasterRTU":
                        mass.append(create_ModbusikMasterRTU(v1))
                        break
                    case "ModbusSlaveRTU":
                        mass.append(create_ModbusSlaveRTU(v1))
                        break
                    case "create_ModbusikMasterTCP":
                        mass.append(create_ModbusikMasterTCP(v1))
                        break
                    case 'create_ModbusSlaveTCP':
                        mass.append(create_ModbusSlaveTCP(v1))
                        break
                    case 'IEC-60870-5-104-Master-#2':
                        mass.append(create_IEC_60870_5_104_Master(v1))
                        break
                 
    return mass

'''Создаёт экземпляры классов'''
def create_IEC_60870_5_104_Master(params):
    params1 = params
    return classes.IEC_60870_5_104_Master(IP=params1['IP'],Port=params1['Port'],
                                          Reconnect=params1['Reconnect'],T1=params1['T1'],T2=params1['T2'],
                                          T3=params1['T3'],W=params1['W'],K=params1['K'],TimeSync=params1['TimeSync'],
                                          TimeSyncFormat=params1['TimeSyncFormat'],TimeShift=params1['TimeShift'],Filter=params1['Filter']
                                          ,NumberOfReconnections=params1['NumberOfReconnections'],SplitIntoParts=params1['SplitIntoParts'],
                                          LogLevel=params1['LogLevel'],Autorun=params1['Autorun'])
def create_IEC_60870_5_104_Slave(params):
    params1 = params
    return classes.IEC_60870_5_104_Slave(Port=params1['Port'], Name=params1['Name'], ASDU=params1['ASDU'], Address=params1['Address']
                                         ,Count=params1['Count'],Type=params1['Type'],Groups=params1['Groups'], Cause_of_transmission=params1['Cause of transmission'],
                                         IOA=params1['IOA'],Range=params1['Range'],Type_send=params1['Type send'],AnswerTimeout=params1['AnswerTimeout'],
                                         InfoTimeout=params1['InfoTimeout'],Downtime=params1['Downtime'],W=params1['W'],K=params1['K'],
                                         MaxConnectionCount=params1['MaxConnectionCount'],QueueSize=params1['QueueSize'],Filter=params1['Filter'],
                                         LogLevel=params1['LogLevel'],Autorun=params1['Autorun'])
def create_ModbusikMasterRTU(params):
    params1 = params
    return classes.ModbusikMasterRTU(Port=params1['Port'], Speed=params1['Speed'], Parity=params1['Parity'], Stop_bits=params1['Stop bits'], Data_bits=params1['Data bits']
                                     , Number_of_retries=params1['Number of retries'], Read_timeout=params1['Read timeout'], Pause=params1['Pause'], Station_Address=params1['Station Address']
                                     , Reconnect=params1['Reconnect'], Allowed_errors=params1['Allowed errors'], LogLevel=params1['LogLevel'], Autorun=params1['Autorun'])
def create_ModbusSlaveRTU(params):
    params1 = params
    return classes.ModbusSlaveRTU(Port=params1['Port'],Address=params1['Address'],Speed=params1['Speed'],Parity=params1['Parity'], Stop_bits=params1['Stop bits'], Data_bits=params1['Data bits']
                                  ,Count=params1['Count'], Number_of_reconnections=params1['Number of reconnections'], Write_messages_in_log=params1['Write messages in log'], 
                                  Autorun=params1['Autorun'])
def create_ModbusikMasterTCP(params):
    params1 = params
    return classes.ModbusikMasterTCP(Ip=params1['Ip'], Port=params1['Port'], Read_timeout=params1['Read timeout'], Pause=params1['Pause'], Station_Address=params1['Station Address'],
                                     Reconnect=params1['Port'], NumberOfReconnections=params1['NumberOfReconnections'],Allowed_errors=params1['Allowed errors'], LogLevel=params1['LogLevel']
                                     , Autorun=params1['Autorun'])
def create_ModbusSlaveTCP(params):
    params1 = params
    return classes.ModbusSlaveTCP(IP=params1['IP'],Port=params1['Port'],Clients_Count=params1['Clients Count'],Device_Address=params1['Device_Address'],Autorun=params1['Autorun'])

def check_mass():
    print(unpack_json('res/result.json'))
