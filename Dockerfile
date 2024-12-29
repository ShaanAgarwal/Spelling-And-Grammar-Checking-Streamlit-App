FROM python:3.10

WORKDIR /app

ADD . /app/

RUN pip3 install -r requirements.txt

#entrypoint
ENTRYPOINT [ "streamlit", "run" ]

CMD ["app.py"]