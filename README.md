#ML pipeline

This little project try to show up an end-to-end machine learing pipeline.
Machine learning are colofull and depends on the companies, project size and so on. However in this humble project I created at least the common parts.


##Installation

### Virtualenvwrapper

```
pip install virtualenvwrapper
```
Set up some env vars
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
Now you are ready to use it! Let's create a virtualenv

```
mkvirtualenv ml_pipe
```

If you are using python 2.7 as default also you can do the following command to use python3.X in your virtualenv

```
mkvirtualenv $(which python3) ml_pipe
```
