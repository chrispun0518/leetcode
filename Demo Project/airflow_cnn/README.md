This is a very simple demonstration to demostrate how to use apache airflow to schedule an automated retrain job. <br>
As the purpose of this task is to demonstrate the functionality of airflow, the model training and data preprocessing part is very simple to speed up the pipeline running, but one can replace a more complex script to build a proper productionalized pipepline. <br>
scheduler.py is the dag put in the airflow. <br>
data_preprocessing.py is a task to download and preproccess the mnist data from the website. <br>
train.py is a classical cnn model for solving the mnist image classification problem. <br>
