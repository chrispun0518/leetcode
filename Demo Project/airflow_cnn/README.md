# Apache Airflow demonstration

This is a very simple demonstration to demostrate how to use apache airflow to schedule an automated retrain job.<br>

As the purpose of this task is to demonstrate the functionality of airflow, the model training and data preprocessing part is very simple to speed up the pipeline running, but one can replace a more complex script to build a proper productionalized pipepline. <br>

## Scripts

<b>data_preprocessing.py</b> is a script to download and preproccess the mnist data from the website.<br>
<b>train.py</b> is a classical CNN model for solving the mnist image classification problem.<br>
<b>scheduler.py</b> is a DAG put in the airflow DAG folder

## Demonstration details

The pipeline first runs the script <b>data_preprocessing.py</b> to get the data from the website, and store the data on the local disk.<br>
Then, the <b>train.py</b> call the keras data image data generator to transform the image data on-the-fly to augement the training data. The scheduler will repeat the data pipeline to retrain the model everyday. 

<br> In the real environment, they may be a new batch of data from different sources everyday. This pipeline can automatically incorporate the new data to the training data set in order to update the model with the latest information.<br>

One can use the UI of the airflow to monitor the job status at each stage, the graph below shows that 2 tasks are run successfully. <br>

![image](https://github.com/chrispun0518/personal_demo/blob/master/Demo%20Project/airflow_cnn/airflow_task.png)

The script also output different information log to help debug and productionalize the model training workflow, such as <i>number of classification samples</i> and <i>model check point instances</i>

