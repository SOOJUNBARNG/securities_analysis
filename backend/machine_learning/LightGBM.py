# 必要なライブラリのインポート
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# ダミーデータの生成
np.random.seed(42)
X = np.random.rand(100, 1)  # 例として1つの特徴量を持つデータを生成
y = 4 * (X - 0.5) ** 2 + np.random.randn(100, 1) / 10  # 二次関数にノイズを加えた目標変数

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LightGBM回帰モデルの構築と学習
lgb_params = {
    'objective': 'regression',
    'metric': 'mse',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

train_data = lgb.Dataset(X_train, label=y_train.ravel())
test_data = lgb.Dataset(X_test, label=y_test.ravel(), reference=train_data)

num_round = 100  # 学習のイテレーション数

lgb_regressor = lgb.train(lgb_params, train_data, num_round, valid_sets=[test_data], early_stopping_rounds=10)

# テストデータでの予測
y_pred = lgb_regressor.predict(X_test, num_iteration=lgb_regressor.best_iteration)

# モデルの評価（平均二乗誤差を使用）
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
