SCL-cookiecutter
==============================

SCL data-science coockiecutter.

To start your project install coockiecutter first (`pip install cookiecutter`).

Clone this repository in your preferred `{path}` , then run 
`cookiecutter {path}/SCL-cookiecutter `  

Modify .env file adding
`PRJPATH={path}`

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── lists          <- Lists.
    │   ├── matching       <- Data generated for matching.
    │   ├── raw            <- The original, immutable data dump.
    |   └── aux	           <- Auxiliary files.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Manuals, documents and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    |── .env               <- File to set environmental variables.
    ├── src                <- Source code for use in this project.
    │   │
    │   ├── utils.py       <- General utils.
    │   │
    │   ├── mapping.py     <- Data dictionaries.
    │   │
    │   ├── matching       <- Scripts to match data to the database
    │   │   └── match.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── snippets       <- Folder where snippets of code are save by function in utils.py
    │   │
    │   └── models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── predict_model.py
    │       └── train_model.py
    │    
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
