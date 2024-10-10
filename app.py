import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers  # Updated import


## function to get response from LLama 2 model
def getresponse(input_text, no_words, blog_style, tone):
    # call llama model
    llm = CTransformers(model=r".\model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        # Use raw string to fix the escape sequence issue
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.5})

    ## prompt template
    template = """write a {tone} blog for the topic {input_text} where the number of words are {no_words} and the style of 
    blog is {blog_style}"""

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words", "tone"], template=template)

    ## generate the response using the invoke method instead of deprecated __call__
    response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words, tone=tone))

    return response


st.set_page_config(page_title="Blog Generation", layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs with LLaMA")

input_text = st.text_input("Enter the blog topic", placeholder="e.g., The future of AI")
no_words = st.number_input("Number of words", min_value=100, max_value=2000, step=100)

col1, col2 = st.columns([5, 5])

with col1:
    blog_style = st.selectbox("Blog Style",
                              ("researcher", "datascientist", "technical writer", "storyteller", "educator"), index=0)
with col2:
    tone = st.selectbox("Tone", ("formal", "casual", "informative"), index=0)

submit = st.button("Generate Blog")

if submit:
    if input_text and no_words:
        with st.spinner('Generating your blog...'):
            try:
                blog = getresponse(input_text, no_words, blog_style, tone)
                st.success("Blog generated successfully!")
                st.write(blog)

                # Add download option
                st.download_button("Download as Text", blog, file_name=f"blog_{input_text}.txt")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in all fields.")
