# Setting Up JupyterHub
This tutorial replicates and extends the information in the [JupyterHub PyData 2016](https://github.com/minrk/jupyterhub-pydata-2016/blob/master/JupyterHub.pdf) presentation.

This tutorial runs the server without ssl encryption. For more details on how to adde ssl, read the link above.

by [Runzhi Yang](https://github.com/RunZGit)

## Installation
JupyterHub requires Python 3.3+, so first download the Python 3.5 version of [Anaconda](https://www.continuum.io/downloads).

In this case, we installed Anaconda3 using root privilege.
```
su
```
Then enter your su password

To set a password for su
```
sudo passwrd
```
To install anaconda do
```
bash anaconda3xxxx.bash
```
When asked, make sure the package will be installed to this directory:
```
/opt/anaconda3/
```
Open .bashrc and root user's .bashrc 
```{r, engine='bash', count_lines}
vi /home/your_directory/.bashrc
vi /root/.bashrc
```
Then add the bin file path to your in the command line:
```
export PATH=”$PATH:/opt/anaconda3/bin"
```
Type the following into the command line to install JupyterHub:
```
conda install -c conda-forge jupyterhub
```
This line adds the conda-forge channel for package management:
```
conda config --add channels conda-forge
```
In order to run Jupyterhub without ssl
```
mkdir /srv/jupyterhub
cd /srv/jupyterhub
jupyterhub --no-ssl
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

### Adding nbgrader for jupyterhub
```
sudo pip3 install nbgrader
sudo nbgrader extension install --symlink
sudo nbgrader extension activate
```
 For each user who needs to create assignments, they need to enter the last in their command line as well

### Tensorflow with graphics compatibility:
I followed this [Korean link](https://www.youtube.com/watch?v=zJTvx0hievk) and installed the tensorflow package. For the record, I do not understand any Korean, all I did was follow the lines he typed.
The official site is [here](https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html#optional-install-cuda-gpus-on-linux)


## Special Instructions for Jupyterflow machine:
To use Graphics card on Tensorflow, type this in command line then start Jupyterhub:
'''
sudo ldconfig /usr/local/cuda/lib64
'''
To serve the hub, type the following in the command line:
```
su
screen
cd /srv/jupyterhub/
jupyterhub --no-ssl
```
Then type Ctrl+a then Ctrl+d to detach the process

The configuration files is stored in the /srv/jupyterhub/ directory as well, for more informatino on config you could read [Minrk's file](http://jupyterhub-tutorial.readthedocs.io/en/latest/) or my project log.


#### For further questions visit my [project log](https://docs.google.com/document/d/1wR0LwaukTm4vCZ2h1PrXUHqaQm6_hlxDviIfTff3ugE/edit?usp=sharing)


The MIT License (MIT)

Copyright (c) 2016 Runzhi Yang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
