from metaphor_python import Metaphor
from bs4 import BeautifulSoup
import openai

#summarize singular html file
def summarize_html_content(document_id):
    #parse HTML using BeautifulSoup
    metaphor = Metaphor("")
    extracted_text = response = metaphor.get_contents([document_id]).contents[0].extract
    #use chatgpt to generate summary
    prompt = "Summarize the following text:\n" + extracted_text
    openai.api_key = ""
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    summarized_text = response.choices[0].text.strip()
    return summarized_text


#get related documents using metaphor api
def get_related_documents(query: str):
    metaphor = Metaphor("")
    documents = metaphor.search(
    query,
    num_results=2,
    use_autoprompt=True,
    )
    return documents.results


#summarize a list of html documents
def summarize_related_documents(documents: list):
    summarized_documents = ""
    for index, document in enumerate(documents):
        summarized_html_text = summarize_html_content(document.id)
        summarized_documents += f"{index}: {document.title}\n"
        summarized_documents += f"{summarized_html_text}\n"
    return summarized_documents

#get summarized list of related documents using metaphor api
def get_summarized_documents(query: str):
    related_documents = get_related_documents(query=query)
    summarized_documents = summarize_related_documents(related_documents)
    return summarized_documents
    
if __name__ == "__main__":
    print(get_summarized_documents("how to swing a golf club"))