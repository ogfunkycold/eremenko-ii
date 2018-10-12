# use classifier and test_datagen from before
# classifier is just a Sequential object
x = test_datagen.flow_from_directory('dataset/image_folder',
                                     target_size = (64, 64),
                                     class_mode = 'binary')
print("It is a %s!" % ("dog" if classifier.predict(x) else "cat"))