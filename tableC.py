import openai
import html

# Set your OpenAI API key
openai.api_key = "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"

# Call the Completion API
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="A two-column spreadsheet of top historical movies and the year of release:\n\nTitle |  Year of release",
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
