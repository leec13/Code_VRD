#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys
import time
import glob
import os.path as path
import getpass
import shutil
import random
import math

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","MacrosDropBox","py","VRD"))
sys.path.append(mypath)

from fenetre import fenetre
from Data import Data

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class Controleur(swing.JFrame):