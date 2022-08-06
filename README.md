# ikamate
Splatoon3レーティングシステム


## ローカルへの開発環境の構築

```
cp .env.sample .env
vim .env
docker compose up -d
docker compose exec webapp bash
python manage.py migrate
python manage.py createsuperuser
```

## Dockerコマンド
'''
docker compose up -d
docker compose down
docker compose ps
docker compose restart
'''
