from metaphor_python import Metaphor

from transformers import pipeline
from bs4 import BeautifulSoup

#summarize singular html file
def summarize_html_content(document_id):
    #parse HTML using BeautifulSoup
    metaphor = Metaphor("a670dd7f-2ae4-4f14-ac0c-55b6af7c0818")
    text = metaphor.get_contents([document_id]).contents[0].extract
    soup = BeautifulSoup(text, 'html.parser')
    paragraphs = soup.find_all('p')  # Change this as needed to match the structure of the HTML page
    extracted_text = ' '.join([p.get_text() for p in paragraphs])
    #use huggingface summarizer to summarize text
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    # Generate the summary
    summarized_text = summarizer(extracted_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summarized_text


#get related documents using metaphor api
def get_related_documents(query: str):
    metaphor = Metaphor("a670dd7f-2ae4-4f14-ac0c-55b6af7c0818")
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