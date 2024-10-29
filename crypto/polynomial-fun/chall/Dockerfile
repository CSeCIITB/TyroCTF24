FROM python:3.11-slim AS app
RUN pip3 install --no-cache-dir cryptography

RUN useradd -ms /bin/bash ctf

USER root
RUN apt-get -y update
RUN apt-get -y install socat build-essential gcc-multilib g++-multilib libc6

WORKDIR /home/ctf
COPY . .

RUN chown -R root:root /home/ctf
RUN chmod -R 755 /home/ctf
RUN chmod 755 server.py


USER ctf
EXPOSE 1337
CMD socat TCP-LISTEN:1337,reuseaddr,fork 'EXEC:./server.py'
