import os
import nativeauthenticator
import shutil

c = get_config()

# Настройки JupyterHub
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.bind_url = 'http://:8000'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]

# Настройка спаунера (используется DockerSpawner)
c.Spawner.mem_limit = '2G'
c.Spawner.default_url = '/lab'
c.DockerSpawner.image = 'jupyter-user-image'
c.DockerSpawner.network_name = 'jupyterhub-network'
c.DockerSpawner.notebook_dir = '/home/jovyan/work'
c.DockerSpawner.volumes = {'jupyterhub-user-{username}': '/home/jovyan/work', '/home/administrator/engineering': '/home/jovyan/work/shared'}
c.DockerSpawner.remove = True

# Настройки аутентификатора (используется NativeAuthenticator)
c.Authenticator.allow_all = True
c.Authenticator.check_common_password = True
c.Authenticator.ask_email_on_signup = True
c.Authenticator.admin_users = {'admin'}
c.NativeAuthenticator.minimum_password_length = 8
c.NativeAuthenticator.allowed_failed_logins = 3
c.NativeAuthenticator.seconds_before_next_try = 600
c.NativeAuthenticator.enable_signup = True
c.NativeAuthenticator.open_signup = True

host_notebook_dir = os.environ.get('HOST_NOTEBOOK_DIR')

# Заменяем монтирование Docker-тома на монтирование папки с хоста
if host_notebook_dir:
    c.DockerSpawner.volumes = {
        f'{host_notebook_dir}/{{username}}': '/home/jovyan/work'
    }
