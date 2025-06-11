from langchain_core.prompts import PromptTemplate

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(template= "generate a tweet about {topic}", input_variables=["topic"])

prompt2 = PromptTemplate(template= "generate a linkedin post about {topic}", input_variables=["topic"])

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


parallel_chain = RunnableParallel({"tweet": RunnableSequence(prompt1, model, parser),
                                   "linkedin" : RunnableSequence(prompt2, model, parser)

})

result = parallel_chain.invoke({"topic":"AI"})

print (result['tweet'])
print ("---"*20)
print (result['linkedin'])