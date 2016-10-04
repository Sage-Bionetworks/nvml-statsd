# nvml-statsd
This Python project integrates the NVIDIA management library with statsd to report GPU metrics to a monitoring tool.  
Example run command:
```
docker run -d --device /dev/nvidia0:/dev/nvidia0 --device /dev/nvidia1:/dev/nvidia1 --device /dev/nvidia2:/dev/nvidia2 --device /dev/nvidia3:/dev/nvidia3 --device /dev/nvidiactl:/dev/nvidiactl --device /dev/nvidia-uvm:/dev/nvidia-uvm -v /usr/lib64/libnvidia-ml.so.1:/usr/lib64/libnvidia-ml.so.1:ro -v /usr/lib64/libnvidia-ml.so.352.99:/usr/lib64/libnvidia-ml.so.352.99:ro --name nvml-statsd docker.synapse.org/syn5644795/nvml-statsd 
```
Note:  using `nvidia-docker run` rather than `docker-run` allows you to omit the device mounts, which nvidia-docker will add for you.
