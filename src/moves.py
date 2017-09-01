# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.

# Front Quarter Turn Clockwise
def F(pos):
	return (pos[6] + pos[14] + pos[2] +
			pos[3] + pos[5] + pos[13] +
			pos[19] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[1] +
			pos[4] + pos[12] + pos[18] +
			pos[15] + pos[16] + pos[0] +
			pos[11] + pos[17] + pos[20])

# Front Quarter Turn Counterclockwise
def Fp(pos):
	return (pos[17] + pos[11] + pos[2] +
			pos[3] + pos[12] + pos[4] +
			pos[0] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[18] +
			pos[13] + pos[5] + pos[1] +
			pos[15] + pos[16] + pos[19] +
			pos[14] + pos[6] + pos[20])

# Front Half Turn
def F2(pos):
	return (pos[19] + pos[18] + pos[2] +
			pos[3] + pos[13] + pos[12] +
			pos[17] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[14] +
			pos[5] + pos[4] + pos[11] +
			pos[15] + pos[16] + pos[6] +
			pos[1] + pos[0] + pos[20])

# Right Quarter Turn Clockwise
def R(pos):
	return (pos[12] + pos[1] + pos[2] +
			pos[4] + pos[18] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[0] + pos[11] + pos[17] +
			pos[20] + pos[13] + pos[14] +
			pos[3] + pos[10] + pos[16] +
			pos[15] + pos[19] + pos[9])

# Right Quarter Turn Counterclockwise
def Rp(pos):
	return (pos[9] + pos[1] + pos[2] +
			pos[15] + pos[3] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[20] + pos[16] + pos[10] +
			pos[0] + pos[13] + pos[14] +
			pos[18] + pos[17] + pos[11] +
			pos[4] + pos[19] + pos[12])

# Right Half Turn
def R2(pos):
	return (pos[20] + pos[1] + pos[2] +
			pos[18] + pos[15] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[12] + pos[17] + pos[16] +
			pos[9] + pos[13] + pos[14] +
			pos[4] + pos[11] + pos[10] +
			pos[3] + pos[19] + pos[0])

# Up Quarter Turn Clockwise
def U(pos):
	return (pos[3] + pos[0] + pos[1] +
			pos[2] + pos[10] + pos[11] +
			pos[4] + pos[5] + pos[6] +
			pos[7] + pos[8] + pos[9] +
			pos[12] + pos[13] + pos[14] +
			pos[15] + pos[16] + pos[17] +
			pos[18] + pos[19] + pos[20])

# Up Quarter Turn Counterclockwise
def Up(pos):
	return (pos[1] + pos[2] + pos[3] +
			pos[0] + pos[6] + pos[7] +
			pos[8] + pos[9] + pos[10] +
			pos[11] + pos[4] + pos[5] +
			pos[12] + pos[13] + pos[14] +
			pos[15] + pos[16] + pos[17] +
			pos[18] + pos[19] + pos[20])

# Up Half Turn
def U2(pos):
	return (pos[2] + pos[3] + pos[0] +
			pos[1] + pos[8] + pos[9] +
			pos[10] + pos[11] + pos[4] +
			pos[5] + pos[6] + pos[7] +
			pos[12] + pos[13] + pos[14] +
			pos[15] + pos[16] + pos[17] +
			pos[18] + pos[19] + pos[20])
