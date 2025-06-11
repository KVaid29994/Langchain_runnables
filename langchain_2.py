from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass

class NakliLLM(Runnable):
    def __init__(self):
        print ("LLM created")

    def invoke(self, prompt):
        response_list = [
            "Delhi is the capital of India", 
            "IPL is a cricket league", 
            "AI stands for artificial intelligence."
        ]
        return {"response": random.choice(response_list)}

    def predict(self, prompt):
        return self.invoke(prompt)

class NaklioutputParser():
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']

class NakliPromptTemplate(Runnable):
    def __init__(self, template, input_variable):
        self.template = template
        self.input_variable = input_variable

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data

# Creating a prompt template
template = NakliPromptTemplate(
    template="write a {length} poem about {topic}", 
    input_variable=["topic", "length"]
)

# LLM object
llm = NakliLLM()
parser = NaklioutputParser()
# Fix: Pass the `template` object, not the result of `template.format(...)`
# chain = RunnableConnector([template, llm, parser])

# # Final invocation with proper key case ("topic", not "Topic")
# result = chain.invoke({"length": "long", "topic": "India"})
# print(result)


template1 = NakliPromptTemplate(template="write a joke about {topic}", input_variable=['topic'])
template2 = NakliPromptTemplate(template="Explain the following joke. {response}", input_variable=['response'])

chain1 = RunnableConnector([template1, llm])
# chain1.invoke({"topic":"AI"})

chain2 = RunnableConnector([template2, llm, parser])
# chain2.invoke({"response" :"This is a joke"})

final_chain = RunnableConnector([chain1,chain2])
print (final_chain.invoke({"topic":"cricket"}))