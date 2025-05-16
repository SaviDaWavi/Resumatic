import subprocess
import os
import sys
import shutil

# === Configuration ===
theme = 'rickosborne'  # Change this to use a different installed theme (e.g., "even", "classic")

def install_playwright():
    """
    Installs Playwright and its required browser drivers if not already available.
    """
    try:
        import playwright  # noqa: F401
        print("✅ Playwright is already installed.")
    except ImportError:
        print("🔧 Playwright not found. Installing via pip...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'playwright'])

        print("🔧 Installing Playwright browser binaries...")
        subprocess.check_call(['playwright', 'install'])
        print("✅ Playwright installation complete.")

def install_resumecli():
    """
    Installs the 'resume-cli' tool globally via npm if it's not already available.
    """
    if shutil.which('resume') is None:
        print("🔧 'resume-cli' not found. Attempting installation via npm...")
        try:
            subprocess.check_call(['npm', 'install', '-g', 'resume-cli'])
            print("✅ 'resume-cli' installed successfully.")
        except FileNotFoundError:
            print("❌ Error: npm not found. Please install Node.js and npm, then try again.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install 'resume-cli': {e}")
            print("🔁 Try running: npm install -g resume-cli")
            sys.exit(1)
    else:
        print("✅ 'resume-cli' is already installed.")

def automate_resume():
    """
    Automates the full resume generation process:
    - Ensures dependencies ('resume-cli' and Playwright) are installed.
    - Converts `resume.json` to `resume.html` using a JSON Resume theme.
    - Converts the HTML to a well-scaled, single-page PDF using Playwright.
    """
    install_resumecli()
    install_playwright()

    resume_json = 'resume.json'
    output_html = 'resume.html'
    output_pdf = 'resume.pdf'
    html_to_pdf_script = 'html_to_pdf.py'

    try:
        # Ensure 'resume' CLI tool is in the PATH
        resume_path = shutil.which('resume')
        if resume_path is None:
            print("❌ Error: 'resume' command not found after installation.")
            sys.exit(1)

        # Check that the HTML to PDF conversion script exists
        if not os.path.exists(html_to_pdf_script):
            print(f"❌ Error: '{html_to_pdf_script}' not found in current directory.")
            sys.exit(1)

        # Convert JSON to HTML resume using the chosen theme
        print(f"📝 Exporting resume using theme '{theme}'...")
        subprocess.run([resume_path, 'export', output_html, '--theme', theme, '--resume', resume_json], check=True)
        print(f"✅ HTML generated: {os.path.abspath(output_html)}")

        # Generate PDF from HTML using custom scaling logic
        print("🖨️  Generating PDF from HTML...")
        subprocess.run([sys.executable, html_to_pdf_script, output_html, output_pdf], check=True)
        print(f"✅ PDF generated: {os.path.abspath(output_pdf)}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Subprocess error: {e}")
        print("🔍 Please verify the input files and configuration.")
    except FileNotFoundError as e:
        print(f"❌ File error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    automate_resume()
