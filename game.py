# from tkinter import *

# window = Tk() # 윈도우 객체 생성
# window.geometry("800x500") # 윈도우 크기
# window.title("슬라이딩 퍼즐 게임") # 제목 설정

# # 사진 리스트
# photo=[PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/1.gif'), 
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/2.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/3.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/4.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/5.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/6.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/7.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/8.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/9.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/10.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/11.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/12.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/13.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/14.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/15.gif'),
# PhotoImage(file='C:/Users/asm96/Documents/python/sliding_puzzle/puzzle_image/16.gif')]

# button=[] # 버튼 리스트

# for x in range(16):
#     button.append(Button(window, image=photo[x])) # 버튼 리스트에 사진 삽입 


# xylst=[[150,0],[275,0],[400,0],[525,0],[150,125],[275,125],[400,125],[525,125],[150,250],[275,250],[400,250],[525,250],[150,375],[275,375],[400,375],[525,375]] # 15x15 좌표


# for a in range(16):
#     button[x].place(x=xylst[a][0], y=[a][1]) # 첫번째 버튼을 첫번째 위치에 놓기 ex) button[1]=(x=150, y=0)



# window.mainloop() # 마우스 클릭 이벤트 처리


# class Over(object):
#     def __init__(self):
#         DISPLAYSURF.fill(BACKGROUND_COLOR)
#         self.font = pygame.font.Font('PFStardust.otf', 20)
#         self.titlefont = pygame.font.Font('PFStardust.otf', 80)

#     def draw_titlemenu(self):
#         #self.restart_rect = self.make_menutext(' 다시 시작 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 150)
#         self.newstart_rect = self. make_menutext(' 새로 시작 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 150)
#         self.title_rect = self.make_menutext(' 메인화면으로 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 120)
#         self.make_title(' 게임 클리어! ', BLACK, BACKGROUND_COLOR, WINDOWWIDTH - 760, WINDOWHEIGHT - 350)
        

#     def make_menutext(self, text, color, bgcolor, top, left): # 텍스트 출력
#         surf = self.font.render(text, True, color, bgcolor)
#         rect = surf.get_rect()
#         rect.topleft = (top, left)
#         DISPLAYSURF.blit(surf, rect) # 배경에 출력
#         pygame.display.update()
#         return rect

#     def make_title(self, text, color, bgcolor, top, left):
#         surf = self.titlefont.render(text, True, color, bgcolor)
#         rect = surf.get_rect()
#         rect.topleft = (top, left)
#         DISPLAYSURF.blit(surf, rect)
#         pygame.display.update()

#     def check_rect(self, pos): # 메뉴가 선택되면 실행
#         if self.newstart_rect.collidepoint(pos): # 어떤 메뉴가 선택되었는지 찾기 위함
#             start_game()
#         elif self.title_rect.collidepoint(pos):
#             main()