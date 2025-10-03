from flask import Flask, render_template_string, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load mô hình và scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
model_features = joblib.load("model_features.pkl")

# Template HTML với Bootstrap
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>🔍 Dự đoán gian lận - Demo</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body { background-color: #ecf0f1; padding: 30px; }
        .container { background: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); }
        h2 { text-align: center; margin-bottom: 20px; color: #2c3e50; }
        .btn-custom { margin: 5px; }
    </style>
</head>
<body>
<div class="container">
    <h2>🔍 Hệ thống dự đoán giao dịch thẻ tín dụng </h2>
    <p class="text-muted">Model expects features: {{ len_features }} features (V1, V2, ..., Amount)</p>

    <div class="mb-3">
        <a href="/auto" class="btn btn-success btn-custom">✅ Auto-run (read excel & predict)</a>
        <a href="/upload" class="btn btn-primary btn-custom">📂 Upload file (.csv/.xlsx)</a>
        <a href="/sample" class="btn btn-secondary btn-custom">⬇️ Download example sample CSV</a>
    </div>

    {% if table %}
    <h5>Kết quả (hiển thị tối đa 50 hàng đầu)</h5>
    {{ table|safe }}
    {% endif %}

    {% if summary %}
    <div class="alert alert-info mt-3">
        <b>📊 Thống kê:</b><br>
        Tổng số giao dịch: {{ summary.total }} <br>
        ✅ Hợp lệ: {{ summary.valid }} <br>
        ❌ Gian lận: {{ summary.fraud }}
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, table=None, summary=None, len_features=len(model_features))

@app.route("/auto")
def auto_run():
    # Đọc dữ liệu từ Excel gốc
    df = pd.read_excel("creditcard_100k_80_20.xlsx")
    X = df[model_features]
    X_scaled = scaler.transform(X)

    preds = model.predict(X_scaled)

    df["Prediction"] = preds
    df["Kết quả"] = df["Prediction"].map({0: "✅ Hợp lệ", 1: "❌ Gian lận"})

    # Thống kê
    summary = {
        "total": len(df),
        "valid": (df["Prediction"] == 0).sum(),
        "fraud": (df["Prediction"] == 1).sum()
    }

    # Xuất bảng đẹp
    table_html = df.head(50).to_html(classes="table table-bordered table-striped text-center", index=False)

    return render_template_string(HTML_TEMPLATE, table=table_html, summary=summary, len_features=len(model_features))

if __name__ == "__main__":
    app.run(debug=True)
