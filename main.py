#!/usr/local/bin/python2.7
# encoding: utf-8
import sys
import os
import statsd
from pynvml import *

def main(argv=None): # IGNORE:C0111
    # add library to search path
    #os.environ['PATH'] += ":"+os.environ['NVML_PATH']
    nvmlInit()
    c = statsd.StatsClient('localhost', 8125)
    
    print "Driver Version:", nvmlSystemGetDriverVersion()
    deviceCount = nvmlDeviceGetCount()
    # can I push the device count to statsd??
    c.gauge('deviceCount', deviceCount)
    
    for i in range(deviceCount):
        handle = nvmlDeviceGetHandleByIndex(i)
        print "Device", i, ":", nvmlDeviceGetName(handle)
    
    nvmlShutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())