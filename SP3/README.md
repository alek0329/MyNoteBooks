I denne SP opgave har jeg løst Opgaverne fra Gruppen med Aleksander Rolander, Magnus Granno Og Oliver Stæhr

Opgave beskrivelsen lød således:

## Cifar datasæt

Dette er et datasæt af 50.000 32x32 farvede trænings billeder og 10.000 test billeder, opdelt i 10 kategorier.

Datasættet kan hentes med koden nedenunder

```python
import tensorflow as tf
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = tf.keras.datasets.cifar10.load_data()

x_train = tf.keras.utils.normalize(x_train,axis=1)
y_train = tf.keras.utils.normalize(y_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)
y_test = tf.keras.utils.normalize(y_test,axis=1)

plt.imshow(x_train[0])
plt.show()
```

Prøv ved hjælp af dette startkode at opbyg et neuralt netværk der kan gennemskue kategorierne i test dataen.

```python
from keras import models
from keras import layers
from keras import optimizers

model = model.Sequential()
```

Da min kode ligger i en notebook, skal man blot køre hele notebooken ("SP3.ipynb") for at eksekvere min kode.
