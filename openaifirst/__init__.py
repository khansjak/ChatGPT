import logging

import azure.functions as func
import openai

prompt = 'Give me a slogan for a security company'
# sample request body 
# {"model": "text-davinci-003","prompt": "Tell me a story in 10 words","max_tokens": 200,"temperature": 0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # authenticate
    secret_key = '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'
    openai.api_key = secret_key

    # get variables from HTTP request body
    req_body = req.get_json()

    # Call OpenAI

    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )

    # format response
    output_text = output['choices'][0]['text']

    # Provide response
    return func.HttpResponse(output_text, status_code=200)
