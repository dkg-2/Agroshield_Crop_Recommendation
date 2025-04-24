import gradio as gr
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

# Prediction function
def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    return f"🌾 Recommended Crop: {crop_dict.get(prediction, 'Unknown')}"

# Custom CSS for black background and white text
custom_css = """
body {
    background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
                url('https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2') no-repeat center center fixed;
    background-size: cover;
    font-family: 'Segoe UI', sans-serif;
    color: #fff;
}
#logo img {
    display: block;
    margin: auto;
    width: 90px;
    margin-bottom: 10px;
}
.gradio-container {
    max-width: 700px;
    margin: auto;
    padding: 25px;
    border-radius: 20px;
    background-color: #222222dd;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
}
.range-box {
    background-color: #333333;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
    font-size: 17px;
    color: #f1f1f1;
    line-height: 1.8;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
    font-weight: bold;
}
"""

# Input range guide (styled and separated)
range_guide = """
🔍 **Input Parameter Ranges**:
🌿 **Nitrogen (N):** 0 - 140  
🌿 **Phosphorus (P):** 5 - 145  
🌿 **Potassium (K):** 5 - 205  
🌡️ **Temperature:** 8.0°C - 43.0°C  
💧 **Humidity:** 14.0% - 100.0%  
⚗️ **pH Value:** 3.5 - 9.9  
🌧️ **Rainfall:** 20.0mm - 300.0mm
"""

# Gradio Interface
with gr.Blocks(css=custom_css) as demo:
    with gr.Column():
        # gr.Markdown("    ##     🌱 **AgroShield - Crop Recommendation System**     ")
        gr.HTML('<h2 style="text-align: center;">🌱 <b>AgroShield - Crop Recommendation System</b></h2>')
        gr.HTML('<div id="logo"><img src="https://img.icons8.com/office/80/plant-under-rain.png" alt="Logo"></div>')
        gr.Markdown("Predict the most suitable crop based on soil and weather inputs.")
        gr.Markdown(f'<div class="range-box">{range_guide}</div>')

        with gr.Row():
            N = gr.Number(label="Nitrogen (N)", value=50)
            P = gr.Number(label="Phosphorus (P)", value=50)
            K = gr.Number(label="Potassium (K)", value=50)

        with gr.Row():
            temp = gr.Number(label="Temperature (°C)", value=25.0)
            humidity = gr.Number(label="Humidity (%)", value=60.0)

        with gr.Row():
            ph = gr.Number(label="pH", value=6.5)
            rainfall = gr.Number(label="Rainfall (mm)", value=100.0)

        output = gr.Textbox(label="Prediction")

        submit = gr.Button("🚀 Recommend Crop")
        submit.click(fn=recommend_crop, inputs=[N, P, K, temp, humidity, ph, rainfall], outputs=output)

# Launch app
demo.launch()