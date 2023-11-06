
import openai

openai.api_key = "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"



user_prompt= input("how can I help Yoy ?") #like msg input

response= openai.Image.create(

    prompt=user_prompt,
    n=1,# because we only want one image
    size= "512x512"
)

image_url= response['data'][0]['URL']

print(image_url)