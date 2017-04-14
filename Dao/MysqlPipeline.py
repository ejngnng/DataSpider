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

def insert_data_api1(item):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='ninja123',
        db='China6_DB',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into letv_all_1(markid,aid,name,subname,category,categoryName,images_1,images_2,episodes,nowEpisodes,isEnd,play,jump,pay) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                           (item['markid'],
                            item['aid'],
                            item['name'],
                            item['subname'],
                            item['category'],
                            item['categoryName'],
                            item['images']['200*150'],
                            item['images']['400*300'],
                            item['episodes'],
                            item['nowEpisodes'],
                            item['isEnd'],
                            item['play'],
                            item['jump'],
                            item['pay']))
            connection.commit()
    except:
        print("insert data api1 failed!!!")
    finally:
        connection.close()

def insert_data_api2(item):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123',
        db='letv_DB',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into letv_all_2(markid, \
            alias,\
            playStatus,\
            cast,\
            fitAge,\
            originator, \
            supervise, \
            dub, \
            rCompany, \
            isHomemade, \
            aid, \
            nameCn, \
            albumTypeKey, \
            varietShow, \
            albumType, \
            subTitle, \
            picCollections_1, \
            picCollections_2, \
            picCollections_3, \
            picCollections_4, \
            score, \
            cid, \
            type, \
            at, \
            releaseDate, \
            platformVideoNum, \
            platformVideoInfo, \
            epsiode, \
            nowEpsiode, \
            isEnd, \
            duration, \
            directory, \
            starring, \
            compere, \
            description, \
            area, \
            language, \
            instructor, \
            subCategory, \
            style, \
            playTv, \
            school, \
            controlAreas, \
            disableType, \
            play, \
            jump, \
            pay, \
            download, \
            tag, \
            relationAlbumID, \
            relationId, \
            subcid) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                           (item['markid'],
                            item['alias'],
                            item['playStatus'],
                            item['cast'],
                            item['fitAge'],
                            item['originator'],
                            item['supervise'],
                            item['dub'],
                            item['rCompany'],
                            item['isHomemade'],
                            item['id'],
                            item['nameCn'],
                            item['albumTypeKey'],
                            item['varietyShow'],
                            item['albumType'],
                            item['subTitle'],
                            item['picCollections']['150*200'],
                            item['picCollections']['300*300'],
                            item['picCollections']['400*300'],
                            item['picCollections']['320*200'],
                            item['score'],
                            item['cid'],
                            item['type'],
                            item['at'],
                            item['releaseDate'],
                            item['platformVideoNum'],
                            item['platformVideoInfo'],
                            item['episode'],
                            item['nowEpisodes'],
                            item['isEnd'],
                            item['duration'],
                            item['directory'],
                            item['starring'],
                            item['compere'],
                            item['description'],
                            item['area'],
                            item['language'],
                            item['instructor'],
                            item['subCategory'],
                            item['style'],
                            item['playTv'],
                            item['school'],
                            item['controlAreas'],
                            item['disableType'],
                            item['play'],
                            item['jump'],
                            item['pay'],
                            item['download'],
                            item['tag'],
                            item['relationAlbumId'],
                            item['relationId'],
                            item['subcid']))
            connection.commit()
    except:
        print("insert data api2 failed!!!")
    finally:
        connection.close()


def insert_data_api3(item):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123',
        db='letv_DB',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into letv_all_3(markid, \
            videoID, \
            cid, \
            nameCn, \
            subTitle, \
            singer, \
            guest, \
            type, \
            btime, \
            etime, \
            duration, \
            mid, \
            episode, \
            porder, \
            pay, \
            download, \
            picAll_1, \
            picAll_2, \
            picAll_3, \
            play, \
            jump, \
            brList_1, \
            brList_2, \
            brList_3, \
            videoType, \
            videoTypeKey, \
            controlAreas, \
            disableType, \
            totalNum, \
            episodeNum) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s, \
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                           (item['markid'],
                            item['id'],
                            item['cid'],
                            item['nameCn'],
                            item['subTitle'],
                            item['singer'],
                            item['guest'],
                            item['type'],
                            item['btime'],
                            item['etime'],
                            item['duration'],
                            item['mid'],
                            item['episode'],
                            item['porder'],
                            item['pay'],
                            item['download'],
                            item['picAll']['120*90'],
                            item['picAll']['200*150'],
                            item['picAll']['320*200'],
                            item['play'],
                            item['jump'],
                            item['brList'][0],
                            item['brList'][1],
                            item['brList'][2],
                            item['videoType'],
                            item['videoTypeKey'],
                            item['controlAreas'],
                            item['disableType'],
                            item['totalNum'],
                            item['episodeNum']))
            connection.commit()
    except:
        print("insert data api3 failed!!!")
    finally:
        connection.close()

def insert_proxy_url(proxy_url):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123',
        db='letv_DB',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("insert into proxy_ip(ip) values(%s)",  proxy_url)
            connection.commit()
    except:
        print("insert data proxy failed!!!")
    finally:
        connection.close()

