# model_comparison.py

import time
from gptj_article_generator import generate_article as gptj_generate
from bloom_article_generator import generate_article as bloom_generate
from gpt_neox_article_generator import generate_article as neox_generate

# Evaluation function to assess speed and quality
def evaluate_model(model_func, prompt, model_name):
    start_time = time.time()
    article = model_func(prompt)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Model: {model_name}")
    print(f"Generated Article: {article}")
    print(f"Generation Time: {duration:.2f} seconds\n")

# Test Prompt
prompt = "Explain the importance of sleep for health."

# Evaluate GPT-J
evaluate_model(gptj_generate, prompt, "GPT-J")

# Evaluate BLOOM
evaluate_model(bloom_generate, prompt, "BLOOM")

# Evaluate GPT-NeoX
evaluate_model(neox_generate, prompt, "GPT-NeoX")
