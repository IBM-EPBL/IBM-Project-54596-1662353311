imort the imagedatagenerator library

from keros.processing.image import imagedatagenerator

image data agumentation
#setting parameter for image data agumentation to the traing data

train_datagen = Imagedatagenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

#Image data aumentation to the testing data

test_datagen=Imagedatagenerator(rescale=1./255)

loading our data and performing data agumentation

#performing data agumentation to train data
x_train = train_datagen.flow_from_directory('../data/train_set',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='categorical')

#performing data agu,mentation to test data
x_test = test_datagen.flow_from_directory('../data/test_set',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='categorical')

Found 742 images belonging to 4 classes.
Found 198 images belonging to 4 classes.
 
