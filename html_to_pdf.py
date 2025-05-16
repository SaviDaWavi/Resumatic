from playwright.sync_api import sync_playwright
from PyPDF2 import PdfReader
import pathlib
import tempfile
import shutil
import os

# === Configuration ===
TARGET_PAGE_COUNT = 1     # Max number of pages allowed in the final PDF
SCALE_START = 2.00        # Max scale to start searching from
SCALE_END = 0.20          # Minimum scale to consider
SCALE_FACTOR = 0.95       # Final scale modifier (e.g., 95% of optimal)

def count_pdf_pages(pdf_path):
    """
    Counts the number of pages in a PDF file.
    """
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        return len(reader.pages)

def generate_pdf(path_html='resume.html', output_pdf='resume.pdf', font_family=None):
    """
    Generates a PDF from HTML using Playwright (Chromium). Tries to fit the content
    within TARGET_PAGE_COUNT pages using a binary search to find the optimal scale.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Convert HTML path to file URI
        file_uri = pathlib.Path(path_html).absolute().as_uri()
        page.goto(file_uri)

        # Ensure all fonts and resources are ready
        page.wait_for_load_state('networkidle')
        page.evaluate("() => document.fonts.ready")
        page.emulate_media(media='print')

        # Optional: Inject custom font override
        if font_family and font_family.strip():
            css = f"* {{ font-family: '{font_family}', sans-serif !important; }}"
            page.add_style_tag(content=css)

        temp_dir = tempfile.mkdtemp()
        best_scale = SCALE_END

        try:
            # Binary search for best fitting scale
            low = SCALE_END
            high = SCALE_START

            while (high - low) > 0.001:
                mid = round((high + low) / 2, 4)
                test_pdf = os.path.join(temp_dir, f"test_{mid:.4f}.pdf")

                # Generate PDF with current mid scale
                page.pdf(
                    path=test_pdf,
                    format='Letter',
                    print_background=True,
                    margin={ 'top': '0.5in', 'bottom': '0.5in', 'left': '0.5in', 'right': '0.5in' },
                    scale=mid
                )

                num_pages = count_pdf_pages(test_pdf)

                if num_pages > TARGET_PAGE_COUNT:
                    # Too large — reduce scale
                    high = mid
                else:
                    # Fits within target — try to increase scale
                    best_scale = mid
                    low = mid

            # Apply final scale adjustment (optional margin)
            final_scale = round(best_scale * SCALE_FACTOR, 4)
            print(f"✅ Using best scale: {best_scale:.4f} → final scale: {final_scale:.4f}")

            # Generate final PDF with best scale
            page.pdf(
                path=output_pdf,
                format='Letter',
                print_background=True,
                margin={ 'top': '0.5in', 'bottom': '0.5in', 'left': '0.5in', 'right': '0.5in' },
                scale=final_scale
            )

        finally:
            shutil.rmtree(temp_dir)
            browser.close()

if __name__ == '__main__':
    # Example usage
    # generate_pdf(path_html='resume.html', output_pdf='resume.pdf', font_family='Arial')
    generate_pdf(path_html='resume.html', output_pdf='resume.pdf')
