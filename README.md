# Language Translation Tool — Local Transformer Models

A translation tool powered by locally-served MarianMT transformer models
(HuggingFace), not a third-party API call.

## Features

- Multiple language pairs (EN↔FR, EN↔DE, EN↔ES, EN↔HI)
- Fully local inference after first model download
- Works offline after model download
- Clean Streamlit UI

## Why local models over an API

Calling Google Translate API is a few lines of requests code. This project instead
loads and runs actual sequence-to-sequence transformer models (MarianMT) locally,
demonstrating real NLP model serving rather than API integration.

## Tech Stack

Python, HuggingFace Transformers, MarianMT, PyTorch, Streamlit

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py