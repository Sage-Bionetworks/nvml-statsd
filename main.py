#!/usr/local/bin/python2.7
# encoding: utf-8
import statsd
from pynvml import *
import time
import os

def main(argv=None):
    nvmlInit()
    c = statsd.StatsClient(os.environ['statsd_host'], 8125)
    
    print "Driver Version:", nvmlSystemGetDriverVersion()
    deviceCount = nvmlDeviceGetCount()
    
    while (True): # TODO if there's a shutdown signal then break from this loop
        for i in range(deviceCount):
            handle = nvmlDeviceGetHandleByIndex(i)
            info = nvmlDeviceGetMemoryInfo(handle)
            c.gauge("gpu.memory.total-"+str(i), info.total)
            c.gauge("gpu.memory.free-"+str(i), info.free)
            c.gauge("gpu.memory.used-"+str(i), info.used)
        time.sleep(60)
    
    nvmlShutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())