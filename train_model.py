import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1. Đọc dữ liệu
df = pd.read_excel("creditcard_100k_80_20.xlsx")

# 2. Chia dữ liệu X (features) và y (nhãn)
X = df.drop(columns=["Class"])
y = df["Class"]

# 3. Chia train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Huấn luyện model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# 6. Đánh giá nhanh
y_pred = model.predict(X_test_scaled)
print("Báo cáo đánh giá Logistic Regression:\n")
print(classification_report(y_test, y_pred))

# 7. Lưu model, scaler và danh sách cột
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(X.columns), "model_features.pkl")

print("✅ Đã lưu model, scaler, và features thành công!")
