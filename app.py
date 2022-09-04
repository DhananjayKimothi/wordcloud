import streamlit as st
import PyPDF2
import io
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

### What to expect 




stopwords = set(STOPWORDS)

original_title = '<p style="font-family:Courier; color:Red; font-size: 40px;">Word Cloud Generator</p>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown('generate word cloud form a pdf document')


heading2 = '<p style="font-family:Courier; color:Blue; font-size: 20px;">What is a word cloud?</p>'
st.markdown(heading2, unsafe_allow_html=True)

st.markdown("A word cloud is a collection, or cluster, of words depicted in different sizes. \
The bigger and bolder the word appears, the more often it's mentioned within a given text and the more important it is.")

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
    text = ' '.join(data)
    # data_ = ' '.join(data)
    if  text:
        tokens = text.split()
        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()
        if tokens:
            comment_words += " ".join(tokens)+" "
            wordcloud = WordCloud(width = 800, height = 800,
                        background_color ='white',
                        stopwords = stopwords,
                        min_font_size = 10).generate(comment_words)
            
  
            fig, ax = plt.subplots()
            im = ax.imshow(wordcloud)
            st.pyplot(fig)
        else:
            heading3 = '<p style="font-family:Courier; color:Red; font-size: 20px;">Sorry!!! OCR unable to extract the text from uploaded pdf, please try another file</p>'
            st.markdown(heading3, unsafe_allow_html=True)




if uploaded_file is not None:
    file = uploaded_file.read()
    file = io.BytesIO(file)
    data = extract_data(file)
    gen_wordcloud(data)

