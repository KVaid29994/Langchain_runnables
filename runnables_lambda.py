# from langchain_core.runnables import RunnableLambda

# # A simple lambda function
# def to_uppercase(text: str) -> str:
#     return text.upper()

# # Wrap it into a RunnableLambda
# uppercase_runnable = RunnableLambda(to_uppercase)

# # Invoke it
# result = uppercase_runnable.invoke("hello langchain!")
# print(result)  

from langchain_core.prompts import PromptTemplate

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough , RunnableLambda

load_dotenv()

prompt = PromptTemplate(template= "generate a tweet about {topic}", input_variables=["topic"])



# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

def word_count(text):
    return len(text.split())

paralled_chain = RunnableParallel( {"joke" : RunnablePassthrough(), "word_count": RunnableLambda(word_count)})

final_chain = RunnableSequence(joke_gen_chain, paralled_chain)

print (final_chain.invoke({"topic", "AI"}))