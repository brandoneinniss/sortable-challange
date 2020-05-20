FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY auction auction
COPY execute.sh execute.sh
RUN ["chmod", "+x", "/execute.sh"]
CMD /execute.sh
