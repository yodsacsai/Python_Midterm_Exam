from ProductManager import ProductManager
from SentManager import SentManager


print("=============================")
print("          รายการสินค้า        ")
print("=============================")
print("1. สบู่บำรุงผิวหน้า     80 บาท/ชิ้น")
print("2. สบู่บำรุงผิวกาย     50 บาท/ชิ้น")
print("3. สบู่คอลลาเจน     100 บาท/ชิ้น")
print("4. เซรั่มบำรุงผิวหน้า   150 บาท/ชิ้น")
print("=============================")
print("           การจัดส่ง        ")
print("1.พัสดุลงทะเบียน 20บาท")
print("2.EMS 50บาท")
print("=============================")
print("")
select_product = int(input("กรุณาเลือกสินค้า: "))
number_product = int(input("กรุณาระบุจำนวนการสั่งซื้อ: "))
select_sent = int(input("กรุณาเลือกวิธีจัดส่ง: "))
product = ProductManager(select_product,number_product)
sent = SentManager(select_sent)
print("")
print("=============================")
print("         สรุปการสั่งซื้อ          ")
print("=============================")
print("สินค้าที่สั่งซื้อ: ", product.product[select_product-1])
print("จำนวน: ", product.number_product)
print("การจัดส่ง: ", sent.mothod[select_sent-1])
print("=============================")
total = product.price + sent.price
print("รวมเป็นเงินทั้งสิ้น: ", str(total) + " บาท")
print("=============================")

