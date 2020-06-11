#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

path_ = sys.path[0]
# sys.path.append("/private/var/mobile/Containers/Shared/AppGroup/BF6D28F7-8CDD-43FE-AAB3-F1369C817B0C/File Provider Storage/Repositories/test_project/mysite")
sys.path.append(path_)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
