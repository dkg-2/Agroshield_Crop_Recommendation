# import gradio as gr
# import pickle
# import numpy as np

# # Load model and scaler
# model = pickle.load(open("model.pkl", "rb"))
# scaler = pickle.load(open("scaler.pkl", "rb"))

# # Crop dictionary
# crop_dict = {
#     1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
#     8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
#     14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
#     19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
# }

# # Prediction function
# def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
#     features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
#     features_scaled = scaler.transform(features)
#     prediction = model.predict(features_scaled)[0]
#     return f"🌾 Recommended Crop: {crop_dict.get(prediction, 'Unknown')}"

# # Custom CSS for black background and white text
# custom_css = """
# body {
#     background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
#                 url('https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2') no-repeat center center fixed;
#     background-size: cover;
#     font-family: 'Segoe UI', sans-serif;
#     color: #fff;
# }
# #logo img {
#     display: block;
#     margin: auto;
#     width: 90px;
#     margin-bottom: 10px;
# }
# .gradio-container {
#     max-width: 700px;
#     margin: auto;
#     padding: 25px;
#     border-radius: 20px;
#     background-color: #222222dd;
#     box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
# }
# .range-box {
#     background-color: #333333;
#     padding: 25px;
#     border-radius: 15px;
#     margin-bottom: 25px;
#     font-size: 17px;
#     color: #f1f1f1;
#     line-height: 1.8;
#     box-shadow: 0 0 10px rgba(0,0,0,0.2);
#     font-weight: bold;
# }
# """

# # Input range guide (styled and separated)
# range_guide = """
# 🔍 **Input Parameter Ranges**:
# 🌿 **Nitrogen (N):** 0 - 140  
# 🌿 **Phosphorus (P):** 5 - 145  
# 🌿 **Potassium (K):** 5 - 205  
# 🌡️ **Temperature:** 8.0°C - 43.0°C  
# 💧 **Humidity:** 14.0% - 100.0%  
# ⚗️ **pH Value:** 3.5 - 9.9  
# 🌧️ **Rainfall:** 20.0mm - 300.0mm
# """

# # Gradio Interface
# with gr.Blocks(css=custom_css) as demo:
#     with gr.Column():
#         # gr.Markdown("    ##     🌱 **AgroShield - Crop Recommendation System**     ")
#         gr.HTML('<h2 style="text-align: center;">🌱 <b>AgroShield - Crop Recommendation System</b></h2>')
#         gr.HTML('<div id="logo"><img src="https://img.icons8.com/office/80/plant-under-rain.png" alt="Logo"></div>')
#         gr.Markdown("Predict the most suitable crop based on soil and weather inputs.")
#         gr.Markdown(f'<div class="range-box">{range_guide}</div>')

#         with gr.Row():
#             N = gr.Number(label="Nitrogen (N)", value=50)
#             P = gr.Number(label="Phosphorus (P)", value=50)
#             K = gr.Number(label="Potassium (K)", value=50)

#         with gr.Row():
#             temp = gr.Number(label="Temperature (°C)", value=25.0)
#             humidity = gr.Number(label="Humidity (%)", value=60.0)

#         with gr.Row():
#             ph = gr.Number(label="pH", value=6.5)
#             rainfall = gr.Number(label="Rainfall (mm)", value=100.0)

#         output = gr.Textbox(label="Prediction")

#         submit = gr.Button("🚀 Recommend Crop")
#         submit.click(fn=recommend_crop, inputs=[N, P, K, temp, humidity, ph, rainfall], outputs=output)

# # Launch app
# demo.launch()



import gradio as gr
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Crop dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 
    7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 
    12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 
    17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 
    21: "Chickpea", 22: "Coffee"
}

def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    return f"🌱 **{crop_dict.get(prediction, 'Unknown')}** is the recommended crop"

# Green theme CSS matching web app
custom_css = """
:root {
    --primary: #2e7d32;  /* Material Green 800 */
    --primary-hover: #1b5e20;  /* Material Green 900 */
    --surface: #f5fbf6;  /* Light green background */
    --border: #c8e6c9;   /* Subtle green border */
}

body {
    background: var(--surface);
    font-family: 'Inter', system-ui, sans-serif;
}

.gradio-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2.5rem;
    background: white;
    border-radius: 1.25rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
    border: 1px solid var(--border);
}

.dark .gradio-container {
    background: #1a3221;
    border-color: #2d4d38;
}

.input-group {
    background: #ffffff;
    padding: 1.75rem;
    border-radius: 1rem;
    border: 1px solid var(--border);
    margin-bottom: 2rem;
}

.input-label {
    font-weight: 600;
    color: var(--primary);
    margin-bottom: 0.75rem;
    display: block;
    font-size: 0.95rem;
    letter-spacing: 0.5px;
}

input[type="number"] {
    width: 100%;
    padding: 0.875rem 1.25rem;
    border: 2px solid var(--border);
    border-radius: 0.75rem;
    background: #f8faf9;
    transition: all 0.2s;
    font-size: 1rem;
}

input[type="number"]:focus {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.15);
    background: white;
}

button {
    background: var(--primary) !important;
    color: white !important;
    padding: 1rem 2.5rem !important;
    border-radius: 0.875rem !important;
    transition: all 0.2s !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.75px;
    border: none !important;
}

button:hover {
    background: var(--primary-hover) !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(46, 125, 50, 0.2);
}

.output-text {
    font-size: 1.375rem;
    font-weight: 700;
    color: var(--primary);
    padding: 1.75rem;
    background: #e8f5e9;
    border-radius: 1rem;
    text-align: center;
    border: 2px dashed var(--border);
    margin: 1.5rem 0;
}

.markdown h1 {
    color: var(--primary) !important;
    font-size: 2rem !important;
    margin-bottom: 0.75rem !important;
    text-align: center;
}

.markdown p {
    color: #4a6350 !important;
    margin-bottom: 2rem !important;
    text-align: center;
    line-height: 1.6;
}

.parameter-list {
    color: #4a6350;
    padding: 1.5rem;
    background: #f0faf1;
    border-radius: 0.75rem;
    margin: 1.5rem 0;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Default()) as demo:
    with gr.Column(elem_classes="gradio-container"):
        gr.Markdown("""
        <div style="margin-bottom: 2.5rem">
            <h1 style="font-size: 2.25rem; margin-bottom: 0.5rem">🌱 Crop Recommendation</h1>
            <p style="font-size: 1.1rem">AI-powered agricultural insights for optimal crop selection</p>
        </div>
        """)
        
        with gr.Column(elem_classes="input-group"):
            gr.Markdown("### Soil Nutrient Levels")
            with gr.Row():
                N = gr.Number(label="Nitrogen (N)", value=50, minimum=0, maximum=140)
                P = gr.Number(label="Phosphorus (P)", value=50, minimum=5, maximum=145)
                K = gr.Number(label="Potassium (K)", value=50, minimum=5, maximum=205)
            
            gr.Markdown("### Environmental Conditions")
            with gr.Row():
                temp = gr.Number(label="Temperature (°C)", value=25.0, minimum=8.0, maximum=43.0)
                humidity = gr.Number(label="Humidity (%)", value=60.0, minimum=14.0, maximum=100.0)
            
            with gr.Row():
                ph = gr.Number(label="pH Level", value=6.5, minimum=3.5, maximum=9.9)
                rainfall = gr.Number(label="Rainfall (mm)", value=100.0, minimum=20.0, maximum=300.0)

        output = gr.Markdown(elem_classes="output-text")
        
        gr.Markdown("""
        <div class="parameter-list">
            <h3 style="color: var(--primary); margin-bottom: 1rem">📏 Parameter Ranges</h3>
            <div style="columns: 2; gap: 2rem">
                <p>🌿 Nitrogen: 0-140</p>
                <p>🌿 Phosphorus: 5-145</p>
                <p>🌿 Potassium: 5-205</p>
                <p>🌡️ Temperature: 8-43°C</p>
                <p>💧 Humidity: 14-100%</p>
                <p>⚗️ pH Level: 3.5-9.9</p>
                <p>🌧️ Rainfall: 20-300mm</p>
            </div>
        </div>
        """)
        
        gr.Button("Generate Recommendation", variant="primary").click(
            fn=recommend_crop,
            inputs=[N, P, K, temp, humidity, ph, rainfall],
            outputs=output
        )

demo.launch()