import tkinter as tk
from tkinter import messagebox
import sys


# -----------------------------------------------------------
# class 이름: Coffee
# (요청하신 Coffee 클래스의 속성과 로직을 GUI 클래스에 통합)
# -----------------------------------------------------------
class CoffeeMachine:

    def __init__(self, root):
        self.root = root
        self.root.title("커피 자판기")
        self.root.geometry("440x420")  # 윈도우 크기 지정
        self.root.resizable(False, False)  # 크기 조절 방지

        # -----------------------------------------------
        # 1) 속성(Properties)
        # -----------------------------------------------
        # 자판기 초기 상태 (제한 사항)
        self.total_amount = 10  # 총 커피 개수 (10개)
        self.total_amount_price = 5000  # 자판기 보유 총 금액 (5000원)
        self.coffee_price = 300  # 커피 한개 가격 (300원)

        # --- GUI와 연동될 변수들 ---
        # [입력]
        self.money_var = tk.StringVar()
        self.coffee_var = tk.StringVar()

        # [출력]
        self.change_var = tk.StringVar()  # 거스름 돈
        self.provided_var = tk.StringVar()  # 제공된 커피 개수

        # [상황창]
        self.status_var = tk.StringVar()

        # --- GUI 위젯 생성 ---
        self.create_widgets()

        # --- 초기 상태 업데이트 ---
        self.update_status(f"자판기 준비 완료 (커피: {self.coffee_price}원)")

    def create_widgets(self):
        """GUI의 레이아웃과 위젯을 생성합니다."""

        # --- [입력] 프레임 ---
        # LabelFrame: 위젯을 그룹화하고 제목을 표시
        frame_input = tk.LabelFrame(self.root, text="[입력]", padx=10, pady=10, font=("", 10, "bold"))
        frame_input.pack(padx=10, pady=10, fill="x")

        # grid 레이아웃 사용 (행/열 기준 정렬)
        tk.Label(frame_input, text="돈 입력 (원):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        entry_money = tk.Entry(frame_input, textvariable=self.money_var, width=18)
        entry_money.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="커피 개수 (잔):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        entry_coffee = tk.Entry(frame_input, textvariable=self.coffee_var, width=18)
        entry_coffee.grid(row=1, column=1, padx=5, pady=5)

        # '주문하기' 버튼
        # command=self.order_coffee : 버튼 클릭 시 order_coffee 메소드 실행
        btn_order = tk.Button(frame_input, text="주문하기",
                              font=("", 10, "bold"),
                              bg="#8B0000", fg="white",  # 이미지의 붉은색 버튼
                              width=8, height=2,
                              command=self.order_coffee)  # 2) requtest() + get() 메소드 역할
        btn_order.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="ns")

        # --- [출력] 프레임 ---
        frame_output = tk.LabelFrame(self.root, text="[출력]", padx=10, pady=10, font=("", 10, "bold"))
        frame_output.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_output, text="거스름돈 (원):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        # state="readonly": 사용자가 수정 불가, 코드로는 수정 가능
        entry_change = tk.Entry(frame_output, textvariable=self.change_var, state="readonly", width=25)
        entry_change.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_output, text="커피 제공 (잔):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        entry_provided = tk.Entry(frame_output, textvariable=self.provided_var, state="readonly", width=25)
        entry_provided.grid(row=1, column=1, padx=5, pady=5)

        # --- [상황창] 프레임 ---
        frame_status = tk.LabelFrame(self.root, text="[상황창]", padx=10, pady=10, font=("", 10, "bold"))
        frame_status.pack(padx=10, pady=10, fill="x")

        # justify="left": 텍스트 왼쪽 정렬, anchor="nw": 북서(North-West)쪽 정렬
        lbl_status = tk.Label(frame_status, textvariable=self.status_var,
                              justify="left", anchor="nw", height=3,
                              font=("", 9))
        lbl_status.pack(padx=5, pady=5, fill="x")

    # -----------------------------------------------
    # 2) 메소드(Method) - 핵심 동작 로직
    # -----------------------------------------------
    def order_coffee(self):
        """'주문하기' 버튼 클릭 시 실행되는 메인 로직입니다."""

        # A. 입력 값 가져오기 및 검증 (숫자인지 확인)
        try:
            put_price = int(self.money_var.get())
            req_coffee_nums = int(self.coffee_var.get())
        except ValueError:
            messagebox.showerror("입력 오류", "돈과 커피 개수는 숫자로 입력해야 합니다.")
            return  # 로직 중단

        if put_price <= 0 or req_coffee_nums <= 0:
            messagebox.showwarning("입력 오류", "0보다 큰 값을 입력해야 합니다.")
            return  # 로직 중단

        # B. 필요한 총 금액 계산
        total_needed_price = req_coffee_nums * self.coffee_price

        # C. [출력] 창 우선 초기화
        self.provided_var.set("0")
        self.change_var.set(str(put_price))  # 실패 시 전액 반환이 기본

        # D. 3) 동작 정의 (로직 실행)
        result_msg = ""

        # 3) 돈을 불충분하게 넣은 경우
        if put_price < total_needed_price:
            result_msg = f"금액 부족. (필요: {total_needed_price}원, 투입: {put_price}원)"
            messagebox.showwarning("주문 실패", result_msg)

        # 3) 돈은 충분하나, 재고가 부족한 경우
        elif req_coffee_nums > self.total_amount:
            result_msg = f"커피 재고 부족. (잔여: {self.total_amount}잔)"
            messagebox.showwarning("주문 실패", result_msg)

        # 1), 2) 돈과 재고가 모두 충분한 경우 (성공)
        else:
            # (속성) remaining_price, remaining_coffee_nums 계산
            change = put_price - total_needed_price
            provided_coffee = req_coffee_nums

            # 자판기 상태 업데이트 (속성 변경)
            self.total_amount -= provided_coffee  # 커피 재고 차감
            self.total_amount_price += total_needed_price  # 자판기 금액 증가

            # [출력] GUI 업데이트
            self.provided_var.set(str(provided_coffee))
            self.change_var.set(str(change))

            # 성공 메시지
            result_msg = f"커피 {provided_coffee}잔 제공 / 거스름돈 {change}원"
            messagebox.showinfo("주문 완료", result_msg)

        # E. 최종 상황창 업데이트 (info() / check_amount() 역할)
        self.update_status(result_msg)

        # F. [입력] 창 초기화
        self.money_var.set("")
        self.coffee_var.set("")

    def update_status(self, result_msg):
        """2) info() / check_amount() 메소드의 역할: 상황창 GUI를 업데이트합니다."""

        # 현재 재고/금액 확인
        stock_msg = f"잔여 커피: {self.total_amount}잔 / 잔여 금액: {self.total_amount_price}원"

        # 이미지의 '체크박스' 모양을 흉내내기 위해 특수문자 사용
        if "실패" in result_msg or "부족" in result_msg:
            # ❌ (U+274C)
            self.status_var.set(f"❌ {result_msg}\n{stock_msg}")
        elif "완료" in result_msg:
            # ☑ (U+2611) - 이미지와 동일한 체크박스
            self.status_var.set(f"☑ {result_msg}\n{stock_msg}")
        else:
            # 준비 메시지 (초기 상태)
            self.status_var.set(f"▶ {result_msg}\n{stock_msg}")


# --- 메인 코드 실행 ---
if __name__ == "__main__":
    # 1. 메인 윈도우 생성
    root = tk.Tk()

    # 2. 윈도우에 CoffeeMachine 클래스 애플리케이션 생성
    app = CoffeeMachine(root)

    # 3. 윈도우 실행 (사용자가 닫을 때까지)
    root.mainloop()