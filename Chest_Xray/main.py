#!/usr/bin/env python
# coding: utf-8

# In[3]:


from PIL import Image
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import tensorflowjs as tfjs


# In[4]:


print(f"The Tensorflow version is {tf.__version__}")
print(f"The Keras version is {tf.keras.__version__}")


# In[5]:


IMG_SIZE = (224,224)
np.shape(plt.imread("./Data/train/NORMAL/IM-0115-0001.jpeg"))


# In[6]:


train_generator = ImageDataGenerator(shear_range=10
                                   ,zoom_range=0.2
                                   ,horizontal_flip=True
                                   ,preprocessing_function=preprocess_input)

valid_generator = ImageDataGenerator(preprocessing_function=preprocess_input)


# In[7]:


train_data = train_generator.flow_from_directory("./Data/train/",target_size=IMG_SIZE,color_mode="rgb")
valid_data = valid_generator.flow_from_directory("./Data/train/",target_size=IMG_SIZE,color_mode="rgb")


# In[8]:


base_model = MobileNetV2(include_top=False,weights="imagenet",input_shape=(224,224,3))


# In[9]:


for layers in base_model.layers:
    layers.trainable = False
base_model.input


# In[10]:


from tensorflow.keras import Model, layers
x = base_model.output
x = layers.Flatten()(x)
x = layers.Dense(1024,activation='relu')(x)
x = layers.Dense(512,activation='relu')(x)
predictions = layers.Dense(2, activation='sigmoid')(x)
model = Model(base_model.input, predictions)


# In[11]:


model.summary()


# In[12]:


optimizer = Adam(learning_rate=0.0005)


# In[13]:


model.compile(loss='binary_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])


# In[14]:


history = model.fit_generator(train_data,steps_per_epoch=10,epochs=5,validation_data=valid_data,validation_steps=10)


# In[1]:


# import json
# with open("./models.json","w") as jsonFile:
#     jsonFile.write(model.to_json())


# In[20]:


# model.to_json()


# In[17]:


tfjs.converters.save_keras_model(model,'model_for_web',weight_shard_size_bytes=int(1e9))


# In[ ]:




