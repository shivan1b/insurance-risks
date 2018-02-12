Insurance Risks
==============================

__Version:__ 0.0.1

An insurance risk app that lets the insurer add risks and as many number of fields of different types as they want.

## Getting up and running

Minimum requirements: **pip, zappa, python3.6 & [postgres][install-postgres]**, setup is tested on Linux (Debian family) only.

```
sudo apt install postgres
pip install zappa
```

[install-postgres]: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04

In your terminal, type or copy-paste the following:

    git clone git@github.com:shivan1b/django-dynamic-models.git; cd django-dynamic-models; virtualenv -p python3.6 venv; source venv/bin/activate

Go grab a cup of coffee, we bake your hot development machine.

Useful commands:

- python manage.py runserver
- zappa init

**NOTE:** Make sure your AWS credentials ae in place. Checkout `zappa_settings.json` for all the information related to deployment.


## Deploying Project

Make sure you install and run `zappa` in virtual environment.
Deploying the project is as simple as
```
zappa deploy <environment_name>
````

After making any updates to the project, just do
```
zappa update <environment_name>
```

## How to release Insurance risks

Execute the following commands:

```
git checkout master
git push origin master
```

## Contributing

Golden Rule:

> Anything in **master** is always **deployable**.

Avoid working on `master` branch, create a new branch with meaningful name, send pull request asap. Be vocal!

Refer to [CONTRIBUTING.md][contributing]

[contributing]: http://github.com/shivan1b/django-dynamic-models/tree/master/CONTRIBUTING.md
