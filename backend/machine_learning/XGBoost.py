# 必要なライブラリのインポート
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# ダミーデータの生成
np.random.seed(42)
X = np.random.rand(100, 1)  # 例として1つの特徴量を持つデータを生成
y = 4 * (X - 0.5) ** 2 + np.random.randn(100, 1) / 10  # 二次関数にノイズを加えた目標変数

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost回帰モデルの構築と学習
xgb_params = {
    'objective': 'reg:squarederror',
    'colsample_bytree': 0.9,
    'learning_rate': 0.1,
    'max_depth': 3,
    'alpha': 10
}

train_data = xgb.DMatrix(X_train, label=y_train)
test_data = xgb.DMatrix(X_test, label=y_test)

num_round = 100  # 学習のイテレーション数

xgb_regressor = xgb.train(xgb_params, train_data, num_round, evals=[(test_data, 'eval')], early_stopping_rounds=10)

# テストデータでの予測
y_pred = xgb_regressor.predict(test_data)

# モデルの評価（平均二乗誤差を使用）
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
