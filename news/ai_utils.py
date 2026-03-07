from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


def summarize_article(text):

    text = text[:1500]

    prompt = "Summarize this news article in 3 sentences: " + text

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        inputs["input_ids"],
        max_length=120,
        min_length=40,
        num_beams=4
    )

    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary