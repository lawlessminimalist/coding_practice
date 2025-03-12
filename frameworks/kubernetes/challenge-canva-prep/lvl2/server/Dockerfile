FROM python

WORKDIR /src

COPY server.py .

RUN ["mkdir","files"]

EXPOSE 8080

CMD [ "python","server.py" ]
