class ProductManager:
    product = ['สบู่บำรุงผิวหน้า', 'สบู่บำรุงผิวกาย', 'สบู่คอลลาเจน', 'เซรั่มบำรุงผิวหน้า']
    price = 0
    number_product = 0
    
        
    def __init__(self,select_product,number_product) -> None:
        self.number_product = number_product
        if  select_product == 1:
            self.price = number_product * 80
        if select_product == 2:
            self.price = number_product * 50
        if select_product == 3:
            self.price = number_product * 100
        if select_product == 4:
            self.price = number_product * 150
        
    