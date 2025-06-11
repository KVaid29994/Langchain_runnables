import random

class NakliLLM():
    def __init__(self):
        print ("LLM created")

    def predict(self, prompt):
        response_list =["Delhi is the capital of India", "IPL is a cricket league", "AI stands for artificial intelligence."]
        return {"response": random.choice(response_list)}
    
llm = NakliLLM()

print(llm.predict("what is the capital of delhi")["response"])


class NakliPromptTemplate():
    def __init__(self, template, input_variable):
        self.template = template
        self.input_variable = input_variable

    def format(self, input_dict):
        return self.template.format(**input_dict)
    

template = NakliPromptTemplate(template= "write a {length} poem about {topic}", input_variable= ["topic", "length"])

prompt = template.format({"topic":"India", "length":"short"})
print (prompt)

llm = NakliLLM()
result = llm.predict(prompt)
print (result["response"])


class NakliLLMchain():
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']


template = NakliPromptTemplate(template= "write a {length} poem about {topic}", input_variable= ["topic", "length"])
# print ("Template for chain is ", template)
llm = NakliLLM()

chain = NakliLLMchain(llm, template)

response = chain.run({"length":"short", "topic":"India"})
print(response)
