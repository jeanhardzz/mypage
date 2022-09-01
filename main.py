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

    html = "<h1>Meu Perfil</h1>"
    st.markdown(html,unsafe_allow_html=True)
    

with st.container():        
    st.title("Curriculum Vitae")
    """    
    * * *
    """

with st.container():        
    """
    ## ![pdf](https://img.icons8.com/ios/30/000000/pdf--v1.png) Jean Lucas Almeida Mota

    ![Download](https://img.icons8.com/material-outlined/20/000000/downloading-updates.png) Download da versão em pdf [aqui](https://drive.google.com/file/d/15h2VtB7J8FaxceLiHX4x3pFUCY3K1zth/view?usp=sharing)
    * ![Data Nascimento](https://img.icons8.com/ios-filled/18/000000/birthday.png) 12/06/1997
    * ![Whatsapp](https://img.icons8.com/material-outlined/20/000000/whatsapp--v1.png) (31) 99468-8276
    * ![Linkedin](https://img.icons8.com/ios-glyphs/20/000000/linkedin-2--v1.png) [linkedin.com/in/jeanlkmota](www.linkedin.com/in/jeanlkmota)
    * ![Email](https://img.icons8.com/ios-filled/20/000000/gmail.png) [jeanlkmota@gmail.com](mailto:jeanlkmota@gmail.com)               
    * ![Instagram](https://img.icons8.com/ios-glyphs/20/000000/instagram-new.png) [instagram.com/jean.lk/](https://www.instagram.com/jean.lk/)               
    * ![Codeforces](https://img.icons8.com/external-tal-revivo-bold-tal-revivo/20/000000/external-codeforces-programming-competitions-and-contests-programming-community-logo-bold-tal-revivo.png) [codeforces.com/profile/jeanhardzz](https://codeforces.com/profile/jeanhardzz)              
    * ![Twitter](https://img.icons8.com/ios-glyphs/20/000000/twitter--v1.png) [twitter.com/Jean_lucks](https://twitter.com/Jean_lucks)              
    
    * * *

    ## ![pdf](https://img.icons8.com/ios/25/000000/info--v1.png) Sobre mim

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical.

    * * *

    ## ![pdf](https://img.icons8.com/ios/25/000000/rocket--v1.png) Habilidades

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical.
    
    * * *

    ## ![pdf](https://img.icons8.com/ios/25/000000/project-management.png) Projetos/Planos

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical.
    
    * * *

    ## ![pdf](https://img.icons8.com/glyph-neue/30/000000/university.png) Formação Acadêmica    

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical.
    
    * * *

    ## ![pdf](https://img.icons8.com/ios/25/000000/new-job.png) Profissional

    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical.
    
    * * *
    """