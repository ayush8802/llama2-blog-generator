# llama2-blog-generator


## Overview

`llama2-blog-generator` is a Streamlit application that harnesses the power of the LLaMA 2 language model to create personalized blog content. This tool is perfect for bloggers, marketers, and content creators looking to streamline their writing process and generate high-quality content tailored to their needs.

## Features

- **Customizable Blog Generation**: Input a blog topic, specify the word count, and select from various writing styles (researcher, data scientist, technical writer, storyteller, educator) and tones (formal, casual, informative).
- **Easy to Use**: A user-friendly interface built with Streamlit allows for a seamless content generation experience.
- **Downloadable Content**: Generate blogs and download them as text files for easy sharing and editing.

## Demo

![Screenshot of the App](https://github.com/ayush8802/llama2-blog-generator/blob/main/img_1)  <!-- Replace with actual screenshot URL -->

## Installation

### Prerequisites

- Python 3.x
- Streamlit
- LangChain
- CTransformers

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/llama2-blog-generator.git
   cd llama2-blog-generator

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   Download the LLaMA model: Place the llama-2-7b-chat.ggmlv3.q8_0.bin file inside the model directory.

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py


### Usage
1. Enter the blog topic in the input field.
2. Select the desired number of words.
3. Choose the blog style and tone.
4. Click on "Generate Blog" to create your content.
5. Download the generated blog as a text file.

### Contributions
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

### Acknowledgments
1. LLaMA 2 for providing the language model.
2. Streamlit for the fantastic framework.
3. LangChain for simplifying prompt management.
