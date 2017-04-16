#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################################################
#
# Description: for mysql driver
#
# Author:      ninja
#
# Date:        created by 2017-04-05
#
###################################################

import pymysql

def connectDB():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='ninja123',
        db='China6_DB',
        charset='utf8mb4',
    )
    return connection

def insert_data(connection, item):
    printItem(item)
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='ninja123',
    #     db='China6_DB',
    #     charset='utf8mb4',
    # )

    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into car_desc(carNum, \
            carType,\
            startLocation,\
            endLocation,\
            midLocation,\
            releaseTime, \
            driveTime, \
            price, \
            comments, \
            carLen, \
            carLoad, \
            carAddr, \
            carStatus, \
            carContacts, \
            phoneNum, \
            carID) values(%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s)", \
                           (item[0],
                            item[1],
                            item[2],
                            item[3],
                            item[4],
                            item[5],
                            item[6],
                            item[7],
                            item[8],
                            item[10],
                            item[11],
                            item[12],
                            item[14],
                            item[15],
                            item[16],
                            item[17]))

            connection.commit()
    except:
        print("insert data failed!!!")
    # finally:
    #     connection.close()

def disconnectDB(connection):
    connection.close()

def printItem(item):
    print('=====================')
    print('item[0]:' + item[0])
    print('item[1]:' + item[1])
    print('item[2]:' + item[2])
    print('item[3]:' + item[3])
    print('item[4]:' + item[4])
    print('item[5]:' + item[5])
    print('item[6]:' + item[6])
    print('item[7]:' + item[7])
    print('item[8]:' + item[8])
    print('item[10]:' + item[10])
    print('item[11]:' + item[11])
    print('item[12]:' + item[12])
    print('item[14]:' + item[14])
    print('item[15]:' + item[15])
    print('item[16]:' + item[16])
    print('item[17]:' + item[17])
    print('====================')