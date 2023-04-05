secret_key='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'
import openai
openai.api_key=secret_key
prompt = 'tell me slogan for a security company'

output = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = prompt,
    max_tokens=200,
    temperature =0
)
print(output)