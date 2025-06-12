# {
# Using VirtualchatbotTest memory
# (venv) python3 -m venv chatbotTest
# (venv) source chatbotTest/bin/activate
# (chatbotTest) (venv)
# }



import json
from langchain_core.prompts import ChatPromptTemplate

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser







# Template for checking kids grammar.
templateSyntaxCorrection="""
You are given a sentence in Hebrew.
The sentence was made by child aged 2-5.
Return if the child said the sentence grammarly correct, else, return the correct sentence.
DO NOT ADD ADDITIONAL TEXT.
Answer shortly, user less than 10 words.
Here is the sentence: 
{input}

Answer:
"""



## Need to be changed to "Correct Sentence" and not "טעות", make llm bigger --> change prompt.
# llama 3.1 8b doesn't handle Hebrew well.
templateSyntaxCorrection="""
You are given a sentence in Hebrew.
The sentence was made by child aged 2-5.
Return "כל הכבוד!" if the child said the sentence grammarly correct, else, return "טעות".
DO NOT ADD ADDITIONAL TEXT.
Answer shortly, user less than 10 words.
Here is the sentence: 
{input}

Answer:
"""
modelLlama3_8_Normal = ChatOllama(model="llama3.1:8b", temperature= 0.7)
modelRouter = ChatOllama(model="llama3.2:3b", temperature=0, format="json")

promptSyntax = ChatPromptTemplate.from_template(templateSyntaxCorrection)
Syntax_Chat = promptSyntax | modelLlama3_8_Normal | StrOutputParser()


# Template For Evaluation, more criteria can be added.
# A better Option will be connecting LLM to RAG of criteria.
templateEvaluation="""
You are given a list of sentence in Hebrew that a child.
Provide a diagnosis based on children sentences.

Here is additional information:
Age 3: Almost exclusively 2 words sentences, Inflection errors.
Age 4: Lack of coordinating conjunction sentences, Conjunction words errors.
Age 5: Lack of subordinating conjunction sentences, Tense errors.
Each age's errors are relevant for the ages above it but not below it.

Tell in the diagnostic that professional opinion is required.

Here are the sentences of the child: 
{input}
Here is the age of the child:
{age}

Evaluation:
"""

promptEvaluation = ChatPromptTemplate.from_template(templateEvaluation)
Evaluation_chat = promptEvaluation | modelLlama3_8_Normal | StrOutputParser()

def run_LLM_model_syntax(userInput):
    print("Running Syntax LLM")
    result = Syntax_Chat.invoke({"input": userInput})
    print(f"The LLM syntax result is:\n{result}")
    return result
def run_LLM_model_evaluation(userInput,age):
    print("Running Evaluation LLM")
    eval_result = Evaluation_chat.invoke({"input": userInput,
                                          "age":age})
    file_name = "evaluation.txt"
    with open(file_name, "w") as file:
        file.write(str(eval_result))  # Convert the result to a string before writing

    print(f"Evaluation result saved to {file_name}")
    return eval_result


# User answer is stored in known path
def run_LLM_model_evaluation_fullInference(age):
    print("Running Evaluation LLM")
    with open("users_answers.txt", "r", encoding="utf-8") as file:
        userInput= file.read()
        print(f"Children History:\n{userInput}")

    eval_result = Evaluation_chat.invoke({"input": userInput,
                                          "age":age})
    file_name = "evaluation.txt"
    with open(file_name, "w") as file:
        file.write(str(eval_result))  # Convert the result to a string before writing

    print(f"Evaluation result saved to {file_name}")
    return eval_result



if __name__ == "__main__":
    # handle_conv()
    with open("users_answers.txt", "r", encoding="utf-8") as file:
        text= file.read()
        print(f"Chldren History:\n{text}")

    result = run_LLM_model_evaluation(userInput=text,age="5")
    print(result)
