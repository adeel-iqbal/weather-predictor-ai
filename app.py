import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Weather Predictor AI",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load saved CatBoost pipeline & Label Encoder
@st.cache_resource
def load_model():
    model = joblib.load('catboost_weather_model.pkl')
    le = joblib.load('label_encoder.pkl')
    return model, le

model, le = load_model()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .main-header p {
        color: #f0f0f0;
        font-size: 1.1rem;
        margin-bottom: 0;
    }
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .prediction-result {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    .prediction-result h2 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .prediction-result p {
        font-size: 1.5rem;
        margin: 0;
    }
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        border-radius: 25px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .sidebar-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .info-card {
   background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   color: white;
   padding: 1rem;
   border-radius: 10px;
   margin-bottom: 1rem;
}
.info-card h3 {
   margin-top: 0;
   margin-bottom: 0.5rem;
}
.info-card p {
   margin: 0.2rem 0;
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🌦️ Weather Predictor AI</h1>
    <p>Powered by CatBoost ML Algorithm | 91.5% Accuracy</p>
</div>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🌡️ Atmospheric Parameters")
    
    # Temperature with color coding
    temp_col1, temp_col2 = st.columns([3, 1])
    with temp_col1:
        temperature = st.slider("Temperature (°C)", min_value=-25.0, max_value=109.0, value=25.0)
    with temp_col2:
        temp_color = "🔥" if temperature > 30 else "🧊" if temperature < 0 else "🌡️"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{temp_color}</div>", unsafe_allow_html=True)
    
    # Humidity with indicator
    hum_col1, hum_col2 = st.columns([3, 1])
    with hum_col1:
        humidity = st.slider("Humidity (%)", min_value=20, max_value=109, value=50)
    with hum_col2:
        hum_color = "💧" if humidity > 70 else "🏜️" if humidity < 40 else "💨"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{hum_color}</div>", unsafe_allow_html=True)
    
    # Wind Speed
    wind_col1, wind_col2 = st.columns([3, 1])
    with wind_col1:
        wind_speed = st.slider("Wind Speed (km/h)", min_value=0.0, max_value=48.5, value=10.0)
    with wind_col2:
        wind_color = "💨" if wind_speed > 20 else "🍃" if wind_speed > 10 else "😴"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{wind_color}</div>", unsafe_allow_html=True)
    
    # Precipitation
    prec_col1, prec_col2 = st.columns([3, 1])
    with prec_col1:
        precipitation = st.slider("Precipitation (%)", min_value=0.0, max_value=109.0, value=20.0)
    with prec_col2:
        prec_color = "☔" if precipitation > 60 else "🌦️" if precipitation > 30 else "☀️"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{prec_color}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("### 🔬 Advanced Metrics")
    
    # Atmospheric Pressure
    press_col1, press_col2 = st.columns([3, 1])
    with press_col1:
        pressure = st.slider("Atmospheric Pressure (hPa)", min_value=800.12, max_value=1199.21, value=1013.0)
    with press_col2:
        press_color = "⬆️" if pressure > 1020 else "⬇️" if pressure < 1000 else "➡️"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{press_color}</div>", unsafe_allow_html=True)
    
    # UV Index
    uv_col1, uv_col2 = st.columns([3, 1])
    with uv_col1:
        uv_index = st.slider("UV Index", min_value=0, max_value=14, value=5)
    with uv_col2:
        uv_color = "🔆" if uv_index > 8 else "☀️" if uv_index > 5 else "🌤️"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{uv_color}</div>", unsafe_allow_html=True)
    
    # Visibility
    vis_col1, vis_col2 = st.columns([3, 1])
    with vis_col1:
        visibility = st.slider("Visibility (km)", min_value=0.0, max_value=20.0, value=10.0)
    with vis_col2:
        vis_color = "👁️" if visibility > 15 else "🌫️" if visibility < 5 else "👀"
        st.markdown(f"<div style='text-align: center; font-size: 2rem; margin-top: 0.5rem;'>{vis_color}</div>", unsafe_allow_html=True)

# Categorical inputs section
st.markdown("---")
st.markdown("### 🌍 Environmental Conditions")

cat_col1, cat_col2, cat_col3 = st.columns(3)

with cat_col1:
    st.markdown("#### ☁️ Cloud Cover")
    cloud_icons = {
        "Overcast": "☁️",
        "Partly Cloudy": "⛅",
        "Clear": "☀️",
        "Cloudy": "🌥️"
    }
    cloud_cover = st.selectbox("", ["Overcast", "Partly Cloudy", "Clear", "Cloudy"])
    st.markdown(f"<div style='text-align: center; font-size: 3rem;'>{cloud_icons[cloud_cover]}</div>", unsafe_allow_html=True)

with cat_col2:
    st.markdown("#### 🗓️ Season")
    season_icons = {
        "Winter": "❄️",
        "Spring": "🌸",
        "Summer": "☀️",
        "Autumn": "🍂"
    }
    season = st.selectbox("", ["Winter", "Spring", "Autumn", "Summer"])
    st.markdown(f"<div style='text-align: center; font-size: 3rem;'>{season_icons[season]}</div>", unsafe_allow_html=True)

with cat_col3:
    st.markdown("#### 📍 Location")
    location_icons = {
        "Inland": "🏞️",
        "Mountain": "⛰️",
        "Coastal": "🏖️"
    }
    location = st.selectbox("", ["Inland", "Mountain", "Coastal"])
    st.markdown(f"<div style='text-align: center; font-size: 3rem;'>{location_icons[location]}</div>", unsafe_allow_html=True)

# Prediction section
st.markdown("---")
st.markdown("### 🔮 Weather Prediction")

# Center the button
button_col1, button_col2, button_col3 = st.columns([1, 2, 1])
with button_col1:
    predict_button = st.button("🔍 Predict Weather Type")

if predict_button:
    with st.spinner("🤖 AI is analyzing weather patterns..."):
        # Create DataFrame for single sample
        input_data = pd.DataFrame({
            'Temperature': [temperature],
            'Humidity': [humidity],
            'Wind Speed': [wind_speed],
            'Precipitation (%)': [precipitation],
            'Atmospheric Pressure': [pressure],
            'UV Index': [uv_index],
            'Visibility (km)': [visibility],
            'Cloud Cover': [cloud_cover.lower()],
            'Season': [season],
            'Location': [location.lower()]
        })

        weather_icons = {
            "Rainy": "🌧️",
            "Sunny": "☀️",
            "Cloudy": "☁️",
            "Snowy": "❄️"
        }

        # Predict
        pred_encoded = model.predict(input_data)[0]
        pred_label = le.inverse_transform([pred_encoded])[0]
        pred_icon = weather_icons[pred_label]

        # Display result with animation
        st.markdown(f"""
        <div class="prediction-result">
            <h2>{pred_icon}</h2>
            <p>Predicted Weather: <strong>{pred_label}</strong></p>
        </div>
        """, unsafe_allow_html=True)

        # Weather recommendations
        recommendations = {
            "Rainy": "☔ Don't forget your umbrella and waterproof jacket!",
            "Sunny": "😎 Perfect day for outdoor activities! Don't forget sunscreen.",
            "Cloudy": "🌤️ Mild conditions ahead. Light jacket recommended.",
            "Snowy": "🧣 Bundle up warm! Watch out for icy conditions."
        }
        
        st.info(recommendations[pred_label])

        # Detailed summary
        st.markdown("### 📊 Input Summary")
        
        # Create a more readable summary
        summary_data = {
            "Parameter": [
                "🌡️ Temperature", "💧 Humidity", "💨 Wind Speed", "🌧️ Precipitation",
                "📊 Pressure", "☀️ UV Index", "👁️ Visibility", "☁️ Cloud Cover",
                "🗓️ Season", "📍 Location", "🔮 Prediction"
            ],
            "Value": [
                f"{temperature}°C", f"{humidity}%", f"{wind_speed} km/h", f"{precipitation}%",
                f"{pressure:.1f} hPa", f"{uv_index}", f"{visibility} km", cloud_cover,
                season, location, f"{pred_icon} {pred_label}"
            ]
        }
        
        summary_df = pd.DataFrame(summary_data)
        st.table(summary_df)

# Sidebar with additional info
with st.sidebar:
    st.markdown("""
    <div class="info-card">
        <h3>🤖 Model Info</h3>
        <p><strong>Algorithm:</strong> CatBoost</p>
        <p><strong>Accuracy:</strong> 91.5%</p>
        <p><strong>Features:</strong> 10 parameters</p>
        <p><strong>Classes:</strong> 4 weather types</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Quick Tips")
    st.markdown("""
    - **Temperature** affects weather type significantly
    - **Precipitation** is key for rainy predictions  
    - **Season** influences overall patterns
    - **Location** affects regional weather characteristics
    """)
    
    st.markdown("### 📈 Model Performance")
    performance_data = {
        "Weather Type": ["Sunny", "Rainy", "Cloudy", "Snowy"],
        "Accuracy": ["92.1%", "91.8%", "90.9%", "91.4%"]
    }
    st.dataframe(pd.DataFrame(performance_data), hide_index=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🚀 Built with Streamlit & CatBoost | 🧠 Powered by Machine Learning</p>
    <p>Made with ❤️ by <strong>Adeel Iqbal</strong></p>
</div>
""", unsafe_allow_html=True)