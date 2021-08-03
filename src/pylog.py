import datetime
import argparse
def log(location,msg,date=True,file=False):
    """Logs

    Args:
        location ([type]): [description]
        msg ([type]): [description]
        date (bool, optional): [description]. Defaults to True.
        file (bool, optional): [description]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[LOG]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file 

def info(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[INFO]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def debug(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[DEBUG]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def warn(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[WARNING]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file

def error(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[ERROR]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def cerror(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[CRITICAL_ERROR]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def ferror(location,msg,date=True,file=False):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[FATAL_ERROR]"+" "
    if date == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file

def message(location,msg,):
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file

    