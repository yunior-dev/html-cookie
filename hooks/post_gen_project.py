from __future__ import print_function

import os
import random
import string

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = '\x1b[0m'
WARNING = '\x1b[1;33m [WARNING]: '
INFO = '\x1b[1;33m [INFO]: '
HINT = '\x1b[3;33m'
SUCCESS = '\x1b[1;32m [SUCCESS]: '


def main():
    print(SUCCESS + 'Project initialized, keep up the good work!' + TERMINATOR)


if __name__ == '__main__':
    main()
