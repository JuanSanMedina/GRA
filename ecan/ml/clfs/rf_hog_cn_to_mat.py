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
    Features = Feature.objects.filter(name='hog_032415')
    cn = {int(e.pk): e.value for e in Common_Name.objects.all()}
    mat = {int(e.pk): e.value for e in Material.objects.all()}
    ft_d = {cn[e]: Features.filter(item__common_name=e) for e in cn}

    results = {}
    results['total_time'] = time.time()
    for key in ft_d:
        if ft_d[key]:
            X = np.array([e.feature for e in ft_d[key]])
            y = [i.item.material.pk for i in ft_d[key]]
            clf = RandomForestClassifier(n_estimators=100)
            clf.fit(X, y)
            fname = '%s_to_mat' % key
            dirp = os.path.join('ecan', 'ml',
                                'clfs', 'rf', fname)
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
