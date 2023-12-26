import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import backend as K
import numpy as np
import pandas as pd


data_size = 1000    # 전체 데이터의 크기
input_dims = 5      # Query, Key, Value의 벡터 크기
attention_column = 3    # attention할 위치 인덱스

def build_data(batch_size, input_size, attention_index):
    train_x = np.random.standard_normal(size=(batch_size, input_size))
    train_y = np.random.randint(low=0, high=2, size=(batch_size,1))
    train_x[:, attention_index] = train_y[:, 0]   # y가 1인 경우에 query의 3번째 자리에 1로 셋팅
    return (train_x, train_y)


# 훈련데이터 만들기
train_x, train_y = build_data(data_size, input_dims, attention_column)

# eager execution 모드 비활성화
tf.compat.v1.disable_eager_execution()

def swap_element(x):
    return tf.gather(x, indices=[3,1,2,0,4], axis=1)

query = layers.Input(shape=(input_dims,), name='input')
key1 = layers.Dense(input_dims, activation='softmax', name='key1')(query)
key2 = layers.Lambda(lambda x: swap_element(x), name='key2')(query)

querykey1Dot = layers.multiply([query, key1], name='dot1')
querykey2Dot = layers.multiply([query, key2], name='dot2')
querykey1Value = layers.Lambda(lambda x: querykey1Dot*x, name='qk1v_vector')(key1)
querykey2Value = layers.Lambda(lambda x: querykey2Dot*x, name='qk2v_vector')(key2)

vectorSum = layers.Add(name='qkv_sum_vector')([querykey1Value, querykey2Value])

y = layers.Dense(20, name='dense')(vectorSum)
y = layers.Dense(1, activation='sigmoid', name='output')(y)
# 0과 1 중에서 예측하는 간단한 모델이기 때문에 sigmoid를 적용함.

model = models.Model(query, y)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 훈련 시작
history = model.fit(train_x, train_y, epochs=50, batch_size=64, validation_split=0.2, verbose=2)


# test 
test_x, test_y = build_data(data_size, input_dims, attention_column)

result = model.evaluate(test_x, test_y, batch_size=64, verbose=0)
print(result)


# key1 vector (특정 layer 출력해보기)
# key1_layer = model.get_layer('key1')
# func = K.function([model.input], [attention_layer.output])

# output = func([test_x])[0]
# print(output[:10])
# attention_vector = np.mean(output, axis=0)


# 신경망의 Weight를 가져옴 
dense_layer = model.get_layer('dense')
weights = dense_layer.get_weights()[0]
 
# 각 입력에 대한 평균 Weight를 계산! 
feature_weights = np.mean(np.abs(weights), axis=1)
 
# 입력값의 자리중 어떤 자리가 가장 영향력이 큰지 알아내자! 
max_weight_index = np.argmax(feature_weights)
 
print(feature_weights)