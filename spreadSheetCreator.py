import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="A two-column spreadsheet of top science fiction movies and the year of release:\n\nTitle |  Year of release",
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)