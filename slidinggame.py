import pygame, sys, random, threading, traceback
from time import *
from pygame.locals import *
from solve3 import Solutions
from crop import crop

BOARDSIZE = 4 # 보드 크기
TILESIZE = 100 # 타일 크기 
WINDOWWIDTH = 800 # 창 너비
WINDOWHEIGHT = 500 # 창 높이
FPS = 30 # 초당 프레임 수 (속도)

#               R    G    B
BLACK =      (  0,   0,   0)
WHITE =      (255, 255, 255)
GOLD =       (255, 191,   0)
BRIGHTGOLD = (255, 220, 115)
DARKGOLD =   (166, 124,   0)
BEIGE =      (248, 233, 200)

BACKGROUND_COLOR = BEIGE # 배경 색
TILE_COLOR = BLACK # 타일 색
TEXT_COLOR = BRIGHTGOLD # 텍스트 색
EDGE_COLOR = DARKGOLD # 타일 테두리 색
FONTSIZE = 30 # 폰트 크기?

BUTTONCOLOR = GOLD # 버튼 색
BUTTONTEXTCOLOR = BLACK # 버튼 텍스트 색
MESSAGECOLOR = BLACK # 메세지 색

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDSIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDSIZE)) / 2)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def start_game():
    DISPLAYSURF.fill(BACKGROUND_COLOR) # 배경화면 색 지정
    menu = Menu() # 메뉴 클래스
    run_game(menu) 

def run_game(menu):
    board = Board() # 보드 클래스
    #timer = Timer(1, make_timetext)
    nums = range(70, 80)
    shuffle_num = random.choice(nums) # 70~80 숫자 랜덤 뽑기
    print('num =', shuffle_num)
    board.shuffle(shuffle_num, menu)

    while True:
        if board.is_solved(): # 해결되었는가?
            menu.show_msg('solve') # 해결됨
        else:
            menu.show_msg('running') # 게임중
            #threading.Thread(target=lambda: timer.every_time(1, timer.make_text)).start()
            #timer()


        check_for_quit()
        for e in pygame.event.get():
            if e.type == MOUSEBUTTONUP: # 마우스 버튼 클릭 판단
                tile = board.get_tile(e.pos)
                if tile:
                    board.find_move(tile)
                else:
                    menu.check_rect(e.pos, board)
            elif e.type == KEYUP: # 방향키 판단
                    board.check_key(e.key)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()


def check_for_quit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

class Title(object):
    def __init__(self):
        DISPLAYSURF.fill(BACKGROUND_COLOR)
        self.font = pygame.font.Font('PFStardust.otf', 20)
        self.titlefont = pygame.font.Font('PFStardust.otf', 80)

    def draw_titlemenu(self):
        self.start_rect = self.make_menutext(' 게임 시작 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 150)
        self.memo_rect = self. make_menutext(' 기록 보기 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 120)
        self.quit_rect = self.make_menutext(' 게임 종료 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 450, WINDOWHEIGHT - 90)
        self.make_title(' 슬라이딩 퍼즐 게임 ', BLACK, BACKGROUND_COLOR, WINDOWWIDTH - 760, WINDOWHEIGHT - 350)
        

    def make_menutext(self, text, color, bgcolor, top, left): # 텍스트 출력
        surf = self.font.render(text, True, color, bgcolor)
        rect = surf.get_rect()
        rect.topleft = (top, left)
        DISPLAYSURF.blit(surf, rect) # 배경에 출력
        pygame.display.update()
        return rect

    def make_title(self, text, color, bgcolor, top, left):
        surf = self.titlefont.render(text, True, color, bgcolor)
        rect = surf.get_rect()
        rect.topleft = (top, left)
        DISPLAYSURF.blit(surf, rect)
        pygame.display.update()

    def check_rect(self, pos): # 메뉴가 선택되면 실행
        if self.start_rect.collidepoint(pos): # 어떤 메뉴가 선택되었는지 찾기 위함
            start_game()
        #elif self.meno_rect.collidepoint(pos):
           # return 2 # 게임 기록
        elif self.quit_rect.collidepoint(pos):
            pygame.QUIT() # 게임 종료

class Tile(object):
    def __init__(self, id, coord):
        self.id = id # 타일 번호
        self.coord = coord # 타일 좌표

        global img_num

        img_num, self.tile_img = crop(BOARDSIZE)


        for x in range(15):
            #self.tile_img.append(pygame.image.load(fr"C:\Users\asm96\Documents\python\sliding_puzzle\puzzle_image\picture01_{x+1}.jpg"))
            #self.tile_img = self.tile_img.resize((100, 10), self.tile_img[x+1])
            #self.tile_img[x] = pygame.transform.scale(self.tile_img[x], (100, 100))

            mode = self.tile_img[x].mode
            size = self.tile_img[x].size
            data = self.tile_img[x].tobytes()
            py_image = pygame.image.fromstring(data, size, mode)
            self.tile_img[x] = pygame.transform.scale(py_image, (100, 100))
        
            

    def move(self, direction, speed): # 방향, 속도 변수
        x, y = self.coord # 좌표
        for s in range(0, TILESIZE, speed): # 0~100까지 이동(한칸이동) speed로 속도 조절
            self.move_tile(x, y, s, direction) 
            pygame.display.update()
            FPSCLOCK.tick(FPS)
        self.move_tile(x, y, TILESIZE + 1, direction)

    def move_tile(self, x, y, distance, direction):
        dx, dy = direction
        self.draw_tile(x + dx, y + dy, BACKGROUND_COLOR)
        self.coord = (x + distance * dx, y + distance * dy) # 좌표는 기존 x + 거리*이동방향
        self.draw()
        pygame.display.update()

    def draw(self):
        self.draw_tile(self.coord[0], self.coord[1], TILE_COLOR)
        self.draw_img(self.tile_img)
        #self.draw_text()

    def draw_tile(self, x, y, color):
        pygame.draw.rect(DISPLAYSURF, color, (x, y, TILESIZE, TILESIZE)) # x,y좌표에 100*100크기의 타일 그리기

    def draw_text(self):
        font = pygame.font.Font('PFStardust.otf', 35)
        surf = font.render(str(self.id), True, TEXT_COLOR)
        rect = surf.get_rect()
        x, y = self.coord
        rect.center = (x + TILESIZE // 2, y + TILESIZE // 2)
        DISPLAYSURF.blit(surf, rect)

    def is_me(self, pos):
        x, y = self.coord
        rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
        return rect.collidepoint(pos)

    def draw_img(self, img):
        rect = img[self.id - 1].get_rect()
        x, y = self.coord
        rect.center = (x + TILESIZE // 2, y + TILESIZE // 2)
        DISPLAYSURF.blit(img[self.id - 1], rect)
        #pygame.display.flip()

class Board(object):
    def __init__(self):
        self.tiles = []
        self.game_moves = []
        self.shuffle_moves = []
        self.make_tiles()
        self.board = self.make_board()
        self.solved = self.make_board()
        self.draw_board()
        self.blank = self.board[BOARDSIZE - 1][BOARDSIZE - 1] # blank[3][3]

    def ida_star(self):
        pass
    
    def is_solved(self): # 해결되었는가?
        return self.board == self.solved
        

    def make_tiles(self): # 타일 생성
        for i in range(BOARDSIZE * BOARDSIZE - 1): # 0~15까지 반복
            x = XMARGIN + (i % BOARDSIZE) * (TILESIZE + 1) # x=400/2 + (0~3)*101    1은 타일끼리 띄어있기 위함
            y = YMARGIN + (i // BOARDSIZE) * (TILESIZE + 1)
            coord = (x, y) # x,y 좌표
            self.tiles.append(Tile(i + 1, coord))
        coord = (x + TILESIZE + 1, y)
        self.tiles.append(Tile(0, coord))

    def make_board(self):
        board = []
        for y in range(BOARDSIZE):
            row = []
            for x in range(BOARDSIZE):
                tile = self.tiles[y * BOARDSIZE + x]
                row.append(tile)
            board.append(row)
        return board
 
    def draw_board(self):
        for boards in self.board:
            for tile in boards:
                if tile.id:
                    tile.draw()
        self.draw_border()
        pygame.display.update()
        pygame.time.wait(500)

    def draw_border(self):
        x = XMARGIN - 5
        y = YMARGIN - 5
        size = TILESIZE * BOARDSIZE + 11
        pygame.draw.rect(DISPLAYSURF, EDGE_COLOR, (x, y, size, size), 4)

    def get_tile(self, pos):
        for boards in self.board:
            for tile in boards:
                if tile.is_me(pos):
                    return tile
        return None

    def get_board_index(self, coord):
        x, y = coord
        x = (x - XMARGIN) // (TILESIZE + 1)
        y = (y - YMARGIN) // (TILESIZE + 1)

        return (x, y)

    def is_tile(self, tile, direction):
        x, y = self.get_board_index(tile.coord)
        x += direction[0]
        y += direction[1]

        return ((x >= 0 and x < BOARDSIZE) and (y >= 0 and y < BOARDSIZE))

    def get_movable_tile(self, direction):
        x, y = self.get_board_index(self.blank.coord)
        x += direction[0]
        y += direction[1]

        return self.board[y][x]

    def get_valid_move(self, tile):
        moves = [UP, DOWN, LEFT, RIGHT]

        for i in range(len(moves) - 1, -1, -1):
            if not self.is_tile(tile, moves[i]):
                moves.remove(moves[i])

        return moves

    def get_random_move(self, last_move, tile):
        moves = self.get_valid_move(tile)
        if last_move:
            moves.remove(last_move)

        return random.choice(moves)

    def move_tile(self, tile, direction, speed):
        x, y = self.get_board_index(tile.coord)
        dx, dy = direction
        coord = tile.coord
        tile.move(direction, speed)
        self.board[y][x], self.board[y + dy][x + dx] = self.board[y + dy][x + dx], self.board[y][x]
        self.blank = self.board[y][x]
        self.blank.coord = coord

    def shuffle(self, nums, msg):
        msg.show_msg('shuffle')
        last_move = None
        for i in range(nums):
            check_for_quit()
            valid_move = self.get_random_move(last_move, self.blank)
            tile = self.get_movable_tile(valid_move)
            last_move = (valid_move[0] * -1, valid_move[1] * -1)
            self.call_move(tile, last_move, self.shuffle_moves, TILESIZE // 3)

    def find_move(self, tile):
        moves = self.get_valid_move(tile)
        x, y = self.get_board_index(tile.coord)
        for move in moves:
            if self.board[y + move[1]][x + move[0]] == self.blank:
                self.call_move(self.board[y][x], move, self.game_moves, TILESIZE // 5)

    def check_key(self, key):
        event = {K_UP: UP, K_DOWN: DOWN, K_LEFT: LEFT, K_RIGHT: RIGHT, K_w: UP, K_s: DOWN, K_a: LEFT, K_d: RIGHT}
        if key in event.keys():
            move = event[key]
            r_move = (move[0] * -1, move[1] * -1)
            if self.is_tile(self.blank, r_move):
                tile = self.get_movable_tile(r_move)
                self.call_move(tile, move, self.game_moves, TILESIZE // 5)

    def call_move(self, tile, move, move_list, speed):
        move_list.append(move)
        self.move_tile(tile, move, speed)

    def reset_board(self): # 다시 시작 → 플레이어의 실행 결과 반대로
        self.game_moves.reverse()

        for move in self.game_moves:
            check_for_quit()
            tile = self.get_movable_tile(move)
            r_move = (move[0] * -1, move[1] * -1)
            self.move_tile(tile, r_move, TILESIZE // 2)
        self.game_moves.clear()

    def sol_puzzle(self, moves, menu):
        menu.show_msg('solving')
        for move in moves:
            x, y = self.get_board_index(self.blank.coord)
            r_move = (move[0] * -1, move[1] * -1)
            tile = self.board[y + move[1]][x + move[0]]
            self.move_tile(tile, r_move, TILESIZE // 5)
            pygame.time.wait(5)
            
    def print_board(self):        
        for boards in self.board:
            for tile in boards:
                print(tile.id, end=' ')
            print()

    def solve(self, menu):
        menu.show_msg('search')
        pygame.display.update()
        sol = Solutions(len(self.board[0]), self.board)
        print('A START ALGORITHM')
        self.print_board()
        sol_moves = sol.get_solution('A_STAR')

        print()
        print('\nIDA STAR ALGORITHM')
        self.print_board()
        # sol_moves = sol.get_solution('BFS')
        sol.set_game(len(self.board[0]), self.board)
        sol_moves = sol.get_solution('IDA_STAR')
        if sol_moves:
            self.sol_puzzle(sol_moves, menu)
        else:
            print('Solved or not found!!!')
                        
        # self.game_moves = self.shuffle_moves + self.game_moves
        # self.reset_board()
        # self.shuffle_moves.clear()

class Menu(object):
    def __init__(self):
        self.font = pygame.font.Font('PFStardust.otf', 20)
        self.menu_img = []
         
        for x in range(4):
             self.menu_img.append(pygame.image.load(f"C:/Users/cwyi6/OneDrive/문서/python/sliding_puzzle/puzzle_image/menu{x+1}.png"))
        self.draw_menu()

    def draw_menu(self): # 메뉴 설정
        self.new_rect = self.make_img(self.menu_img[0], WINDOWHEIGHT + 160, WINDOWHEIGHT - 180)
        self.reset_rect = self.make_img(self.menu_img[1], WINDOWHEIGHT + 160, WINDOWHEIGHT - 300)
        self.solve_rect = self.make_img(self.menu_img[2], WINDOWHEIGHT + 160, WINDOWHEIGHT - 420)
        self.hint_rect = self.make_text(' 힌트 ', TEXT_COLOR, BLACK, WINDOWWIDTH - 730, WINDOWHEIGHT - 250)
        #self.reset_rect = self.make_text(' 다시 시작 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)
        #self.new_rect = self.make_text(' 새로 시작 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
        #self.solve_rect = self.make_text(' 해결하기 ', TEXT_COLOR, TILE_COLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    def show_msg(self, msg_id):
        msg = {
            'shuffle': '퍼즐을 섞는 중                                           ',
            'running': '마우스 클릭이나 방향키를 사용                             ',
            'solve': '클리어!                                                   ',
            'solving': '해결중                                                  ',
            'search': '해결방법을 탐색중                                         ',
            'reset': '다시시작                                                  '
        }
        self.make_text(msg[msg_id], MESSAGECOLOR, BACKGROUND_COLOR, 5, 5)

    def make_text(self, text, color, bgcolor, top, left): # 텍스트 출력s
        surf = self.font.render(text, True, color, bgcolor)
        rect = surf.get_rect()
        rect.topleft = (top, left)
        DISPLAYSURF.blit(surf, rect) # 배경에 출력
        return rect

    def make_img(self, img, top, left): # 이미지 출력
        rect = img.get_rect()
        rect.topleft = (top, left)
        DISPLAYSURF.blit(img, rect)
        return rect

    def show_hint(self):
        img = pygame.image.load(f"C:/Users/cwyi6/OneDrive/문서/python/sliding_puzzle/puzzle_image/picture{img_num}.jpg")
        img = pygame.transform.scale(img, (100, 100))
        rect = img.get_rect()
        rect.topleft = (WINDOWWIDTH - 752, WINDOWHEIGHT - 200)
        DISPLAYSURF.blit(img, rect)
        #for x in range(3):            
            #nrect = self.make_text(f'{3-x}', BLACK, BACKGROUND_COLOR, WINDOWWIDTH - 720, WINDOWHEIGHT - 270)
        #sleep(1)
        #self.hide_hint()
    
    def hide_hint(self):
        back_img = pygame.image.load(f'C:/Users/cwyi6/OneDrive/문서/python/sliding_puzzle/puzzle_image/background.png')
        back_img = pygame.transform.scale(back_img, (100, 100))
        rect = back_img.get_rect()
        rect.topleft = (WINDOWWIDTH - 755, WINDOWHEIGHT - 200)
        DISPLAYSURF.blit(back_img, rect)

    def check_rect(self, pos, board): # 메뉴가 선택되면 실행
        if self.reset_rect.collidepoint(pos): # 어떤 메뉴가 선택되었는지 찾기 위함
            self.show_msg('reset') # 다시 시작
            board.reset_board() # 명령 수행을 위함
        elif self.new_rect.collidepoint(pos):
            run_game(self) # 새로 시작
        elif self.solve_rect.collidepoint(pos):
            board.solve(self) # 해결하기
        elif self.hint_rect.collidepoint(pos):
            self.show_hint()

class Timer(object):
    def __init__(self, interval, function):
        self.font = pygame.font.Font('PFStardust.otf', 30)
        self.minute = 00
        self.second = 00
        self.timer = None
        self.interval = interval
        self.function = function
        self.is_running = False
        self.start()

    def run(self):
        self.is_running = False
        self.start()
        self.function()
    
    def start(self):
        if not self.is_running:
            self.timer = threading(self.interval, self.run)
            self.timer.start()
            self.is_running = True

    def stop(self):
        self.timer.cancel()
        self.is_running = False

    #def every_time(delay, task):
        #next_time = time.time() + delay
        #while True:
            #time.sleep(max(0, next_time - time.time()))
            #try:
                #task()
            #except Exception:
                #traceback.print_exc()
            #next_time += (time.time() - next_time)

    def show_time(self, text, color, bgcolor, top, left): # 텍스트 출력
        surf = self.font.render(text, True, color, bgcolor)
        rect = surf.get_rect()
        rect.topleft = (top, left)
        DISPLAYSURF.blit(surf, rect) # 배경에 출력

    def make_text(self):
        self.second +=1
        if self.second >= 60:
            self.show_time(f'   :    ', BLACK, BACKGROUND_COLOR, WINDOWWIDTH - 765, WINDOWHEIGHT - 400)
            self.second = 00
            self.minute += 1
        print(self.second)
        self.show_time(f' {self.minute} : {self.second} ', BLACK, BACKGROUND_COLOR, WINDOWWIDTH - 765, WINDOWHEIGHT - 400)

    def save_time(self):
        ...

def main():
    global FPSCLOCK, DISPLAYSURF # 프레임 속도, 화면

    pygame.init()
    FPSCLOCK = pygame.time.Clock() # 프레임 속도
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # 파이게임 창
    pygame.display.set_caption('Slide Puzzle') # 창 제목

    title = Title()
    title.draw_titlemenu()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP: # 마우스 버튼 클릭 판단
                title.check_rect(event.pos)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)



if __name__ == '__main__':
    main()

