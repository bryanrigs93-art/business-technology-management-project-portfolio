# Hacker News — Engagement Analysis
## Análisis de interacción en Hacker News

[← Portfolio / Portafolio](../../../README.md) · [Notebook / Cuaderno](hacker_news_engagement_analysis.ipynb) · [Open in Colab / Abrir en Colab](https://colab.research.google.com/drive/1ruE0dm5EbukzDUa2nQuhpubpCPv3i9IB?usp=sharing)

**Tools / Herramientas:** Python · Requests · BeautifulSoup · Pandas · Matplotlib · XlsxWriter · Google Colab

## English

I wanted to compare which technology stories on Hacker News receive the most attention, so I built a Python script to collect posts, clean the information and summarize the results.

The script reads the first three pages of Hacker News and captures titles, sources, scores, authors and comment counts. One detail I had to account for is that a story and its metadata appear in **separate HTML rows**. I combined those rows before working with the data.

I then checked for missing values and duplicate IDs, calculated a simple **engagement score (points + comments)**, compared stories and sources, and produced charts and Excel/CSV reports.

Because the script uses live pages, the results change each time it runs.

## Español

Quería comparar cuáles noticias tecnológicas reciben más atención en Hacker News, así que desarrollé un programa en Python para recopilar publicaciones, limpiar los datos y resumir los resultados.

El programa lee las primeras tres páginas de Hacker News y obtiene títulos, fuentes, puntajes, autores y cantidad de comentarios. Un detalle que tuve que resolver es que cada noticia y sus datos adicionales aparecen en **filas HTML distintas**. Primero relacioné esas filas y después trabajé con los registros completos.

Luego revisé valores faltantes e identificadores duplicados, calculé una medida sencilla de **interacción (puntos + comentarios)**, comparé noticias y fuentes, y generé gráficos y reportes en Excel y CSV.

Como el programa consulta páginas en vivo, los resultados cambian en cada ejecución.

## Files / Archivos

- [Jupyter notebook / Cuaderno de Jupyter](hacker_news_engagement_analysis.ipynb)
- [Python script / Script de Python](hacker_news_analysis.py)
- [Dependencies / Dependencias](requirements.txt)

**Run it / Para ejecutarlo:** Open the notebook in Colab and run the cells, or run the Python script from the repository root. / Abre el cuaderno en Colab y ejecuta las celdas, o ejecuta el script desde la raíz del repositorio.
