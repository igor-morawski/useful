
import sklearn
from sklearn import model_selection
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.externals import joblib
import os


def train_SVM(features, labels, test_size=0.2, scaler=None, output_path="."):
    if not os.path.isdir(output_path):
        raise OSError(2, 'No such file or directory', dataset_dir)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        features, labels, test_size=test_size)
    if scaler:
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

    param = [
        {
            "kernel": ["linear"],
            "C": [1, 10, 100, 1000]
        },
        {
            "kernel": ["rbf"],
            "C": [1, 10, 100, 1000],
            "gamma": [1e-2, 1e-3, 1e-4, 1e-5]
        }
    ]

    svm = SVC(probability=True)
    clf = GridSearchCV(svm, param,
                       cv=10, n_jobs=4, , verbose=3)
    clf.fit(X_train, y_train)
    joblib.dump(value=clf.best_estimator_, filename=output_path+"model.pkl")
