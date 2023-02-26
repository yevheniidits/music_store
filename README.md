# Music Store API
### GeekHub Python course demo project

## Description
A platform used for educational purposes, 
demonstration of various libraries, practices, etc.

## Usage
The project is launched inside Docker containers. 

Run the `bin/setup` script to build the `docker-compose.yml` file 
and give confirmation to start the containers. 

To interact with the Django application, 
use the script `bin/manage <command>` (e.g. `bin/manage migrate`). 
If you make changes to the requirements, 
do not forget to re-build the `docker-compose.yml` 
with `docker-compose build` or simply use `bin/setup` script.

## Requirements
You must have Docker Desktop installed in your system 
(or use CLI application if you are Linux user).
For more details please visit https://www.docker.com/.

## FAQ
### django-extensions
To use Python/Django console as `django-extensions`'s Shell Plus with showing SQL queries
replace code in `settings -> Build, Execution, Deployment -> Console -> Django Console` with 
```python
import sys;

print("Python {} on {}".format(sys.version, sys.platform))
import django;

print("Django {}".format(django.get_version()))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
if "setup" in dir(django): django.setup()
from django_extensions.management.shells import import_objects
from django.core.management.color import color_style

style = color_style(force_color=True)

globals().update(import_objects({"dont_load": [], "quiet_load": False}, style))

from django_extensions.management.debug_cursor import monkey_patch_cursordebugwrapper

monkey_patch_cursordebugwrapper(print_sql=True).__enter__()  # activate monkey patch inside context manager
import django_manage_shell;

django_manage_shell.run(PROJECT_ROOT)
```

