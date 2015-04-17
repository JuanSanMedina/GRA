# Add path where ecan application resides
import sys
sys.path.append('../..')

# Path where media resides
media_path = 'api/site_media/media/'

# needed to use foreing keys in models
import django
django.setup()

import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn import metrics
from sklearn import preprocessing

from ecan.models import Item, Feature, Common_Name, Material, Shape, Logo
# print Items.objects.all()

hogs = Feature.objects.filter(name='hog_032415')
pixs = Feature.objects.filter(name='thumb_1:8')

target_matrix = np.array([
                [e.item.common_name.value,
                e.item.material.value,
                e.item.shape.value,
                e.item.logo.value] for e in hogs])

le = preprocessing.LabelEncoder()
le.fit(target_matrix[:, 0])
target = le.transform(target_matrix[:, 0])
# le.inverse_transform(np.unique(target))

h_data = np.array([e.feature for e in hogs])
p_data = np.array([e.feature for e in pixs])

h_rf_clf = RandomForestClassifier(n_estimators=100)
h_rf_scores = cross_validation.cross_val_score(h_rf_clf, h_data, target.tolist(), cv=2)
print h_rf_scores
