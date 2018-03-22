from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils

def main():
    #데이터 로드
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    img_width = x_train.shape[1] 
    img_height = x_train.shape[2]
    img_size= img_width * img_height

    #데이터 전처리 및 표준화
    x_train = x_train.reshape(x_train.shape[0],img_size).astype('float32')
    x_test = x_test.reshape(x_test.shape[0],img_size).astype('float32')
    x_train /= 255
    x_test /= 255

    y_train = np_utils.to_categorical(y_train,10)
    y_test = np_utils.to_categorical(y_test,10)

    #모델 생성
    model = build_model()
    model.fit(x_train, y_train,
    batch_size=128, nb_epoch=20, verbose=1,
    validation_data=(x_test,y_test))

    #모델 저장
    model.save_weights('mnist.hdf5')

    #모델 평가
    score = model.evaluate(x_test, y_test, verbose=0)
    print('score=',score)


def build_model():
    ##모델 정의
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    ##모델 컴파일
    model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['accuracy'])

    return model


if __name__ == '__main__':
    main()