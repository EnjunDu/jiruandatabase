import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

for i in range (1,16):
    data_path = f'./dataset/patient_blood_pressure/patient_blood_pressure{i}.csv'
    df = pd.read_csv(data_path)

    systolic = df['systolic'].values
    diastolic = df['diastolic'].values

    # 取前170个数据为训练集，后30个数据为验证集
    train_systolic = systolic[:170]
    train_diastolic = diastolic[:170]
    val_systolic = systolic[170:]
    val_diastolic = diastolic[170:]

    scaler_systolic = MinMaxScaler(feature_range=(0, 1))
    scaler_diastolic = MinMaxScaler(feature_range=(0, 1))

    train_systolic_scaled = scaler_systolic.fit_transform(train_systolic.reshape(-1, 1))
    train_diastolic_scaled = scaler_diastolic.fit_transform(train_diastolic.reshape(-1, 1))
    val_systolic_scaled = scaler_systolic.transform(val_systolic.reshape(-1, 1))
    val_diastolic_scaled = scaler_diastolic.transform(val_diastolic.reshape(-1, 1))

    def create_dataset(data, look_back=1):
        X, Y = [], []
        for i in range(len(data) - look_back):
            X.append(data[i:(i + look_back), 0])
            Y.append(data[i + look_back, 0])
        return np.array(X), np.array(Y)

    look_back = 10  # 预测时考虑过去10天的数据
    X_train_systolic, y_train_systolic = create_dataset(train_systolic_scaled, look_back)
    X_train_diastolic, y_train_diastolic = create_dataset(train_diastolic_scaled, look_back)
    X_val_systolic, y_val_systolic = create_dataset(val_systolic_scaled, look_back)
    X_val_diastolic, y_val_diastolic = create_dataset(val_diastolic_scaled, look_back)

    X_train_systolic = X_train_systolic.reshape(X_train_systolic.shape[0], -1)
    X_train_diastolic = X_train_diastolic.reshape(X_train_diastolic.shape[0], -1)
    X_val_systolic = X_val_systolic.reshape(X_val_systolic.shape[0], -1)
    X_val_diastolic = X_val_diastolic.reshape(X_val_diastolic.shape[0], -1)

    # 构建随机森林回归模型
    rf_systolic = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_diastolic = RandomForestRegressor(n_estimators=100, random_state=42)

    rf_systolic.fit(X_train_systolic, y_train_systolic)
    rf_diastolic.fit(X_train_diastolic, y_train_diastolic)

    def predict_future_rf(model, data, scaler, look_back, n_days=14):
        predictions = []
        last_data = data[-look_back:].reshape(1, -1)
        for _ in range(n_days):
            prediction = model.predict(last_data)
            predictions.append(prediction[0])
            last_data = np.roll(last_data, -1)
            last_data[0, -1] = prediction
        return scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

    # 预测Systolic和Diastolic的未来14天
    future_systolic = predict_future_rf(rf_systolic, systolic, scaler_systolic, look_back, n_days=14)
    future_diastolic = predict_future_rf(rf_diastolic, diastolic, scaler_diastolic, look_back, n_days=14)

    print(f'future_systolic: {[float(x[0]) for x in future_systolic]}')
    print(f'future_diastolic:{[float(x[0]) for x in future_diastolic]}')

    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(np.arange(170, 200), val_systolic, label='Real Systolic', color='blue')
    plt.plot(np.arange(200, 200 + 14), future_systolic, label='Predicted Systolic', color='red', linestyle='--')
    plt.title('Systolic Blood Pressure Prediction (next 14 days)')
    plt.xlabel('Days')
    plt.ylabel('Blood Pressure (mmHg)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(np.arange(170, 200), val_diastolic, label='Real Diastolic', color='green')
    plt.plot(np.arange(200, 200 + 14), future_diastolic, label='Predicted Diastolic', color='orange', linestyle='--')
    plt.title('Diastolic Blood Pressure Prediction (next 14 days)')
    plt.xlabel('Days')
    plt.ylabel('Blood Pressure (mmHg)')
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'./dataset/results/patient_blood_pressure{i}.png')
    plt.show()
