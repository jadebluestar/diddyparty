"""
FastAPI backend for Resume to Portfolio Converter
"""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io
import zipfile
from resume_parser import ResumeParser
from portfolio_generator import PortfolioGenerator

app = FastAPI(title="Resume to Portfolio Converter API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"message": "Resume to Portfolio Converter API is running"}


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    """
    Accept a resume file (PDF or DOCX), parse it, and generate a portfolio ZIP.
    
    Returns:
        StreamingResponse: ZIP file containing the generated portfolio
    """
    # Validate file type
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    file_ext = file.filename.split('.')[-1].lower()
    if file_ext not in ['pdf', 'docx']:
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Please upload a PDF or DOCX file."
        )
    
    try:
        # Read file content
        contents = await file.read()
        
        # Parse resume
        parser = ResumeParser()
        resume_data = parser.parse(contents, file_ext)
        
        # Generate portfolio
        generator = PortfolioGenerator()
        portfolio_files = generator.generate(resume_data)
        
        # Create ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Add index.html
            zip_file.writestr('portfolio/index.html', portfolio_files['html'])
            
            # Add styles.css
            zip_file.writestr('portfolio/styles.css', portfolio_files['css'])
            
            # Add any assets if needed
            if 'assets' in portfolio_files:
                for asset_name, asset_content in portfolio_files['assets'].items():
                    zip_file.writestr(f'portfolio/assets/{asset_name}', asset_content)
        
        zip_buffer.seek(0)
        
        # Return ZIP file as streaming response
        return StreamingResponse(
            io.BytesIO(zip_buffer.read()),
            media_type="application/zip",
            headers={
                "Content-Disposition": f"attachment; filename=portfolio.zip"
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")

