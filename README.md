# nvml-statsd
This Python project integrates the NVIDIA management library with statsd to report GPU metrics to a monitoring tool.  To run:
```
docker run -it --rm -v /usr/local/cuda-7.5/targets/x86_64-linux/lib:/nvmlpath:ro -e NVML_PATH=/nvmlpath docker.synapse.org/syn5644795/nvml-statsd
```