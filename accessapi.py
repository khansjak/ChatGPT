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
print(output)
