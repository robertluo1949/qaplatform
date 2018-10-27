#coding:utf-8
'''
title:打印日志功能
author:Robert
date:20171127
email:luoshuibo@vcredut.com
content:
other:
'''
# 第一步，创建一个logger


import logging
import datetime
import config



# loggername='UCEX StessTesting'
loggername = config.OBJ_LOGGER

if config.LOG_LEVEL == "CRITICAL":
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.CRITICAL)

    try:
        fh = logging.FileHandler(config.FILE_LOGGER)
    except FileNotFoundError as ex_f:
        print("file not fund error", ex_f)

    fh.setLevel(logging.CRITICAL)

    ch = logging.StreamHandler()
    ch.setLevel(logging.CRITICAL)

elif config.LOG_LEVEL == "ERROR":
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.ERROR)

    try:
        fh = logging.FileHandler(config.FILE_LOGGER)
    except FileNotFoundError as ex_f:
        print("file not fund error",ex_f)

    fh.setLevel(logging.ERROR)

    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)


elif config.LOG_LEVEL == "INFO":
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.INFO)

    try:
        fh = logging.FileHandler(config.FILE_LOGGER)
    except FileNotFoundError as ex_f:
        print("file not fund error", ex_f)

    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

elif config.LOG_LEVEL == "DEBUG":
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)

    try:
        fh = logging.FileHandler(config.FILE_LOGGER)
    except FileNotFoundError as ex_f:
        print("file not fund error", ex_f)

    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)



