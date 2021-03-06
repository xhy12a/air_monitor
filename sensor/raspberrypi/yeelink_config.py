class MYCONFIG():
    device_id = ''
    sensor_pm25_id = ''
    sensor_CO_id = ''
    sensor_SO2_id = ''
    sensor_O3_id = ''
    sensor_HCHO_id = ''
    sensor_MQ2_id = ''
    apikey = "779bfd896876dc377d3ed78d0fa1dbf4"


myconfig = MYCONFIG()


def init(myid):
    if myid == 0:
        myconfig.device_id = '353097'
        myconfig.sensor_pm25_id = '397985'
        myconfig.sensor_CO_id = '398391'
        myconfig.sensor_SO2_id = '400110'
        myconfig.sensor_O3_id = '400118'
        myconfig.sensor_HCHO_id = '403705'
        myconfig.sensor_MQ2_id = '403706'
    elif myid == 1:
        myconfig.device_id = '354298'
        myconfig.sensor_pm25_id = '400108'
        myconfig.sensor_CO_id = '400109'
        myconfig.sensor_SO2_id = '400111'
        myconfig.sensor_O3_id = '400119'
        myconfig.sensor_HCHO_id = '403707'
        myconfig.sensor_MQ2_id = '403708'


def apikey():
    return myconfig.apikey


def device_id():
    return myconfig.device_id


def sensor_pm25_id():
    return myconfig.sensor_pm25_id


def sensor_CO_id():
    return myconfig.sensor_CO_id


def sensor_SO2_id():
    return myconfig.sensor_SO2_id


def sensor_O3_id():
    return myconfig.sensor_O3_id


def sensor_HCHO_id():
    return myconfig.sensor_HCHO_id


def sensor_MQ2_id():
    return myconfig.sensor_MQ2_id
