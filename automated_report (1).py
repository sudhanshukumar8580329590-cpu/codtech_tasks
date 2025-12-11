import pandas as pd  # For reading and analyzing CSV data
from fpdf import FPDF

class InvoicePDF(FPDF):
    def header(self):
        # Add logo (ensure the image path is correct)
        self.image('task 2/pdf_icon.png', 165, 15, 33)  # Logo
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Invoice Report', 1, 0, 'C')  # Title
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

# Function to read and analyze data
def read_and_analyze_data(file_path):
    # Read CSV into a DataFrame
    df = pd.read_csv(file_path)
    
    # Analysis: Calculate subtotal for each item and grand total
    df['Subtotal'] = df['Quantity'] * df['Price']
    total_quantity = df['Quantity'].sum()
    grand_total = df['Subtotal'].sum()
    
    # Return analyzed data
    return df, total_quantity, grand_total

# Main script
def generate_pdf_report(data_file, output_file):
    # Read and analyze data
    df, total_quantity, grand_total = read_and_analyze_data(data_file)
    
    # Initialize PDF
    pdf = InvoicePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    
    # Add summary section
    pdf.cell(0, 10, f'Total Items: {len(df)} | Total Quantity: {total_quantity} | Grand Total: ${grand_total:.2f}', 0, 1)
    pdf.ln(10)
    
    # Add table header
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Item', 1, 0, 'C')
    pdf.cell(30, 10, 'Quantity', 1, 0, 'C')
    pdf.cell(30, 10, 'Price', 1, 0, 'C')
    pdf.cell(30, 10, 'Subtotal', 1, 1, 'C')
    
    # Add data rows
    pdf.set_font('Times', '', 12)
    for _, row in df.iterrows():
        pdf.cell(60, 10, row['Item'], 1, 0, 'L')
        pdf.cell(30, 10, str(row['Quantity']), 1, 0, 'C')
        pdf.cell(30, 10, f"${row['Price']:.2f}", 1, 0, 'C')
        pdf.cell(30, 10, f"${row['Subtotal']:.2f}", 1, 1, 'C')
    
    # Output PDF
    pdf.output(output_file, 'F')
    print(f"PDF report generated: {output_file}")

# Run the script
if __name__ == "__main__":
    generate_pdf_report('task 2/invoice_data.csv', 'task 2/Internship_Report.pdf.')
