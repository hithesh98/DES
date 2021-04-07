def permutation(inputX, pbox, blocksize):
    y = 0
    for i in pbox:
        y <<= 1
        y ^= (inputX >> (blocksize - i)) & 1
    return y