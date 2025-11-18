'''
## 🥑 실습 체크리스트: 나만의 책(Book) 클래스 만들기
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"제목: {self.title}, 저자: {self.author}")


book1 = Book("일반수학2", "김인덕")
book2 = Book("의사소통 영어", "박비룡")

book1.display_info()
book2.display_info()

'''
## 🚀 미션: 카페 프로그램 만들기
'''
class Menu:
    def __init__(self):
        self.orderList = {}   # 메뉴 저장할 딕셔너리
        self.total = 0
        # 1) cafe.txt 파일 열기
        with open("cafe.txt", "r", encoding="utf-8") as f:
            # 2) 한 줄씩 읽어서 파싱
            for line in f:
                name, price, stock = line.strip().split(":")

                # 3) 딕셔너리에 저장
                self.orderList[name] = {
                    "가격": int(price),
                    "재고": int(stock)
                }
    def addMenu(self):
        name = input("추가할 메뉴 이름: ")
        price = int(input("가격: "))
        stock = int(input("재고: "))

        # 딕셔너리에도 반영
        self.orderList[name] = {"가격": price, "재고": stock}

        # cafe.txt 파일에 한 줄 추가
        with open("cafe.txt", "a", encoding="utf-8") as f:
            f.write(f"{name}:{price}:{stock}\n")

        print(f"{name} 메뉴가 추가되었습니다.")

    def printMenu(self):
        print("-- Menu --")
        # 번호 붙여서 출력
        for idx, (name, info) in enumerate(self.orderList.items(), start=1):
            print(f"{idx}. {name}: {info['가격']}원, 재고: {info['재고']}")

class Order(Menu):
    def __init__(self):
        self.orderResult = {}
    def orderMenu(self,menuNum):
        self.menuNum = menuNum
        print(Menu.printMenu)
        for i in range(self.orderList[idx]):
            if i:
                print("존재하지 않는 메뉴입니다.")
                break;
            if

