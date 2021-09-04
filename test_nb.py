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

def test_4_2():
    _exec_notebook('4.2-balancing.ipynb')

def test_5_2():
    _exec_notebook('5.2-cross-validation.ipynb')