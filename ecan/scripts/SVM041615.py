# Add path where ecan application resides
import sys
sys.path.append('../..')

# Path where media resides
media_path = 'api/site_media/media/'

# needed to use foreing keys in models
import django
django.setup()

# Modules
import json
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn import metrics
from sklearn import preprocessing
from ecan.models import Item, Feature, Common_Name, Material, Shape, Logo

hogs = Feature.objects.filter(name='hog_032415')
pixs = Feature.objects.filter(name='thumb_1:8')

results = {}
results[hogs[0].name] = {}
results[hogs[0].name]['description'] = hogs[0].description
results[pixs[0].name] = {}
results[pixs[0].name]['description'] = pixs[0].description


def run():
    target_matrix = np.array([
        [e.item.common_name.value,
                e.item.material.value,
                e.item.shape.value,
                e.item.logo.value] for e in hogs])

    le = preprocessing.LabelEncoder()
    le.fit(target_matrix[:, 0])
    target = le.transform(target_matrix[:, 0])
    # le.inverse_transform(np.unique(target))

    data = np.array([e.feature for e in hogs])
    h_rf_clf = svm()
    h_rf_scores = cross_validation.cross_val_score(h_rf_clf,
                                                   data,
                                                   target.tolist(),
                                                   cv=10)
    print "hog"
    print h_rf_scores

    data = np.array([e.feature for e in pixs])
    p_rf_clf = svm()
    p_rf_scores = cross_validation.cross_val_score(p_rf_clf,
                                                   data,
                                                   target.tolist(),
                                                   cv=10)
    print "pixel"
    print p_rf_scores

    results[hogs[0].name]['10cv result'] = h_rf_scores
    results[pixs[0].name]['10cv result'] = p_rf_scores

    with open('results/SVM041615.json', 'w') as f:
        json.dump(results, f)
    pass
