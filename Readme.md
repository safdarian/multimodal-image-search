# Multimodal Image Search

**Multimodal Image Search** is a web-based application that allows users to search for images using text queries. The project leverages advanced AI models such as CLIP and Sentence Transformers to provide highly relevant image search results.

---

## Features

- **Text-to-Image Search**: Search for images based on text descriptions.
- **Image Uploads**: Add new images to the searchable database.
- **Efficient Image Retrieval**: Uses vector embeddings for fast and accurate search results.
- **Interactive Web Interface**: User-friendly web interface built with FastAPI and Jinja2 templates.

---

## How It Works

1. **Database Management**: Images are stored and managed using LanceDB, optimized for handling large-scale vector embeddings.
2. **Embeddings Extraction**:
   - **Image Embeddings**: Generated using OpenAI's CLIP model.
   - **Text Embeddings**: Generated using a pre-trained Sentence Transformer model.
3. **Search Functionality**: Vector similarity search retrieves the most relevant images based on a given text query.

---

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- CUDA-enabled GPU (optional, for faster performance)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/safdarian/multimodal-image-search.git
   cd multimodal-image-search
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create necessary directories:
   ```bash
   mkdir images static templates
   ```

---

## Usage

1. **Start the Application**:
   Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The server will start at `http://127.0.0.1:8000`.

2. **Upload Images**:
   Use the web interface or API endpoint `/upload/` to upload new images.

3. **Search Images**:
   Enter a text query in the search bar on the homepage or use the API endpoint `/search/`.

---

## File Structure

- **`main.py`**: Contains the FastAPI server logic and routes.
- **`lanceDB_manager.py`**: Handles database connections, schema creation, and search functionalities using LanceDB.
- **`requirements.txt`**: Lists all dependencies required for the project.

---

## Technologies Used

- **Language**: Python
- **Framework**: FastAPI
- **Database**: LanceDB
- **AI Models**:
  - OpenAI CLIP (image embeddings)
  - Sentence Transformers (text embeddings)
- **Other Libraries**: PyTorch, Pandas, Jinja2, Uvicorn

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- OpenAI for the CLIP model.
- HuggingFace for the Sentence Transformers.
- LanceDB for efficient vector storage and retrieval.