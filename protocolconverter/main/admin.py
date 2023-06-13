from django.contrib import admin
from .models import IEC_60870_5_104_Master,IEC_60870_5_104_Slave, ModbusikMasterTCP, ModbusikMasterRTU, ModbusSlaveTCP,ModbusSlaveRTU
# Register your models here.


admin.site.register(IEC_60870_5_104_Master)
admin.site.register(IEC_60870_5_104_Slave)
admin.site.register(ModbusikMasterTCP)
admin.site.register(ModbusikMasterRTU)
admin.site.register(ModbusSlaveTCP)
admin.site.register(ModbusSlaveRTU)