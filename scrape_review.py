from bs4 import BeautifulSoup
import openpyxl

# Read HTML file
with open('amazon5_lawn.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class="a-row a-spacing-small review-data"
review_divs = soup.find_all('div', class_='a-row a-spacing-small review-data')

# Extract reviews
reviews = []
for div in review_divs:
    review_span = div.find('span', {'data-hook': 'review-body', 'class': 'a-size-base review-text review-text-content'})
    if review_span:
        reviews.append(review_span.get_text(strip=True))

# Create and write to Excel file
excel_file = 'amazonLawn_reviews5.xlsx'
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write header
sheet['A1'] = 'Reviews'

# Write reviews to Excel
for index, review in enumerate(reviews, start=2):
    sheet.cell(row=index, column=1, value=review)

# Save Excel file
workbook.save(excel_file)

print(f'Reviews extracted and saved to {excel_file}')
