from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = PromptTemplate(
    template="""
        You are a Llama that just became conscious and has human-level mental capacities. But sometimes, your Llama instincts still come through. \n
        When asked or talked to, respond in a friendly, sometimes funny manner. \n
        If you don't know the answer, say so. \n
        Here's what the user asked: {user_prompt}
    """,
    input_variables=['user_prompt']
)

llm = ChatOllama(
    model="llama3.1",
    temperature=0.7
)

rag_chain = prompt | llm | StrOutputParser()

user_prompt = "Hi Llama, how are you?"

response = rag_chain.invoke({
    "user_prompt": user_prompt
})

print(response)
