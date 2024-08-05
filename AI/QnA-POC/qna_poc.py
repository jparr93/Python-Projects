from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

endpoint = "https://qna-jp-uks.cognitiveservices.azure.com/"
credential = AzureKeyCredential("")
knowledge_base_project = "qna"
deployment = "production"
inputted_question = input('What do you want to ask the QNA bot?')

def main():
    client = QuestionAnsweringClient(endpoint, credential)
    with client:
        question = inputted_question
        output = client.get_answers(
            question = question,
            project_name=knowledge_base_project,
            deployment_name=deployment
        )
    print("Q: {}".format(question))
    print("A: {}".format(output.answers[0].answer))

if __name__ == '__main__':
    main()