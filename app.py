# # import streamlit as st
# # from story_generator import generate_story


# # st.title("🏰 AI Dungeon Story Generator")

# # st.write(
# #     "Create interactive fantasy stories using GPT-2"
# # )


# # genre = st.selectbox(
# #     "Choose Genre",
# #     [
# #         "Fantasy",
# #         "Mystery",
# #         "Adventure",
# #         "Sci-Fi"
# #     ]
# # )


# # prompt = st.text_area(
# #     "Enter your story beginning:"
# # )


# # if st.button("Generate Story"):

# #     full_prompt = (
# #         f"{genre} story: {prompt}"
# #     )

# #     stories = generate_story(full_prompt)


# #     for i, story in enumerate(stories):

# #         st.subheader(
# #             f"Continuation {i+1}"
# #         )

# #         st.write(story)


# #         with open(
# #             f"story_{i+1}.txt",
# #             "w",
# #             encoding="utf-8"
# #         ) as file:

# #             file.write(story)


# #     st.success(
# #         "Stories generated and saved!"
# #     )

# import streamlit as st
# import random
# from transformers import pipeline


# # ==========================================
# # PAGE CONFIGURATION
# # ==========================================

# st.set_page_config(
#     page_title="AI Dungeon Story Generator",
#     page_icon="🏰",
#     layout="centered"
# )



# # ==========================================
# # MAGICAL CSS THEME
# # ==========================================

# st.markdown(
# """
# <style>

# .stApp {

# background:
# linear-gradient(
# 135deg,
# #090014,
# #21004b,
# #000000
# );

# color:white;

# }


# h1 {

# color:#FFD700;
# text-align:center;
# font-family:Georgia;

# }


# h2,h3 {

# color:#ffcc66;

# }


# .stButton button {

# background-color:#6a0dad;
# color:white;
# border-radius:20px;
# font-size:18px;
# border:none;
# padding:10px 20px;

# }


# .stButton button:hover {

# background-color:#9b30ff;
# color:white;

# }


# textarea {

# background-color:#12001f !important;
# color:white !important;

# }


# </style>

# """,
# unsafe_allow_html=True
# )



# # ==========================================
# # LOAD GPT-2 MODEL
# # ==========================================

# @st.cache_resource
# def load_model():

#     model = pipeline(
#         "text-generation",
#         model="gpt2"
#     )

#     return model



# generator = load_model()



# # ==========================================
# # STORY GENERATION FUNCTION
# # ==========================================

# def generate_story(prompt):


#     result = generator(

#         prompt,

#         max_new_tokens=400,

#         temperature=0.95,

#         top_k=60,

#         top_p=0.95,

#         repetition_penalty=1.3,

#         no_repeat_ngram_size=3,

#         do_sample=True,

#         num_return_sequences=3,

#         pad_token_id=generator.tokenizer.eos_token_id

#     )


#     stories = []


#     for item in result:

#         stories.append(
#             item["generated_text"]
#         )


#     return stories





# # ==========================================
# # TITLE
# # ==========================================

# st.title("🏰 AI Dungeon Story Generator")


# st.markdown(
# """
# ### ✨ Create your own magical adventure using Artificial Intelligence

# Choose your hero, select a realm, and allow the ancient AI scroll to create your legendary tale.

# """
# )




# # ==========================================
# # HERO SELECTION
# # ==========================================

# character = st.selectbox(

#     "🧙 Choose your Hero",

#     [

#         "Wizard",

#         "Warrior",

#         "Elf",

#         "Dragon Rider",

#         "Vampire",

#         "Knight",

#         "Sorcerer"

#     ]

# )



# # ==========================================
# # GENRE SELECTION
# # ==========================================

# genre = st.selectbox(

#     "🌎 Choose your Realm",

#     [

#         "Fantasy",

#         "Mystery",

#         "Adventure",

#         "Science Fiction",

#         "Dark Fantasy",

#         "Magical Kingdom"

#     ]

# )



# # ==========================================
# # RANDOM QUESTS
# # ==========================================

# quests = [

# "A forgotten dragon kingdom awakens after a thousand years",

# "A mysterious forest hides a powerful ancient crystal",

# "A wizard discovers a portal to another universe",

# "A cursed sword chooses a legendary warrior",

# "An ancient castle appears in the middle of the ocean",

# "A lost civilization sends a magical message",

# "A young hero finds a mysterious glowing artifact"

# ]



# if "prompt" not in st.session_state:

#     st.session_state.prompt = ""




# if st.button("🎲 Generate Random Quest"):


#     st.session_state.prompt = random.choice(quests)

#     st.rerun()





# # ==========================================
# # STORY BEGINNING INPUT
# # ==========================================

# prompt = st.text_area(

#     "📜 Write your story beginning",

#     value=st.session_state.prompt,

#     height=160,

#     placeholder="Example: A young wizard entered an ancient forest and discovered a hidden portal..."

# )





# # ==========================================
# # CAST SPELL BUTTON
# # ==========================================

# if st.button("✨ Cast Story Spell"):



#     if prompt.strip() == "":


#         st.warning(
#             "Please enter a story beginning first."
#         )



#     else:


#         final_prompt = f"""

# You are an award-winning fantasy novelist.

# Write an immersive and cinematic {genre} adventure story.

# The main hero is a {character}.

# Story opening:

# {prompt}


# Continue the story with:

# - magical worlds
# - powerful creatures
# - ancient secrets
# - emotional character moments
# - exciting adventures
# - mysterious discoveries
# - realistic dialogue
# - unexpected twists
# - a satisfying ending


# Make the story feel like a bestselling fantasy novel.

# Write around 300-400 words.

# """



#         with st.spinner(
#             "🪄 The magical scroll is being written..."
#         ):



#             stories = generate_story(
#                 final_prompt
#             )



#         st.success(
#             "✨ Your legendary adventure has been created!"
#         )



#         for index, story in enumerate(stories):


#             st.subheader(
#                 f"📖 Chapter {index+1}"
#             )


#             st.write(
#                 story
#             )


#             st.download_button(

#                 label="📜 Download Magical Scroll",

#                 data=story,

#                 file_name=f"AI_Dungeon_Story_{index+1}.txt",

#                 mime="text/plain"

#             )
# #streamlit run app.py
import streamlit as st
import random
from transformers import pipeline


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Dungeon Story Generator",
    page_icon="🏰",
    layout="centered"
)


# ==========================================
# MAGICAL CSS THEME
# ==========================================

st.markdown(
"""
<style>

.stApp {
    background:
    linear-gradient(
        135deg,
        #090014,
        #21004b,
        #000000
    );

    color:white;
}


h1 {
    color:#FFD700;
    text-align:center;
    font-family:Georgia;
}


h2, h3 {
    color:#ffcc66;
}


.stButton button {

    background-color:#6a0dad;
    color:white;
    border-radius:20px;
    font-size:18px;
    border:none;
    padding:10px 20px;

}


.stButton button:hover {

    background-color:#9b30ff;
    color:white;

}


textarea {

    background-color:#12001f !important;
    color:white !important;

}


.story-box {

    background-color:#12001f;
    border:2px solid #FFD700;
    border-radius:15px;
    padding:20px;
    margin-top:20px;
    line-height:1.7;
    font-size:17px;

}


</style>

""",
unsafe_allow_html=True
)



# ==========================================
# LOAD GPT-2 MODEL
# ==========================================

@st.cache_resource
def load_model():

    model = pipeline(
        "text-generation",
        model="gpt2"
    )

    return model



generator = load_model()



# ==========================================
# STORY GENERATION ENGINE
# ==========================================

def generate_story(prompt):

    result = generator(

        prompt,

        max_new_tokens=500,

        min_new_tokens=250,

        temperature=0.75,

        top_k=40,

        top_p=0.92,

        repetition_penalty=1.5,

        no_repeat_ngram_size=4,

        do_sample=True,

        num_return_sequences=3,

        pad_token_id=generator.tokenizer.eos_token_id

    )


    stories = []


    for item in result:

        text = item["generated_text"]

        # Remove prompt instructions from output
        cleaned = text.replace(prompt, "").strip()

        stories.append(cleaned)


    return stories
# ==========================================
# APPLICATION TITLE
# ==========================================

st.title("🏰 AI Dungeon Story Generator")


st.markdown(
"""
### ✨ Create your own legendary adventure using Artificial Intelligence

Choose your hero, select a realm, and allow the magical AI scroll
to write a cinematic fantasy story.

"""
)



# ==========================================
# HERO SELECTION
# ==========================================

character = st.selectbox(

    "🧙 Choose your Hero",

    [

        "Wizard",
        "Warrior",
        "Elf",
        "Dragon Rider",
        "Vampire",
        "Knight",
        "Sorcerer",
        "Royal Guardian",
        "Ancient Mage"

    ]

)



# ==========================================
# GENRE / REALM SELECTION
# ==========================================

genre = st.selectbox(

    "🌎 Choose your Realm",

    [

        "Epic Fantasy",
        "Dark Fantasy",
        "Mystical Adventure",
        "Magical Kingdom",
        "Ancient Civilization",
        "Science Fantasy",
        "Supernatural Mystery"

    ]

)



# ==========================================
# ADVANCED RANDOM QUEST DATABASE
# ==========================================

quests = [

    "A forgotten dragon kingdom awakens after a thousand years, and a young hero must prevent an ancient war.",


    "Deep inside an enchanted forest, a hidden crystal reveals a secret that could change the fate of all kingdoms.",


    "A mysterious portal appears beneath an abandoned castle and leads to a world lost beyond time.",


    "A cursed sword chooses an ordinary warrior and grants a power that comes with a terrible price.",


    "A dragon rider discovers an ancient prophecy predicting the return of a legendary enemy.",


    "A floating kingdom in the clouds sends a magical message asking for help before darkness arrives.",


    "An ancient artifact is discovered by a young adventurer, but it awakens a forgotten evil.",


    "A vampire guardian protects a hidden magical city from creatures that exist between worlds.",


    "A forgotten civilization leaves behind a mysterious map that leads to the source of ultimate power."

]



# ==========================================
# SESSION STORAGE
# ==========================================

if "prompt" not in st.session_state:

    st.session_state.prompt = ""



# ==========================================
# RANDOM QUEST BUTTON
# ==========================================

if st.button("🎲 Generate Random Quest"):

    st.session_state.prompt = random.choice(quests)

    st.rerun()



# ==========================================
# STORY INPUT
# ==========================================

prompt = st.text_area(

    "📜 Write your story beginning",

    value=st.session_state.prompt,

    height=180,

    placeholder=
    """
Example:

A young wizard entered an ancient forest and discovered
a forgotten portal hidden beneath the roots of an ancient tree...
"""

)



# ==========================================
# BUILD ADVANCED AI PROMPT
# ==========================================

def create_prompt(character, genre, prompt):


    return f"""

You are a professional fantasy novelist.

Write a complete and immersive {genre} adventure story.

Main character:
{character}


Writing requirements:

- Write 400-500 words.
- Use excellent English grammar.
- Create vivid descriptions.
- Use cinematic storytelling.
- Include realistic dialogue.
- Create emotional character moments.
- Add magical creatures and ancient secrets.
- Build suspense gradually.
- Include an unexpected plot twist.
- Give the hero a meaningful challenge.
- Create a powerful climax.
- End with a satisfying conclusion.
- Separate the story into clear paragraphs.
- Do not write explanations.
- Do not mention AI.
- Do not create bullet points.
- Write only the finished story.


Story opening:

{prompt}


Continue the story:

"""
# ==========================================
# CAST STORY SPELL BUTTON
# ==========================================

if st.button("✨ Cast Story Spell"):


    if prompt.strip() == "":

        st.warning(
            "⚠️ Please enter a story beginning first."
        )


    else:

        final_prompt = create_prompt(
            character,
            genre,
            prompt
        )


        with st.spinner(
            "🪄 The magical scroll is being written..."
        ):

            try:

                stories = generate_story(
                    final_prompt
                )


                st.success(
                    "✨ Your legendary adventure has been created!"
                )


                # ==========================================
                # DISPLAY GENERATED STORIES
                # ==========================================

                for index, story in enumerate(stories):


                    st.subheader(
                        f"📖 Chapter {index + 1}"
                    )


                    formatted_story = story.strip()


                    st.markdown(

                        f"""
                        <div class="story-box">

                        {formatted_story}

                        </div>
                        """,

                        unsafe_allow_html=True

                    )


                    # ==========================================
                    # DOWNLOAD BUTTON
                    # ==========================================

                    st.download_button(

                        label="📜 Download Magical Scroll",

                        data=formatted_story,

                        file_name=
                        f"AI_Dungeon_Story_Chapter_{index+1}.txt",

                        mime="text/plain"

                    )


            except Exception as e:


                st.error(
                    "❌ Something went wrong while creating the story."
                )


                st.write(
                    e
                )



# ==========================================
# FOOTER
# ==========================================

st.markdown(
"""
<br><br>

<center>

⚔️ Powered by GPT-2 + Hugging Face Transformers  
<br>
🏰 AI Dungeon Story Generator

</center>

""",
unsafe_allow_html=True
)
