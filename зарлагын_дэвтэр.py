
ANGILAL = ["hool", "transport", "delguur", "busad"]


ANGILAL = ["hool", "transport", "delguur", "busad"]


def Зардал_нэмэх():
    while True:
        category = input(
            "Ангилал (hool / transport / delguur / busad), гарах бол stop: "
        ).strip().lower()

        if category == "stop":
            return

        if category not in ANGILAL:
            print("Ангилал зөвхөн:", ", ".join(ANGILAL))
            continue

        item = input("Барааны нэр, үнэ (жишээ: талх 3000): ").strip()
        parts = item.split()

        if len(parts) != 2:
            print("Нэр болон үнээ оруулна уу. Жишээ: талх 3000")
            continue

        name = parts[0]
        amount = parts[1]

     

        with open("Зардал.txt", "a", encoding="utf-8") as file:
            file.write(f"{category} - {name} - {int(amount)}\n")

        print("===== Нэмэгдлээ:", name, amount)
        
def Зардал_харах():
    with open("Зардал.txt", "r") as file:
      aguulga = file.read()
    
      return aguulga

def Нийлбэр_авах():
    with open("Зардал.txt", "r") as file:
      total = 0

      for baraaune in file:
        parts = baraaune.strip().split(" - ")
        amount = int(parts[2])
        total += amount
        
    return total

def category_total():
      with open("Зардал.txt", "r") as file:
        totals = {}

        for baraaune in file:

         if baraaune.strip() == "":
          continue

         parts = baraaune.strip().split(" - ")

         category = parts[0]
         amount = int(parts[2])

         if category in totals:
          totals[category] += amount

         else:
          totals[category] = amount

      return totals

def Хамгийн_их_зарлага():
    amounts = []
    
    with open("Зардал.txt", "r") as file:
        for baraaune in file:
            parts = baraaune.strip().split("-")
            
            name = parts[1].strip()
            amount = int(parts[2])
            amounts.append((amount, name))
            
    return max(amounts)    

def Хамгийн_бага_зарлага():
    amounts = []
    
    with open("Зардал.txt", "r") as file:
        for baraaune in file:
            parts = baraaune.strip().split("-")
            
            name = parts[1].strip()
            amount = int(parts[2])
            amounts.append((amount, name))
            
    return min(amounts)    

def Зардал_цэвэрлэх():
    Батлах = input("===== Бүх зардал устгах уу? yes/no: ")
    
    if Батлах == "yes":
        with open("Зардал.txt", "w") as file:
            pass
        
        return "===== Бүх зарлага устлаа"
    
    else:
        return "===== Цуцлагдлаа"

def Нийт_зарлагын_тоо():
    Зарлага = []
    
    with open("Зардал.txt", "r") as file:
        for baraaune in file:
                Зарлага.append(baraaune)
                
    return len(Зарлага)


while True:
    print("\n1. Зарлага нэмэх")
    print("2. Зарлага харах")
    print("3. EXIT")
    print("4. Нийт дүн")
    print("5. Ангилал тус бүрийн нийт")
    print("6. Хамгийн их зарлага")
    print("7. Хамгийн бага зарлага")
    print("8. Бүх зардал цэвэрлэх")
    print("9. Нийт зарлагын тоо")

    choice = input("Сонголт=====>>>: ")

    if choice == "1":
        Зардал_нэмэх()

    elif choice == "2":
        print(Зардал_харах())

    elif choice == "3":
        break

    elif choice == "4":
        print("===== Нийт дүн:", Нийлбэр_авах())

    elif choice == "5":
      result = category_total()

      for category, total in result.items():
        print("===== Ангилал тус бүрийн нийт:", category, "-", total)
        
    elif choice == "6":
        print("===== Хамгийн их зарлага:", Хамгийн_их_зарлага())
        
    elif choice == "7":
        print("===== Хамгийн бага зарлага:", Хамгийн_бага_зарлага())
        
    elif choice == "8":
        print(Зардал_цэвэрлэх())
        
    elif choice == "9":
        print("===== Нийт зарлагын тоо", Нийт_зарлагын_тоо())