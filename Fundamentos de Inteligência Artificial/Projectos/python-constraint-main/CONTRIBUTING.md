# Contributing

If you discover issues, have ideas for improvements or new features, please report them to the [issue tracker](https://github.com/python-constraint/python-constraint/issues).
After this you can help by fixing it submitting a pull request (PR).
Please, try to follow these guidelines when you do so.

## Issue reporting

* Check that the issue has not already been reported.
* Check that the issue has not already been fixed in the latest code (a.k.a. `main`).
* Be clear, concise and precise in your description of the problem.
* Open an issue with a descriptive title and a summary in grammatically correct, complete sentences.
* Mention your Python version and operating system.
* Include any relevant code to the issue summary.

A [Minimal Working Example (MWE)](https://en.wikipedia.org/wiki/Minimal_Working_Example) can help.

### Reporting bugs

When reporting bugs it's a good idea to provide stacktrace messages to the bug report makes it easier to track down bugs. 
Some steps to reproduce a bug reliably would also make a huge difference.

## Pull requests

* Read [how to properly contribute to open source projects on Github](http://gun.io/blog/how-to-github-fork-branch-and-pull-request).
* Use a topic branch to easily amend a pull request later, if necessary.
* Make sure that all tests are passing (run `nox`). This will be checked via GitHub Actions tests, so not meeting the tests will result in rejection. 
* Use the same coding conventions as the rest of the project, can easily be checked by running `nox -s lint`. This is enforced by `ruff` on pull requests, so not doing this will result in rejection. 
* Write good, descriptive commit messages.
* Mention related tickets in the commit messages (e.g. `[Fix #N] Add command ...`).
* Update the [changelog](https://github.com/python-constraint/python-constraint/blob/main/CHANGELOG.md).
* Squash related commits together.
* Open a [pull request](https://help.github.com/articles/using-pull-requests) that relates to *only* one subject with a clear title and description in grammatically correct, complete sentences.
