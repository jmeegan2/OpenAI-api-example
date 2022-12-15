import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="A two-column spreadsheet of top science fiction movies and the year of release:\n\nTitle |  Year of release",
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response) # prints the completed text
# print(response.model) # prints the model used for the completion
