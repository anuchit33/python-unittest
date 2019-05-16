

class Tictactoe():
    player = ['O','X']
    def play(self):
        grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        p = 1
        while(True):
            position = 1
            for i in range(0,3):
                s = '|'
                for j in range(0,3):
                    s += str(position if grid[i][j]==0 else  self.player[grid[i][j]-1])
                    s += ' | '
                    position +=1
                print('%s \n ------------' %s)
            position = int(input("%s Enter coin one = " %(self.player[p-1])))
            _position = 1
            for i in range(0,3):
                for j in range(0,3):
                    if _position == position :
                        if grid[i][j] == 0:
                            grid[i][j] = p
                        else:
                            print('You can not select positohn : %s' % position)
                            p = 1 if p == 2 else 2
                    _position += 1
            res = self.getStatus(grid)
            if res != 'Runing':
                print(res)
                break
            p = 1 if p == 2 else 2

    def getStatus(self,grid):
        status = ''
        # backslash
        if grid[0][0] != 0 and grid[1][1] == grid[0][0] and grid[0][0] == grid[2][2]:
            status = self.player[grid[0][0]-1]
        # slash
        if grid[0][2] != 0 and grid[1][1] == grid[0][2] and grid[0][2] == grid[2][0]:
            status = self.player[grid[0][2]-1]

        # row
        for i in range(0,3):
            if grid[i][0] != 0 and grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2]:
                status = self.player[grid[i][0]-1]
                break
        # colum
        for i in range(0,3):
            if grid[0][i] != 0 and grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i]:
                status = self.player[grid[0][i]-1]
                break

        if status == '':
            is_stop = True
            for i in range(0,3):
                for j in range(0,3):
                    if grid[i][j] == 0:
                        is_stop = False
            if is_stop:
                return 'Always'
        if status == '':
            return 'Runing'
        else:
            return "%s is Winner!" % (status)

if __name__ == "__main__":

    Tictactoe().play()