#!/usr/bin/env python
<<<<<<< HEAD
=======
"""Django's command-line utility for administrative tasks."""
>>>>>>> 1fd53bc81600c97dba14ba080ca23a590d233dfb
import os
import sys


def main():
<<<<<<< HEAD
=======
    """Run administrative tasks."""
>>>>>>> 1fd53bc81600c97dba14ba080ca23a590d233dfb
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
<<<<<<< HEAD
=======
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
>>>>>>> 1fd53bc81600c97dba14ba080ca23a590d233dfb
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> 1fd53bc81600c97dba14ba080ca23a590d233dfb
