import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_1():
    _exec_notebook('1-introduction.ipynb')

def test_2():
    _exec_notebook('2-classification_metrics.ipynb')

def test_3_1():
    _exec_notebook('3.1-knn.ipynb')

def test_3_2():
    _exec_notebook('3.2-scaling.ipynb')

def test_4_1():
    _exec_notebook('4.1-trees.ipynb')

def test_4_2():
    _exec_notebook('4.2-balancing.ipynb')

def test_5_1():
    _exec_notebook('5.1-svm.ipynb')

def test_5_2():
    _exec_notebook('5.2-cross-validation.ipynb')

def test_5_3():
    _exec_notebook('5.3-grid-search.ipynb')

def test_6():
    _exec_notebook('6-regression.ipynb')

def test_7():
    _exec_notebook('7-dimensionality_reduction.ipynb')