#!/bin/bash

cd "$(dirname "$0")"

# Определяем, что доступно: docker compose или docker-compose
if docker compose version >/dev/null 2>&1; then
    DC="docker compose"
elif docker-compose version >/dev/null 2>&1; then
    DC="docker-compose"
else
    echo "Ошибка: docker compose не найден в системе"
    exit 1
fi

echo "Шаг 1: Сборка пользовательского образа Docker..."
docker build -t jupyter-user-image ./user-image

echo "Шаг 1.2: Поиск и удаление старых пользовательских контейнеров..."
CONTAINER_IDS=$(docker ps -a -q --filter "name=jupyter-")

if [ -n "$CONTAINER_IDS" ]; then
    echo "Найдены следующие контейнеры для удаления:"
    docker ps -a --filter "name=jupyter-" --format '{{.Names}}'
    docker rm -f $CONTAINER_IDS
    echo "Старые пользовательские контейнеры успешно удалены."
else
    echo "Старых пользовательских контейнеров не найдено."
fi

echo "Шаг 1.3: Поиск и удаление старых пользовательских томов..."
VOLUME_NAMES=$(docker volume ls -q --filter "name=jupyterhub-user-")

if [ -n "$VOLUME_NAMES" ]; then
    echo "Найдены следующие тома для удаления:"
    docker volume ls --filter "name=jupyterhub-user-" --format '{{.Name}}'
    docker volume rm -f $VOLUME_NAMES
    echo "Старые пользовательские тома успешно удалены."
else
    echo "Старых пользовательских томов не найдено."
fi

echo "Шаг 2: Запуск сервисов через docker-compose..."

$DC down -v --remove-orphans
$DC up -d --build