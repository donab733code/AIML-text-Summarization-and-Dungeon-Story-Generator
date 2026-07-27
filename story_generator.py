# from transformers import pipeline, set_seed


# generator = pipeline(
#     "text-generation",
#     model="gpt2",
#     pad_token_id=50256
# )

# set_seed(42)



# def generate_story(prompt, length=200):

#     result = generator(
#         prompt,
#         max_new_tokens=length,
#         num_return_sequences=3,
#         temperature=0.8,
#         top_p=0.9,
#         do_sample=True,
#         pad_token_id=50256
#     )

#     stories = []

#     for story in result:
#         stories.append(story["generated_text"])

#     return stories


from transformers import pipeline, set_seed


# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2",
    pad_token_id=50256
)

set_seed(42)


def generate_story(prompt):

    results = generator(
        prompt,
        max_new_tokens=120,
        num_return_sequences=2,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        pad_token_id=50256
    )

    stories = []

    for result in results:
        stories.append(result["generated_text"])

    return stories

