FROM python:3.8.2
COPY /file_helper.py /file_helper.py
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "file_helper.py"]