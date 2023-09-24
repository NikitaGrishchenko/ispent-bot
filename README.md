ispent

1 Доход 
0 Расход

docker-compose -f .\docker\docker-compose.dev.yml --env-file .\.env up -d

docker build -t grishchenkonikita/aiogram -f .\docker\Dockerfile .

docker push grishchenkonikita/aiogram