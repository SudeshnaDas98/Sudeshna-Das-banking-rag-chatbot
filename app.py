import gradio as gr
from main import ask_chatbot

def chatbot_interface(message, history):

    response = ask_chatbot(message)

    return response

demo = gr.ChatInterface(
    fn=chatbot_interface,
    title="🏦 Banking Support Chatbot"
)

demo.launch()
