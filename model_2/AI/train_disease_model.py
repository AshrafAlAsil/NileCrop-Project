import json
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_disease_classifier():
    """
    Trains a CNN model (MobileNetV2) using transfer learning for plant disease detection.
    """
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False
    
    x = GlobalAveragePooling2D()(base_model.output)
    x = Dropout(0.2)(x)
    predictions = Dense(15, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, horizontal_flip=True)
    val_datagen = ImageDataGenerator(rescale=1./255)
    
    train_gen = datagen.flow_from_directory('plant_dataset/train', target_size=(224, 224), batch_size=32)
    val_gen = val_datagen.flow_from_directory('plant_dataset/val', target_size=(224, 224), batch_size=32)
    
    class_map = {str(v): k for k, v in train_gen.class_indices.items()}
    with open('disease_classes.json', 'w') as f:
        json.dump(class_map, f)
        
    model.fit(train_gen, epochs=3, validation_data=val_gen)
    model.save('disease_model.h5')
    print("Model training complete and saved as 'disease_model.h5'")

if __name__ == "__main__":
    train_disease_classifier()