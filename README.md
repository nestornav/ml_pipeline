# ML pipeline

This little project try to show up an end-to-end machine learning pipeline. Try to show up a macro view of a machine learning project, not just focused in the model exploration and generation.
Machine learning projects are colorful and depends on the companies, project size and so on. However in this humble project I created at least the common parts you will facing up.
This pipeline isn't integrated into a specific platform such as Airflow. The solution are isolated files, that can be then extrapolated to a DAG for Airflow for example later.


## Project Installation

This project is managed by Poetry. It is a tool for dependency management and packaging in Python.
> Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies. This is the recommended way of installing poetry.
> You only need to install Poetry once. It will automatically pick up the current Python version and use it to create virtualenvs accordingly.

### Installing Poetry

Follow the next steps to get Poetry working on your system. For more information check their documentation [here](https://python-poetry.org/docs/#installation).

#### osx / linux

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Open a fresh terminal and check if all goes right

```
poetry --version
```

### Project dependencies installation

```
poetry install
```
