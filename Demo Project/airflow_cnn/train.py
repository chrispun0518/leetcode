import argparse
import logging
import os

import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Input, Flatten, Dense, Reshape
from tensorflow.keras.models import Model
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import categorical_accuracy
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator


if __name__ == '__main__':
    # Set the commandline tools
    parser = argparse.ArgumentParser(description='Train the model')
    parser.add_argument('date', type=str, help='date of the run')
    parser.add_argument('data_path', type=str, help='path storing the training data')
    parser.add_argument('model_path', type=str, help='path for saving the model')
    parser.add_argument('log_path', type=str, help='path for training log')

    args = parser.parse_args()

    date = args.date
    data_path = args.data_path
    model_path = args.model_path
    if not os.path.exists(args.log_path):
        os.makedirs(args.log_path)
    log_path = '{}/{}_log.log'.format(args.log_path, date)
    logging.basicConfig(filename=log_path,
                         filemode='w',
                         format='%(asctime)s - %(levelname)s : %(message)s',
                         level=logging.INFO,
                         datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    logger.info(f'date: {date}')
    logger.info(f'data_path: {data_path}')
    logger.info(f'model_path: {model_path}')

    # Apply Image data augmentation
    gen = ImageDataGenerator(horizontal_flip=True, rescale=1/255, rotation_range=10)
    logger.info('import data')
    train_gen = gen.flow_from_directory(f'{data_path}/train', target_size=(28,28), color_mode='grayscale')
    test_gen = gen.flow_from_directory(f'{data_path}/test', target_size=(28,28), color_mode='grayscale')
    logger.info('import data sccessfully')

    # log the basic statistic of the samples
    for folder in os.listdir(f'{data_path}/train'):
        logger.info(f'Class {folder}: ' + str(len(os.listdir(f'{data_path}/train/{folder}'))) + ' samples')
    for folder in os.listdir(f'{data_path}/test'):
        logger.info(f'Class {folder}: ' + str(len(os.listdir(f'{data_path}/test/{folder}'))) + ' samples')

    # set up the model architecture
    inputs = Input(shape=(28,28,1))
    x = Conv2D(4, (3,3), activation='relu')(inputs)
    x = MaxPool2D((3,3))(x)
    x = Conv2D(8, (3,3), activation='relu')(x)
    x = MaxPool2D((3,3))(x)
    x = Dropout(0.2)(x)
    x = Conv2D(16, (2,2), activation='relu')(x)
    x = Flatten()(x)
    outputs = Dense(10, activation='softmax')(x)

    model = Model(inputs=inputs, outputs=outputs)

    callbacks_list = [ModelCheckpoint(model_path+'/fashion_{val_loss:.2f}'), EarlyStopping(min_delta=0.05, patience=3)]
    model.compile(loss=CategoricalCrossentropy(),
                optimizer='adam',
                metrics=categorical_accuracy)

    # train the model
    logger.info('train the model')
    history = model.fit_generator(train_gen,
                        validation_data=test_gen,
                        epochs=20, 
                        callbacks=callbacks_list)
    logging.info('model training success')