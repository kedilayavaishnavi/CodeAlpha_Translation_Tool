import streamlit as st
from translator_engine import translate, LANGUAGE_MODELS

st.set_page_config(page_title="AI Translator", page_icon="🌐")
st.title("🌐 Language Translation Tool")

langs = sorted(set([p[0] for p in LANGUAGE_MODELS] + [p[1] for p in LANGUAGE_MODELS]))

LANG_NAMES = {
    "en": "English",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "hi": "Hindi"
}

col1, col2 = st.columns(2)

with col1:
    src = st.selectbox(
        "Source language",
        langs,
        format_func=lambda x: LANG_NAMES.get(x, x)
    )

with col2:
    tgt = st.selectbox(
        "Target language",
        langs,
        index=1,
        format_func=lambda x: LANG_NAMES.get(x, x)
    )

text = st.text_area("Enter text to translate", height=120)

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")

    elif src == tgt:
        st.warning("Source and target languages must differ.")

    else:
        with st.spinner("Translating..."):
            result = translate(text, src, tgt)

        st.success(result)
        st.code(result, language=None)