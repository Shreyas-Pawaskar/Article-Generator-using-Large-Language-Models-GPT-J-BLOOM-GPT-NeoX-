
# Article Generator using Large Language Models (GPT-J, BLOOM, GPT-NeoX)

## Project Overview

This project compares the performance of three large language models (LLMs) — **GPT-J**, **BLOOM**, and **GPT-NeoX** — for the task of generating articles based on user input prompts. The models were evaluated on several metrics, including generation time, perplexity, fluency, coherence, and relevance. The project includes model fine-tuning, evaluation, and report generation.

## Models Used
- **GPT-J** (6 billion parameters)
- **BLOOM** (176 billion parameters, multilingual)
- **GPT-NeoX** (20 billion parameters)

## Performance Evaluation

The models were evaluated based on:
- **Generation Time:** Time taken to generate a 200-word article.
- **Perplexity:** A measure of how well the model fits the text (lower is better).
- **Fluency, Coherence, and Relevance:** Subjective human evaluation.

## Requirements

- Python 3.8+
- Hugging Face Transformers
- PyTorch
- Accelerate (`pip install accelerate`)
- Additional libraries: `pandas`, `numpy`, `docx` for report generation

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/article_generator.git
   cd article_generator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

To run the article generation for any model, use the following command:

```bash
python gptj_article_generator.py  # For GPT-J
python bloom_article_generator.py  # For BLOOM
python gptneox_article_generator.py  # For GPT-NeoX
```

## Results

A comparison report on the models' performance is generated in a Word document (`Article_Generator_Comparison_Report.docx`), which includes the evaluation of generation time, perplexity, and human evaluations for fluency and coherence.

## Future Work

- Dynamic knowledge integration for expanding the LLMs' knowledge base.
- Support for multiple languages and sentiment analysis integration.
- Further fine-tuning of the models for specific domains.

## License

This project is licensed under the MIT License.
