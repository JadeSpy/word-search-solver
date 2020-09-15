#Input
#["these", "areco","lumns","5lett","ers12"]=each string is a column, not a row! grid 
grid = []
for i in range(200):
	column = "a"*200
	grid.append(column)

answers_to_find = ["here", "comes", "johnny", "ceg", "these", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]



































#End input
answers_backwards = []
for answer in answers_to_find:
	answers_backwards.append(answer[::-1])
answers_found = []

def search_rows(grid, answer_list, answers_found):
	column = 0
	for row in grid:
		column+=1
		row_str = ""
		for char in row:
			row_str+=char
		for answer in answer_list:
			pos = row_str.find(answer)
			if(pos!=-1):
				answers_found.append([[pos,column],[pos+len(answer)-1,column]])
def search_columns(grid, answer_list, answers_found):
	column_len = len(grid)
	row_len = len(grid[0])
	for column in range(row_len):
		column_str = ""
		for row in range(column_len):
			column_str+=grid[row][column]
			for answer in answer_list:
				pos = column_str.lower().find(answer.lower())
				if(pos!=-1):
					answers_found.append([[column,pos],[column,pos+len(answer)-1]])
def search_diagonals(grid, answer_list, answers_found):
	#right and down
	x_base = 0
	x_base_end = len(grid[0])-1
	y_base = len(grid)
	while True:
		if(y_base>0):
			y_base-=1
		else:
			x_base+=1
			if(x_base>x_base_end):
				break
		x_change = 0
		y_change = 0
		diagonal_string = ""
		while True:
			x_pos = x_change+x_base
			y_pos = y_change+y_base
			if(x_pos>x_base_end or y_pos>len(grid)-1):
				for answer in answer_list:
					pos = diagonal_string.lower().find(answer.lower())
					if(pos!=-1):
						#sub string was found
						answers_found.append([[x_base+pos,y_base+pos], [x_base+(pos+len(answer)-1),y_base+(pos+len(answer)-1)]])
				break
			#reached end of diagonal
			diagonal_string+=grid[y_pos][x_pos]
			
			x_change+=1
			y_change+=1
	#left and down
	y_base = len(grid)
	x_base = len(grid[0])-1
	while True:
		if(y_base>0):
			y_base-=1
		else:
			x_base-=1
			if(x_base<0):
				break
		x_change = 0
		y_change = 0
		diagonal_string = ""
		while True:
			x_pos = x_change+x_base
			y_pos = y_change+y_base
			if(x_pos<0 or y_pos>len(grid)-1):
				for answer in answer_list:
					pos = diagonal_string.lower().find(answer.lower())
					if(pos!=-1):
						#sub string was found
						answers_found.append([[x_base+pos,y_base+pos], [x_base+(pos+len(answer)-1),y_base+(pos+len(answer)-1)]])
				break
			#reached end of diagonal
			diagonal_string+=grid[y_pos][x_pos]
			
			x_change-=1
			y_change+=1

search_diagonals(grid,answers_to_find+answers_backwards, answers_found)	
search_columns(grid,answers_to_find+answers_backwards, answers_found)
search_rows(grid,answers_to_find+answers_backwards, answers_found)
print(answers_found)
