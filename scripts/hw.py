# Add path where ecan application resides
import sys
sys.path.append('../..')

# Path where media resides
media_path = 'api/site_media/media/'

# needed to use foreing keys in models
import django
django.setup()

import os
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

from skimage import color, exposure
from PIL import Image
from skimage.feature import hog

from datetime import datetime
import time

import pandas as pd
import numpy as np

from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn import metrics
from sklearn import preprocessing

print 'juan'
# print Items.objects.all()