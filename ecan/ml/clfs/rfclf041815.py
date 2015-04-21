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
sys.path.append('../..')  # Add path where ecan application resides
django.setup()  # needed to use foreing keys in models
media_path = 'api/site_media/media/'  # Path where media resides


def run():
    results = {}
    results['total_time'] = time.time()
    hogs = Feature.objects.filter(name='hog_032415')
    target_matrix = np.array([
        [e.item.common_name.value,
                e.item.material.value,
                e.item.shape.value,
                e.item.logo.value] for e in hogs])

    le = preprocessing.LabelEncoder()
    le.fit(target_matrix[:, 0])
    target = le.transform(target_matrix[:, 0]).tolist()
    data = np.array([e.feature for e in hogs])

    clf = RandomForestClassifier(n_estimators=100)
    X, y = data, target
    clf.fit(X, y)

    fname = 'rfclf_on_cn_%s.pkl' % datetime.now().strftime("%m%d%y")
    lname = 'le_on_cn_%s.pickle' % datetime.now().strftime("%m%d%y")
    dirp = os.path.join('ecan', 'ml', 'clfs', fname)
    try:
        os.mkdir(dirp)
    except OSError as e:
        print str(e)

    clf_p = os.path.join(dirp, fname)
    le_p = os.path.join(dirp, lname)

    from sklearn.externals import joblib
    joblib.dump(clf, clf_p)

    with open(le_p, 'wb') as f:
        pickle.dump(le, f)

    results['total_time'] = time.time() - results['total_time']
    with open(dirp + 'results.json', 'w+') as f:
        json.dump(results, f)

    # with open('filename.pickle', 'rb') as handle:
    #   b = pickle.load(handle)
    # a = {'hello': 'world'}
    # clf2 = joblib.load(fp)
    # clf2.predict(X[0])
    # print y
    # pass
