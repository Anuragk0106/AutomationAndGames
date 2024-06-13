from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def generate_receipt(receipt_info):
    file_name = f"receipt_{receipt_info['transaction_id']}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Payment Receipt")

    # Company Info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, "Company Name")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 120, "Address Line 1")
    c.drawString(50, height - 140, "Address Line 2")
    c.drawString(50, height - 160, "City, State, ZIP")
    c.drawString(50, height - 180, "Phone: (123) 456-7890")

    # Receipt Info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400, height - 100, f"Receipt ID: {receipt_info['transaction_id']}")
    c.setFont("Helvetica", 12)
    c.drawString(400, height - 120, f"Date: {receipt_info['date']}")
    
    # Draw line
    c.line(50, height - 200, width - 50, height - 200)

    # Customer Info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 220, "Customer Information")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 240, f"Name: {receipt_info['customer_name']}")
    c.drawString(50, height - 260, f"Email: {receipt_info['customer_email']}")
    c.drawString(50, height - 280, f"Phone: {receipt_info['customer_phone']}")

    # Items
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 320, "Item")
    c.drawString(300, height - 320, "Quantity")
    c.drawString(400, height - 320, "Price")
    c.drawString(500, height - 320, "Total")
    c.line(50, height - 330, width - 50, height - 330)

    y_position = height - 350
    for item in receipt_info['items']:
        c.drawString(50, y_position, item['description'])
        c.drawString(300, y_position, str(item['quantity']))
        c.drawString(400, y_position, f"${item['price']:.2f}")
        c.drawString(500, y_position, f"${item['total']:.2f}")
        y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400, y_position - 20, "Total Amount:")
    c.drawString(500, y_position - 20, f"${receipt_info['total_amount']:.2f}")

    c.save()
    print(f"Receipt saved as {file_name}")

if __name__ == "__main__":
    receipt_info = {
        "transaction_id": "123456789",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "customer_name": "John Doe",
        "customer_email": "john.doe@example.com",
        "customer_phone": "(123) 456-7890",
        "items": [
            {"description": "Product 1", "quantity": 2, "price": 10.00, "total": 20.00},
            {"description": "Product 2", "quantity": 1, "price": 15.00, "total": 15.00},
            {"description": "Product 3", "quantity": 3, "price": 7.50, "total": 22.50},
        ],
        "total_amount": 57.50
    }
    
    generate_receipt(receipt_info)
