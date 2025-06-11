## ✅ Example: Joke vs Poem Based on Topic

from langchain_core.prompts import PromptTemplate

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough , RunnableLambda, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate.from_template("write a detailed report on {topic}")
prompt2 = PromptTemplate.from_template("Summarise the following text \n {text}")
# default_prompt = PromptTemplate.from_template("I don't know what to do with {topic}, so just describe it.")


# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

# Chains
report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch((lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
                              RunnablePassthrough() 
                              )

final_chain = RunnableSequence(report_gen_chain,branch_chain)




# Run it
result = final_chain.invoke({"topic": "Russia vs ukraine"})
print(result)
