flask-tutorial
==============

Implementation of Miguel Grinberg's Flask Mega Tutorial

Latest section finished: Part 3 - Webforms

To do: 1) Write Gherkin features/scenarios and use behaving to test web app
       2) Part 4 - Database


To run the BDD tests just run 'behave' on the command line (with the virtual environment activated).

# Notes:

1. If behave complains about the 'six' package like this:
```
pkg_resources.DistributionNotFound: six
```
... then uninstall six and install using easy_install instead of pip:

```
pip uninstall six
easy_install six
```