from openai import AzureOpenAI


def receive_data(prompt):
    url = "https://fi-openaibr.openai.azure.com"
    llm = "gpt-4o-mini"
    api = "2024-12-01-preview"

    client = AzureOpenAI(api_key="762508777fc84125bfbab5ee155f7576", azure_endpoint=url, api_version=api)
    messages = [
        {"role":"user", "content":prompt}
    ]
    completion = client.chat.completions.create(model=llm, messages=messages, temperature=0)
    completionContent = completion.choices[0].message.content
    completionContent = completionContent.replace("```","")
    completionContent = completionContent.replace("json","")
    completionContent = completionContent.split("</think>")[-1]
    completionContent = completionContent.strip()
    return completionContent