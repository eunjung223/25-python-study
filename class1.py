class Menu:
    def __init__(self):
        # 전체 메뉴를 저장할 딕셔너리
        # 구조 예: { "커피": {"가격": 3000, "재고": 10}, "라떼": {...} }
        self.orderList = {}

        # 전체 매출액 저장 변수
        self.total = 0

        # cafe.txt 파일을 읽어서 메뉴 정보를 orderList에 저장
        with open("cafe.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()              # 줄 끝 개행 제거
                if not line:                    # 빈 줄은 무시
                    continue
                name, price, stock = line.split(":")   # 형식: 메뉴:가격:재고
                self.orderList[name] = {               # 딕셔너리 형태로 저장
                    "가격": int(price),
                    "재고": int(stock)
                }

    # -----------------------------
    # 새로운 메뉴를 추가하는 기능
    # -----------------------------
    def addMenu(self):
        name = input("추가할 메뉴 이름을 입력하세요: ")
        price = int(input("메뉴 가격을 입력하세요: "))
        stock = int(input("초기 재고를 입력하세요: "))

        # 메모리에 추가
        self.orderList[name] = {
            "가격": price,
            "재고": stock
        }

        # cafe.txt 파일 마지막 줄에 append
        with open("cafe.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{name}:{price}:{stock}")

        print(f"'{name}' 메뉴가 추가되었습니다.")

    # -----------------------------
    # 메뉴판 출력 기능
    # -----------------------------
    def printMenu(self):
        print("--- Menu ---")
        menu_names = list(self.orderList.keys())      # 메뉴 이름 리스트 추출

        # 번호 붙여 출력
        for idx, name in enumerate(menu_names, start=1):
            info = self.orderList[name]
            print(f"{idx}. {name}: {info['가격']}원, 재고: {info['재고']}")
        print("---")

        return menu_names   # 메뉴 번호 선택용 리스트 반환


# -----------------------------------------
#  Order 클래스 : 주문 기능 담당
# -----------------------------------------

class Order:
    def __init__(self, menu: Menu):
        self.menu = menu        # Menu 객체 받아서 사용 (조합 방식)
        self.orderResult = {}   # 주문 결과 저장용 딕셔너리

    # -----------------------------
    # 주문 기능
    # -----------------------------
    def orderMenu(self):
        self.orderResult = {}   # 주문 초기화
        total_qty = 0           # 총 주문 개수
        total_price = 0         # 총 주문 금액

        while True:
            menu_names = self.menu.printMenu()   # 메뉴판 출력
            choice = input("주문할 메뉴 번호를 입력하세요 (종료: end): ")

            # 주문 종료
            if choice == "end":
                break

            # 번호 입력이 숫자가 아니면 오류 처리
            if not choice.isdigit():
                print("메뉴 번호는 숫자로 입력해주세요.")
                continue

            idx = int(choice)

            # 메뉴 번호 유효성 검사
            if not (1 <= idx <= len(menu_names)):
                print("존재하지 않는 메뉴입니다.")
                continue

            # 선택한 메뉴명
            menu_name = menu_names[idx - 1]
            info = self.menu.orderList[menu_name]

            # 주문 수량은 기본 1개로 설정
            qty = 1

            # 재고가 0일 경우 품절
            if info["재고"] == 0:
                print("품절되었습니다.")
                continue

            # 재고 부족 시 (ex: 한 번에 여러 개 주문으로 확장할 경우 대비)
            if info["재고"] < qty:
                print("수량이 부족합니다.")
                continue

            # 정상 주문 처리
            info["재고"] -= qty                     # 재고 감소
            price = info["가격"] * qty              # 주문 금액 계산
            total_qty += qty                        # 총 수량 증가
            total_price += price                    # 총 금액 증가
            self.menu.total += price                # 총 매출 증가

            # 주문 기록 저장
            self.orderResult[menu_name] = self.orderResult.get(menu_name, 0) + qty

        # 주문 종료 후 결과 출력
        print("---")
        print(f"총 주문 수량: {total_qty}개")
        print(f"총 주문 금액: {total_price}원")


# -----------------------------------------
#  Manage 클래스 : 재고 관리 + 매출 확인
# -----------------------------------------

class Manage:
    def __init__(self, menu: Menu):
        self.menu = menu

    # -----------------------------
    # 재고 추가 기능
    # -----------------------------
    def Management(self, menuNum=None):
        print("--- 재고 관리 ---")
        print("현재 재고 상태입니다.")

        while True:
            menu_names = self.menu.printMenu()   # 현재 재고 출력
            num = input("재고를 추가할 메뉴 번호를 입력하세요 (종료: end): ")

            # 종료
            if num == "end":
                print("재고 관리를 종료하고 메인 메뉴로 돌아갑니다.")
                break

            if not num.isdigit():
                print("메뉴 번호는 숫자로 입력해주세요.")
                continue

            idx = int(num)

            # 번호 범위 검사
            if not (1 <= idx <= len(menu_names)):
                print("존재하지 않는 메뉴입니다.")
                continue

            menu_name = menu_names[idx - 1]

            # 추가할 수량 입력
            qty_str = input("추가할 수량을 입력하세요: ")
            if not qty_str.isdigit():
                print("수량은 숫자로 입력해주세요.")
                continue

            qty = int(qty_str)

            # 재고 증가 처리
            self.menu.orderList[menu_name]["재고"] += qty
            print(f"'{menu_name}'의 재고가 {qty}개 추가되었습니다.")

    # -----------------------------
    # 총 매출 출력
    # -----------------------------
    def totalSale(self):
        print(f"총 매출액: {self.menu.total}원")


# -----------------------------------------
#  프로그램 전체 동작 (메인 루프)
# -----------------------------------------

def main():
    menu = Menu()               # 메뉴/재고 로드
    order_system = Order(menu)  # 주문 시스템 준비
    manager = Manage(menu)      # 재고·매출 관리 객체

    while True:
        print("\n원하는 작업을 선택하세요: [1. 주문 | 2. 재고 관리 | 3. 종료]")
        choice = input("> ")

        if choice == "1":
            order_system.orderMenu()     # 주문 기능 실행

        elif choice == "2":
            manager.Management()         # 재고 관리 실행
            check = input("총 매출액을 확인하시겠습니까? (y/n): ")
            if check.lower() == "y":
                manager.totalSale()      # 매출 확인

        elif choice == "3":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못 입력하셨습니다. 다시 선택해주세요.")


# -----------------------------------------
#  이 파일을 직접 실행할 때만 main() 실행됨
#  다른 파일에서 import 할 경우 자동 실행되지 않음
# -----------------------------------------
if __name__ == "__main__":
    main()

