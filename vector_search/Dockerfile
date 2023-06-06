FROM pytorch/pytorch:1.8.1-cuda11.1-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "embeddings.py"]