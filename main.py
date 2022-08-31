#IMPORTACOES

import streamlit as st
import time 

#CONFIGURACOES BASICAS DA PAGINA
st.set_page_config(
    page_title="Jean Mota",
    page_icon="🍌",
    layout="centered",    
)

#CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

with st.sidebar:

    html = "<h1>Menu vazio ainda</h1>"
    st.markdown(html,unsafe_allow_html=True)
    

with st.container():        
    st.title("Curriculum Vitae")
    """    
    * * *
    """

with st.container():        
    st.title(":scroll:Jean Lucas Almeida Mota")        


    pdf_download = ":inbox_tray: Download da versão em pdf <a href='https://drive.google.com/file/d/15h2VtB7J8FaxceLiHX4x3pFUCY3K1zth/view?usp=sharing'>aqui</a>"
    st.markdown(pdf_download,unsafe_allow_html=True)
    """
    :date: 12/06/1997

    :phone: (31) 99468-8276
    """

    link = "<div align='left' style='display: inline_block'><a href='https://www.linkedin.com/in/jean-lucas-almeida-mota-957b0b152/'><img align='center' src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white' alt=''></a>  <a href='https://codeforces.com/profile/jeanhardzz'><img align='center' src='https://img.shields.io/badge/Codeforces-445f9d?style=for-the-badge&logo=Codeforces&logoColor=whiteg' alt=''/></a>  <a href='mailto:jean.lk@hotmail.com'><img align='center' src='https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white' alt=''/></a>  <a href='https://www.instagram.com/jean.lk/'><img align='center' src='https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white' alt=''/></a>  <a href='https://twitter.com/Jean_lucks'><img align='center' src='https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white' alt=''/></a>"
    st.markdown(link, unsafe_allow_html=True)
    """
    * * *
    """

with st.container():
    """
    Where does it come from?

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32    
    * * *
    """

with st.container():
    """
    Why do we use it?

    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).    
    * * *
    """