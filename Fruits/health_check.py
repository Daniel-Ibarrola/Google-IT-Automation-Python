#!/usr/bin/env python3
import os
import psutil
import shutil
import socket
import sys
from emails import generate_error_report
from emails import send_email

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage"""
    return psutil.cpu_percent(1) > 80

#print()

def check_memory():
    """Returns true if  available memory is less than 500MB"""
    memory = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024  # 500MB
    if memory.available <= threshold:
        return True
    else:
        return False

def check_disk_full(disk, min_percent):
    """Returns True if there is not enough free diskspace, otherwise false."""
    total, used, free = shutil.disk_usage("/")
    percent_free = 100 * free/total
    if percent_free < min_percent:
        return True
    else:
        return False

def check_root_full():
    """Returns true if the root partition is full, False otherwise"""
    return check_disk_full(disk='/', min_percent=20)

def check_no_network():
    """Returns True if it fails to resolve the URL, False otherwise"""
    try:
        socket.gethostbyname('127.0.0.1')
        return False
    except:
        return True

def main(argv):
    checks = [
        (check_cpu_constrained, 'Error - CPU usage is over 80%'),
        (check_memory, 'Error - Available memory is less than 500MB'),
        (check_root_full, 'Error - Available disk space is less than 20%'),
        (check_no_network, 'Error - localhost cannot be resolved to 127.0.0.1')
    ]
    everything_ok= True
    for check, msg in checks:
        if check():
            email_msg = generate_error_report('automation@example.com',
                     'student-02-faee917e59b7@example.com',
                     msg,
                     'Please check your system and resolve the issue as soon as possible.')
            send_email(email_msg)
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)


    print('Everything ok.')
    sys.exit(0)

if __name__ == "__main__":
  main(sys.argv)
