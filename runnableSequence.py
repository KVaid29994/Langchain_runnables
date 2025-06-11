from langchain_core.prompts import PromptTemplate

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(template= "Write a joke about {topic}", input_variables=["topic"])

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()
prompt2 = PromptTemplate(template= "Explain the joke {response}", input_variables={"response"})

chain = RunnableSequence(prompt1, model, parser,prompt2, model, parser)
print(chain.invoke({"topic":"AI"}))
