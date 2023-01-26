# Training and saving the Mobilenet model for scene classification

import tensorflow as tf

from tensorflow import keras

from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.mobilenet import decode_predictions

from tensorflow.keras.preprocessing.image import ImageDataGenerator


# specify the paths to the data directories
train_dir = "data/train"
val_dir = "data/validation"
test_dir = "data/test"


# Function to create model

def make_model(learning_rate=0.01):
    base_model = MobileNet(weights='imagenet',
                          include_top=False,
                          input_shape=(224,224,3))

    base_model.trainable = False
    
    #########################################
    
    inputs = keras.Input(shape=(224,224, 3))
    base = base_model(inputs, training=False)
    vectors = keras.layers.GlobalAveragePooling2D()(base)
    outputs = keras.layers.Dense(3)(vectors)
    model = keras.Model(inputs, outputs)
    
    #########################################
    
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    loss = keras.losses.CategoricalCrossentropy(from_logits=True)

    # Compile the model
    model.compile(optimizer=optimizer,
                  loss=loss,
                  metrics=['accuracy'])
    
    return model


# Training with Data Augmentation

train_gen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range = 30,
    width_shift_range = 10.0,
    height_shift_range=10.0,
    zoom_range=0.1,
    vertical_flip=True
)

train_ds = train_gen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32
)

val_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

val_ds = val_gen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    shuffle=False
)

checkpoint = keras.callbacks.ModelCheckpoint(
    'mobilenet_v1_{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only=True,
    monitor='val_accuracy',
    mode='max'
)


learning_rate = 0.01

model = make_model(learning_rate=learning_rate)

history = model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds,
    callbacks=[checkpoint]
)





