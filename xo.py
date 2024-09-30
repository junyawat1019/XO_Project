import tkinter as tk
from tkinter import messagebox

#ฟังก์ชันในการตรวจสอบผู้ชนะ
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return buttons[row][0]['text']
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return buttons[0][col]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']
    return None

#ฟังก์ชันการคลิกปุ่ม
def on_click(row, col):
    if buttons[row][col]['text'] == "" and turn[0]:
        buttons[row][col]['text'] = "X" if turn[0] % 2 == 1 else "O"
        buttons[row][col]['fg'] = "deepskyblue" if turn[0] % 2 == 1 else "tomato"
        turn[0] += 1
        winner = check_winner() 
        if winner:
            update_score(winner)  #อัปเดตคะแนนเมื่อมีผู้ชนะ
            messagebox.showinfo("Result", f"Winner is {winner}!")
            reset_game()
        elif turn[0] == 10:
            messagebox.showinfo("Result", "Draw!")
            reset_game()

#ฟังก์ชันเพื่ออัปเดตคะแนน
def update_score(winner):
    if winner == "X":
        x_score[0] += 1
    elif winner == "O":
        o_score[0] += 1
    #แสดงคะแนนใหม่
    x_score_label.config(text=f"X : {x_score[0]}")
    I_score_label.config(text=f"|")
    o_score_label.config(text=f"O : {o_score[0]}")

#ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ""
    turn[0] = 1

#ฟังก์ชันรีเซ็ตคะแนน
def reset_score():
    x_score[0] = 0
    o_score[0] = 0
    #รีเซ็ตคะแนนแสดงผล
    x_score_label.config(text=f"X : {x_score[0]}")
    I_score_label.config(text=f"|")
    o_score_label.config(text=f"O : {o_score[0]}")

#หน้าต่างหลักของเกม
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry('480x750')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
root.resizable(False, False)
root.configure(bg='#2C2C2C')

#Label ชื่อเกม
title = tk.Label(root, text="Tic Tac Toe", font=('MN Khop Khun', 24), bg='#2C2C2C', fg="white")
title.grid(row=0, column=0, columnspan=3, pady=10)

#Label แสดงคะแนน
x_score = [0]  # คะแนนของ X
o_score = [0]  # คะแนนของ O
x_score_label = tk.Label(root, text=f"X : {x_score[0]}", font=('MN Khop Khun', 20), bg='#2C2C2C', fg="deepskyblue")
x_score_label.grid(row=1, column=0, columnspan=2, pady=10)
I_score_label = tk.Label(root, text=f"|", font=('MN Khop Khun', 20), bg='#2C2C2C', fg="white")
I_score_label.grid(row=1, column=1, columnspan=1, pady=10)
o_score_label = tk.Label(root, text=f"O : {o_score[0]}", font=('MN Khop Khun', 20), bg='#2C2C2C', fg="tomato")
o_score_label.grid(row=1, column=1, columnspan=2, pady=10)

#ตารางปุ่มสำหรับเกม
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('Arial', 36), width=5, height=2, bg="#3C3F41", fg="white",
                                      relief="flat", activebackground="#3C3F41", activeforeground="white",
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row+2, column=col, padx=5, pady=5)

#ปุ่มสำหรับเริ่มเกมใหม่
reset_button = tk.Button(root, text="Reset Game", font=('MN Khop Khun', 18), command=reset_game, bg="#2C2C2C", fg="white",
                         relief="flat", activebackground="#2C2C2C", activeforeground="white")
reset_button.grid(row=5, column=1, columnspan=3, pady=20)

# มสำหรับรีเซ็ตคะแนน
reset_score_button = tk.Button(root, text="Reset Score", font=('MN Khop Khun', 18), command=reset_score, bg="#2C2C2C", fg="white",
                                relief="flat", activebackground="#2C2C2C", activeforeground="white")
reset_score_button.grid(row=5, column=0, columnspan=2, pady=10)

#ตัวแปรสำหรับตรวจจับตาเดิน
turn = [1] 
#เริ่มเกม
root.mainloop()
