bigtrees-flask
--------------

.. image:: https://travis-ci.org/tensorjack/bigtrees-flask.svg?branch=master
    :target: https://travis-ci.org/tensorjack/bigtrees-flask

.. image:: https://coveralls.io/repos/tensorjack/bigtrees-flask/badge.png
  :target: https://coveralls.io/r/tensorjack/bigtrees-flask

Minimal "read from a csv in response to a user request, then show them the results" example web app, created using `Flask <http://flask.pocoo.org/>`__.

Installation
~~~~~~~~~~~~

First, clone this repository onto your computer by entering the following command into the terminal:

::

    $ git clone https://github.com/tensorjack/bigtrees-flask

Once it is downloaded, go into the ``bigtrees-flask`` directory and install the app's dependencies (by convention, these are listed in a ``requirements.txt`` file):

::

    $ cd bigtrees-flask
    $ pip install -r requirements.txt

The second command installs the dependencies required by bigtrees-flask to run -- in this case, just Flask itself.  Note: if you are not using a virtual environment, you may need to prepend ``sudo`` to the second command.

Usage
~~~~~

To run the web app on your localhost, go into the ``bigtrees-flask`` directory, and type:

::
   
    $ python app.py

Open up your web browser and go to ``http://127.0.0.1:5000``.  Voila!

Tests
~~~~~

To illustrate how you can test a web app, I sketched out a few simple unit tests.  They're in the ``/tests`` directory.  To run these:

::

    $ pip install -r test_requirements.txt
    $ py.test tests/test_app.py --doctest-modules -v --cov app --cov-report term-missing

The cov and cov-report flags in the ``py.test`` command tells py.test to generate a coverage report -- that is, a report that tells you what lines in ``app.py`` are not covered by the unit tests.  (Ideally, you want coverage to be at 100%.  However, for web apps, there is often some "boilerplate" code that is not run during tests, such as the lines in the ``if __name__ == "__main__"`` block.)

Test results will appear in your terminal.  If you want to access the coverage report later, it is stored in a file called ``.coverage`` (in the same directory).
