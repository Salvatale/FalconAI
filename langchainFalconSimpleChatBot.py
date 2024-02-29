import chainlit as cl

import os
huggingfacehub_api_token = os.environ['HUGGINGFACEHUB_API_TOKEN']


from langchain import HuggingFaceHub

repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=huggingfacehub_api_token,
                     repo_id=repo_id,
                     model_kwargs={"temperature":0.6,"max_new_tokens":500})

from langchain import PromptTemplate, LLMChain

template = """
You are a helpful AI assistant and provide the answer for the question asked politely.

{question}

Answer: .
"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

while True:
    question = input("User: ")
    if question in ["bye","exit"]:
        break

    print(llm_chain.run(question))

# @cl.on_chat_start
# def main():
#     # Instantiate the chain for that user session
#     prompt = PromptTemplate(template=template, input_variables=["question"])
#     llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

#     # Store the chain in the user session
#     cl.user_session.set("llm_chain", llm_chain)


# @cl.on_message
# async def main(message: str):
#     # Retrieve the chain from the user session
#     llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

#     # Call the chain asynchronously
#     res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

#     # Do any post processing here

#     # Send the response
#     await cl.Message(content=res["text"]).send()
