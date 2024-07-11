# from tkinter import *
# import random

# window = Tk() # 윈도우 객체 생성
# window.geometry("800x500") # 윈도우 크기
# window.title("슬라이딩 퍼즐 게임") # 제목 설정

# # 사진 변수
# photo1=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/1.gif'), 
# photo2=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/2.gif'),
# photo3=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/3.gif'),
# photo4=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/4.gif'),
# photo5=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/5.gif'),
# photo6=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/6.gif'),
# photo7=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/7.gif'),
# photo8=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/8.gif'),
# photo9=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/9.gif'),
# photo10=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/10.gif'),
# photo11=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/11.gif'),
# photo12=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/12.gif'),
# photo13=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/13.gif'),
# photo14=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/14.gif'),
# photo15=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/15.gif'),
# photo16=PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/16.gif')


# def button1_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==1:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==1: # p1가 1번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button1.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button2_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==2:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==2: # p1가 2번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button2.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button3_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==3:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==3: # p1가 3번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button3.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button4_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==4:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==4: # p1가 4번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button4.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button5_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==5:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==5: # p1가 5번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button5.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button6_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==6:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==6: # p1가 6번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button6.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button7_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==7:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==7: # p1가 7번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button7.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button8_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==8:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==8: # p1가 8번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button8.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button9_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==9:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==9: # p1가 9번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button9.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button10_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==10:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==10: # p1가 10번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button10.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button11_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==11:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==11: # p1가 11번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button11.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button12_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==12:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==12: # p1가 12번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button12.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button13_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==13:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==13: # p1가 13번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button13.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return 

# def button14_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==14:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==14: # p1가 14번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button14.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return    

# def button15_move():
#     for em in xylist:
#         if em[0]==16: # 16번째 버튼(공백)의 위치 파악
#             em_x=em[1] # 16번째 버튼의 x좌표
#             em_y=em[2] # 16번째 버튼의 y좌표

#     for bt in xylist:
#        if bt[0]==15:
#            if (bt[1]-125 == em_x and bt[2]== em_y) or (bt[1]+125 == em_x and bt[2]== em_y) or (bt[1] == em_x and bt[2]-125 == em_y) or (bt[1] == em_x and bt[2]+125 == em_y): # 상하좌우에 16번째 버튼이 있는지 확인
#                for p1 in range(16):
#                    if xylist[p1][0]==15: # p1가 15번째 버튼
#                        for p16 in range(16):
#                            if xylist[p16][0]==16: # p2가 16번째 버튼
#                                xylist[p1][0], xylist[p16][0] = xylist[p16][0], xylist[p1][0]  # 버튼 좌표 둘이 교환

#                                button15.place(x=xylist[p16][1], y=xylist[p16][2])
#                                button16.place(x=xylist[p1][1], y=xylist[p1][2])

#                                return                                           

# placelist=[[150,0],[275,0],[400,0],[525,0],[150,125],[275,125],[400,125],[525,125],[150,250],[275,250],[400,250],[525,250],[150,375],[275,375],[400,375],[525,375]] # 15x15 좌표
# # 1 2 3 4
# # 5 6 7 8
# # 9 10 11 12
# # 13 14 15 16

# numlist=[] # 숫자 저장 리스트
# xylist=[] # 버튼 좌표 리스트

# for x in range(16): # 숫자 16개 뽑기
#     num=(random.randint(0, 15)) 
#     while num in numlist: # 중복 없이 숫자를 뽑을 수 있도록 확인
#         num=(random.randint(0, 15)) # 중복이라면 다시 뽑기
#     numlist.append(num)
#     xylist.append([x+1, placelist[int(numlist[x])][0], placelist[int(numlist[x])][1]])



# # newlist=['']*16

# # for n in numlist:
# #     for i , j in zip(list(range(16)), numlist):
# #         newlist[j]=i
# #         xylist.append([j+1, placelist[int(newlist[j])][0], placelist[int(newlist[j])][1]])
# # print(newlist)

# # 슬라이딩 퍼즐 게임 해결 알고리즘? → numlist에 저장된 값을 가지고 아래 여부를 판단
# # 랜덤으로 뽑은 값을 가지고 클리어가 가능한지 판단 (클리어가 불가능한 구조가 존재)
# # 최소 이동 횟수를 정해서 운좋게 게임이 빨리 끝나지 않도록 함
# # 전제에 만족하지 않으면 다시 뽑기! / 만족하면 게임 시작


# # 버튼 16개 생성
# button1 = Button(window, image=photo1, command=button1_move)
# button2 = Button(window, image=photo2, command=button2_move)
# button3 = Button(window, image=photo3, command=button3_move)
# button4 = Button(window, image=photo4, command=button4_move)
# button5 = Button(window, image=photo5, command=button5_move)
# button6 = Button(window, image=photo6, command=button6_move)
# button7 = Button(window, image=photo7, command=button7_move)
# button8 = Button(window, image=photo8, command=button8_move)
# button9 = Button(window, image=photo9, command=button9_move)
# button10 = Button(window, image=photo10, command=button10_move)
# button11 = Button(window, image=photo11, command=button11_move)
# button12 = Button(window, image=photo12, command=button12_move)
# button13 = Button(window, image=photo13, command=button13_move)
# button14 = Button(window, image=photo14, command=button14_move)
# button15 = Button(window, image=photo15, command=button15_move)
# button16 = Button(window, image=photo16)

# print(xylist)
# print(numlist)

# # 16개 버튼 좌표 랜덤 부여
# button1.place(x=xylist[0][1], y=xylist[0][2])
# button2.place(x=xylist[1][1], y=xylist[1][2])
# button3.place(x=xylist[2][1], y=xylist[2][2])
# button4.place(x=xylist[3][1], y=xylist[3][2])
# button5.place(x=xylist[4][1], y=xylist[4][2])
# button6.place(x=xylist[5][1], y=xylist[5][2])
# button7.place(x=xylist[6][1], y=xylist[6][2])
# button8.place(x=xylist[7][1], y=xylist[7][2])
# button9.place(x=xylist[8][1], y=xylist[8][2])
# button10.place(x=xylist[9][1], y=xylist[9][2])
# button11.place(x=xylist[10][1], y=xylist[10][2])
# button12.place(x=xylist[11][1], y=xylist[11][2])
# button13.place(x=xylist[12][1], y=xylist[12][2])
# button14.place(x=xylist[13][1], y=xylist[13][2])
# button15.place(x=xylist[14][1], y=xylist[14][2])
# button16.place(x=xylist[15][1], y=xylist[15][2])

# if xylist[0][0]==(numlist[0]+1) and xylist[1][0]==(numlist[1]+1) and xylist[2][0]==(numlist[2]+1) and xylist[3][0]==(numlist[3]+1) and xylist[4][0]==(numlist[4]+1) and xylist[5][0]==(numlist[5]+1) and xylist[6][0]==(numlist[6]+1) and xylist[7][0]==(numlist[7]+1) and xylist[8][0]==(numlist[8]+1) and xylist[9][0]==(numlist[9]+1) and xylist[10][0]==(numlist[10]+1) and xylist[11][0]==(numlist[11]+1) and xylist[12][0]==(numlist[12]+1) and xylist[13][0]==(numlist[13]+1) and xylist[14][0]==(numlist[14]+1) and xylist[15][0]==(numlist[15]+1) :
#     quit_button = Button(window, text='게임 클리어!', command=quit)

# # (150,000) (275,000) (400,000) (525,000)
# # (150,125) (275,125) (400,125) (525,125)
# # (150,250) (275,250) (400,250) (525,250)
# # (150,375) (275,375) (400,375) (525,375)

# window.mainloop() # 마우스 클릭 이벤트 처리