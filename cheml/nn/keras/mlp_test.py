import os
from json import dump

from keras.datasets import mnist
from keras.utils import to_categorical

from mlp import MLP

(Xtr, ytr), (Xte, yte) = mnist.load_data()
Xtr = Xtr.reshape(60000, 784).astype('float32')
Xte = Xte.reshape(10000, 784).astype('float32')
Xtr /= 255.
Xte /= 255.
ytr = to_categorical(ytr, 10)

nepochs = 20
batch_size = 100

def make_layer_config_file():
    fpath = os.path.join(os.path.expanduser('~'), 'cheml_keras_example_layers.config')
    layer_config = [('Dense', {'units': 512, 'activation': 'relu'}),
                    ('Dropout', {'rate' : 0.2}),
                    ('Dense', {'units': 512, 'activation': 'relu'}),
                    ('Dropout', {'rate': 0.2}),
                    ('Dense', {'units': 10, 'activation': 'softmax'})]
    with open(fpath, 'w') as f:
        dump(layer_config, f)
    return fpath

def make_opt_config_file():
    fpath = os.path.join(os.path.expanduser('~'), 'cheml_keras_example_opt.config')
    opt = ['SGD', {'lr': 0.1, 'momentum': 0.9}]
    with open(fpath, 'w') as f:
        dump(opt, f)
    return fpath

def test_init_via_config():

    print 'testing MLP by passing config files to constructor'

    mlp = MLP(regression=False, nclasses=10,
              nepochs=nepochs, batch_size=batch_size, loss='categorical_crossentropy',
              layer_config_file=make_layer_config_file(),
              opt_config_file=make_opt_config_file())

    mlp.fit(Xtr, ytr)
    print 'test accuracy', mlp.score(Xte, yte)
    mlp.model.summary()

def test_init_via_params():

    print 'testing MLP by passing params to constructor'

    mlp = MLP(nhidden=2, nneurons=[512, 512], activations=['relu', 'relu'],
              learning_rate=0.1,
              nepochs=nepochs, batch_size=batch_size, loss='categorical_crossentropy',
              regression=False, nclasses=10)


    mlp.fit(Xtr, ytr)
    print mlp.score(Xte, yte)
    mlp.model.summary()

if __name__ == '__main__':
    test_init_via_config()
    raw_input()
    test_init_via_params()


