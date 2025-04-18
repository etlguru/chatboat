from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt):
    return generator(prompt, max_length=100)[0]['generated_text']
