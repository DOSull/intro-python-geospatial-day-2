FROM mcr.microsoft.com/devcontainers/anaconda

RUN conda install -n base -c conda-forge mamba

RUN umask 0002 && /opt/conda/bin/mamba env create -n intro-python-2 -c conda-forge python=3.11 jupyter ipykernal ipywidgets geopandas mapclassify contextily; fi && rm -rf /tmp/conda-tmp
