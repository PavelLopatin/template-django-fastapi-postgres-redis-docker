# simpliest django(uvicorn)+postgresql+fastapi+redis+nginx docker-compose (ready for production and dev)
To run:
`docker-compose up -d`

Site available on 8000 port.

You can make any changes in code, they will appear automatically. If you want to execute something with manage.py use:
```
docker-compose exec app python3 manage.py migrate
docker-compose exec app python3 manage.py makemigrations
docker-compose exec app python3 manage.py update_admin admin adminpass # create superuser
```
and so on.
