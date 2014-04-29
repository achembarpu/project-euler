How To Contribute
=============

You can:

* discuss ideas via the [Wiki](https://github.com/arvindch/project-euler/wiki), comments or email.
* contribute your alternative solutions and improvements via [Pull Requests](https://github.com/arvindch/project-euler/pulls).
* report bugs via the [Issue Tracker](https://github.com/arvindch/project-euler/issues).

## Workflow

#### System Setup

* Required: (minimum versions)
  * Python - [2.7.x](https://www.python.org/download/releases/2.7.6/)
  * GCC - [4.7.x](http://gcc.gnu.org/gcc-4.7/)
  * JDK - [7ux](http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html)
  * Git - [latest](http://git-scm.com/downloads)
* Recommended:
  * OS - [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/)
  * IDE - [Eclipse Standard 4.3.2](https://www.eclipse.org/downloads/packages/eclipse-standard-432/keplersr2) + [PyDev Plugin](http://pydev.org/download.html)

#### Getting Started
* Create a [GitHub account](https://github.com/signup/free)
* [Fork](https://github.com/arvindch/project-euler/fork) this repository on GitHub
* [Setup](https://help.github.com/articles/set-up-git) Git locally and connect it to GitHub
* Download your fork: `git clone https://github.com/user_name/project-euler.git`

#### Start Coding
* Choose a Project Euler problem
* Create & Use a branch for your work: `git branch problem-n master`, `git checkout work`
* Follow the Code Guidelines

#### Validating & Timing
* To test your solution, run [tester.py](https://github.com/arvindch/project-euler/blob/master/test/tester.py): `./tester.py`
* If the validation fails, fix your code.
* If the execution time in `timings.txt` is too long, optimize your code.
* Acceptable solutions validate and run in under a minute...

#### Submitting Solutions
* Check your changes: `git status`
* Stage & Commit changes to your branch: `git add .`, `git commit`
* Merge & Push changes to your fork: `git checkout master`, `git merge work`, `git push`
* Submit a [Pull Request](https://github.com/arvindch/project-euler/compare/)
* Wait for other maintainers to review your code...

If all goes well, your solution will be accepted and merged!

## Code Guidelines:

* Keep your code clean and readable.
* Refer pre-existing source for formatting styles.
* Preferably, avoid the usage of non-default modules/headers/packages.
* Reusable functions should be modularized and categorized.

### Help
* [Git](http://git-scm.com/doc)
* [Eclipse](http://help.eclipse.org/kepler/index.jsp)
* [Ubuntu](https://help.ubuntu.com/14.04/index.html)
* [Linux/Bash Shell](http://linuxcommand.org/learning_the_shell.php)
