# Add path where ecan application resides
import sys
sys.path.append('../..')

# Path where media resides
media_path = 'api/site_media/media/'

# needed to use foreing keys in models
import django
django.setup()

# Modules
import os
import json
import pickle
from datetime import datetime
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from ecan.models import Item, Feature, Common_Name, Material, Shape, Logo

hogs = Feature.objects.filter(name='hog_032415')[:100]
# pixs = Feature.objects.filter(name='thumb_1:8')
start_global = datetime.now()

results = {}
results[hogs[0].name] = {}
results[hogs[0].name]['description'] = hogs[0].description
results[pixs[0].name] = {}
results[pixs[0].name]['description'] = pixs[0].description
results['start'] = str(start_global)


def run():


    target_matrix = np.array([
        [e.item.common_name.value,
                e.item.material.value,
                e.item.shape.value,
                e.item.logo.value] for e in hogs])

    le = preprocessing.LabelEncoder()
    le.fit(target_matrix[:, 0])
    target = le.transform(target_matrix[:, 0])

    a = {'hello': 'world'}

    with open('filename.pickle', 'wb') as handle:
      pickle.dump(a, handle)


    # with open('filename.pickle', 'rb') as handle:
    #   b = pickle.load(handle)

    clf = RandomForestClassifier(n_estimators=100)
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    clf.fit(X, y)

    fname = 'rfclf'
    dirp = os.path.join('ecan', 'ml', 'clfs', fname)
    try:
        os.mkdir(dirp)
    except OSError as e:
        print str(e)
        pass

    fp = os.path.join(dirp, fname + '.pkl')

    from sklearn.externals import joblib
    joblib.dump(clf, fp)

    clf2 = joblib.load(fp)
    clf2.predict(X[0])

    print y
    pass
