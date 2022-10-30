FROM python
WORKDIR ../Ex2
RUN apt-get update
RUN apt-get install tk
RUN apt-get install libx11-dev
RUN apt-get install python3-tk -y
RUN pip install pandas
RUN pip install matplotlib
RUN apk add g++ jpeg-dev zlib-dev libjpeg make
COPY . ../Ex2
ADD plot /
CMD [ "python", "./plot" ]