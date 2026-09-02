
import streamlit as st
import pandas as pd
import joblib

# Load saved model and preprocessing objects
model = joblib.load("conversion_model.pkl")
encoder = joblib.load("onehot_encoder.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="E-Commerce Conversion Predictor",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 E-Commerce Session Conversion Predictor")
st.write("Predict whether a website session is likely to result in an order.")

st.subheader("Enter Session Details")

# Numeric feature
is_repeat_session = st.selectbox(
    "Is this a repeat session?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# Categorical features
utm_source = st.selectbox(
    "UTM Source",
    list(encoder.categories_[0])
)

utm_campaign = st.selectbox(
    "UTM Campaign",
    list(encoder.categories_[1])
)

utm_content = st.selectbox(
    "UTM Content",
    list(encoder.categories_[2])
)

device_type = st.selectbox(
    "Device Type",
    list(encoder.categories_[3])
)

http_referer = st.selectbox(
    "HTTP Referrer",
    list(encoder.categories_[4])
)

if st.button("Predict Conversion"):

    # Create input data
    input_data = pd.DataFrame({
        "is_repeat_session": [is_repeat_session],
        "utm_source": [utm_source],
        "utm_campaign": [utm_campaign],
        "utm_content": [utm_content],
        "device_type": [device_type],
        "http_referer": [http_referer]
    })

    # Separate numeric and categorical features
    numeric_input = input_data[["is_repeat_session"]]
    categorical_input = input_data[
        [
            "utm_source",
            "utm_campaign",
            "utm_content",
            "device_type",
            "http_referer"
        ]
    ]

    # Apply same preprocessing used during training
    numeric_scaled = scaler.transform(numeric_input)
    categorical_encoded = encoder.transform(categorical_input)

    # Combine features
    import numpy as np

    processed_input = np.hstack([
        numeric_scaled,
        categorical_encoded
    ])

    # Prediction
    prediction = model.predict(processed_input)[0]
    probability = model.predict_proba(processed_input)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Likely to Convert")
    else:
        st.warning("⚠️ Unlikely to Convert")

    st.metric(
        "Conversion Probability",
        f"{probability * 100:.2f}%"
    )
