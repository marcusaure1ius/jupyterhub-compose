# Установка JupyterHub<br/>

Особенности:
- Для аутентификации используется Native Authenticator (учетные записи создаются в самом Jupyter на странице регистрации)
- Для спавна пользовательских серверов используется Docker Spawner (у каждого пользователя отдельный автоподнимаемый контейнер)
- У каждого пользователя отдельный volumne
- Есть настройка для ограничения по использованию RAM

### Сервисы

- `jupyterhub-service` - контейнер, который управляет JupyterHub
- `jupyterhub-user-{username}` - контейнер с образом jupyter/minimal-notebook (набор библиотек для анализа данных)

### Установка

1. Клонируйте репозиторий и перейдите в папку с проектом

```bash
git clone https://github.com/marcusaure1ius/jupyterhub-compose.git
```

2. Сделайте исполняемым файл `clean_install.sh`, который сделает все необходимые приготовления и запустит контенейры

```bash
chmod +x clean_install.sh
```

> [!IMPORTANT]
> При запуске скрипта `clean_install.sh` удаляются все volumes. В случае, если вам необходимо, например, добавить новые библиотеки и сделать новый билд, выполните команду `docker compose down && docker compose up --build -d`
> Для просмотра файлов определенного пользователя можно посмотреть путь до его volume с помощью команды `docker volume inspect jupyterhub-user-admin`

### Использование

Перейдите по адресу `http://YOUR_HOST/:8000` и, если все успешно, вы увидите страницу входа. Для регистрации админа перейдите по ссылке `/signup/` для регистрации

### Референсы

- https://github.com/jupyterhub/jupyterhub-deploy-docker/blob/main/basic-example/docker-compose.yml
- https://native-authenticator.readthedocs.io/en/latest/quickstart.html
- https://jupyterhub-dockerspawner.readthedocs.io/en/latest/
- https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html

##### Автор - https://github.com/marcusaure1ius