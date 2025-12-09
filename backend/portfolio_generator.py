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
        
        # A stunning, professional portfolio with advanced animations and effects
        html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
  <title>{self._escape_html(name)} — Portfolio</title>
  <link rel=\"stylesheet\" href=\"styles.css\">
</head>
<body>
  <div class=\"stars\"></div>
  <div class=\"glow-orb glow-1\"></div>
  <div class=\"glow-orb glow-2\"></div>
  <div class=\"glow-orb glow-3\"></div>

  <nav class=\"navbar\">
    <div class=\"nav-container\">
      <a href=\"#\" class=\"nav-brand\">
        <span class=\"brand-icon\">✨</span>
        {self._escape_html(name)}
      </a>
      <ul class=\"nav-links\">
        <li><a href=\"#about\"><span class=\"nav-indicator\"></span>About</a></li>
        <li><a href=\"#projects\"><span class=\"nav-indicator\"></span>Projects</a></li>
        <li><a href=\"#experience\"><span class=\"nav-indicator\"></span>Experience</a></li>
        <li><a href=\"#contact\"><span class=\"nav-indicator\"></span>Contact</a></li>
      </ul>
    </div>
  </nav>

  <header class=\"hero\">
    <div class=\"hero-bg\">
      <div class=\"blob blob-1\"></div>
      <div class=\"blob blob-2\"></div>
      <div class=\"blob blob-3\"></div>
    </div>
    <div class=\"hero-content\">
      <div class=\"hero-badge\">Welcome to my portfolio</div>
      <h1 class=\"hero-title\">{self._escape_html(name)}</h1>
      <p class=\"hero-subtitle\">{self._escape_html(data.get('title', 'Developer & Designer'))}</p>
      <p class=\"hero-description\">Crafting beautiful digital experiences with modern code and design</p>
      <div class=\"hero-buttons\">
        <a href=\"#projects\" class=\"btn btn-primary\">
          <span>View My Work</span>
          <span class=\"btn-icon\">→</span>
        </a>
        <a href=\"#contact\" class=\"btn btn-secondary\">
          <span>Get In Touch</span>
          <span class=\"btn-icon\">💬</span>
        </a>
      </div>
    </div>
    <div class=\"hero-gradient\"></div>
  </header>

  <main>
    <section id=\"about\" class=\"section about-section\">
      <div class=\"section-bg\"></div>
      <div class=\"container\">
        <h2 class=\"section-title\"><span class=\"title-number\">01</span>About</h2>
        <div class=\"about-content\">
          <p>Welcome to my portfolio. I'm passionate about creating exceptional web experiences through thoughtful design and clean code.</p>
        </div>
      </div>
    </section>

    <section id=\"projects\" class=\"section projects-section\">
      <div class=\"container\">
        <h2 class=\"section-title\"><span class=\"title-number\">02</span>Featured Projects</h2>
{self._generate_projects_section(projects)}
      </div>
    </section>

    <section id=\"experience\" class=\"section experience-section\">
      <div class=\"container\">
        <div class=\"two-col\">
          <div>
            <h2 class=\"section-title\"><span class=\"title-number\">03</span>Experience</h2>
{self._generate_experience_section(experience)}
          </div>
          <div>
            <h2 class=\"section-title\"><span class=\"title-number\">04</span>Education</h2>
{self._generate_education_section(education)}
          </div>
        </div>
      </div>
    </section>

    <section class=\"section skills-section\">
      <div class=\"section-bg\"></div>
      <div class=\"container\">
        <h2 class=\"section-title\"><span class=\"title-number\">05</span>Skills & Expertise</h2>
{self._generate_skills_section(skills)}
      </div>
    </section>

    <section id=\"contact\" class=\"section contact-section\">
      <div class=\"contact-bg\">
        <div class=\"contact-blob\"></div>
      </div>
      <div class=\"container\">
        <h2 class=\"section-title\"><span class=\"title-number\">06</span>Let's Connect</h2>
        <div class=\"contact-content\">
          <p class=\"contact-text\">I'd love to hear from you. Reach out through any of these channels:</p>
          <div class=\"contact-links\">
{self._generate_contact_html(contact)}
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class=\"footer\">
    <div class=\"container\">
      <p>&copy; 2024 {self._escape_html(name)}. All rights reserved.</p>
      <div class=\"footer-glow\"></div>
    </div>
  </footer>

  <script>
    // Smooth scroll with active nav highlighting
    const navLinks = document.querySelectorAll('.nav-links a');
    window.addEventListener('scroll', () => {{
      let current = '';
      document.querySelectorAll('section').forEach(section => {{
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) current = section.getAttribute('id');
      }});
      navLinks.forEach(link => {{
        link.style.color = '#333';
        if (link.getAttribute('href').slice(1) === current) {{
          link.style.color = '#0B66FF';
        }}
      }});
    }});
  </script>
</body>
</html>"""
        return html
    
    def _generate_contact_html(self, contact: Dict) -> str:
        """Generate contact information HTML."""
        contact_items = []
        
        if contact.get('email'):
            contact_items.append(f'            <a href="mailto:{contact["email"]}" class="contact-link\"><i>✉</i> {contact["email"]}</a>')
        
        if contact.get('phone'):
            contact_items.append(f'            <a class="contact-link\"><i>📞</i> {contact["phone"]}</a>')
        
        if contact.get('linkedin'):
            contact_items.append(f'            <a href="{contact["linkedin"]}" target="_blank" class="contact-link\"><i>in</i> LinkedIn</a>')
        
        if contact.get('github'):
            contact_items.append(f'            <a href="{contact["github"]}" target="_blank" class="contact-link\"><i>⚡</i> GitHub</a>')
        
        if contact.get('website'):
            contact_items.append(f'            <a href="{contact["website"]}" target="_blank" class="contact-link\"><i>🌐</i> Website</a>')
        
        if not contact_items:
            return '            <p>Contact information</p>'
        
        return '\n'.join(contact_items)
    
    def _generate_skills_section(self, skills: List[str]) -> str:
        """Generate skills section HTML."""
        if not skills:
            return ''
        skills_html = '        <div class="skills-grid">\n'

        for skill in skills:
            skills_html += f'          <div class="skill-item">{self._escape_html(skill)}</div>\n'

        skills_html += '        </div>\n'
        
        return skills_html
    
    def _generate_experience_section(self, experience: List[Dict]) -> str:
        """Generate experience section HTML."""
        if not experience:
            return ''
        exp_html = ''
        
        for exp in experience:
            exp_html += '        <div class="timeline-item">\n'
            exp_html += f'          <h3 class="timeline-title">{self._escape_html(exp.get("title", ""))}</h3>\n'
            
            if exp.get('company'):
                exp_html += f'          <p class="timeline-meta">{self._escape_html(exp["company"])}'
                if exp.get('dates'):
                    exp_html += f' • {self._escape_html(exp["dates"])}'
                exp_html += '</p>\n'
            
            if exp.get('description'):
                exp_html += '          <ul class="timeline-desc">\n'
                for desc in exp['description']:
                    exp_html += f'            <li>{self._escape_html(desc)}</li>\n'
                exp_html += '          </ul>\n'
            
            exp_html += '        </div>\n'
        
        return exp_html
    
    def _generate_education_section(self, education: List[Dict]) -> str:
        """Generate education section HTML."""
        if not education:
            return ''
        
        edu_html = ''
        
        for edu in education:
            edu_html += '        <div class="timeline-item">\n'
            edu_html += f'          <h3 class="timeline-title">{self._escape_html(edu.get("degree", ""))}</h3>\n'
            
            if edu.get('school'):
                edu_html += f'          <p class="timeline-meta">{self._escape_html(edu["school"])}'
                if edu.get('year'):
                    edu_html += f' • {self._escape_html(edu["year"])}'
                edu_html += '</p>\n'
            
            edu_html += '        </div>\n'
        
        return edu_html
    
    def _generate_projects_section(self, projects: List[Dict]) -> str:
        """Generate projects section HTML."""
        if not projects:
            return '        <p class="no-content">No projects to display yet.</p>\n'
        
        proj_html = '        <div class="projects-grid">\n'
        
        for proj in projects:
            proj_html += '          <div class="project-card">\n'
            proj_html += f'            <h3 class="project-title">{self._escape_html(proj.get("name", ""))}</h3>\n'
            
            if proj.get('description'):
                proj_html += '            <ul class="project-desc">\n'
                for desc in proj['description']:
                    proj_html += f'              <li>{self._escape_html(desc)}</li>\n'
                proj_html += '            </ul>\n'
            
            proj_html += '          </div>\n'
        
        proj_html += '        </div>\n'
        
        return proj_html
    
    def _generate_css(self) -> str:
        """Generate CSS styles."""
        return """/* Premium Fancy Portfolio with Advanced Effects */

:root {
  --primary: #0B66FF;
  --primary-dark: #0854d1;
  --primary-light: #4A9FFF;
  --secondary: #00D4FF;
  --tertiary: #FF006E;
  --dark: #05204A;
  --text: #1a1a2e;
  --text-light: #666;
  --bg: #ffffff;
  --bg-light: #f8faff;
  --border: rgba(11,102,255,0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: var(--text);
  background: var(--bg);
  overflow-x: hidden;
  position: relative;
}

html {
  scroll-behavior: smooth;
}

/* Background Stars */
.stars {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -2;
}

.stars::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(1px 1px at 20px 30px, #eee, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 60px 70px, #fff, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 50px 50px, #ddd, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 130px 80px, #fff, rgba(0,0,0,0)),
    radial-gradient(1px 1px at 90px 10px, #eee, rgba(0,0,0,0));
  background-repeat: repeat;
  background-size: 200px 200px;
  animation: twinkle 5s ease-in-out infinite;
}

@keyframes twinkle {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.8; }
}

/* Glow Orbs */
.glow-orb {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  z-index: -1;
  filter: blur(80px);
}

.glow-1 {
  width: 300px;
  height: 300px;
  top: 10%;
  left: 10%;
  background: rgba(11, 102, 255, 0.15);
  animation: float1 20s ease-in-out infinite;
}

.glow-2 {
  width: 250px;
  height: 250px;
  top: 50%;
  right: 10%;
  background: rgba(0, 212, 255, 0.1);
  animation: float2 25s ease-in-out infinite;
}

.glow-3 {
  width: 280px;
  height: 280px;
  bottom: 10%;
  left: 50%;
  background: rgba(255, 0, 110, 0.08);
  animation: float3 30s ease-in-out infinite;
}

@keyframes float1 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(30px, -50px); } }
@keyframes float2 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(-40px, 60px); } }
@keyframes float3 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(50px, 40px); } }

/* Navbar */
.navbar {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(11, 102, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.brand-icon {
  font-size: 1.8rem;
  animation: spin 3s linear infinite;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-links a {
  text-decoration: none;
  color: var(--text);
  font-weight: 600;
  transition: all 0.3s;
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-indicator {
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  transition: width 0.3s;
}

.nav-links a:hover {
  color: var(--primary);
}

.nav-links a:hover .nav-indicator {
  width: 20px;
}

/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding: 4rem 2rem;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(11, 102, 255, 0.08), rgba(0, 212, 255, 0.04));
  z-index: 0;
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  overflow: hidden;
}

.blob {
  position: absolute;
  filter: blur(100px);
  opacity: 0.6;
}

.blob-1 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  top: -100px;
  left: -100px;
  animation: blobMove1 15s ease-in-out infinite;
}

.blob-2 {
  width: 350px;
  height: 350px;
  background: linear-gradient(135deg, var(--secondary), var(--tertiary));
  bottom: -50px;
  right: -50px;
  animation: blobMove2 18s ease-in-out infinite;
}

.blob-3 {
  width: 300px;
  height: 300px;
  background: linear-gradient(135deg, var(--tertiary), var(--primary));
  top: 50%;
  right: 10%;
  animation: blobMove3 20s ease-in-out infinite;
}

@keyframes blobMove1 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(50px, 100px); } }
@keyframes blobMove2 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(-50px, -100px); } }
@keyframes blobMove3 { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(100px, -50px); } }

.hero-content {
  max-width: 900px;
  text-align: center;
  z-index: 2;
  animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(50px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-badge {
  display: inline-block;
  padding: 12px 30px;
  background: rgba(11, 102, 255, 0.1);
  border: 1px solid rgba(11, 102, 255, 0.3);
  border-radius: 50px;
  font-weight: 600;
  color: var(--primary);
  margin-bottom: 1.5rem;
  animation: slideDown 0.8s ease-out;
}

@keyframes slideDown {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-title {
  font-size: 4.5rem;
  font-weight: 900;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--primary), var(--secondary), var(--tertiary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.1;
  letter-spacing: -2px;
  animation: slideUp 1s ease-out 0.2s both;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-subtitle {
  font-size: 1.8rem;
  color: var(--text-light);
  margin-bottom: 1rem;
  font-weight: 600;
  animation: slideUp 1s ease-out 0.4s both;
}

.hero-description {
  font-size: 1.2rem;
  color: var(--text-light);
  max-width: 600px;
  margin: 0 auto 2.5rem;
  animation: slideUp 1s ease-out 0.6s both;
}

.hero-buttons {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
  animation: slideUp 1s ease-out 0.8s both;
}

.btn {
  padding: 15px 40px;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 700;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  border: none;
  cursor: pointer;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  position: relative;
  overflow: hidden;
}

.btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(45deg, transparent, rgba(255,255,255,0.3), transparent);
  transform: translateX(-100%);
  animation: shine 3s infinite;
}

@keyframes shine {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-light));
  color: white;
  box-shadow: 0 15px 40px rgba(11, 102, 255, 0.3);
}

.btn-primary:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 60px rgba(11, 102, 255, 0.5);
}

.btn-secondary {
  background: rgba(11, 102, 255, 0.1);
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-secondary:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-5px);
  box-shadow: 0 20px 50px rgba(11, 102, 255, 0.4);
}

.btn-icon {
  font-size: 1.2rem;
  transition: transform 0.3s;
}

.btn:hover .btn-icon {
  transform: translateX(4px);
}

/* Sections */
.section {
  padding: 8rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}

.section-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(11, 102, 255, 0.03), transparent);
  pointer-events: none;
  z-index: 0;
}

.section-title {
  font-size: 3rem;
  font-weight: 900;
  margin-bottom: 3.5rem;
  color: var(--dark);
  position: relative;
  display: inline-block;
  z-index: 1;
}

.title-number {
  display: inline-block;
  font-size: 1rem;
  color: var(--primary);
  font-weight: 700;
  margin-right: 1rem;
  background: rgba(11, 102, 255, 0.1);
  padding: 4px 12px;
  border-radius: 50px;
  letter-spacing: 2px;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 0;
  width: 80px;
  height: 6px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  border-radius: 3px;
  box-shadow: 0 5px 20px rgba(11, 102, 255, 0.3);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
}

/* Projects Grid */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  position: relative;
  z-index: 1;
}

.project-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(248, 250, 255, 0.9));
  backdrop-filter: blur(20px);
  border: 1px solid rgba(11, 102, 255, 0.2);
  border-radius: 16px;
  padding: 2.5rem;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(11,102,255,0.2), transparent);
  transition: left 0.5s;
  z-index: 0;
}

.project-card:hover::before {
  left: 100%;
}

.project-card:hover {
  transform: translateY(-15px) translateX(-2px);
  box-shadow: 0 30px 60px rgba(11, 102, 255, 0.2), inset 0 1px 0 rgba(255,255,255,0.6);
  border-color: var(--primary);
}

.project-title {
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 1.2rem;
  color: var(--dark);
  position: relative;
  z-index: 1;
}

.project-desc {
  list-style: none;
  padding: 0;
  position: relative;
  z-index: 1;
}

.project-desc li {
  padding-left: 1.8rem;
  margin-bottom: 0.8rem;
  color: var(--text-light);
  position: relative;
  font-weight: 500;
}

.project-desc li::before {
  content: '✨';
  position: absolute;
  left: 0;
  color: var(--primary);
  font-size: 1.1rem;
}

/* Timeline */
.timeline-item {
  padding: 2.5rem;
  border-left: 4px solid var(--primary);
  margin-bottom: 2.5rem;
  background: linear-gradient(135deg, rgba(248, 250, 255, 0.5), rgba(255, 255, 255, 0.8));
  backdrop-filter: blur(10px);
  border-radius: 12px;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
  overflow: hidden;
}

.timeline-item::after {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 4px;
  height: 0;
  background: linear-gradient(180deg, var(--secondary), var(--tertiary));
  transition: height 0.3s;
}

.timeline-item:hover::after {
  height: 100%;
}

.timeline-item:hover {
  box-shadow: 0 15px 40px rgba(11, 102, 255, 0.15);
  transform: translateX(8px);
}

.timeline-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--dark);
  margin-bottom: 0.5rem;
}

.timeline-meta {
  font-size: 0.95rem;
  color: var(--text-light);
  margin-bottom: 1rem;
  font-weight: 600;
}

.timeline-desc {
  list-style: none;
  padding: 0;
  margin: 0;
}

.timeline-desc li {
  padding-left: 1.5rem;
  margin-bottom: 0.6rem;
  color: var(--text-light);
  position: relative;
  font-weight: 500;
}

.timeline-desc li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: var(--secondary);
  font-weight: bold;
}

/* Skills */
.skills-section {
  background: linear-gradient(135deg, rgba(11, 102, 255, 0.05), rgba(0, 212, 255, 0.03));
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1.8rem;
  position: relative;
  z-index: 1;
}

.skill-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(248, 250, 255, 0.6));
  backdrop-filter: blur(20px);
  border: 2px solid var(--border);
  padding: 2rem 1.5rem;
  border-radius: 14px;
  text-align: center;
  font-weight: 700;
  color: var(--primary);
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.skill-item::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  opacity: 0;
  transition: opacity 0.3s;
  z-index: -1;
}

.skill-item:hover::before {
  opacity: 1;
}

.skill-item:hover {
  color: white;
  transform: translateY(-8px) scale(1.05);
  box-shadow: 0 20px 50px rgba(11, 102, 255, 0.3);
  border-color: var(--primary);
}

/* Contact Section */
.contact-section {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  position: relative;
  overflow: hidden;
}

.contact-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.contact-blob {
  position: absolute;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(255,255,255,0.1), transparent);
  border-radius: 50%;
  animation: blobFloat 8s ease-in-out infinite;
  bottom: -100px;
  right: -100px;
}

@keyframes blobFloat {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, -30px); }
}

.contact-section .section-title {
  color: white;
  position: relative;
  z-index: 1;
}

.contact-section .section-title::after {
  background: rgba(255, 255, 255, 0.7);
  box-shadow: 0 5px 20px rgba(255, 255, 255, 0.3);
}

.contact-content {
  text-align: center;
  position: relative;
  z-index: 1;
}

.contact-text {
  font-size: 1.2rem;
  margin-bottom: 2.5rem;
  opacity: 0.95;
  font-weight: 500;
}

.contact-links {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.contact-link {
  display: inline-block;
  padding: 14px 28px;
  background: rgba(255, 255, 255, 0.15);
  border: 2px solid white;
  border-radius: 50px;
  color: white;
  text-decoration: none;
  font-weight: 700;
  transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  backdrop-filter: blur(10px);
}

.contact-link:hover {
  background: white;
  color: var(--primary);
  transform: translateY(-5px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
}

/* About Section */
.about-section {
  text-align: center;
}

.about-content {
  max-width: 800px;
  margin: 0 auto;
  font-size: 1.2rem;
  line-height: 1.8;
  color: var(--text-light);
  position: relative;
  z-index: 1;
}

/* Footer */
.footer {
  background: linear-gradient(135deg, var(--dark), #0f3a7d);
  color: white;
  padding: 3rem 2rem;
  text-align: center;
  border-top: 1px solid rgba(11, 102, 255, 0.2);
  position: relative;
  overflow: hidden;
}

.footer-glow {
  position: absolute;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(11, 102, 255, 0.1), transparent);
  border-radius: 50%;
  bottom: -100px;
  right: -100px;
  pointer-events: none;
}

/* Responsive */
@media (max-width: 768px) {
  .nav-links { gap: 1rem; font-size: 0.9rem; }
  .hero-title { font-size: 2.8rem; }
  .hero-subtitle { font-size: 1.3rem; }
  .section { padding: 5rem 1rem; }
  .section-title { font-size: 2rem; }
  .two-col { grid-template-columns: 1fr; gap: 2rem; }
  .projects-grid { grid-template-columns: 1fr; }
  .skills-grid { grid-template-columns: repeat(2, 1fr); }
  .hero-buttons { flex-direction: column; }
  .btn { width: 100%; }
}

@media (max-width: 480px) {
  .nav-links { flex-direction: column; gap: 0.5rem; }
  .hero-title { font-size: 1.8rem; }
  .hero-subtitle { font-size: 1rem; }
  .section { padding: 3rem 1rem; }
  .section-title { font-size: 1.4rem; }
  .skills-grid { grid-template-columns: 1fr; }
  .blob { width: 200px !important; height: 200px !important; }
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

