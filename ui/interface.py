import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gradio as gr
from app.model import generate_text

def chat(prompt):
    return generate_text(prompt)

grad_interface = gr.Interface(fn=chat, inputs="text", outputs="text", title="Mini LLM Chatbot")

# grad_interface.launch(server_name="0.0.0.0", server_port=7860)
grad_interface.launch(server_name="0.0.0.0", server_port=7860)

