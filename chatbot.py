import openai 

openai.api_key = 'sk-proj-BlbkFJwCVqNB-5wfOmPgO0TuGKKagUhu6ALjJHNypW52wtB706P_XfmNU2dbXUVSEN8SUSob4SS8Qw8A'

def message(message): 
    resposta = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        message = [
            { "role": "user", "content":message}
        ]
    ) 
    return resposta ["choices"]

print(message("Por que o planeta é redondo?"))
