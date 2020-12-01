import threading
from threading import *
import time
import json

#https://github.com/sriharsha9598/CRD-operations-of-a-file-based-key-value-data-store

f=open("data.json",)
d=json.load(f)

def create(key, value, timeout=0):
    if key in d:
        print("error: this key already exists")  # error message1
    else:
        if (key.isalpha()):
            if len(d) < (1024 * 1020 * 1024) and value <= (
                    16 * 1024 * 1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    d[key] = l
            else:
                print("Error: Memory limit exceeded!! ")  # error message2
        else:
            print(
                "Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")  # error message3



def read(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key")  # error message4
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:
                stri = str(key) + ":" + str(
                    b[0])
                return stri
            else:
                print("Error: time-to-live of", key, "has expired")  # error message5
        else:
            stri = str(key) + ":" + str(b[0])
            return stri



def delete(key):
    if key not in d:
        print("Error: Given key does not exist in database. Please enter a valid key")  # error message4
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")  # error message5
        else:
            del d[key]
            print("key is successfully deleted")





def modify(key, value):
    b = d[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key")  # error message6
            else:
                l = []
                l.append(value)
                l.append(b[1])
                d[key] = l
        else:
            print("error: time-to-live of", key, "has expired")  # error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key")  # error message6
        else:
            l = []
            l.append(value)
            l.append(b[1])
            d[key] = l

