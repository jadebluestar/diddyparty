# Resume → Portfolio Converter

A full-stack web application that converts your résumé (PDF or DOCX) into a minimal, clean personal portfolio website.

## Features

- 📄 Upload PDF or DOCX résumé files
- 🔍 Automatic extraction of:
  - Name
  - Contact information (email, phone, LinkedIn, GitHub, website)
  - Skills
  - Work experience
  - Education
  - Projects
- 🎨 Generates a clean, minimal portfolio website
- 📦 Downloads as a ZIP file ready for hosting

## Tech Stack

### Frontend
- **React** - UI framework
- **Vite** - Build tool
- **TailwindCSS** - Styling

### Backend
- **FastAPI** - Python web framework
- **pdfplumber** - PDF parsing
- **python-docx** - DOCX parsing
- **Regex/Heuristics** - Data extraction

## Project Structure

```
diddy/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── resume_parser.py        # Resume parsing logic
│   ├── portfolio_generator.py # Portfolio HTML/CSS generator
│   └── requirements.txt        # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React component
│   │   ├── main.jsx           # React entry point
│   │   └── index.css          # Global styles
│   ├── index.html             # HTML template
│   ├── package.json           # Node dependencies
│   ├── vite.config.js         # Vite configuration
│   ├── tailwind.config.js     # TailwindCSS configuration
│   └── postcss.config.js      # PostCSS configuration
└── README.md                  # This file
```

## How to Run Locally

### Prerequisites

- **Python 3.8+**
- **Node.js 16+** and npm

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## How to Use

1. Open the frontend application in your browser (`http://localhost:5173`)
2. Click "Upload Resume" and select a PDF or DOCX file
3. Click "Generate Portfolio"
4. Wait for the processing to complete
5. Click "Download Portfolio" to get the ZIP file
6. Extract the ZIP file to get the `portfolio` folder

## How to Host the Generated Portfolio

After downloading and extracting the portfolio ZIP file, you have several options:

### GitHub Pages

1. Create a new repository on GitHub
2. Upload the contents of the `portfolio` folder to the repository
3. Go to Settings → Pages
4. Select the main branch and `/ (root)` folder
5. Your portfolio will be available at `https://yourusername.github.io/repository-name`

### Netlify

1. Go to [netlify.com](https://www.netlify.com) and sign up/login
2. Drag and drop the `portfolio` folder onto the Netlify dashboard
3. Your portfolio will be live immediately with a Netlify URL
4. You can customize the domain name in the site settings

### Vercel

1. Go to [vercel.com](https://vercel.com) and sign up/login
2. Click "Add New Project"
3. Import your Git repository or upload the `portfolio` folder
4. Deploy - your portfolio will be live with a Vercel URL

## Portfolio Template Features

The generated portfolio follows a clean, minimal design:

- **White background** with black text
- **Large name** displayed at the top
- **Two-column layout** for sections (responsive on mobile)
- **Thin, light dividers** between sections
- **Pure CSS** - no JavaScript required
- **Fully responsive** - works on all devices

## API Endpoints

### `POST /upload-resume`

Upload a résumé file and receive a portfolio ZIP file.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `file` (PDF or DOCX file)

**Response:**
- Content-Type: `application/zip`
- Body: ZIP file containing the portfolio

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/upload-resume" \
  -F "file=@your-resume.pdf"
```

## Development

### Backend Development

The backend uses FastAPI with automatic API documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Frontend Development

The frontend uses Vite with hot module replacement for fast development.

## Troubleshooting

### Backend Issues

- **Port already in use**: Change the port in the uvicorn command: `--port 8001`
- **Import errors**: Make sure you're in the virtual environment and all dependencies are installed
- **File parsing errors**: Ensure the uploaded file is a valid PDF or DOCX

### Frontend Issues

- **CORS errors**: Make sure the backend is running and CORS is properly configured
- **Connection refused**: Verify the backend is running on port 8000
- **Build errors**: Run `npm install` again to ensure all dependencies are installed

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

