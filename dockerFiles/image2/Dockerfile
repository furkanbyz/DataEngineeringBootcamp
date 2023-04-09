FROM python:3.8
# python üzerinden çalışacağız

RUN  mkdir /code
# code isimli klasör oluşturuldu

WORKDIR /code
# klasörü, çalışma dizini olarak seçildi

COPY requirements.txt .
COPY requirements.txt /root
# requirement.txt ayarları ilgili dizinlere kopyalandı
# . var olan dizin demek "./" gibi

RUN pip install -r requirements.txt
# requirements.txt içindeki gereklilikleri image içine yüklendi

COPY . .
# asıl    COPY source dest     format budur

CMD ["uvicorn","main:app","--host=0.0.0.0.","--port=8000"]
# 8000 containerın portu