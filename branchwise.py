import pandas as pd
sheet1 = pd.read_excel("Sheet1.xlsx")
sheet2 = pd.read_excel("Sheet2.xlsx")
sheet1.columns = sheet1.columns.str.strip().str.lower()
sheet2.columns = sheet2.columns.str.strip().str.lower()
def filter_tags(tags):
    if pd.isna(tags):
        return False
    tags_str = str(tags).upper()
    return tags_str.strip() == "ANY" or "A4" in tags_str
filtered = sheet1[sheet1['tags'].apply(filter_tags)]
merged = pd.merge(
    filtered,
    sheet2[['station name', 'stipend']],
    on='station name',
    how='left'
)
result = merged[['station name', 'business domain', 'stipend', 'centre (city)']]
result.columns = ['name', 'domain', 'stipend', 'location']
result.to_excel("filtered_companies.xlsx", index=False)
