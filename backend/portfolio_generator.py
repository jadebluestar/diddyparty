"""
Portfolio HTML/CSS generator module.
Creates a clean, minimal portfolio website from parsed resume data.
"""
from typing import Dict, List


class PortfolioGenerator:
    """Generate portfolio HTML and CSS from resume data."""
    
    def generate(self, resume_data: Dict) -> Dict[str, str]:
        """
        Generate portfolio files (HTML and CSS).
        
        Args:
            resume_data: Dictionary containing parsed resume information
            
        Returns:
            Dictionary with 'html', 'css', and optionally 'assets' keys
        """
        html = self._generate_html(resume_data)
        css = self._generate_css()
        
        return {
            'html': html,
            'css': css
        }
    
    def _generate_html(self, data: Dict) -> str:
        """Generate HTML content."""
        name = data.get('name', 'Your Name')
        contact = data.get('contact', {})
        skills = data.get('skills', [])
        experience = data.get('experience', [])
        education = data.get('education', [])
        projects = data.get('projects', [])
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1 class="name">{self._escape_html(name)}</h1>
            <div class="contact">
{self._generate_contact_html(contact)}
            </div>
        </header>
        
        <main>
{self._generate_skills_section(skills)}
{self._generate_experience_section(experience)}
{self._generate_education_section(education)}
{self._generate_projects_section(projects)}
        </main>
    </div>
</body>
</html>"""
        return html
    
    def _generate_contact_html(self, contact: Dict) -> str:
        """Generate contact information HTML."""
        contact_items = []
        
        if contact.get('email'):
            contact_items.append(f'                <a href="mailto:{contact["email"]}">{contact["email"]}</a>')
        
        if contact.get('phone'):
            contact_items.append(f'                <span>{contact["phone"]}</span>')
        
        if contact.get('linkedin'):
            contact_items.append(f'                <a href="{contact["linkedin"]}" target="_blank">LinkedIn</a>')
        
        if contact.get('github'):
            contact_items.append(f'                <a href="{contact["github"]}" target="_blank">GitHub</a>')
        
        if contact.get('website'):
            contact_items.append(f'                <a href="{contact["website"]}" target="_blank">Website</a>')
        
        if not contact_items:
            return '                <span>Contact information</span>'
        
        return '\n'.join(contact_items)
    
    def _generate_skills_section(self, skills: List[str]) -> str:
        """Generate skills section HTML."""
        if not skills:
            return ''
        
        skills_html = '            <section class="section">\n'
        skills_html += '                <h2>Skills</h2>\n'
        skills_html += '                <div class="skills-grid">\n'
        
        for skill in skills:
            skills_html += f'                    <span class="skill-tag">{self._escape_html(skill)}</span>\n'
        
        skills_html += '                </div>\n'
        skills_html += '            </section>\n'
        
        return skills_html
    
    def _generate_experience_section(self, experience: List[Dict]) -> str:
        """Generate experience section HTML."""
        if not experience:
            return ''
        
        exp_html = '            <section class="section">\n'
        exp_html += '                <h2>Experience</h2>\n'
        
        for exp in experience:
            exp_html += '                <div class="entry">\n'
            exp_html += f'                    <h3>{self._escape_html(exp.get("title", ""))}</h3>\n'
            
            if exp.get('company'):
                exp_html += f'                    <p class="meta">{self._escape_html(exp["company"])}'
                if exp.get('dates'):
                    exp_html += f' <span class="dates">• {self._escape_html(exp["dates"])}</span>'
                exp_html += '</p>\n'
            
            if exp.get('description'):
                exp_html += '                    <ul class="description">\n'
                for desc in exp['description']:
                    exp_html += f'                        <li>{self._escape_html(desc)}</li>\n'
                exp_html += '                    </ul>\n'
            
            exp_html += '                </div>\n'
        
        exp_html += '            </section>\n'
        
        return exp_html
    
    def _generate_education_section(self, education: List[Dict]) -> str:
        """Generate education section HTML."""
        if not education:
            return ''
        
        edu_html = '            <section class="section">\n'
        edu_html += '                <h2>Education</h2>\n'
        
        for edu in education:
            edu_html += '                <div class="entry">\n'
            edu_html += f'                    <h3>{self._escape_html(edu.get("degree", ""))}</h3>\n'
            
            if edu.get('school'):
                edu_html += f'                    <p class="meta">{self._escape_html(edu["school"])}'
                if edu.get('year'):
                    edu_html += f' <span class="dates">• {self._escape_html(edu["year"])}</span>'
                edu_html += '</p>\n'
            
            edu_html += '                </div>\n'
        
        edu_html += '            </section>\n'
        
        return edu_html
    
    def _generate_projects_section(self, projects: List[Dict]) -> str:
        """Generate projects section HTML."""
        if not projects:
            return ''
        
        proj_html = '            <section class="section">\n'
        proj_html += '                <h2>Projects</h2>\n'
        
        for proj in projects:
            proj_html += '                <div class="entry">\n'
            proj_html += f'                    <h3>{self._escape_html(proj.get("name", ""))}</h3>\n'
            
            if proj.get('description'):
                proj_html += '                    <ul class="description">\n'
                for desc in proj['description']:
                    proj_html += f'                        <li>{self._escape_html(desc)}</li>\n'
                proj_html += '                    </ul>\n'
            
            proj_html += '                </div>\n'
        
        proj_html += '            </section>\n'
        
        return proj_html
    
    def _generate_css(self) -> str:
        """Generate CSS styles."""
        return """/* Portfolio Styles - Clean and Minimal */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #000;
    background-color: #fff;
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
}

header {
    text-align: center;
    margin-bottom: 60px;
    padding-bottom: 30px;
    border-bottom: 1px solid #e0e0e0;
}

.name {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 20px;
    letter-spacing: -0.02em;
}

.contact {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    font-size: 0.95rem;
}

.contact a {
    color: #000;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s;
}

.contact a:hover {
    border-bottom-color: #000;
}

.contact span {
    color: #666;
}

main {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
}

.section {
    margin-bottom: 40px;
}

.section h2 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.skills-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.skill-tag {
    display: inline-block;
    padding: 5px 12px;
    background-color: #f5f5f5;
    border: 1px solid #e0e0e0;
    border-radius: 3px;
    font-size: 0.85rem;
}

.entry {
    margin-bottom: 30px;
}

.entry h3 {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 5px;
}

.entry .meta {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 10px;
}

.entry .dates {
    color: #999;
}

.entry .description {
    list-style: none;
    padding-left: 0;
}

.entry .description li {
    position: relative;
    padding-left: 15px;
    margin-bottom: 8px;
    font-size: 0.9rem;
    line-height: 1.5;
}

.entry .description li:before {
    content: '•';
    position: absolute;
    left: 0;
    color: #999;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 30px 15px;
    }
    
    .name {
        font-size: 2rem;
    }
    
    main {
        grid-template-columns: 1fr;
        gap: 30px;
    }
    
    .contact {
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    
    .section {
        margin-bottom: 30px;
    }
}

@media (max-width: 480px) {
    .name {
        font-size: 1.75rem;
    }
    
    .section h2 {
        font-size: 0.85rem;
    }
    
    .entry h3 {
        font-size: 1rem;
    }
}
"""
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters."""
        if not text:
            return ''
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

