#!/usr/bin/python3
#
# Bruli2Domoticz
# author: z1mEk
# version: 0.9.1
# date: 2018-06-06
# case url: https://www.facebook.com/groups/domoticzpl/permalink/2136742746558544/
#

import requests
import logging

logging.basicConfig(filename='/home/pi/bruli.log', level=logging.DEBUG) # For silent set logging.CRTITICAL, please set path to log file.
logging.debug('Started')

def setvaltempdomo(idx, sValue):
#    r = requests.get('http://192.168.1.208:8080/json.htm?type=command&param=udevice&idx=' + str(idx) + '&nvalue=0&svalue=' + str(sValue), auth=('admin', 'password'))
    logging.debug('Domoticz response code: ' + str(r.status_code) + ', Content: ' + r.text)

def tempval(arg1, arg2):
    logging.debug('temval: ' + arg1 + ', ' + arg2)
    temp = Form_Load(int(arg2), int(arg1)) / 10
    logging.debug('Temp: ' + str(temp))
    return temp

def Form_Load(HiByte, LoByte):
    logging.debug('Form_load: ' + str(HiByte) + ', ' + str(LoByte))
    return 0xFF * HiByte + LoByte

r = requests.get('http://192.168.1.111:80?com=02010006000000006103', auth=('user', 'password')) # mock - replace to Bruli url e.g. http://<ip>?com=02010006000000006103
logging.debug('Bruli response code: ' + str(r.status_code) + ', Content: ' + r.text)

if r.status_code == 200:
    valarray = r.text[1:-1].split(',')

    sal = tempval(valarray[16], valarray[17])
    run = setvaltempdomo(227, sal)

    hol = tempval(valarray[18], valarray[19])
    run = setvaltempdomo(228, hol)

    out = tempval(valarray[20], valarray[21])
    run = setvaltempdomo(229, out)

    cwu = tempval(valarray[22], valarray[23])
    run = setvaltempdomo(230, cwu)

    ret = tempval(valarray[24], valarray[25])
    run = setvaltempdomo(231, ret)

    co  = tempval(valarray[28], valarray[29])
    run = setvaltempdomo(232, co)

    kom = tempval(valarray[30], valarray[31])
    run = setvaltempdomo(233, kom)

    fuel = valarray[75]
    run = setvaltempdomo(234, fuel)
else:
    logging.warning('Bruli response code is ' + str(r.status_code) + ', Content: ' + r.text )

logging.debug('Ending')
