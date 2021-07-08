import win32console, win32con, time

import sys
import os

import key_capture

class Board:
    def __init__(self, m, n, h, state=None):
        self.rows=m
        self.cols=n
        self.H = h
        self.board = [0]*m
        self.control = 0
        self.h_locations = [0] * self.H
        self.nums = [str(i) for i in range(self.H)]
        self.parity = 0

        self.hWnd = win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)

        self.keyc = key_capture.KeyCapture()

        self.board_list = []
        self.h_locations_list = []


        for i in range(m):
            self.board[i] = [0] * n
        
        if state == None:
            for i in range(m):
                for j in range(n):
                    if (i+j)%2==1-self.parity:
                        self.board[i][j] = 'X'
                    else:
                        self.board[i][j] = ' '
            h_count = self.H-1
            i_pointer = 0
            j_pointer = 0
            while h_count >= 0:
                if self.board[i_pointer][j_pointer] == ' ' and (i_pointer + j_pointer)%2 == self.parity:
                    self.board[i_pointer][j_pointer] = str(h_count)
                    self.h_locations[h_count] = [i_pointer, j_pointer]
                    h_count -= 1
                else:
                    if i_pointer < self.rows - 1:
                        i_pointer+=1
                    else:
                        if j_pointer < self.cols - 1:
                            j_pointer += 1
                        else:
                            print('wtf')
                            exit()

            self.board_list.append(copy_2(self.board))
            self.h_locations_list.append(copy_2(self.h_locations))

            self.parity = 1 - self.parity




    def update_board(self):
        return


    def move(self):
        board_copy = [0] * self.rows
        state_count = 0
        for i in range(self.rows):
            board_copy[i] = [' '] * self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'X':
                    board_copy[i][j] = ' '
                elif self.board[i][j] in self.nums:
                    board_copy[i][j] = ' '
                else:
                    if i > 0 and self.board[i-1][j] == 'X':
                        state_count += 1
                        board_copy[i][j] = 'X'
                    if j > 0 and self.board[i][j-1] == 'X':
                        state_count += 1
                        board_copy[i][j] = 'X'
                    if i < self.rows-1 and self.board[i+1][j] == 'X':
                        state_count += 1
                        board_copy[i][j] = 'X'
                    if j < self.cols-1 and self.board[i][j+1] == 'X':
                        state_count += 1
                        board_copy[i][j] = 'X'
        
        if state_count == 0:
            print('################')
            print('################')
            print('YOU DID IT')
            print('################')
            print('################')
            exit()


        self.board = board_copy




        
        h_count = self.H-1
        i_pointer = 0
        j_pointer = 0
        while h_count >= 0:
            if self.board[i_pointer][j_pointer] == ' ' and (i_pointer + j_pointer)%2 == self.parity:
                self.board[i_pointer][j_pointer] = str(h_count)
                self.h_locations[h_count] = [i_pointer, j_pointer]
                h_count -= 1
            else:
                if i_pointer < self.rows - 1:
                    i_pointer+=1
                else:
                    if j_pointer < self.cols - 1:
                        j_pointer += 1
                    else:
                        print('wtf')
                        exit()
        self.parity = 1 - self.parity



        self.board_list.append(copy_2(self.board))
        self.h_locations_list.append(copy_2(self.h_locations))


    def reverse(self):
        self.board_list.pop()
        self.h_locations_list.pop()
        if len(self.board_list) == 0:
            self.__init__(self.rows, self.cols, self.H)
            return
        
        self.board = self.board_list[-1]
        self.h_locations = self.h_locations_list[-1]
        self.parity = 1 - self.parity
        return

        
                



    def grid(self):
        """version with string concatenation"""
        sep = '\n' + '+---'*self.cols + '+\n'
        
        return sep + "".join(["".join(['| ' + self.board[row][col] + ' ' for col in range(self.cols)]) + '|' + sep for row in range(self.rows)])








    def display(self):
        os.system('cls')
        print(self.grid())




        

    def turn(self):
        self.display()
        key_press = None
        while key_press not in ['ESC']:

            

            x = self.keyc.input()
            
            if x == 'ESC':
                exit()

            if x in self.nums:
                print(x)
                self.control = int(x)

            if x == 'U':
                i, j = self.h_locations[self.control]
                if i >= 1:
                    if j >= 1:                    
                        self.h_locations[self.control][0] -= 1
                        self.h_locations[self.control][1] -= 1
                        swap(self.board, (i,j), (i-1,j-1))
                    elif j <= self.cols-2:                    
                        self.h_locations[self.control][0] -= 1
                        self.h_locations[self.control][1] += 1
                        swap(self.board, (i,j), (i-1,j+1))
            
            
            if x == 'D':
                i, j = self.h_locations[self.control]
                if i <= self.rows-2:
                    if j <= self.cols-2:                    
                        self.h_locations[self.control][0] += 1
                        self.h_locations[self.control][1] += 1
                        swap(self.board, (i,j), (i+1,j+1))
                    elif j >= 1:                    
                        self.h_locations[self.control][0] += 1
                        self.h_locations[self.control][1] -= 1
                        swap(self.board, (i,j), (i+1,j-1))


            if x == 'L':
                i, j = self.h_locations[self.control]
                if j >= 2:
                    self.h_locations[self.control][1] -= 2
                    swap(self.board, (i,j), (i,j-2))

            if x == 'R':
                i, j = self.h_locations[self.control]
                if j <= self.cols-3:
                    self.h_locations[self.control][1] += 2
                    swap(self.board, (i,j), (i,j+2))



            if x == 'DEL':
                self.reverse()


            if x == 'GO':
                self.move()



            self.update_board()
            self.display()
        exit()
        return


    def start(self):
        cleared = False
        while cleared==False:
            self.turn()





def swap(l, ind1, ind2):
    temp = l[ind1[0]][ind1[1]]
    l[ind1[0]][ind1[1]] = l[ind2[0]][ind2[1]]
    l[ind2[0]][ind2[1]] = temp

def copy_2(l):
    l2 = [0] * len(l)
    for i in range(len(l)):
        l2[i] = l[i].copy()
    return l2


print('Number of Rows of Board = :')
rows_num = int(input())

print('Number of Columns of Board = :')
cols_num = int(input())

print('H, Number of Holes = :')
h_num = int(input())


board = Board(rows_num, cols_num, h_num)

os.system('cls')

board.start()

