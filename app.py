import streamlit as st
import PyPDF2
import io
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt



stopwords = set(STOPWORDS)

st.write("Word Cloud") 

def extract_data(pdfFileObj):
        # creating a pdf file object 
    # pdfFileObj = open(pdf_file, 'rb') 
        
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
    # printing number of pages in pdf file 
    st.write('number of pages',pdfReader.numPages)

    numPages = pdfReader.numPages
    text = []
    i = 0
    while numPages:
    # creating a page object 
        pageObj = pdfReader.getPage(i) 
        text.append(pageObj.extractText())
        i += 1
        numPages -= 1
    # extracting text from page 
    # st.write(text) 
    # st.write(text[0])
    # closing the pdf file object 
    pdfFileObj.close()
    return text 



uploaded_file = st.file_uploader("Upload a pdf file", "pdf")
# st.write(uploaded_file)

def gen_wordcloud(data):
    comment_words = ''
    for text in data:
        tokens = text.split()
        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        comment_words += " ".join(tokens)+" "
        wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10).generate(comment_words)
        break
    # print(comment_words)

    # plot the WordCloud image
    fig, ax = plt.subplots()
    im = ax.imshow(wordcloud)
    st.pyplot(fig)




if uploaded_file is not None:
    file = uploaded_file.read()
    file = io.BytesIO(file)
    data = extract_data(file)
    gen_wordcloud(data)

 


