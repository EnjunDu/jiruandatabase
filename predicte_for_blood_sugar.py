import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from torch.utils.data import DataLoader, TensorDataset

for j in range(1,16):
    data = pd.read_csv(f'./dataset/patient_blood_sugar/patient_blood_sugar.csv{j}.csv')

    blood_sugar_data = data['blood_sugar'].values

    # 数据归一化，使用MinMaxScaler将数据缩放到0-1范围
    scaler = MinMaxScaler(feature_range=(0, 1))
    blood_sugar_data = blood_sugar_data.reshape(-1, 1)
    scaled_blood_sugar = scaler.fit_transform(blood_sugar_data)

    # 使用前170天的数据作为训练集，后30天的数据作为验证集
    train_data = scaled_blood_sugar[:170]
    val_data = scaled_blood_sugar[170:200]


    def create_dataset(data, time_step=1):
        X, y = [], []
        for i in range(len(data) - time_step):
            X.append(data[i:(i + time_step), 0])
            y.append(data[i + time_step, 0])
        return np.array(X), np.array(y)


    time_step = 7  # 选择时间步长，用过去7天预测下一天
    X_train, y_train = create_dataset(train_data, time_step)
    X_val, y_val = create_dataset(val_data, time_step)

    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
    y_val_tensor = torch.tensor(y_val, dtype=torch.float32).view(-1, 1)


    # 构建全连接神经网络模型（MLP）
    class MLP(nn.Module):
        def __init__(self, input_dim, hidden_dim, output_dim):
            super(MLP, self).__init__()
            self.fc1 = nn.Linear(input_dim, hidden_dim)
            self.fc2 = nn.Linear(hidden_dim, hidden_dim)
            self.fc3 = nn.Linear(hidden_dim, output_dim)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.fc3(x)
            return x


    input_dim = time_step
    hidden_dim = 64
    output_dim = 1

    model = MLP(input_dim, hidden_dim, output_dim)

    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    num_epochs = 100
    batch_size = 16

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    for epoch in range(num_epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            optimizer.zero_grad()

            outputs = model(inputs)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {running_loss / len(train_loader):.4f}")

    model.eval()
    with torch.no_grad():
        val_pred = model(X_val_tensor)
        val_pred = val_pred.numpy()
        y_val_true = y_val_tensor.numpy()

    val_pred = scaler.inverse_transform(val_pred)
    y_val_true = scaler.inverse_transform(y_val_true)

    val_mae = mean_absolute_error(y_val_true, val_pred)
    print(f'Validation MAE: {val_mae}')


    full_data = np.concatenate((train_data, val_data), axis=0)
    full_data = full_data.reshape(-1, 1)

    full_data_tensor = torch.tensor(full_data, dtype=torch.float32)

    # 预测未来14天
    predicted_blood_sugar = []
    model.eval()

    for i in range(14):
        input_data = full_data_tensor[-time_step:].view(1, -1)  # 获取过去time_step天的数据
        input_data = input_data.float()
        pred = model(input_data)
        predicted_blood_sugar.append(pred.item())

        full_data_tensor = torch.cat((full_data_tensor, pred.view(1, 1)), dim=0)

    predicted_blood_sugar = scaler.inverse_transform(np.array(predicted_blood_sugar).reshape(-1, 1))

    print([float(x[0]) for x in predicted_blood_sugar])

    train_len = len(train_data)
    val_len = len(val_data)
    predicted_blood_sugar_full = np.concatenate((y_val_true, predicted_blood_sugar), axis=0)

    plt.figure(figsize=(10, 6))
    plt.plot(np.arange(0, train_len + val_len),
             np.concatenate((blood_sugar_data[:train_len], blood_sugar_data[train_len:train_len + val_len])),
             label=f'patient_{j}_Real Data_blood_sugar', color='blue')
    plt.plot(np.arange(train_len + val_len, train_len + val_len + 14), predicted_blood_sugar,
             label=f'patient_{j}_Predicted Future Data_blood_sugar', color='red')
    plt.legend()
    plt.savefig(f'./dataset/results/predict_for_patient_blood_sugar{j}.png')
    plt.show()
