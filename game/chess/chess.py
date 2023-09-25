import pygame, sys
from pygame.locals import*
# board = 왼쪽 24 빼야함, 위쪽 18 빼야함
# board size = 754 * 748
# cell = 93 * 93, 각 셀마다 1px 유격 있음
pygame.init()
pygame.display.set_caption("chess game") # 프로그램의 제목을 설정
screen = pygame.display.set_mode((800, 800)) # 프로그램의 사이즈 설정
chess_board_img = pygame.image.load("source/chess_board.png")
chess_board_img = pygame.transform.scale(chess_board_img, (800, 800))
w_pawn_img = pygame.image.load("source/w_pawn.png")
w_pawn_img = pygame.transform.scale(w_pawn_img, (61, 92))

while True:
    screen.blit(chess_board_img, (0, 0))
    screen.blit(w_pawn_img, (24, 110))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()