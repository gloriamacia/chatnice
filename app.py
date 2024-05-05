# https://chatnice-e080a5e359b1.herokuapp.com/
# https://chatnice.uk/
import streamlit as st
import os

def main():
    # Set the app layout 
    st.set_page_config(page_title="ChatNICE", page_icon="assets/favicon.png")
    # Set the layout to have two columns
    col1, col2 = st.columns(2)

    # Left column: Title and text
    with col1:
        st.title("Ask ChatNICE")
        text = """An artificial intelligence chatbot trained on guidances from NICE. It is based on a large language model like gpt-4. 
        ChatNICE is a proof of concept for research purposes only. This webite is not affiliated with nice.org.uk
        The user assumes full liability for any other use. This preview is trained on the 'Caesarean birth' guidance (NG192). 
        Contact Gloria Macia at g.macia-munoz@lse.ac.uk for further inquiries"""
        # You can add more text or other elements as needed.
        st.markdown(text)

    # Right column: Image
    with col2:
        # Add an image to the right column
        image_path = os.path.join('assets', 'chat.png')
        st.image(image_path, use_column_width=True)
    
    # Embed the chat bubble code
    st.components.v1.iframe("https://www.chatbase.co/chatbot-iframe/DcpTIYic0VkmgY2JyNd4Z", height=500)

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
