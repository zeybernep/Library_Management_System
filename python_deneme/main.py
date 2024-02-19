class Library:
    def __init__(self):
      
        self.file = open("books.txt", "a+")

    def __del__(self):
        
        self.file.close()

    def list_books(self):
        
        self.file.seek(0)  
        books = self.file.read().splitlines()
        for book in books:
            book_info = book.split(",")
            print(f"Kitap Adı: {book_info[0]}, Yazar: {book_info[1]}")
       

    def add_book(self):
        
        name = input("Kitap adı: ")
        author = input("Yazar: ")
        release_year = input("İlk yayın yılı: ")
        pages = input("Sayfa sayısı: ")
        self.file.write(f"{name},{author},{release_year},{pages}\n")
        

    def remove_book(self):
    
        remove_title = input("Çıkarılacak kitap adı: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        books = [book for book in books if not book.startswith(remove_title)]
        self.file.close()  
        with open("books.txt", "w") as f:
            pass
    
        self.file = open("books.txt", "a+")
        self.file.seek(0)  
        for book in books:
            self.file.write(f"{book}\n")
        self.file.seek(0) 
        pass


    def search_books(self,criteria,value):
        self.file.seek(0)
        books = self.file.read().splitlines()
        found_books = []

    def search_books(self, criteria, value):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        found_books = []  

        for book in books:
            book_details = book.split(",")
            book_name = book_details[0].strip().lower()
            author_name = book_details[1].strip().lower()
            release_year = book_details[2].strip()
            pages = book_details[3].strip()

            if criteria == "isim" and value.lower() in book_name:
                found_books.append(book)
            elif criteria == "yazar" and value.lower() in author_name:
                found_books.append(book)
            elif criteria == "yil":
                try:
                    if int(release_year) == int(value):
                        found_books.append(book)
                except ValueError:
                    print("Yıl için geçersiz bir değer girildi.")
            elif criteria == "sayfa":
                try:
                    if int(pages) == int(value):
                        found_books.append(book)
                except ValueError:
                    print("Sayfa sayısı için geçersiz bir değer girildi.")

        if found_books:
            print("\nArama Sonuçları:")
            for book in found_books:
                print(book)
        else:
            print("Arama kriterlerine uygun kitap bulunamadı.")

def main():

    lib = Library()

# Menü
    while True:
        print("*** MENÜ ***")
        print("1) Kitapları Listele")
        print("2) Kitap Ekle")
        print("3) Kitap Çıkar")
        print("4) Arama yap")
        print("5) Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
         lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            criteria = input("Arama kriterini girin (isim, yazar, yıl,sayfa): ")
            value = input(f"{criteria.capitalize()} için arama değerini girin: ")
            lib.search_books(criteria, value)
        elif choice == "5":
            break    
        else:
            print("Geçersiz seçim.")
if __name__ == "__main__":
    main()