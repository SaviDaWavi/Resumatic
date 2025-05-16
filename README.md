
# 📄 Resumatic – Automated Resume Builder

**Resumatic** is a Python-based tool that renders and exports beautiful resume PDFs using [JSON Resume](https://jsonresume.org/) themes. It streamlines the process with easy automation, so you can focus on what matters: your content.

![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square)
![Node.js](https://img.shields.io/badge/Uses-Node.js%20%26%20NPM-green?style=flat-square)

---

## 🚀 Quick Start

### 1. Open Command Prompt in the Project Directory
Make sure you're inside the folder that contains:

- `resumatic.py`
- `resumatic.bat`

### 2. Install a Theme
Run this command in your terminal:

```bash
npm install jsonresume-theme-rickosborne
```

> 🔁 Replace `rickosborne` with any other [JSON Resume theme](https://www.npmjs.com/search?q=jsonresume-theme).

### 3. Run Resumatic
Use either command:

```bash
python resumatic.py
```
or:
```bash
resumatic.bat
```

This will:
- Load your `resume.json`
- Render it using the selected theme
- Export both `resume.html` and `resume.pdf`

---

## 🎨 Changing the Theme

To use a different theme:

1. Open `resumatic.py`
2. Find this line:

   ```python
   theme = "rickosborne"
   ```

3. Change it to another theme, e.g., `"even"`.

> ⚠️ You **must install** the theme first:
```bash
npm install jsonresume-theme-even
```

---

## 🛠️ PDF Export Configuration

Customize the PDF output by editing `html_to_pdf.py`:

```python
TARGET_PAGE_COUNT = 1     # Max number of pages
SCALE_START = 2.00        # Start zoom level (200%)
SCALE_END = 0.20          # Minimum zoom level (20%)
SCALE_STEP = 0.01         # Step size per iteration
SCALE_FACTOR = 0.95       # Zoom reduction factor
```

Tweak these to ensure your resume fits your desired layout or page count.

---

## 📄 resume.json – Your Resume Data

This file holds all your resume information. You can:

- Edit the included `resume.json`
- Replace it with your own (keep the filename as `resume.json`)

---

## 📁 File Overview

| File             | Description                                |
|------------------|--------------------------------------------|
| `resumatic.py`   | Main automation script                     |
| `resumatic.bat`  | Windows shortcut for quick execution       |
| `html_to_pdf.py` | PDF export with dynamic scaling            |
| `resume.json`    | Your resume data in JSON Resume format     |
| `README.md`      | This documentation                         |

---

## 📤 Output Files

| File          | Description                              |
|---------------|------------------------------------------|
| `resume.html` | HTML resume rendered from your JSON data |
| `resume.pdf`  | Final printable PDF output                |

---

## 🙏 Special Thanks

This project builds on amazing open-source tools:

- [**resumed**](https://github.com/rbardini/resumed) – CLI tool for rendering JSON Resume data
- [**jsonresume-theme-class**](https://github.com/jsonresume/jsonresume-theme-class) – A clean and professional base theme

Under the hood, Resumatic uses `resume-cli` to convert your `resume.json` into themed HTML.

---

## 🔗 Resources & Help

- 🔍 Browse themes: [npmjs.com/search?q=jsonresume-theme](https://www.npmjs.com/search?q=jsonresume-theme)
- 📖 Learn about the format: [jsonresume.org](https://jsonresume.org)

---

Feel free to open an issue or PR if you’d like to contribute or report bugs. Happy resume building! 💼✨

--- 
