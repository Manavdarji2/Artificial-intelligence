from get_api_key_value import API_KEY

import google.generativeai as genai
def get_task(text1):
  genai.configure(api_key=API_KEY)

  # Set up the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 2048,
  }
  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]
  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[
  ])

  convo.send_message(f"{text1}")
  return convo.last.text