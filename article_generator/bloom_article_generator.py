# bloom_article_generator.py

from transformers import BloomForCausalLM, AutoTokenizer
import torch

# Load BLOOM model and tokenizer
model_name = "bigscience/bloom-3b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BloomForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

def generate_article(prompt, max_length=250):
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    outputs = model.generate(inputs.input_ids, max_length=max_length, do_sample=True, top_p=0.95, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test the article generator
if __name__ == "__main__":
    prompt = "Write an article on the impact of climate change"
    article = generate_article(prompt)
    print("BLOOM Generated Article:\n", article)
