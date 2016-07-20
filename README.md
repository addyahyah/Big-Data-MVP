# Setting Up JupyterHub
This tutorial replicates and extends the information in the [JupyterHub Pydata 2016](https://github.com/minrk/jupyterhub-pydata-2016/blob/master/JupyterHub.pdf) presentation.
## Installation
JupyterHub requires Python 3.3+, so first download the Python 3.5 version of [Anaconda](https://www.continuum.io/downloads).

When asked, make sure the package will be installed to this directory:
```
/opt/anaconda3/
```
Then add the bin file path to your .bashrc and root user's .bashrc in the command line:
```{r, engine='bash', count_lines}
export PATH=”$PATH:/opt/anaconda3/bin"
```
Type the following into the command line to install JupyterHub:
```
conda install -c conda-forge jupyterhub
```
## Optional Steps
You do not have to install Jupyter Notebook if you are only running a server, but you could by typing the following:
```
conda install notebook
```
Using minrk's github repo will help you install oauthenticator, dockerspawner, and netifaces:
```
git clone https://github.com/minrk/jupyterhub-pydata-2016 /srv/jupyterhub
cd /srv/jupyterhub
conda env create -f environment.yml
```
This line adds the conda-forge channel for package management:
```
conda config --add channels conda-forge
```

### Installing Docker
Install Docker here: [Docker.io](https://docs.docker.com/engine/installation/linux/ubuntulinux/)

### Adding Python2 and R to your JupyerHub
Python2:
```
conda create -n py2 python=2 anaconda
source activate py2
ipython kernel install
```
R:
```
conda install -c r r-essentials
conda create -n my-r-env -c r r-essentials
```
For more in-depth information on using R in the Jupyter Notebook environment, check out Christine Doig's blog [Jupyter and Conda for R](https://www.continuum.io/blog/developer/jupyter-and-conda-r).
