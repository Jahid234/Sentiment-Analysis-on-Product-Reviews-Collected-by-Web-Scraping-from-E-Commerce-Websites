from bs4 import BeautifulSoup
import openpyxl

# Read HTML file
file_path = 'amazon5_lawn.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class="a-row"
divs_a_row = soup.find_all('div', class_='a-row')

# Create Excel workbook and sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Add headers to the Excel sheet
sheet.append(['Stars'])

# Loop through each div with class="a-row" and extract the required information
for div in divs_a_row:
    review_title = div.find('a', class_='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold', attrs={'data-hook': 'review-title'})
    
    # Check if review title is found
    if review_title:
        review_star_rating = review_title.find_next('i', attrs={'data-hook': 'review-star-rating'})
        
        # Check if review star rating is found
        if review_star_rating:
            stars_span = review_star_rating.find('span', class_='a-icon-alt')
            
            # Check if span with class='a-icon-alt' is found
            if stars_span:
                stars = stars_span.text
                
                # Append the stars value to the Excel sheet
                sheet.append([stars])

# Save the Excel file
excel_file_name = 'stars_lawn5.xlsx'
wb.save(excel_file_name)

print(f'The stars information has been saved to {excel_file_name}')
