FROM python:3.12-slim

LABEL "com.gmc.navin3d"="smnavin65@gmail.com"
LABEL version="0.1"

WORKDIR /usr/app

COPY pyproject.toml .
RUN uv sync

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]