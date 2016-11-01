#!/usr/local/bin/python2.7
# encoding: utf-8
#
# See https://developer.nvidia.com/nvidia-management-library-nvml
# See https://github.com/npinto/pynvml/blob/master/pynvml.py
#
# Author: Bruce Hoff
# Author: Thomas Schaffter (thomas.schaff...@gmail.com)

import statsd
from pynvml import *
import time
import os
import signal

def signal_handler(signal, frame):
	print('Shutting down.')
	sys.exit(1)

def main(argv=None):
	nvmlInit()
	c = statsd.StatsClient(os.environ['statsd_host'], 8125)
    
	print "Driver Version:", nvmlSystemGetDriverVersion()
	deviceCount = nvmlDeviceGetCount()

	while (True):
		for i in range(deviceCount):
			handle = nvmlDeviceGetHandleByIndex(i)
			info = nvmlDeviceGetMemoryInfo(handle)
			c.gauge("gpu.memory.total-"+str(i), info.total)
			c.gauge("gpu.memory.free-"+str(i), info.free)
			c.gauge("gpu.memory.used-"+str(i), info.used)
			c.gauge("gpu.power.state-"+str(i), nvmlDeviceGetPowerState(handle))
			c.gauge("gpu.power.usage-"+str(i), nvmlDeviceGetPowerUsage(handle))
			c.gauge("gpu.temperature-"+str(i), nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU))
			#c.gauge("gpu.fan.speed-"+str(i), nvmlDeviceGetFanSpeed(handle)) # not supported
			c.gauge("gpu.clock.graphics-"+str(i), nvmlDeviceGetClockInfo(handle, NVML_CLOCK_GRAPHICS))
			c.gauge("gpu.clock.sm-"+str(i), nvmlDeviceGetClockInfo(handle, NVML_CLOCK_SM))
			c.gauge("gpu.clock.mem-"+str(i), nvmlDeviceGetClockInfo(handle, NVML_CLOCK_MEM))
			info = nvmlDeviceGetUtilizationRates(handle)
			c.gauge("gpu.utilization.gpu-"+str(i), info.gpu)
			c.gauge("gpu.utilization.memory-"+str(i), info.memory)

		print "NVML metrics pushed to statsd"
		time.sleep(60)

	nvmlShutdown()
	return 0

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	signal.signal(signal.SIGTERM, signal_handler)
	sys.exit(main())
