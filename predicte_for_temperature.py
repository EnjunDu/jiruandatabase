import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping

for j in range (1,16):
    data = pd.read_csv(f'./dataset/patient_temperature/patient_temperature{j}.csv')

    temperature_data = data['temperature'].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    temperature_data = temperature_data.reshape(-1, 1)
    scaled_temperature = scaler.fit_transform(temperature_data)

    # 使用前180天的数据作为训练集，后20天的数据作为验证集
    train_data = scaled_temperature[:180]
    val_data = scaled_temperature[180:200]


    def create_dataset(data, time_step=1):
        X, y = [], []
        for i in range(len(data) - time_step):
            X.append(data[i:(i + time_step), 0])
            y.append(data[i + time_step, 0])
        return np.array(X), np.array(y)


    time_step = 7  # 选择时间步长，假设用过去7天预测下一天
    X_train, y_train = create_dataset(train_data, time_step)
    X_val, y_val = create_dataset(val_data, time_step)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], 1)

    #构建深度学习模型（LSTM）
    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(time_step, 1)))
    model.add(LSTM(units=50, return_sequences=False))

    model.add(Dense(units=1))

    model.compile(optimizer='adam', loss='mean_squared_error')


    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

    xhistory = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_val, y_val),
                        callbacks=[early_stopping])


    train_pred = model.predict(X_train)
    val_pred = model.predict(X_val)

    train_pred = scaler.inverse_transform(train_pred)
    y_train_true = scaler.inverse_transform(y_train.reshape(-1, 1))

    val_pred = scaler.inverse_transform(val_pred)
    y_val_true = scaler.inverse_transform(y_val.reshape(-1, 1))

    train_mae = mean_absolute_error(y_train_true, train_pred)
    val_mae = mean_absolute_error(y_val_true, val_pred)

    print(f'Train MAE: {train_mae}')
    print(f'Validation MAE: {val_mae}')


    full_data = np.concatenate((train_data, val_data), axis=0)  # 合并训练和验证数据
    full_data = full_data.reshape(-1, 1)

    # 预测未来14天
    predicted_temperature = []

    for i in range(14):
        input_data = full_data[-time_step:].reshape(1, time_step, 1)
        pred = model.predict(input_data)
        predicted_temperature.append(pred[0][0])

        full_data = np.append(full_data, pred)

    predicted_temperature = scaler.inverse_transform(np.array(predicted_temperature).reshape(-1, 1))

    # 输出预测的未来14天数据
    print([float(x[0]) for x in predicted_temperature])

    train_len = len(train_data)
    val_len = len(val_data)
    predicted_temperature_full = np.concatenate((y_train_true, y_val_true, predicted_temperature), axis=0)

    # 绘制真实数据与预测数据的对比图
    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(0, train_len + val_len),
             np.concatenate((temperature_data[:train_len], temperature_data[train_len:train_len + val_len])),
             label=f'patient_{j}_Real Data_temperature', color='blue')
    plt.plot(np.arange(train_len + val_len, train_len + val_len + 14), predicted_temperature,
             label=f'patient_{j}_Predicted Future Data_temperature', color='red')
    plt.legend()
    plt.savefig(f'./dataset/results/predict_for_patient_temperature{j}.png')
    plt.show()