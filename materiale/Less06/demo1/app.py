import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

df = pd.DataFrame(np.random.randint(0,40000,size=(1500, 4)), columns=list('ABCD'))
image = Image.open('dog.jpg')


def main():
    st.title('La mia prima esercitazione')
    st.write("buongiorno a tutti")
    st.dataframe(df)
    st.image(image,use_column_width=True)

    ##################################
    add_selectbox = st.sidebar.selectbox(
        'Come vuoi essere contattato?',
        ('Email', 'Telefono Fisso', 'Cell'))
    st.write(add_selectbox)

    add_slider1 = st.slider(
        'Selezionare il range',
        0.0, 100.0, 25.0)
    st.write(add_slider1)

    add_slider2 = st.slider(
        'Selezionare il range',
        0.0, 100.0, (25.0, 75.0))
    st.write(add_slider2)



    # Add a selectbox to the sidebar:
    # Add a slider to the sidebar:
    ####################
    if st.button('Conferma'):
        st.write('Confermato!!')
    else:
        st.write('Arrivederci')
    
############################################

    genre = st.radio(
     "Seleziona il tuo genere preferito",
     ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('Hai selezionato Comedy') 
    else:
        st.write("la tua selezione non è Comedy")
        

###############################################
    first = st.checkbox('First checkbox')
    if first:
        st.write('First is checked')

    second = st.checkbox('Second checkbox')
    if second:
        st.write('Second is checked')

    third = st.checkbox('Third checkbox')
    if third:
        st.write('Third is checked')



if __name__=='__main__':
    main()