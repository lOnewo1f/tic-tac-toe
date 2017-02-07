#for win scenarios value+=x
if block_dict[(1,1)] :
	value+=2
if block_dict[(0,0)] || block_dict[(0,2)] || block_dict[(2,0)] || block_dict[(2,2)] :
	value+=1

for block[(0,0)]:
	if (block_dict[(0,1)] => 0 && block_dict[(0,2)] => 0) || (block_dict[(1,0)] => 0 && block_dict[(2,0)] => 0) || (block_dict[(1,1)] => 0 && block_dict[(2,2)] => 0) :
#for probable pattern 2 positive, 1 zero/negative
		value+=2
for block[(0,1)]:
	if (block_dict[(0,0)] => 0 && block_dict[(0,2)] => 0) || (block_dict[(1,1)] => 0 && block_dict[(2,1)] => 0) :
		value+=2
for block[(0,2)]:
	if (block_dict[(0,1)] => 0 && block_dict[(0,0)] => 0) || (block_dict[(1,2)] => 0 && block_dict[(2,2)] => 0) || (block_dict[(1,1)] => 0 && block_dict[(2,0)] => 0) :
		value+=2
for block[(1,0)]:
	if (block_dict[(0,0)] => 0 && block_dict[(2,0)] => 0) || (block_dict[(1,1)] => 0 && block_dict[(1,2)] => 0) :
		value+=2
for block[(1,1)]:
	if (block_dict[(0,1)] => 0 && block_dict[(2,1)] => 0) || (block_dict[(0,0)] => 0 && block_dict[(2,2)] => 0) || (block_dict[(1,0)] => 0 && block_dict[(1,2)] => 0) || block_dict[(2,0)] => 0 && block_dict[(0,2)] => 0) :
		value+=2
for block[(1,2)]:
	if (block_dict[(1,0)] => 0 && block_dict[(1,1)] => 0) || (block_dict[(0,2)] => 0 && block_dict[(2,2)] => 0) :
		value+=2
for block[(2,0)]:
	if (block_dict[(1,1)] => 0 && block_dict[(0,2)] => 0) || (block_dict[(1,0)] => 0 && block_dict[(0,0)] => 0) || (block_dict[(2,1)] => 0 && block_dict[(2,2)] => 0) :
		value+=2
for block[(2,1)]:
	if (block_dict[(0,1)] => 0 && block_dict[(1,1)] => 0) || (block_dict[(2,2)] => 0 && block_dict[(2,0)] => 0) :
		value+=2
for block[(2,2)]:
	if (block_dict[(1,2)] => 0 && block_dict[(0,2)] => 0) || (block_dict[(2,1)] => 0 && block_dict[(2,0)] => 0) || (block_dict[(1,1)] => 0 && block_dict[(0,0)] => 0) :
		value+=2
