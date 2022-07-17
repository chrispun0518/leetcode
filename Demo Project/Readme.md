# Personal Demo of Chris Pun

I have been working as a data scientist in different companies for 4 years. This folder contains some of the sample scripts that demostrate my skill sets.
Due to the confidentiality of the datasets, I cannot reproduce the complete work product of my previous projects at work. However, I can apply some of the skills that I used at work in the following notebooks using some toy datasets.

## Demostrations

<b>churn_model.ipynb is done</b> in around early 2020. It demonstrates on how I tackle a classic customer churn prediction using some time series data.

<b>Deep_Q_Learning_Cartpole.ipynb</b> is done in mid 2020. It demonstrate on how to adapt the deep neural network to solve a classical Cartpole problem using reinforcement learning.

<b>classification_with_API.ipynb</b> in late 2020. It demonstrates how to serve the model through http requests using flask. The model is stored at the backend of the website. Once a valid http request is posted, it can submit the data to the model and respond the model prediction result to the frontend.

<b>airflow_cnn</b> folder focus more on model deployment and is done in mid 2022. It contains a set of codes on demonstrating how to use apache airflow to schedule inter-dependent machine learning jobs to automate data preprocessing pipeline and model retrain

<b>tfp_nn</b> uses the <i>tensorflow probability</i> extension to build probablistic models. By imposing a proper assumption utilize the technique in bayesian statistics, one can regularize the model parameters to aviod overfitting. This may provide another perspective to deal with shift of distribution between the training and testing dataset
