from transformers import MarianMTModel, MarianTokenizer
import functools

LANGUAGE_MODELS = {
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
    ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",
}

@functools.lru_cache(maxsize=8)
def load_model(src, tgt):
    name = LANGUAGE_MODELS[(src, tgt)]
    tokenizer = MarianTokenizer.from_pretrained(name)
    model = MarianMTModel.from_pretrained(name)
    return tokenizer, model

def translate(text, src_lang, tgt_lang):
    if (src_lang, tgt_lang) not in LANGUAGE_MODELS:
        return "Language pair not supported."

    tokenizer, model = load_model(src_lang, tgt_lang)

    batch = tokenizer([text], return_tensors="pt", padding=True)
    generated = model.generate(**batch)

    return tokenizer.decode(generated[0], skip_special_tokens=True)