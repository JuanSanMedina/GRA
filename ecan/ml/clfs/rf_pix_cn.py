import os
import json
import pickle
import time
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from ecan.models import Item, Feature, Common_Name, \
                        Material, Shape, Logo
import django
from datetime import datetime
import sys
from sklearn.externals import joblib
sys.path.append('../..')  # Add path where ecan application resides
django.setup()  # needed to use foreing keys in models
media_path = 'api/site_media/media/'  # Path where media resides


def run():
    results = {}
    results['total_time'] = time.time()

    Features = Feature.objects.filter(name='thumb_1:8')
    cn = {int(e.pk): e.value for e in Common_Name.objects.all()}

    X = np.array([e.feature for e in Features])
    y = [int(i.item.common_name.pk) for i in Features]
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X, y)
    fname = 'cn'
    dirp = os.path.join('ecan', 'ml',
                        'clfs', 'rf_pix', fname)
    try:
        os.mkdir(dirp)
    except OSError as e:
        print str(e)
    clf_p = os.path.join(dirp, fname + '.pkl')
    joblib.dump(clf, clf_p)

    results['total_time'] = time.time() - results['total_time']
    resultsp = os.path.join(dirp, 'results.json')
    with open(resultsp, 'w+') as f:
        json.dump(results, f)
