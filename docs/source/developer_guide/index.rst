===============
Developer guide
===============

Running the tests
+++++++++++++++++

The following will discover and run all unit test::

    pip install -e .[testing]
    pytest -v

Automatic coding style checks
+++++++++++++++++++++++++++++

Enable enable automatic checks of code sanity and coding style::

    pip install -e .[pre-commit]
    pre-commit install

After this, the `yapf <https://github.com/google/yapf>`_ formatter,
the `pylint <https://www.pylint.org/>`_ linter
and the `prospector <https://pypi.org/project/prospector/>`_ code analyzer will
run at every commit.

If you ever need to skip these pre-commit hooks, just use::

    git commit -n


Continuous integration
++++++++++++++++++++++

``aiida-orca`` comes with a ``.github`` folder that contains continuous integration tests on every commit using `GitHub Actions <https://github.com/features/actions>`_. It will:

#. run all tests for the ``django`` ORM
#. build the documentation
#. check coding style and version number (not required to pass by default)

Building the documentation
++++++++++++++++++++++++++

 #. Install the ``docs`` extra::

        pip install -e .[docs]

 #. Edit the individual documentation pages::

        docs/source/index.rst
        docs/source/developer_guide/index.rst
        docs/source/user_guide/index.rst
        docs/source/user_guide/get_started.rst
        docs/source/user_guide/tutorial.rst

 #. Use `Sphinx`_ to generate the html documentation::

        cd docs
        make

Check the result by opening ``build/html/index.html`` in your browser.

.. _ReadTheDocs: https://readthedocs.org/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
