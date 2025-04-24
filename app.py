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
    return f"🌾 Recommended Crop: **{crop_dict.get(prediction, 'Unknown')}**"

# Modern CSS matching web app
custom_css = """
:root {
    --primary: #3b82f6;
    --primary-hover: #2563eb;
}

body {
    background: #f8fafc;
    font-family: 'Inter', system-ui, sans-serif;
}

.gradio-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    border-radius: 1rem;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.dark .gradio-container {
    background: #1e293b;
}

.input-group {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 0.5rem;
    border: 1px solid #e2e8f0;
    margin-bottom: 1.5rem;
}

.input-label {
    font-weight: 500;
    color: #334155;
    margin-bottom: 0.5rem;
    display: block;
}

input[type="number"] {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #cbd5e1;
    border-radius: 0.375rem;
    background: #f8fafc;
}

button {
    background: var(--primary) !important;
    color: white !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 0.5rem !important;
    transition: all 0.2s !important;
}

button:hover {
    background: var(--primary-hover) !important;
    transform: translateY(-1px);
}

.output-text {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1e293b;
    padding: 1.5rem;
    background: #f1f5f9;
    border-radius: 0.5rem;
    text-align: center;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Default()) as demo:
    with gr.Column(elem_classes="gradio-container"):
        gr.Markdown("""
        <div class="text-center mb-8">
            <h1 class="text-3xl font-bold mb-2">Crop Recommendation System</h1>
            <p class="text-gray-600">Input soil and climate parameters for AI-powered recommendations</p>
        </div>
        """)
        
        with gr.Column(elem_classes="input-group"):
            gr.Markdown("### Soil Nutrients")
            with gr.Row():
                N = gr.Number(label="Nitrogen (N)", value=50, minimum=0, maximum=140)
                P = gr.Number(label="Phosphorus (P)", value=50, minimum=5, maximum=145)
                K = gr.Number(label="Potassium (K)", value=50, minimum=5, maximum=205)
            
            gr.Markdown("### Environmental Factors")
            with gr.Row():
                temp = gr.Number(label="Temperature (°C)", value=25.0, minimum=8.0, maximum=43.0)
                humidity = gr.Number(label="Humidity (%)", value=60.0, minimum=14.0, maximum=100.0)
            
            with gr.Row():
                ph = gr.Number(label="pH Level", value=6.5, minimum=3.5, maximum=9.9)
                rainfall = gr.Number(label="Rainfall (mm)", value=100.0, minimum=20.0, maximum=300.0)

        output = gr.Markdown(elem_classes="output-text")
        
        gr.Markdown("""
        **Parameter Ranges**  
        - Nitrogen (N): 0-140  
        - Phosphorus (P): 5-145  
        - Potassium (K): 5-205  
        - Temperature: 8-43°C  
        - Humidity: 14-100%  
        - pH: 3.5-9.9  
        - Rainfall: 20-300mm
        """)
        
        gr.Button("Generate Recommendation", variant="primary").click(
            fn=recommend_crop,
            inputs=[N, P, K, temp, humidity, ph, rainfall],
            outputs=output
        )

demo.launch()