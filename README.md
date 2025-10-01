# AskQL: Intelligent Database Assistant

AskQL is a powerful tool that allows users to query databases using natural language. Built with LangChain and Gemini AI, it translates plain English questions into SQL queries and provides human-readable answers.

##  Features

- Natural language to SQL query conversion
- Support for multiple database types (MySQL, SQLite, PostgreSQL)
- Interactive web interface using Streamlit
- Few-shot learning for better query understanding
- Error handling and graceful fallbacks
- Semantic similarity for query examples

##  Requirements

- Python 3.8+
- Google Gemini API key
- Database connection URL

##  Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AskQL.git
cd AskQL
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🔧 Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Enter your database connection URL in the format:
```
mysql://user:password@host:port/database
sqlite:///path/to/database.db
postgresql://user:password@host:port/database
```

3. Ask your question in plain English, for example:
- "How many items are left for Nike in XS size and white color?"
- "What is the total value of all small-sized items?"
- "Calculate the revenue for Levi's items with discounts applied"

## 🏗️ Project Structure

```
AskQL/
├── main.py           # Streamlit web interface
├── askql.py         # Core query processing logic
├── .env             # Environment variables
└── README.md        # Documentation
```

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Limitations

- Requires proper database schema information
- Query complexity is limited by the model's capabilities
- Performance depends on database size and connection speed

## 🔗 Links

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Gemini AI Platform](https://cloud.google.com/vertex-ai)
- [Streamlit Documentation](https://docs.streamlit.io)