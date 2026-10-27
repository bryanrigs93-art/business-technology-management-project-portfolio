# Bryan Bodegas | Technology Portfolio / Portafolio tecnológico

**EN:** Business Technology Management student transitioning from BPO customer support into technology-focused roles. This portfolio highlights academic case studies and hands-on learning artifacts; it does not present academic work as paid industry experience.

**ES:** Estudiante de Business Technology Management en transición desde Customer Support en BPO hacia puestos tecnológicos. Este portafolio presenta casos académicos y evidencias de aprendizaje práctico; no presenta los trabajos universitarios como experiencia laboral remunerada en el sector.

## 🔐 Cybersecurity & Technology Risk / Ciberseguridad y Riesgo Tecnológico

**[Explore all four cybersecurity projects / Explorar los cuatro proyectos](cybersecurity/README.md)**

| Academic case study / Caso académico | What it demonstrates / Qué demuestra | Explore / Explorar |
|---|---|---|
| **DataProtect** | 9-scenario risk matrix in Excel and proposed remediation / Matriz de 9 riesgos en Excel y remediación propuesta | [EN / ES](cybersecurity/01-dataprotect/README.md) |
| **Equifax (2017)** | Vulnerability and breach analysis / Análisis de vulnerabilidades e incidentes | [EN / ES](cybersecurity/02-equifax/README.md) |
| **Bank of America / Infosys McCamish** | Third-party security risk and proposed KPIs / Riesgo de proveedores e indicadores propuestos | [EN / ES](cybersecurity/03-bank-of-america/README.md) |
| **Tech del Futuro** | Information security policy and awareness plan / Política de seguridad y plan de concienciación | [EN / ES](cybersecurity/04-tech-del-futuro/README.md) |

> **Scope / Alcance:** Academic exercises and simulations, not security work performed for the organizations named. / Ejercicios y simulaciones académicas, no trabajos de seguridad realizados para las organizaciones mencionadas.

---

## 📊 Data Analytics / Análisis de datos

**EN:** The next section documents an existing Python project analyzing Hacker News engagement.  
**ES:** La siguiente sección documenta un proyecto existente de Python sobre participación en Hacker News. El material técnico previo se conserva.

---

# Hacker News Tech Engagement Analysis

[Open the live notebook in Google Colab](https://colab.research.google.com/drive/1ruE0dm5EbukzDUa2nQuhpubpCPv3i9IB?usp=sharing)

A compact Python portfolio project that collects technology news from Hacker News, cleans and validates the data, engineers an engagement metric, and exports CSV and formatted Excel reports.

## Why this project

The goal is not just to demonstrate web scraping. The project shows an end-to-end analyst workflow:

**Web data extraction → HTML inspection → data cleaning → validation → feature engineering → analysis → reporting**

It is designed to be small enough to review quickly while still demonstrating practical problem-solving with real, changing web data.

## Business question

**Which Hacker News stories and recurring sources generate the strongest reader engagement?**

## Tech stack

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- XlsxWriter
- Google Colab

## Data collected

For each story, the project collects:

| Field | Description |
|---|---|
| `Story_ID` | Hacker News story identifier |
| `Rank` | Position on the page |
| `Title` | Story title |
| `Source` | Source domain |
| `Score` | Hacker News points |
| `Author` | User who submitted the story |
| `Age` | Relative publication age |
| `Comments` | Number of comments |
| `Link` | Story URL |
| `Page` | Page scraped |
| `Engagement` | Custom metric: `Score + Comments` |

## Project workflow

1. Request the first three Hacker News pages.
2. Parse story rows with BeautifulSoup.
3. Read metadata from the sibling row below each story.
4. Handle missing sources, scores, authors, and zero-comment stories.
5. Convert numeric fields to numeric data types.
6. Validate nulls and duplicate story IDs.
7. Create an engagement metric.
8. Identify top stories and recurring high-engagement sources.
9. Build two concise visualizations.
10. Export:
   - `hacker_news_engagement.csv`
   - `hacker_news_engagement_analysis.xlsx`

The Excel workbook contains three formatted sheets:

- **Stories** — full cleaned dataset
- **Top Stories** — highest-engagement stories
- **Source Analysis** — aggregated source performance

## Key technical challenge

Hacker News stores the story title and its metadata in **two separate sibling table rows**. The scraper therefore cannot treat one HTML row as a complete record.

The project links:

```text
Story row
├── Rank
├── Title
├── Link
└── Source

Next sibling row
├── Score
├── Author
├── Age
└── Comments
```

This is a useful example of inspecting a page structure before writing extraction logic.

## Run the project

The easiest option is Google Colab.

1. Open the [live Colab notebook](https://colab.research.google.com/drive/1ruE0dm5EbukzDUa2nQuhpubpCPv3i9IB?usp=sharing).
2. Run the cells from top to bottom.
3. The notebook scrapes live Hacker News data.
4. The final cells generate a CSV and a formatted Excel report.
5. In Google Colab, the Excel file downloads automatically.

Install dependencies locally with:

```bash
pip install -r requirements.txt
```

You can also run the standalone script:

```bash
python src/hacker_news_analysis.py
```

## Portfolio skills demonstrated

- Web scraping and HTML inspection
- CSS selectors and DOM navigation
- Pagination
- Error-tolerant extraction
- Data cleaning with Pandas
- Data-quality checks
- Feature engineering
- Grouped analysis
- Basic data visualization
- Automated CSV and Excel reporting

## Notes

Hacker News is live and changes continuously, so story counts and analysis results will differ between runs. The project intentionally uses only three pages to keep the analysis focused and easy to review.

---

**Author:** Bryan Bodegas  
**Portfolio focus:** Business Technology Management · Business Analysis · Data Analysis
