FROM python:2.7
RUN pip install statsd
RUN pip install nvidia-ml-py
COPY main.py /main.py
CMD python /main.py
