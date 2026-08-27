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
from humanmodelgenerator.generate import main

if __name__ == "__main__":
    main()
