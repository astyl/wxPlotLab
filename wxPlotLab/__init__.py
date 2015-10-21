# -*-coding:Utf-8 -*
#
# Name:      wxmplot
# Version:   0.9.14
# Purpose:   Provide user-configurable 2D plotting module, using wxPython
#            and matplotlib.
# Author:    Andre ASTYL
# Copyright: Andre ASTYL
# Licence:   MIT license
# Updated:   21/10/2015
#-----------------------------------------------------------------------------

""" description here
"""
__version__  = '0.1'
__date__     = '21/10/2015'

import sys
try:
    if not hasattr(sys, 'frozen'):
        import wxversion
        wxversion.ensureMinimal('2.8')
except ImportError:
    pass
except: # probably a useless exception from ensureMinimal() about wx already being Imported.
    pass

# Utils
from utils import log,\
                  configParser,\
                  msgMap,\
                  createError,\
                  getErrHdlr,\
                  regErrHdlr,\
                  remErrHdlr,\
                  checkTypeParams,\
                  checkTypeReturned

# Models
from dataModel import Slide,\
                      Variable,\
                      Collection,\
                      Projection,\
                      Container

# App
from graphics import newWxPlotApp,\
                     newWxPlotFrame,\
                     newWxPlotPanel
