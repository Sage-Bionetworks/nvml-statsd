#!/usr/local/bin/python2.7
# encoding: utf-8
import statsd
from pynvml import *
import time

def main(argv=None):
    nvmlInit()
    c = statsd.StatsClient('localhost', 8125)
    
    print "Driver Version:", nvmlSystemGetDriverVersion()
    deviceCount = nvmlDeviceGetCount()
    
    while (True): # TODO if there's a shutdown signal then break from this loop
        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            info = nvmlDeviceGetMemoryInfo(handle)
            c.gauge("Total Memory GPU-"+str(i), info.total)
            c.gauge("Free Memory GPU-"+str(i), info.free)
            c.gauge("Used Memory GPU-"+str(i), info.used)
        time.sleep(60)
    
    nvmlShutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())