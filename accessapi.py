import openai
prompt = 'tell me slogan for a security company'
secret_key = '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'
openai.api_key = secret_key


output = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    max_tokens=200,
    temperature=0
)
output_text=output['choices'][0]['text']
print(output_text)
