#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""
test.py
~~~~~~~

Simply run pytest tests - use this because the ``py.test`` binary doesn't work
too well on ARM.

:author: Douglas Watson <douglas.watson@epfl.ch>
:date: 2015
:license: MIT

"""

import pytest

if __name__ == '__main__':
    pytest.main([
        '--ignore=env/',
        '--ignore=doc/',
        '...',
    ])
