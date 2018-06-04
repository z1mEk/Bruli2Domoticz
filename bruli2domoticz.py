#!/usr/bin/python3
#
# Bruli2Domoticz
# author: z1mEk
# date: 2018-06-04
# case url: https://www.facebook.com/groups/domoticzpl/permalink/2136742746558544/
#

import requests
import logging

logging.basicConfig(filename='/home/pi/bruli.log', level=logging.DEBUG) # For silent set logging.CRTITICAL, please set path to log file.
logging.info('Started')

def setvaltempdomo(idx, sValue):
    r = requests.get('http://192.168.1.175:8080/json.htm?type=command&param=udevice&idx=' + str(idx) + '&nvalue=0&svalue=' + str(sValue), auth=('admin', 'password'))
    logging.debug('Domoticz response code: ' + str(r.status_code) + ', Content: ' + r.text)

def tempval(arg1, arg2):
    logging.debug('temval: ' + arg1 + ', ' + arg2)
    return Form_Load(int(arg2), int(arg1)) / 10

def Form_Load(HiByte, LoByte):
    logging.debug('Form_load: ' + str(HiByte) + ', ' + str(LoByte))
    return (HiByte and 0x7F) * 0x100 or LoByte or - (HiByte > 0x7F) * 0x8000

r = requests.get('https://gabrielzima.pl/b.php', auth=('user', 'password')) # mock - replace to Bruli url e.g. http://piec?com=02010006000000006103
logging.debug('Bruli response code: ' + str(r.status_code) + ', Content: ' + r.text)

if r.status_code == 200:
    valarray = r.text[1:-1].split(',')

    sal = tempval(valarray[16], valarray[17])
    run = setvaltempdomo(412, sal)

    hol = tempval(valarray[18], valarray[19])
    run = setvaltempdomo(200, hol)

    out = tempval(valarray[20], valarray[21])
    run = setvaltempdomo(196, out)

    cwu = tempval(valarray[22], valarray[23])
    run = setvaltempdomo(198, cwu)

    ret = tempval(valarray[24], valarray[25])
    run = setvaltempdomo(203, ret)

    co  = tempval(valarray[28], valarray[29])
    run = setvaltempdomo(197, co)

    kom = tempval(valarray[30], valarray[31])
    run = setvaltempdomo(202, kom)

    fuel = valarray[75]
    run = setvaltempdomo(201, fuel)
else:
    logging.warning('Bruli response code is ' + str(r.status_code) + ', Content: ' + r.text )

logging.info('Ending')
