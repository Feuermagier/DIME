#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#$ -j y
#$ -jc gtn-container_g1

#$ -ac d=none

# -------------- do not modify, enables internet access -----------------
export MY_PROXY_URL="http://10.1.10.1:8080/"
export HTTP_PROXY=$MY_PROXY_URL
export HTTPS_PROXY=$MY_PROXY_URL
export FTP_PROXY=$MY_PROXY_URL
export http_proxy=$MY_PROXY_URL
export https_proxy=$MY_PROXY_URL
export ftp_proxy=$MY_PROXY_URL
# -------------- do not modify, enables internet access -----------------

cd $HOME

source ${HOME}/.bashrc

singularity exec --bind /home:/home,/data:/data,/tmp:/tmp --nv cudagl_egl.sif bash -ic "cd $HOME/code/DIME && micromamba activate dime && python3 run_dime.py &> raiden_logs/run_dime.log"
