import sys
sys.path.append('../..')
# needed to uses foreing keys in models
import django
django.setup()

from PIL import Image
from skimage.feature import hog
from ecan.models import Item, Feature
import numpy as np
# from datetime import datetime
# import os
# from sklearn.metrics import confusion_matrix
# import matplotlib.pyplot as plt
# from skimage import color, exposure
# import time
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

Items = Item.objects.all()
Features = Feature.objects.all()

d = {
    'cells_per_block': (1, 1),
    'orientations': 8,
    'pixels_per_cell': (12, 12),
    'normalise': True,
    'visualise': False
}
name = 'hog_032415'

for item in Items:
    if not Feature.objects.filter(item=item, name='hog_032415'):
        img = item.im.path.encode('ascii', 'replace')
        img = Image.open(img).convert('L')
        img = np.array(img)
        ft = hog(img, **d)
        feat = Feature(
            name=name,
            description=d,
            feature=ft,
            item=item
        )
        feat.save(force_insert=True)
