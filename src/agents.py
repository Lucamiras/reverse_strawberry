from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class Agent:
    def __init__(self, name, prompt, model="llama3.1", temperature=0.7):
        self.name = name
        self.prompt = prompt
        self.llm = ChatOllama(
            model=model,
            temperature=temperature
        )
        self.prompt_template = PromptTemplate(
            template="""
                {prompt} \n
                Finally, here's your materials: \n
                {user_prompt} \n
                Good luck, Agent!
            """,
            input_variables=['prompt', 'user_prompt']
        )

    def deploy_agent(self, user_prompt):
        rag_chain = self.prompt_template | self.llm | StrOutputParser()
        response = rag_chain.invoke({
            "prompt": self.prompt,
            "user_prompt": user_prompt
        })
        return response


