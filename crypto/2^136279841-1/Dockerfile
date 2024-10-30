FROM python:3.11-slim AS app
RUN pip3 install --no-cache-dir pycryptodome

RUN useradd -ms /bin/bash ctf

USER root
RUN apt-get -y update
RUN apt-get -y install socat build-essential gcc-multilib g++-multilib libc6

WORKDIR /home/ctf
COPY m136279841.py .

RUN chown -R root:root /home/ctf
RUN chmod -R 755 /home/ctf
RUN chmod 755 m136279841.py

ENV FLAG="tyroCTF{w0rld'5_l4r6357_pr1m3}"

USER ctf
EXPOSE 1337
CMD socat TCP-LISTEN:1337,reuseaddr,fork 'EXEC:./m136279841.py'
