## postgresql settings
docker run --name test1-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test1-db -p 5432:5432 -d postgres

## python version
python3.11

## How to start?
```
docker run --name test1-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test1-db -p 5432:5432 -d postgres

pip install -r requirements.txt

python main.py
```