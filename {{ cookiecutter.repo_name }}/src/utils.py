from IPython.core.magic import register_line_magic, register_cell_magic
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

PRJPATH = os.environ.get("PRJPATH")

@register_cell_magic
def save_snippet(line, cell):
    if line:
        get_ipython().run_cell(cell)
        path = PRJPATH + '/src/snippets/'
        with open(os.path.join(path, '{}.py'.format(line)), 'w') as f:
            f.writelines(cell)
    else:
        raise ValueError('must have name (%%magic name)')

@register_line_magic
def load_snippet(line):
    path = PRJPATH + '/src/snippets/'
    get_ipython().magic('load {}'.format(os.path.join(path, '{}.py'.format(line))))
