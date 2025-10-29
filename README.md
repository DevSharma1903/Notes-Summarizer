# AI Note Summarizer

A sleek, retro-styled web application that uses AI to generate intelligent summaries of long text documents. Built with Flask and powered by Google's PEGASUS transformer model for high-quality abstractive summarization.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Transformers](https://img.shields.io/badge/Transformers-4.35.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Abstractive Summarization**: Uses Google's PEGASUS-XSUM model for intelligent, human-like summaries
- **Retro Vim-Inspired UI**: Clean, dark-mode interface with custom cursor animations
- **Real-time Processing**: Instant summary generation with live word count tracking
- **Smart Text Handling**: Automatically handles text length validation and optimization
- **Statistics Display**: Shows original length, summary length, and reduction percentage


## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**

git clone https://github.com/DevSharma1903/Notes-Summarizer.git
cd Notes-Summarizer


2. **Create a virtual environment**

python -m venv venv


3. **Activate the virtual environment**
- Windows (Command Prompt):
  ```
  venv\Scripts\activate
  ```
- Windows (PowerShell):
  ```
  venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. **Install dependencies**
pip install -r requirements.txt


5. **Run the application**
python app.py


6. **Open your browser**

Navigate to `http://127.0.0.1:5000`

## 📦 Dependencies

flask==3.0.0
transformers==4.35.0
torch==2.1.0
gunicorn==21.2.0
sentencepiece==0.1.99
protobuf==4.25.0


## 💻 Tech Stack

- **Backend**: Flask (Python web framework)
- **ML Model**: Google PEGASUS-XSUM (Abstractive text summarization)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Render / Hugging Face Spaces compatible

## 🎯 How to Use

1. Enter or paste your text (minimum 50 words) into the input field
2. Click the `:summarize` button or press `Ctrl + Enter`
3. View your generated summary with statistics
4. Copy or use the summary as needed

**Note**: The first run will take 2-3 minutes as the PEGASUS model (~2GB) downloads automatically.

## 🗂️ Project Structure

Notes-Summarizer/
├── app.py # Flask application and API routes
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend interface
├── .gitignore # Git ignore rules
└── README.md # Project documentation



## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] PDF and DOCX file upload support
- [ ] Multiple summarization models (T5, BART)
- [ ] Summary length control slider
- [ ] Export summaries as PDF/TXT
- [ ] User authentication and history
- [ ] Batch processing for multiple documents
- [ ] API endpoint for programmatic access

## 🐛 Known Issues

- First-time model loading takes 2-3 minutes
- Free tier hosting may have cold start delays
- Input limited to 500 words for performance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dev Sharma**
- GitHub: [@DevSharma1903](https://github.com/DevSharma1903)

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/) for the PEGASUS model
- [Google Research](https://github.com/google-research/pegasus) for PEGASUS architecture
- Inspired by Vim text editor aesthetics

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

⭐ **If you find this project useful, please consider giving it a star!** ⭐
