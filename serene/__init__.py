"""
Copyright (C) 2016 Data61 CSIRO
Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>

Serene Python client: Data Integration Software
"""
from serene.const import CODE_VERSION
from .core import Serene
from .semantics import Ontology
from .elements import *
from .api import *

__version__ = CODE_VERSION
