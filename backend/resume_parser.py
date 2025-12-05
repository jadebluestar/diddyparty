"""
Resume parsing module for extracting structured data from PDF and DOCX files.
"""
import re
import io
import pdfplumber
from docx import Document
from typing import Dict, List, Optional


class ResumeParser:
    """Parse resume files and extract structured information."""
    
    def __init__(self):
        self.name_patterns = [
            r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)',  # First Last or First Middle Last
        ]
        
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.phone_pattern = r'(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        self.url_pattern = r'https?://[^\s]+|www\.[^\s]+|linkedin\.com/[^\s]+|github\.com/[^\s]+'
        
    def parse(self, file_content: bytes, file_type: str) -> Dict:
        """
        Parse resume file and extract structured data.
        
        Args:
            file_content: Raw file bytes
            file_type: 'pdf' or 'docx'
            
        Returns:
            Dictionary with extracted resume data
        """
        text = self._extract_text(file_content, file_type)
        return self._extract_data(text)
    
    def _extract_text(self, file_content: bytes, file_type: str) -> str:
        """Extract raw text from file."""
        if file_type == 'pdf':
            return self._extract_from_pdf(file_content)
        elif file_type == 'docx':
            return self._extract_from_docx(file_content)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
    
    def _extract_from_pdf(self, file_content: bytes) -> str:
        """Extract text from PDF using pdfplumber."""
        text_parts = []
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
        return '\n'.join(text_parts)
    
    def _extract_from_docx(self, file_content: bytes) -> str:
        """Extract text from DOCX using python-docx."""
        doc = Document(io.BytesIO(file_content))
        text_parts = []
        for paragraph in doc.paragraphs:
            text_parts.append(paragraph.text)
        return '\n'.join(text_parts)
    
    def _extract_data(self, text: str) -> Dict:
        """Extract structured data from resume text."""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        # Extract name (usually first line or first few lines)
        name = self._extract_name(lines)
        
        # Extract contact information
        contact = self._extract_contact(text)
        
        # Extract sections
        skills = self._extract_skills(text, lines)
        experience = self._extract_experience(text, lines)
        education = self._extract_education(text, lines)
        projects = self._extract_projects(text, lines)
        
        return {
            'name': name,
            'contact': contact,
            'skills': skills,
            'experience': experience,
            'education': education,
            'projects': projects
        }
    
    def _extract_name(self, lines: List[str]) -> str:
        """Extract name from resume (usually at the top)."""
        # Check first 3 lines for name pattern
        for i, line in enumerate(lines[:3]):
            # Name is usually 2-4 words, all capitalized or title case
            if re.match(r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}$', line):
                return line
            # Also check for all caps
            if re.match(r'^[A-Z\s]{5,30}$', line) and len(line.split()) <= 4:
                return line.title()
        
        # Fallback: return first line if it looks like a name
        if lines:
            first_line = lines[0]
            if len(first_line.split()) <= 4 and not any(char.isdigit() for char in first_line):
                return first_line
        return "Your Name"
    
    def _extract_contact(self, text: str) -> Dict[str, str]:
        """Extract contact information (email, phone, URLs)."""
        contact = {}
        
        # Extract email
        emails = re.findall(self.email_pattern, text)
        if emails:
            contact['email'] = emails[0]
        
        # Extract phone
        phones = re.findall(self.phone_pattern, text)
        if phones:
            # Clean up phone number
            phone = re.sub(r'[^\d+]', '', phones[0])
            if len(phone) == 10:
                phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
            contact['phone'] = phone
        
        # Extract URLs (LinkedIn, GitHub, personal website)
        urls = re.findall(self.url_pattern, text)
        for url in urls[:3]:  # Limit to first 3 URLs
            if 'linkedin' in url.lower():
                contact['linkedin'] = url if url.startswith('http') else f'https://{url}'
            elif 'github' in url.lower():
                contact['github'] = url if url.startswith('http') else f'https://{url}'
            elif not any(key in contact for key in ['linkedin', 'github']):
                contact['website'] = url if url.startswith('http') else f'https://{url}'
        
        return contact
    
    def _extract_skills(self, text: str, lines: List[str]) -> List[str]:
        """Extract skills section."""
        skills = []
        
        # Look for skills section
        skills_section = self._find_section(text, ['skills', 'technical skills', 'core competencies', 'competencies'])
        
        if skills_section:
            # Extract skills (usually comma-separated or bullet points)
            skill_lines = skills_section.split('\n')
            for line in skill_lines:
                # Remove bullets and clean
                line = re.sub(r'^[•\-\*]\s*', '', line.strip())
                if line:
                    # Split by comma, semicolon, or pipe
                    items = re.split(r'[,;|]', line)
                    for item in items:
                        skill = item.strip()
                        if skill and len(skill) > 1:
                            skills.append(skill)
        
        # If no skills section found, look for common tech keywords
        if not skills:
            tech_keywords = [
                'python', 'javascript', 'java', 'react', 'node', 'sql', 'html', 'css',
                'aws', 'docker', 'kubernetes', 'git', 'linux', 'mongodb', 'postgresql',
                'django', 'flask', 'fastapi', 'vue', 'angular', 'typescript', 'c++', 'c#',
                'machine learning', 'ai', 'data science', 'agile', 'scrum'
            ]
            text_lower = text.lower()
            for keyword in tech_keywords:
                if keyword in text_lower and keyword.title() not in skills:
                    skills.append(keyword.title())
        
        return skills[:20]  # Limit to 20 skills
    
    def _extract_experience(self, text: str, lines: List[str]) -> List[Dict]:
        """Extract work experience."""
        experience = []
        
        # Find experience section
        exp_section = self._find_section(text, [
            'experience', 'work experience', 'employment', 'professional experience',
            'career', 'employment history'
        ])
        
        if exp_section:
            # Split by common date patterns or job title patterns
            entries = self._split_into_entries(exp_section)
            
            for entry in entries[:5]:  # Limit to 5 most recent
                exp_item = self._parse_experience_entry(entry)
                if exp_item:
                    experience.append(exp_item)
        
        return experience
    
    def _extract_education(self, text: str, lines: List[str]) -> List[Dict]:
        """Extract education section."""
        education = []
        
        # Find education section
        edu_section = self._find_section(text, [
            'education', 'academic', 'qualifications', 'degrees'
        ])
        
        if edu_section:
            entries = self._split_into_entries(edu_section)
            
            for entry in entries[:3]:  # Limit to 3 entries
                edu_item = self._parse_education_entry(entry)
                if edu_item:
                    education.append(edu_item)
        
        return education
    
    def _extract_projects(self, text: str, lines: List[str]) -> List[Dict]:
        """Extract projects section."""
        projects = []
        
        # Find projects section
        proj_section = self._find_section(text, [
            'projects', 'project', 'portfolio', 'personal projects'
        ])
        
        if proj_section:
            entries = self._split_into_entries(proj_section)
            
            for entry in entries[:5]:  # Limit to 5 projects
                proj_item = self._parse_project_entry(entry)
                if proj_item:
                    projects.append(proj_item)
        
        return projects
    
    def _find_section(self, text: str, section_names: List[str]) -> Optional[str]:
        """Find a section by name."""
        text_lower = text.lower()
        
        for section_name in section_names:
            # Look for section header (usually all caps or title case)
            pattern = rf'(?i)(?:^|\n)\s*{re.escape(section_name)}\s*(?:\n|:|\|)'
            match = re.search(pattern, text)
            
            if match:
                start = match.end()
                # Find next major section (all caps line or new section header)
                next_section = re.search(r'\n\s*[A-Z][A-Z\s]{5,}\s*\n', text[start:])
                if next_section:
                    return text[start:start + next_section.start()].strip()
                else:
                    return text[start:start + 2000].strip()  # Limit section size
        
        return None
    
    def _split_into_entries(self, section: str) -> List[str]:
        """Split section into individual entries."""
        # Split by double newlines or lines that look like headers
        entries = re.split(r'\n\s*\n', section)
        
        # Also try splitting by date patterns or bullet points
        if len(entries) == 1:
            # Look for date patterns (YYYY, MM/YYYY, etc.)
            date_pattern = r'\d{4}|\d{1,2}/\d{4}|\d{1,2}-\d{4}'
            splits = re.split(rf'\n(?=.*{date_pattern})', section)
            if len(splits) > 1:
                entries = splits
        
        return [e.strip() for e in entries if e.strip()]
    
    def _parse_experience_entry(self, entry: str) -> Optional[Dict]:
        """Parse a single experience entry."""
        lines = [l.strip() for l in entry.split('\n') if l.strip()]
        if not lines:
            return None
        
        # First line usually contains job title and company
        first_line = lines[0]
        
        # Look for date range
        date_pattern = r'(\d{1,2}[/-])?\d{4}\s*[-–—]\s*(\d{1,2}[/-])?\d{4}|present|current'
        dates = re.findall(date_pattern, entry, re.IGNORECASE)
        
        # Extract job title and company
        title = first_line
        company = ""
        
        # Try to separate title and company (often separated by |, -, or at)
        if '|' in first_line:
            parts = first_line.split('|')
            title = parts[0].strip()
            company = parts[1].strip() if len(parts) > 1 else ""
        elif ' at ' in first_line.lower():
            parts = re.split(r'\s+at\s+', first_line, flags=re.IGNORECASE)
            title = parts[0].strip()
            company = parts[1].strip() if len(parts) > 1 else ""
        elif len(lines) > 1:
            # Second line might be company
            company = lines[1]
        
        # Extract description (remaining lines)
        description = []
        start_idx = 2 if len(lines) > 1 and company else 1
        for line in lines[start_idx:]:
            # Remove bullets
            line = re.sub(r'^[•\-\*]\s*', '', line)
            if line and len(line) > 10:  # Filter out very short lines
                description.append(line)
        
        return {
            'title': title,
            'company': company,
            'dates': dates[0] if dates else "",
            'description': description
        }
    
    def _parse_education_entry(self, entry: str) -> Optional[Dict]:
        """Parse a single education entry."""
        lines = [l.strip() for l in entry.split('\n') if l.strip()]
        if not lines:
            return None
        
        degree = lines[0]
        school = lines[1] if len(lines) > 1 else ""
        
        # Look for graduation year
        year_match = re.search(r'\b(19|20)\d{2}\b', entry)
        year = year_match.group() if year_match else ""
        
        return {
            'degree': degree,
            'school': school,
            'year': year
        }
    
    def _parse_project_entry(self, entry: str) -> Optional[Dict]:
        """Parse a single project entry."""
        lines = [l.strip() for l in entry.split('\n') if l.strip()]
        if not lines:
            return None
        
        name = lines[0]
        description = []
        
        for line in lines[1:]:
            line = re.sub(r'^[•\-\*]\s*', '', line)
            if line and len(line) > 10:
                description.append(line)
        
        return {
            'name': name,
            'description': description
        }

