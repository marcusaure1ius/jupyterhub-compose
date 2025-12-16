# В качестве основы берем готовый образ от Jupyter
FROM jupyter/minimal-notebook:latest

# Переключаемся на пользователя root для установки системных пакетов
USER root

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Возвращаемся к обычному пользователю, чтобы не работать под root
USER ${NB_USER}

# Устанавливаем основные Python-библиотеки для анализа данных
RUN mamba install --yes \
    'altair' \
    'beautifulsoup4' \
    'bokeh' \
    'bottleneck' \
    'cloudpickle' \
    'cython' \
    'dask' \
    'dill' \
    'oracledb' \
    'h5py' \
    'ipympl' \
    'ipywidgets' \
    'jupyterlab-git' \
    'matplotlib-base' \
    'numba' \
    'numexpr' \
    'openpyxl' \
    'pandas' \
    'patsy' \
    'protobuf' \
    'psycopg2-binary' \
    'plotly' \
    'pytables' \
    'scikit-image' \
    'scikit-learn' \
    'scipy' \
    'seaborn' \
    'sqlalchemy' \
    'statsmodels' \
    'sympy' \
    'widgetsnbextension' \
    'xlrd' && \
    mamba clean --all -f -y
