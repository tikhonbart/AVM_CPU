# Generated by Django 4.2.2 on 2023-06-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_iec_60870_5_104_master_iec_60870_5_104_slave_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Command',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Data',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Endpoints',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Files',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Interrogation_periods',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_master',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_slave',
            name='Command',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_slave',
            name='Data',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_slave',
            name='Description',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_slave',
            name='Files',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iec_60870_5_104_slave',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Bytes_Order',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Composition',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Control',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Count',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Data_Type',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Filter',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Name',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Period',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Read_registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Registers_Type',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Start',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmasterrtu',
            name='Write_registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmastertcp',
            name='Endpoints',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmastertcp',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmastertcp',
            name='Read_registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusikmastertcp',
            name='Write_registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusslavertu',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusslavertu',
            name='Registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusslavetcp',
            name='Name_ID',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modbusslavetcp',
            name='Registers',
            field=models.CharField(default='null', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='iec_60870_5_104_master',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='iec_60870_5_104_master',
            name='SplitIntoParts',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='iec_60870_5_104_master',
            name='TimeSync',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='iec_60870_5_104_slave',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusikmasterrtu',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusikmastertcp',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusikmastertcp',
            name='Pause',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusikmastertcp',
            name='Read_timeout',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusikmastertcp',
            name='Station_Address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavertu',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavertu',
            name='Count',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavertu',
            name='Data_bits',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavertu',
            name='Speed',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavertu',
            name='Write_messages_in_log',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='modbusslavetcp',
            name='Autorun',
            field=models.CharField(max_length=255),
        ),
    ]
