from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import os

def run():
    clf = RandomForestClassifier(n_estimators=100)
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    clf.fit(X, y)

    fname = 'rfclf'
    dirp = os.path.join('ecan', 'ml', 'clfs', fname)
    fp = os.mkdir(dirp, fname + '.pkl')

    from sklearn.externals import joblib
    joblib.dump(clf, fp)

    clf2 = joblib.load(fp)
    clf2.predict(X[0])

    print y
    pass
