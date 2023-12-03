from django.shortcuts import render
import openai
from django.http import JsonResponse
from .models import llm_data

OPENAI_KEY = "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"

openai.api_key = OPENAI_KEY

def gpt_wrapper(user_prompt:str, system_prompt:str="You are a helpful AI assistant", print:bool=True) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
  ]
  )

    output = response.choices[0].message["content"]
 
    return output

# Create your views here.
def llm_landing(request):
    if request.method == "POST":
        print(request.method)
        print(request.user)
        prompt = request.POST["message"]
        output = gpt_wrapper(prompt)
        data = llm_data(user=request.user,message=prompt,response=output)
        data.save()
        return JsonResponse({"message":prompt,"response":output})
    else:
        return render(request,"llm/UI.html")

