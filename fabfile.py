from fabric.api import *


__author__ = 'Andrey Shipilov <a@andreyshipilov.com>'

env.project_name = 'andreyshipilov'
env.hosts = ['tezro.webfactional.com']
env.user = 'tezro'
env.venv_path = '../andreyshipilov_venv'


@task
def prod():
    """
    Sets production environment variables.
    """
    env.type = 'prod'
    env.settings = '{0}.settings.prod'.format(env.project_name)
    env.settings_args = '--settings={0}.settings.{1}'.format(env.project_name, env.type)
    env.root_dir = '/home/tezro/django_projects/{0}/{1}_django'.format(env.project_name, env.project_name)


@task
def restart():
    """
    Restarts Apache service.
    """

    with cd(env.root_dir):
        run('uwsgi --reload ~/pids/andreyshipilov_uwsgi.pid')
        run('~/bin/nginx -s reload')


@task
def update():
    """
    Updates the code from GIT. Installs all the requirements. Syncs database.
    Migrates schema changes. Collects static files.
    """

    with cd(env.root_dir):
        run('git pull')
        with prefix(". {0}/{1}/bin/activate".format(env.root_dir, env.venv_path)):
            run('pip install -r requirements/{0}.txt'.format(env.type))
            run('python manage.py migrate {0}'.format(env.settings_args))
            run('python manage.py collectstatic --noinput {0}'.format(env.settings_args))
            run('python manage.py compilemessages {0}'.format(env.settings_args))


@task
def clear_cache():
    """
    Clears 'sorl.thumbnail' cache and Django cache set by the settings.
    """
    with cd(env.root_dir):
        with prefix(". {0}/{1}/bin/activate".format(env.root_dir, env.venv_path)):
            run('python manage.py thumbnail cleanup {0}'.format(env.settings_args))
            run('python manage.py clear_cache {0}'.format(env.settings_args))


@task
def deploy():
    """
    Deploys the project using selected settings.
    Runs all the needed commands one after another.
    """
    update()
    clear_cache()
    restart()
