How To Contribute
=============

You can:

* discuss ideas via the [Wiki](https://github.com/arvindch/project-euler/wiki), comments or email.
* contribute your alternative solutions and improvements via [Pull Requests](https://github.com/arvindch/project-euler/pulls).
* report bugs via the [Issue Tracker](https://github.com/arvindch/project-euler/issues).

## Workflow

#### System Setup

* OS - [Ubuntu 12.04.x LTS](http://releases.ubuntu.com/12.04/)
* Python - [2.7.6](https://www.python.org/download/releases/2.7.6/)

#### Getting Started
* Make sure you have a [GitHub account](https://github.com/signup/free)
* [Fork](https://github.com/arvindch/project-euler/fork) the repository on GitHub
* Setup [Git](http://git-scm.com/) locally


#### Get Coding
* Clone the master repository: `git clone project-euler`
* Create & Use a branch for your work: `git branch problem-n master`, `git checkout problem-n`
* Follow the Code Guidelines

#### Validate & Time
* To test your solution, run [tester.sh](https://github.com/arvindch/project-euler/blob/master/test/tester.sh): `$ ./tester.sh problem_num user_name`
* If the validation fails, fix your code.
* If the execution time (found in `timings.txt`) is too long, optimize your code.
* Correct solutions validate and run in under a minute...

#### Start Submitting
* Check your changes: `git status`
* Stage & Commit changes: `git add .`, `git commit`
* Push changes to your fork: `git checkout master`, `git merge problem-n`, `git push`
* Submit a [Pull Request](https://github.com/arvindch/project-euler/compare/).
* Wait for other maintainers to review your code.

If all goes well, your solution will be merged!


## Code Guidelines:

* Keep your code [pythonic](http://legacy.python.org/dev/peps/pep-0020/).
* Refer [pre-existing solutions](https://github.com/arvindch/project-euler/tree/master/src/solutions) for formatting styles.
* Preferably, avoid the usage of non-default Python modules.
* Reusable functions should be [modularized and categorized](https://github.com/arvindch/project-euler/tree/master/src/custom).
* Use the [Timer() class](https://github.com/arvindch/project-euler/blob/master/src/custom/tools.py#L7), to automatically time your solutions/code-snippets.
