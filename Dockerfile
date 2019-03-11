FROM python:3

WORKDIR /usr/src/polititweet

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY polititweet .

EXPOSE 8000

CMD [ "./launch.sh" ]