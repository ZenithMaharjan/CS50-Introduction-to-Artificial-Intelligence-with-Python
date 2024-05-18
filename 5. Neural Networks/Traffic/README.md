The convolutional neural network model is based on the TensorFlow Keras Sequential Model.

1.  The first model was created using _one_ convolutional layer with 32 filters and a 3x3 kernel,
    _one_ max-pooling layer with 2x2 pool size, _one_ hidden layer with 128 units and a 0.5 dropout.
    The accuracy obtained was not satisfiable and seemed to be the model was unable to learn the
    data due to the size of the image. So, seeminly unable to predict image with correct accuracy.

        Epoch 1/10
        497/497 [==============================] - 4s 8ms/step - loss: 5.1419 - accuracy: 0.0524
        Epoch 2/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.5686 - accuracy: 0.0562
        Epoch 3/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.5311 - accuracy: 0.0557
        Epoch 4/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.4766 - accuracy: 0.0562
        Epoch 5/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.4745 - accuracy: 0.0562
        Epoch 6/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.4731 - accuracy: 0.0562
        Epoch 7/10
        497/497 [==============================] - 4s 7ms/step - loss: 3.4724 - accuracy: 0.0554
        Epoch 8/10
        497/497 [==============================] - 4s 7ms/step - loss: 3.4706 - accuracy: 0.0555
        Epoch 9/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.4700 - accuracy: 0.0562
        Epoch 10/10
        497/497 [==============================] - 4s 8ms/step - loss: 3.4655 - accuracy: 0.0556
        331/331 - 1s - loss: 3.4837 - accuracy: 0.0574

2.  The second model was created by adding two more hidden layers with 128 units with activation function
    relu to compensate with the complex nature of the data. The results were improved from the first model
    but still not satisfiable. More layers seemed to train diverse data much better.

         Epoch 1/10
         497/497 [==============================] - 3s 7ms/step - loss: 3.2287 - accuracy: 0.3184
         Epoch 2/10
         497/497 [==============================] - 4s 7ms/step - loss: 1.1034 - accuracy: 0.6563
         Epoch 3/10
         497/497 [==============================] - 4s 7ms/step - loss: 0.7232 - accuracy: 0.7994
         Epoch 4/10
         497/497 [==============================] - 4s 8ms/step - loss: 0.5114 - accuracy: 0.8585
         Epoch 5/10
         497/497 [==============================] - 4s 7ms/step - loss: 0.4451 - accuracy: 0.8780
         Epoch 6/10
         497/497 [==============================] - 3s 7ms/step - loss: 0.3738 - accuracy: 0.9002
         Epoch 7/10
         497/497 [==============================] - 3s 7ms/step - loss: 0.3427 - accuracy: 0.9118
         Epoch 8/10
         497/497 [==============================] - 3s 7ms/step - loss: 0.3127 - accuracy: 0.9209
         Epoch 9/10
         497/497 [==============================] - 3s 7ms/step - loss: 0.2487 - accuracy: 0.9326
         Epoch 10/10
         497/497 [==============================] - 3s 7ms/step - loss: 0.2330 - accuracy: 0.9395
         331/331 - 1s - loss: 0.3226 - accuracy: 0.9295

3.  The final model was created by adding another convolutional and pooling layer as it seems the filters help
    generalize the common images into one. Adding pooling help improve the accuracy of the model while preserving
    loss making the result of the model satisfiable.

        Epoch 1/10
        497/497 [==============================] - 3s 7ms/step - loss: 2.8686 - accuracy: 0.3052
        Epoch 2/10
        497/497 [==============================] - 4s 7ms/step - loss: 1.1733 - accuracy: 0.6533
        Epoch 3/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.6370 - accuracy: 0.8115
        Epoch 4/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.4136 - accuracy: 0.8793
        Epoch 5/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.2983 - accuracy: 0.9171
        Epoch 6/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.2715 - accuracy: 0.9251
        Epoch 7/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.2239 - accuracy: 0.9393
        Epoch 8/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.1857 - accuracy: 0.9497
        Epoch 9/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.1619 - accuracy: 0.9581
        Epoch 10/10
        497/497 [==============================] - 4s 8ms/step - loss: 0.1507 - accuracy: 0.9604
        331/331 - 1s - loss: 0.1485 - accuracy: 0.9654
