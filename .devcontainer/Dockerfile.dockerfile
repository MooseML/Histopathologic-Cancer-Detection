FROM tensorflow/tensorflow:2.13.0-gpu

# install system dependencies for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# install JupyterLab, Kaggle API, and other Python dependencies
RUN pip install jupyterlab opencv-python seaborn kaggle zipfile36

# ensure Kaggle API can access kaggle.json (it will be mounted from devcontainer.json)
RUN mkdir -p /root/.kaggle && chmod 600 /root/.kaggle/kaggle.json

# set working directory
WORKDIR /workspace

# expose JupyterLab port
EXPOSE 8888
