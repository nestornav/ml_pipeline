# ML pipeline

This little project try to show up an end-to-end machine learning pipeline. Try to show up a macro view of a machine learning project, not just focused in the model exploration and generation.
Machine learning projects are colorful and depends on the companies, project size and so on. However in this humble project I created at least the common parts you will facing up.
This pipeline isn't integrated into a specific platform such as Airflow. The solution are isolated files, that can be then extrapolated to a DAG for Airflow for example later.


## Working with the project

This project is handled by [Poetry](https://python-poetry.org/docs/). This tool handle your project dependencies as well as a virtual environment to work.

### Installing Poetry

The next lines are from Poetry documentation. For further information about how to works and advanced configuration go the official doc.

**osx/linux**
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Run the following command to check that all is right

```
poetry --version
```

### Project initialization

```
poetry init
```
