from django.urls import path, include
from main.views import *
from django.contrib import admin

urlpatterns = [
    path('', index, name="home"),
    path('controllerInfo/', viewBlocks, name="blockview"),   # http://127.0.0.1:8000/main/controllerInfo +
    path('admin', admin.site.urls),
    #+
    path('get/IEC_60870_5_104_Slave', IEC_60870_5_104_Slave_View.as_view(), name='getIECs'),
    path('get/IEC_60870_5_104_Master', IEC_60870_5_104_Master_View.as_view(), name='getIECm'),
    path('get/ModbusikMasterTCP', ModbusikMasterTCP_View.as_view(), name='getModbusikMasterTCP'),
    path('get/ModbusikMasterRTU', ModbusikMasterRTU_View.as_view(), name='getModbusikMasterRTU'),
    path('get/ModbusSlaveTCP', ModbusSlaveTCP_View.as_view(), name='getModbusSlaveTCP'),
    path('get/ModbusSlaveRTU', ModbusSlaveRTU_View.as_view(), name='getModbusSlaveRTU'),


    path('post/ModbusSlaveRTU', insert_ModbusSlaveRTU, name='postModbusSlaveRTU'),
    path('post/IEC_60870_5_104_Master', insert_IEC_60870_5_104_Master, name='postIECm'), #+
    path('post/IEC_60870_5_104_Slave', insert_IEC_60870_5_104_Slave, name='postIECs'),
    path('post/ModbusSlaveTCP', insert_ModbusSlaveTCP, name='postModbusSlaveTCP'),
    path('post/ModbusikMasterRTU', insert_ModbusikMasterRTU, name='postModbusikMasterRTU'),
    path('post/ModbusikMasterTCP', insert_ModbusikMasterTCP, name='postModbusikMasterTCP'),

    path('delete/all', delete_db, name='deleteDB'), #+
    path('delete/ModbusSlaveRTU', delete_ModbusSlaveRTU, name='deleteModbusSlaveRTU'),
    path('delete/ModbusSlaveTCP', delete_ModbusSlaveTCP, name='deleteModbusSlaveTCP'),
    path('delete/ModbusikMasterRTU', delete_ModbusikMasterRTU, name='deleteModbusikMasterRTU'),
    path('delete/ModbusikMasterTCP', delete_ModbusikMasterTCP, name='deleteModbusikMasterTCP'),
    path('delete/IEC_60870_5_104_Master', delete_IEC_60870_5_104_Master, name='deleteIECm'),
    path('delete/IEC_60870_5_104_Slave', delete_IEC_60870_5_104_Slave, name='deleteIECs')
]