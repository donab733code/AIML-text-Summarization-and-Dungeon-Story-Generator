from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

result = generator(
    "A young wizard entered an ancient forest and discovered",
    max_new_tokens=80,
    do_sample=True,
    temperature=0.8
)

print(result[0]["generated_text"])
