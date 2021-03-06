from mlxtend.data import iris_data
from mlxtend.data import wine_data
from mlxtend.data import autompg_data

def test_import_wine_data():
    X, y = wine_data()
    assert(X.shape[0] == 178)
    assert(X.shape[1] == 13)
    print(y.shape)
    assert(y.shape[0] == 178)

def test_import_iris_data():
    X, y = iris_data()
    assert(X.shape[0] == 150)
    assert(X.shape[1] == 4)
    print(y.shape)
    assert(y.shape[0] == 150)

def test_import_autompg_data():
    X, y = autompg_data()
    assert(X.shape[0] == 392)
    assert(X.shape[1] == 8)
    print(y.shape)
    assert(y.shape[0] == 392)