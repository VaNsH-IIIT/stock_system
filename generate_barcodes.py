import barcode
from barcode.writer import ImageWriter

# Item names and assigned barcode numbers
items = {
    'Red': '100001',
    'Yellow': '100002',
    'Blue': '100003',
    'Green': '100004',
}

for name, code in items.items():
    barcode_class = barcode.get_barcode_class('code128')
    barcode_obj = barcode_class(code, writer=ImageWriter())
    filename = barcode_obj.save(f'{name}_barcode')  # Saves as Red_barcode.png, etc.
    print(f"Generated barcode for {name}: {filename}")
