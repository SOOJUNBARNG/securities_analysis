# 必要なライブラリのインポート
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# ダミーデータの生成
np.random.seed(42)
X = np.random.rand(100, 1)  # 例として1つの特徴量を持つデータを生成
print(X)
y = 4 * (X - 0.5) ** 2 + np.random.randn(100, 1) / 10  # 二次関数にノイズを加えた目標変数
print(y)

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gradient Boosting Regressionモデルの構築と学習
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=42)
gb_regressor.fit(X_train, y_train.ravel())

# テストデータでの予測
y_pred = gb_regressor.predict(X_test)

# モデルの評価（平均二乗誤差を使用）
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")