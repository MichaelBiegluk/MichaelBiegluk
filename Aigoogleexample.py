"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a scavenger hunt for street food around the city of Seoul, Korea.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## Seoul Street Food Scavenger Hunt: \n\n**Welcome to the ultimate Seoul Street Food Adventure!** This scavenger hunt will take you on a delicious journey through the bustling streets of Seoul, where you'll discover iconic Korean street food and hidden gems. \n\n**Instructions:**\n\n* **Team Up:**  Form a team of 2-4 players.\n* **Choose Your Starting Point:**  Select a central location in Seoul as your starting point. \n* **Follow the Clues:**  Each clue will guide you to a specific street food stall or location.\n* **Taste & Conquer:**  Once you've found the food, taste it and enjoy!\n* **Take Photos:**  Capture the delicious moments and share your food adventures on social media!\n* **Don't Forget:**  Be mindful of your surroundings and be respectful of local customs.\n\n**Clues:**\n\n**1. Start your journey where history meets street food.** \n  -  Find the spot where the past and present collide, a landmark with towering gates.\n  -  There you'll find a food vendor, with aroma so bold, serving the perfect bite to start your stroll.\n  -  **What is the food?**  **Tteokbokki** (Spicy Rice Cakes)\n\n**2. Seek a green oasis, where tradition resides.** \n  -  A serene park, with lush greenery, is your next stop.\n  -  Look for a vendor selling sweet treats, with a history so deep.\n  -  **What is the food?** **Bungeoppang** (Fish-Shaped Pastry)\n\n**3.  Venture to a vibrant street, with neon lights so bright.** \n  -  Find a street where energy pulses, a place of bustling delight. \n  -  Look for a vendor with a unique name, a place for laughter and gain.\n  -  **What is the food?** **Kimbap** (Seaweed Rice Rolls)\n\n**4.  Next, seek a hidden treasure, a secret spot for pleasure.**\n  -  An alleyway, tucked away, where aroma fills the day.\n  -  There, you'll find a vendor with a special brew, a savory delight, just for you.\n  -  **What is the food?** **Odeng** (Fish Cake Skewers)\n\n**5.  Your final challenge lies near a famous landmark, a place for a sweet command.**\n  -  Head to the place with a majestic view, where ancient history intertwines with the new.\n  -  Find the vendor with colorful treats, a reward for all the feats.\n  -  **What is the food?** **Hotteok** (Sweet Pancakes)\n\n**Bonus Challenge:** \n\n* **Take a selfie with a friendly local enjoying street food.**\n* **Find a street vendor who speaks a little English and ask them for a food recommendation.**\n\n**Enjoy the delicious journey through Seoul's street food scene!**",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
