class Player2:
	def __init__(self):
		permitted_blocks_dict = {'58': [(1, 2), (2, 1)], '30': [(0, 1), (1, 0)], '81': [(2, 0), (2, 2)], '54': [(2, 0), (2, 2)], '42': [(0, 2), (2, 2)], '48': [(0, 2), (2, 2)], '50': [(1, 0), (2, 1)], '60': [(0, 1), (1, 0)], '61': [(0, 0), (0, 2)], '62': [(0, 1), (1, 2)], '57': [(2, 0), (2, 2)], '64': [(0, 0), (0, 2)], '53': [(1, 0), (2, 1)], '66': [(0, 1), (1, 0)], '67': [(0, 0), (0, 2)], '68': [(0, 1), (1, 2)], '83': [(1, 0), (2, 1)], '80': [(1, 0), (2, 1)], '52': [(1, 2), (2, 1)], '86': [(1, 0), (2, 1)], '87': [(2, 0), (2, 2)], '84': [(2, 0), (2, 2)], '85': [(1, 2), (2, 1)], '02': [(0, 1), (1, 2)], '03': [(0, 1), (1, 0)], '00': [(0, 1), (1, 0)], '01': [(0, 0), (0, 2)], '06': [(0, 1), (1, 0)], '07': [(0, 0), (0, 2)], '04': [(0, 0), (0, 2)], '05': [(0, 1), (1, 2)], '46': [(0, 0), (2, 0)], '47': [(1, 1)], '08': [(0, 1), (1, 2)], '45': [(0, 2), (2, 2)], '28': [(1, 2), (2, 1)], '43': [(0, 0), (2, 0)], '40': [(0, 0), (2, 0)], '41': [(1, 1)], '82': [(1, 2), (2, 1)], '14': [(1, 1)], '78': [(0, 2), (2, 2)], '51': [(2, 0), (2, 2)], '24': [(2, 0), (2, 2)], '56': [(1, 0), (2, 1)], '25': [(1, 2), (2, 1)], '26': [(1, 0), (2, 1)], '77': [(1, 1)], '76': [(0, 0), (2, 0)], '75': [(0, 2), (2, 2)], '27': [(2, 0), (2, 2)], '73': [(0, 0), (2, 0)], '72': [(0, 2), (2, 2)], '71': [(1, 1)], '70': [(0, 0), (2, 0)], '20': [(1, 0), (2, 1)], '38': [(0, 1), (1, 2)], '74': [(1, 1)], '21': [(2, 0), (2, 2)], '11': [(1, 1)], '10': [(0, 0), (2, 0)], '13': [(0, 0), (2, 0)], '12': [(0, 2), (2, 2)], '15': [(0, 2), (2, 2)], '22': [(1, 2), (2, 1)], '17': [(1, 1)], '16': [(0, 0), (2, 0)], '33': [(0, 1), (1, 0)], '18': [(0, 2), (2, 2)], '31': [(0, 0), (0, 2)], '23': [(1, 0), (2, 1)], '37': [(0, 0), (0, 2)], '36': [(0, 1), (1, 0)], '35': [(0, 1), (1, 2)], '34': [(0, 0), (0, 2)], '55': [(1, 2), (2, 1)], '63': [(0, 1), (1, 0)], '88': [(1, 2), (2, 1)], '32': [(0, 1), (1, 2)], '44': [(1, 1)], '65': [(0, 1), (1, 2)]}
		# permitted_cells = 
		unavailable_blocks = []
		all_blocks = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
	def move(self, temp_board, temp_block, old_move, flag):
		permitted_blocks_dict = {'58': [(1, 2), (2, 1)], '30': [(0, 1), (1, 0)], '81': [(2, 0), (2, 2)], '54': [(2, 0), (2, 2)], '42': [(0, 2), (2, 2)], '48': [(0, 2), (2, 2)], '50': [(1, 0), (2, 1)], '60': [(0, 1), (1, 0)], '61': [(0, 0), (0, 2)], '62': [(0, 1), (1, 2)], '57': [(2, 0), (2, 2)], '64': [(0, 0), (0, 2)], '53': [(1, 0), (2, 1)], '66': [(0, 1), (1, 0)], '67': [(0, 0), (0, 2)], '68': [(0, 1), (1, 2)], '83': [(1, 0), (2, 1)], '80': [(1, 0), (2, 1)], '52': [(1, 2), (2, 1)], '86': [(1, 0), (2, 1)], '87': [(2, 0), (2, 2)], '84': [(2, 0), (2, 2)], '85': [(1, 2), (2, 1)], '02': [(0, 1), (1, 2)], '03': [(0, 1), (1, 0)], '00': [(0, 1), (1, 0)], '01': [(0, 0), (0, 2)], '06': [(0, 1), (1, 0)], '07': [(0, 0), (0, 2)], '04': [(0, 0), (0, 2)], '05': [(0, 1), (1, 2)], '46': [(0, 0), (2, 0)], '47': [(1, 1)], '08': [(0, 1), (1, 2)], '45': [(0, 2), (2, 2)], '28': [(1, 2), (2, 1)], '43': [(0, 0), (2, 0)], '40': [(0, 0), (2, 0)], '41': [(1, 1)], '82': [(1, 2), (2, 1)], '14': [(1, 1)], '78': [(0, 2), (2, 2)], '51': [(2, 0), (2, 2)], '24': [(2, 0), (2, 2)], '56': [(1, 0), (2, 1)], '25': [(1, 2), (2, 1)], '26': [(1, 0), (2, 1)], '77': [(1, 1)], '76': [(0, 0), (2, 0)], '75': [(0, 2), (2, 2)], '27': [(2, 0), (2, 2)], '73': [(0, 0), (2, 0)], '72': [(0, 2), (2, 2)], '71': [(1, 1)], '70': [(0, 0), (2, 0)], '20': [(1, 0), (2, 1)], '38': [(0, 1), (1, 2)], '74': [(1, 1)], '21': [(2, 0), (2, 2)], '11': [(1, 1)], '10': [(0, 0), (2, 0)], '13': [(0, 0), (2, 0)], '12': [(0, 2), (2, 2)], '15': [(0, 2), (2, 2)], '22': [(1, 2), (2, 1)], '17': [(1, 1)], '16': [(0, 0), (2, 0)], '33': [(0, 1), (1, 0)], '18': [(0, 2), (2, 2)], '31': [(0, 0), (0, 2)], '23': [(1, 0), (2, 1)], '37': [(0, 0), (0, 2)], '36': [(0, 1), (1, 0)], '35': [(0, 1), (1, 2)], '34': [(0, 0), (0, 2)], '55': [(1, 2), (2, 1)], '63': [(0, 1), (1, 0)], '88': [(1, 2), (2, 1)], '32': [(0, 1), (1, 2)], '44': [(1, 1)], '65': [(0, 1), (1, 2)]}
		if old_move == (-1,-1):
			return (4,4)
		print "previous move was: ", old_move
		board = copy.deepcopy(temp_board)
		permitted_cells = self.getPermittedCells(board,old_move,flag,permitted_blocks_dict)
		length = len(permitted_cells)
		move = permitted_cells[random.randrange(length)]
		print "move will be made: ", move
		print "board at this move is: ",board[move[0]][move[1]]
		return move

	
	def getPermittedCells(self,temp_board,old_move, flag,permitted_blocks_dict):
		
		all_blocks = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
		permitted_blocks = permitted_blocks_dict["%d%d" %(old_move[0],old_move[1])]
		print "permitted blocks by norm are: ", permitted_blocks
		permitted_cells = []
		pb = copy.deepcopy(permitted_blocks)
		for block in pb:
			blockCheck = self.checkBlockValidity(block,temp_board)
			if blockCheck == False:
				print "remove block ", block
				permitted_blocks.remove(block)
				
		if permitted_blocks == []:
			print "2 blocks full"
			permitted_blocks = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
		# permitted_blocks = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

		print "after all blocks added: ",permitted_blocks
		
		pb = copy.deepcopy(permitted_blocks)
		for block in pb:
			blockCheck = self.checkBlockValidity(block,temp_board)
			if blockCheck == False:
				permitted_blocks.remove(block)

		print "move will be made in block: ", permitted_blocks
			
		permitted_cells = self.getCellsForBlock(permitted_blocks)
		print "cells for given block are: ", permitted_cells
		pc = copy.deepcopy(permitted_cells)
		for cell in pc:
			if temp_board[cell[0]][cell[1]] !='-':
				permitted_cells.remove(cell)
		print "valid cells are: ",permitted_cells
		return permitted_cells



	def getCellsForBlock(self,blocks):
		permitted_cells = []
		for block in blocks:
			x = block[0]
			y = block[1]
			for i in range(3*x, 3*x + 3):
				for j in range(3*y, 3*y + 3):
					permitted_cells.append((i,j))
		return permitted_cells


	

	def checkBlockValidity(self,block,board):
		x = block[0]
		y = block[1]
		flag = 0
		if board[3*x][3*y] == board[3*x][3*y + 1] and board[3*x][3*y + 1] == board[3*x][3*y + 2] and board[3*x][3*y] != '-':
				flag = 1
				return False
		elif board[3*x + 1][3*y] == board[3*x + 1][3*y + 1] and board[3*x + 1][3*y + 1] == board[3*x + 1][3*y + 2] and board[3*x + 1][3*y] != '-':
			flag = 1
			return False
		elif board[3*x + 2][3*y] == board[3*x + 2][3*y + 1] and board[3*x + 2][3*y + 1] == board[3*x + 2][3*y + 2] and board[3*x + 2][3*y] != '-':
			flag = 1
			return False
		elif board[3*x][3*y] == board[3*x + 1][3*y] and board[3*x + 1][3*y] == board[3*x + 2][3*y] and board[3*x][3*y] != '-':
			flag = 1
			return False
		elif board[3*x][3*y + 1] == board[3*x + 1][3*y + 1] and board[3*x + 1][3*y + 1] == board[3*x + 2][3*y + 1] and board[3*x][3*y + 1] != '-':
			flag = 1
			return False
		elif board[3*x][3*y + 2] == board[3*x + 1][3*y + 2] and board[3*x + 1][3*y + 2] == board[3*x + 2][3*y + 2] and board[3*x][3*y + 2] != '-':
			flag = 1
			return False
		elif board[3*x][3*y] == board[3*x + 1][3*y + 1] and board[3*x + 1][3*y + 1] == board[3*x + 2][3*y + 2] and board[3*x][3*y] != '-':
			flag = 1
			return False
		elif board[3*x][3*y + 2] == board[3*x + 1][3*y + 1] and board[3*x + 1][3*y + 1] == board[3*x + 2][3*y] and board[3*x][3*y + 2] != '-':
			flag = 1
			return False
		flag2 = 0
		for i in range(3*x,3*x + 3):
			if flag2 != 1:
				for j in range(3*y, 3*y + 3):
					if board[i][j] == '-':
						flag2 = 1
						break
		if flag == 0 and flag2 == 1:
			return True
		return False



	def generateHeuristic(self,board,move,flag):
		x = move[0]
		y = move[1]
		
		value = 0.0
		probability = 0.0
		
		myflag = flag
		oppflag = 'x'
		if flag == 'x':
			oppflag = 'o'

		
		for j in range(3*y,3*y+3):
			if probability != 1 and probability != -1:
				if board[3*x][j]==oppflag and board[3*x+1][j]=='-' and board[3*x+2][j]=='-':
					value -= 1
				elif board[3*x][j]=='-' and board[3*x+1][j]==oppflag and board[3*x+2][j]=='-':
					value -= 1
				elif board[3*x][j]=='-' and board[3*x+1][j]=='-' and board[3*x+2][j]==oppflag:
					value -= 1
				elif board[3*x][j]==oppflag and board[3*x+1][j]==oppflag and board[3*x+2][j]=='-':
					value -= 10
				elif board[3*x][j]==oppflag and board[3*x+1][j]=='-' and board[3*x+2][j]==oppflag:
					value -= 10
				elif board[3*x][j]=='-' and board[3*x+1][j]==oppflag and board[3*x+2][j]==oppflag:
					value -= 10
				elif board[3*x][j]==oppflag and board[3*x+1][j]==oppflag and board[3*x+2][j]==oppflag:
					probability = -1
					break
				elif board[3*x][j]==myflag and board[3*x+1][j]=='-' and board[3*x+2][j]=='-':
					value += 1
				elif board[3*x][j]=='-' and board[3*x+1][j]==myflag and board[3*x+2][j]=='-':
					value += 1
				elif board[3*x][j]=='-' and board[3*x+1][j]=='-' and board[3*x+2][j]==myflag:
					value += 1
				elif board[3*x][j]==myflag and board[3*x+1][j]==myflag and board[3*x+2][j]=='-':
					value += 10
				elif board[3*x][j]==myflag and board[3*x+1][j]=='-' and board[3*x+2][j]==myflag:
					value += 10
				elif board[3*x][j]=='-' and board[3*x+1][j]==myflag and board[3*x+2][j]==myflag:
					value += 10
				elif board[3*x][j]==myflag and board[3*x+1][j]==myflag and board[3*x+2][j]==myflag:
					probability = 1
					break
		
		for i in range(3*x,3*x+3):
			if probability != 1 and probability != -1:
				if board[i][3*y]==oppflag and board[i][3*y+1]=='-' and board[i][3*y+2]=='-':
					value -= 1
				elif board[i][3*y]=='-' and board[i][3*y+1]==oppflag and board[i][3*y+2]=='-':
					value -= 1
				elif board[i][3*y]=='-' and board[i][3*y+1]=='-' and board[i][3*y+2]==oppflag:
					value -= 1
				elif board[i][3*y]==oppflag and board[i][3*y+1]==oppflag and board[i][3*y+2]=='-':
					value -= 10
				elif board[i][3*y]==oppflag and board[i][3*y+1]=='-' and board[i][3*y+2]==oppflag:
					value -= 10
				elif board[i][3*y]=='-' and board[i][3*y+1]==oppflag and board[i][3*y+2]==oppflag:
					value -= 10
				elif board[i][3*y]==oppflag and board[i][3*y+1]==oppflag and board[i][3*y+2]==oppflag:
					probability = -1
					break
				elif board[i][3*y]==myflag and board[i][3*y+1]=='-' and board[i][3*y+2]=='-':
					value += 1
				elif board[i][3*y]=='-' and board[i][3*y+1]==myflag and board[i][3*y+2]=='-':
					value += 1
				elif board[i][3*y]=='-' and board[i][3*y+1]=='-' and board[i][3*y+2]==myflag:
					value += 1
				elif board[i][3*y]==myflag and board[i][3*y+1]==myflag and board[i][3*y+2]=='-':
					value += 10
				elif board[i][3*y]==myflag and board[i][3*y+1]=='-' and board[i][3*y+2]==myflag:
					value += 10
				elif board[i][3*y]=='-' and board[i][3*y+1]==myflag and board[i][3*y+2]==myflag:
					value += 10
				elif board[i][3*y]==myflag and board[i][3*y+1]==myflag and board[i][3*y+2]==myflag:
					probability = 1
					break


		
		if probability != 1 and probability != -1:
			if board[3*x][3*y+2] == oppflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == '-':
				value -= 1
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y] == '-':
				value -= 1
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == oppflag:
				value -= 1
			elif board[3*x][3*y+2] == oppflag and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y] == '-':
				value -= 10
			elif board[3*x][3*y+2] == oppflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == oppflag:
				value -= 10
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y] == oppflag:
				value -= 10
			elif board[3*x][3*y+2] == oppflag and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y] == oppflag:
				probability = -1
			elif board[3*x][3*y+2] == myflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == '-':
				value += 1
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y] == '-':
				value += 1
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == myflag:
				value += 1
			elif board[3*x][3*y+2] == myflag and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y] == '-':
				value += 10
			elif board[3*x][3*y+2] == myflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y] == myflag:
				value += 10
			elif board[3*x][3*y+2] == '-' and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y] == myflag:
				value += 10
			elif board[3*x][3*y+2] == myflag and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y] == myflag:
				probability = 1
		

			if probability != 1 and probability != -1:
			if board[3*x][3*y] == oppflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == '-':
				value -= 1
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y+2] == '-':
				value -= 1
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == oppflag:
				value -= 1
			elif board[3*x][3*y] == oppflag and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y+2] == '-':
				value -= 10
			elif board[3*x][3*y] == oppflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == oppflag:
				value -= 10
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y+2] == oppflag:
				value -= 10
			elif board[3*x][3*y] == oppflag and board[3*x+1][3*y+1] == oppflag and board[3*x+2][3*y+2] == oppflag:
				probability = -1
			elif board[3*x][3*y] == myflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == '-':
				value += 1
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y+2] == '-':
				value += 1
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == myflag:
				value += 1
			elif board[3*x][3*y] == myflag and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y+2] == '-':
				value += 10
			elif board[3*x][3*y] == myflag and board[3*x+1][3*y+1] == '-' and board[3*x+2][3*y+2] == myflag:
				value += 10
			elif board[3*x][3*y] == '-' and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y+2] == myflag:
				value += 10
			elif board[3*x][3*y] == myflag and board[3*x+1][3*y+1] == myflag and board[3*x+2][3*y+2] == myflag:
				probability = 1


		if probability != 1 and probability != -1:
			probability = (float(value))/100
		return probability