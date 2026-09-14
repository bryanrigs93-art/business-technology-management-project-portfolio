import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://news.ycombinator.com/news"
PAGES_TO_SCRAPE = 3


def scrape_hacker_news(pages=PAGES_TO_SCRAPE):
    """Collect Hacker News stories from the requested number of pages."""
    stories_data = []

    for page in range(1, pages + 1):
        print(f"Processing page {page}...")

        response = requests.get(
            BASE_URL,
            params={"p": page},
            timeout=30,
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        stories = soup.select("tr.athing")

        for story in stories:
            story_id = story.get("id")

            rank_element = story.select_one("span.rank")
            rank = (
                rank_element.get_text(strip=True).replace(".", "")
                if rank_element
                else None
            )

            title_element = story.select_one("span.titleline > a")
            title = title_element.get_text(strip=True) if title_element else None
            link = title_element.get("href") if title_element else None

            source_element = story.select_one("span.sitestr")
            source = (
                source_element.get_text(strip=True)
                if source_element
                else "news.ycombinator.com"
            )

            metadata_row = story.find_next_sibling("tr")

            score_element = metadata_row.select_one("span.score") if metadata_row else None
            if score_element:
                score = (
                    score_element.get_text(strip=True)
                    .replace(" points", "")
                    .replace(" point", "")
                )
            else:
                score = 0

            author_element = metadata_row.select_one("a.hnuser") if metadata_row else None
            author = author_element.get_text(strip=True) if author_element else "Unknown"

            age_element = metadata_row.select_one("span.age") if metadata_row else None
            age = age_element.get_text(strip=True) if age_element else None

            comments = 0
            if metadata_row:
                for link_element in metadata_row.select("a"):
                    text = link_element.get_text(strip=True)
                    if "comment" in text:
                        comments = text.split()[0]
                    elif text == "discuss":
                        comments = 0

            stories_data.append(
                {
                    "Story_ID": story_id,
                    "Rank": rank,
                    "Title": title,
                    "Source": source,
                    "Score": score,
                    "Author": author,
                    "Age": age,
                    "Comments": comments,
                    "Link": link,
                    "Page": page,
                }
            )

        time.sleep(1)

    return pd.DataFrame(stories_data)


def clean_and_engineer(df):
    """Convert data types, validate basic quality, and create engagement."""
    numeric_columns = ["Rank", "Score", "Comments", "Page"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["Engagement"] = df["Score"].fillna(0) + df["Comments"].fillna(0)

    print("\nDataset dimensions:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate Story IDs:")
    print(df["Story_ID"].duplicated().sum())

    return df


def build_analysis(df):
    """Create recruiter-friendly analytical tables."""
    top_stories = (
        df[["Title", "Source", "Score", "Comments", "Engagement"]]
        .sort_values("Engagement", ascending=False)
        .head(10)
    )

    source_analysis = (
        df.groupby("Source")
        .agg(
            Stories=("Title", "count"),
            Average_Score=("Score", "mean"),
            Average_Comments=("Comments", "mean"),
            Average_Engagement=("Engagement", "mean"),
        )
        .reset_index()
    )

    source_analysis = (
        source_analysis[source_analysis["Stories"] >= 2]
        .sort_values("Average_Engagement", ascending=False)
    )

    return top_stories, source_analysis


def save_charts(df):
    """Save two concise charts for portfolio review."""
    top_10 = (
        df.sort_values("Engagement", ascending=False)
        .head(10)
        .sort_values("Engagement")
    )

    plt.figure(figsize=(10, 6))
    plt.barh(top_10["Title"], top_10["Engagement"])
    plt.xlabel("Engagement")
    plt.ylabel("Story")
    plt.title("Top 10 Hacker News Stories by Engagement")
    plt.tight_layout()
    plt.savefig("top_stories_engagement.png", dpi=160, bbox_inches="tight")
    plt.close()

    top_sources = df["Source"].value_counts().head(10).sort_values()

    plt.figure(figsize=(9, 5))
    plt.barh(top_sources.index, top_sources.values)
    plt.xlabel("Number of Stories")
    plt.ylabel("Source")
    plt.title("Most Frequent Sources on Hacker News")
    plt.tight_layout()
    plt.savefig("most_frequent_sources.png", dpi=160, bbox_inches="tight")
    plt.close()


def export_reports(df, top_stories, source_analysis):
    """Export CSV plus a formatted three-sheet Excel workbook."""
    csv_file = "hacker_news_engagement.csv"
    excel_file = "hacker_news_engagement_analysis.xlsx"

    df.to_csv(csv_file, index=False, encoding="utf-8-sig")

    with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Stories", index=False)
        top_stories.to_excel(writer, sheet_name="Top Stories", index=False)
        source_analysis.to_excel(writer, sheet_name="Source Analysis", index=False)

        workbook = writer.book
        integer_format = workbook.add_format({"num_format": "0", "align": "center"})
        decimal_format = workbook.add_format({"num_format": "0.00"})

        worksheet = writer.sheets["Stories"]
        rows, columns = df.shape
        worksheet.add_table(
            0,
            0,
            rows,
            columns - 1,
            {
                "name": "StoriesTable",
                "style": "Table Style Medium 2",
                "columns": [{"header": column} for column in df.columns],
            },
        )
        worksheet.freeze_panes(1, 0)
        worksheet.set_column("A:A", 14)
        worksheet.set_column("B:B", 8, integer_format)
        worksheet.set_column("C:C", 65)
        worksheet.set_column("D:D", 25)
        worksheet.set_column("E:E", 10, integer_format)
        worksheet.set_column("F:F", 18)
        worksheet.set_column("G:G", 15)
        worksheet.set_column("H:H", 12, integer_format)
        worksheet.set_column("I:I", 55)
        worksheet.set_column("J:J", 8, integer_format)
        worksheet.set_column("K:K", 14, integer_format)

        engagement_column = df.columns.get_loc("Engagement")
        worksheet.conditional_format(
            1, engagement_column, rows, engagement_column, {"type": "data_bar"}
        )

        worksheet_top = writer.sheets["Top Stories"]
        top_rows, top_columns = top_stories.shape
        worksheet_top.add_table(
            0,
            0,
            top_rows,
            top_columns - 1,
            {
                "name": "TopStoriesTable",
                "style": "Table Style Medium 4",
                "columns": [{"header": column} for column in top_stories.columns],
            },
        )
        worksheet_top.freeze_panes(1, 0)
        worksheet_top.set_column("A:A", 70)
        worksheet_top.set_column("B:B", 25)
        worksheet_top.set_column("C:E", 15)

        if "Engagement" in top_stories.columns:
            engagement_top_col = top_stories.columns.get_loc("Engagement")
            worksheet_top.conditional_format(
                1,
                engagement_top_col,
                top_rows,
                engagement_top_col,
                {"type": "data_bar"},
            )

        worksheet_sources = writer.sheets["Source Analysis"]
        source_rows, source_columns = source_analysis.shape
        worksheet_sources.add_table(
            0,
            0,
            source_rows,
            source_columns - 1,
            {
                "name": "SourceAnalysisTable",
                "style": "Table Style Medium 9",
                "columns": [{"header": column} for column in source_analysis.columns],
            },
        )
        worksheet_sources.freeze_panes(1, 0)
        worksheet_sources.set_column("A:A", 30)
        worksheet_sources.set_column("B:B", 12)
        worksheet_sources.set_column("C:E", 20, decimal_format)

    print(f"\nCreated: {csv_file}")
    print(f"Created: {excel_file}")


def main():
    df = scrape_hacker_news()
    df = clean_and_engineer(df)
    top_stories, source_analysis = build_analysis(df)
    save_charts(df)
    export_reports(df, top_stories, source_analysis)


if __name__ == "__main__":
    main()
