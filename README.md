# Cold Email Generator

Cold Email Generator is a Streamlit application that reads a job posting URL, extracts job requirements using Groq and LangChain, matches the required skills against a local portfolio database, and generates a personalized cold outreach email.

## Features

- Accepts a job posting URL
- Scrapes and cleans job page text
- Extracts role, experience, skills, and description as structured JSON
- Stores portfolio projects in ChromaDB
- Matches job skills to relevant portfolio links
- Generates personalized cold emails using Groq
- Streamlit UI for quick demos

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq Llama model
- ChromaDB
- Pandas
- WebBaseLoader
- dotenv

## Project Structure

```text
cold-email-generator/
├── app/
│   ├── main.py                     # Streamlit app entry point
│   ├── email_chain.py              # Groq/LangChain extraction + email generation
│   ├── portfolio.py                # ChromaDB portfolio matching
│   ├── utils.py                    # Text cleaning utilities
│   ├── resource/
│   │   └── my_portfolio.csv        # Portfolio tech stack and links
│   └── vectorstore/                # ChromaDB persistent store
├── .gitignore
└── README.md
```

## How It Works

1. User enters a job posting URL in Streamlit.
2. `WebBaseLoader` loads the page content.
3. `clean_text()` removes HTML, URLs, symbols, and extra whitespace.
4. `Chain.extract_jobs()` asks Groq to return structured job JSON.
5. `Portfolio.load_portfolio()` loads portfolio rows into ChromaDB.
6. `Portfolio.query_links()` finds relevant portfolio links for job skills.
7. `Chain.write_mail()` generates a personalized cold email.
8. Streamlit displays the generated email.

## Setup

```bash
cd app
python -m venv .venv
.venv\Scripts\activate
pip install streamlit langchain langchain-community langchain-groq chromadb pandas python-dotenv beautifulsoup4
```

## Environment Variables

Create `app/.env`:

```text
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` to GitHub.

## Live Server

Start the local Streamlit live server from the `app` folder:

```bash
.venv\Scripts\activate
streamlit run main.py --server.port 8501
```

Then open:

```text
http://localhost:8501
```

The app page can load without `GROQ_API_KEY`, but email generation requires the key. If the key is missing, add it to `app/.env` and restart the server.

## Deploy

This app is ready for Streamlit Community Cloud deployment.

1. Push this repository to GitHub.
2. Open `https://share.streamlit.io`.
3. Create a new app from this repository.
4. Set the entrypoint file to:

```text
app/main.py
```

5. Add this secret in the app settings:

```text
GROQ_API_KEY="your_groq_api_key"
```

6. Deploy the app. Streamlit will install dependencies from `requirements.txt`.

## Run

```bash
cd app
streamlit run main.py
```

## Portfolio Data

Portfolio links are stored in:

```text
app/resource/my_portfolio.csv
```

Each row contains:

- `Techstack`
- `Links`

Update this file with real project links to improve email personalization.

## Main Files

- `app/main.py` - Streamlit UI and orchestration
- `app/email_chain.py` - job extraction and cold email generation
- `app/portfolio.py` - ChromaDB portfolio retrieval
- `app/utils.py` - page text cleaning

## Example Workflow

1. Open the app.
2. Paste a job posting URL.
3. Click `Submit`.
4. Review the generated cold email with relevant portfolio links.

## Notes

This project is designed for portfolio/demo use. Generated emails should be reviewed before sending.
