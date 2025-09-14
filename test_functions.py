def calculate_vat(price, vat_rate=20):
    vat_ammount = price * vat_rate / 100
    total_price = price + vat_ammount
    return vat_ammount


product_price = float(input("Enter product price:"))
vat = calculate_vat(product_price)
print("Vat ammount =", vat)
