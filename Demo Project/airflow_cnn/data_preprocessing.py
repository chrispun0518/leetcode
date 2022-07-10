import tensorflow_datasets as tfds
from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description='Train the model')
parser.add_argument('data_path', type=str, help='path storing the training data')

args = parser.parse_args()
data_path = args.data_path

data = tfds.load('fashion_mnist', data_dir='data', download=True)
train = data['train']
test = data['test']
i = 0

for batch in train:
    X = batch['image']
    y = batch['label'].numpy()
    im = Image.fromarray(X.numpy().squeeze(axis=-1))
    if str(y) not in os.listdir(f'{data_path}/train'):
        os.mkdir(f'{data_path}/train/{y}')
    im.save(f'{data_path}/train/{y}/{i}.jpg')
    i += 1
i = 0
for batch in test:
    X = batch['image']
    y = batch['label'].numpy()
    im = Image.fromarray(X.numpy().squeeze(axis=-1))
    if str(y) not in os.listdir(f'{data_path}/test'):
        os.mkdir(f'{data_path}/test/{y}')
    im.save(f'{data_path}/test/{y}/{i}.jpg')
    i += 1