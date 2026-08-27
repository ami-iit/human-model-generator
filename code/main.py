# SPDX-FileCopyrightText: Fondazione Istituto Italiano di Tecnologia
#
# SPDX-License-Identifier: BSD-3-Clause


"""
|:-----------------------------:|
|                               |
|    HUMAN MODEL GENERATOR      |
|                               |
|:-----------------------------:|
"""

import os
import sys

# Not packaged: run directly from source without installing the project
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from humanmodelgenerator import cli

if __name__ == "__main__":
    argv = sys.argv[1:]
    # Default to the config.py sitting next to this script unless the user passed their own
    if "--config" not in argv and "-c" not in argv:
        argv = [*argv, "--config", os.path.join(os.path.dirname(__file__), "config.py")]
    sys.exit(cli.main(argv))

