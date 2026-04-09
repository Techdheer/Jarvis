from groq import Groq

# Initialize Groq
client = Groq(api_key="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")

# Prompt
prompt = "Write a professional resignation email to my boss"

# Correct API call
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",   # ✅ UPDATED MODEL
    messages=[
        {"role": "system", "content": "You are a professional email writer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=300
)

# Output
print(response.choices[0].message.content)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company], and I am grateful for the opportunity to work here. I have learned a great deal during my time in this position, and I am grateful for the experience.\n\nIf I can be of any assistance during this transition, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1683815400,
  "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 125,
    "prompt_tokens": 9,
    "total_tokens": 134
  }
}
'''