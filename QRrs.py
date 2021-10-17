class ReedSolomon:
    def __init__(self, numbers_temp_block, EC_codewords_per_block):
        self.numbers_temp_block = numbers_temp_block
        self.EC_codewords_per_block = EC_codewords_per_block

        self.__GFEXP = [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90, 180, 117,
                        234, 201,
                        143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238,
                        193, 159,
                        35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97,
                        194, 153,
                        47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127,
                        254, 225,
                        223, 163, 91, 182, 113, 226, 217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189,
                        103, 206,
                        129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23, 46, 92,
                        184,
                        109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77, 154, 41, 82, 164, 85, 170, 73,
                        146, 57,
                        114, 228, 213, 183, 115, 230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246,
                        241,
                        255, 227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65, 130, 25, 50,
                        100, 200,
                        141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166, 81, 162, 89, 178, 121, 242, 249, 239, 195,
                        155, 43,
                        86, 172, 69, 138, 9, 18, 36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11,
                        22, 44,
                        88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1, 2, 4, 8, 16, 32, 64,
                        128, 29,
                        58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48,
                        96, 192,
                        157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159, 35, 70, 140, 5, 10,
                        20, 40, 80,
                        160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97, 194, 153, 47, 94, 188, 101, 202,
                        137, 15,
                        30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113,
                        226, 217,
                        175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206, 129, 31, 62, 124, 248,
                        237, 199,
                        147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23, 46, 92, 184, 109, 218, 169, 79, 158, 33,
                        66, 132,
                        21, 42, 84, 168, 77, 154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115, 230,
                        209, 191,
                        99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241, 255, 227, 219, 171, 75, 150, 49,
                        98, 196,
                        149, 55, 110, 220, 165, 87, 174, 65, 130, 25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224,
                        221, 167,
                        83, 166, 81, 162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138, 9, 18, 36,
                        72, 144,
                        61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22, 44, 88, 176, 125, 250, 233, 207,
                        131, 27,
                        54, 108, 216, 173, 71, 142, 1, 2]
        self.__GFLOG = [0, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75, 4, 100, 224, 14, 52, 141,
                        239, 129,
                        28, 193, 105, 248, 200, 8, 76, 113, 5, 138, 101, 47, 225, 36, 15, 33, 53, 147, 142, 218,
                        240, 18,
                        130, 69, 29, 181, 194, 125, 106, 39, 249, 185, 201, 154, 9, 120, 77, 228, 114, 166, 6, 191,
                        139, 98,
                        102, 221, 48, 253, 226, 152, 37, 179, 16, 145, 34, 136, 54, 208, 148, 206, 143, 150, 219,
                        189, 241,
                        210, 19, 92, 131, 56, 70, 64, 30, 66, 182, 163, 195, 72, 126, 110, 107, 58, 40, 84, 250,
                        133, 186,
                        61, 202, 94, 155, 159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87, 7, 112, 192,
                        247, 140,
                        128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24, 227, 165, 153, 119, 38, 184, 180, 124, 17,
                        68, 146,
                        217, 35, 32, 137, 46, 55, 63, 209, 91, 149, 188, 207, 205, 144, 135, 151, 178, 220, 252,
                        190, 97,
                        242, 86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71, 109, 65, 162, 31, 45, 67, 216, 183,
                        123,
                        164, 118, 196, 23, 73, 236, 127, 12, 111, 246, 108, 161, 59, 82, 41, 157, 85, 170, 251, 96,
                        134, 177,
                        187, 204, 62, 90, 203, 89, 95, 176, 156, 169, 160, 81, 11, 245, 22, 235, 122, 117, 44, 215,
                        79, 174,
                        213, 233, 230, 231, 173, 232, 116, 214, 244, 234, 168, 80, 88, 175]

    ## GALOIS PRIMITIVE OPERATIONS
    # -----
    # Galois multiplication
    # argX, argY: multiplicand, multiplier
    # byteValu: product
    def __gfMult(self, argX, argY):
        # parametre checks
        if ((argX == 0) or (argY == 0)):
            byteValu = 0
        else:
            # perform the operation
            byteValu = self.__GFLOG[argX]
            byteValu += self.__GFLOG[argY]
            byteValu = self.__GFEXP[byteValu]

        # return the product result
        return (byteValu)

    # Galois division
    # argX, argY: dividend, divisor
    # byteValu: quotient
    def __gfDivi(self, argX, argY):
        # validate the divisor
        if (argY == 0):
            raise ZeroDivisionError()

        # validate the dividend
        if (argX == 0):
            byteValu = 0
        else:
            # perform the division
            byteValu = self.__GFLOG[argX] - self.__GFLOG[argY]
            byteValu += 255
            byteValu = self.__GFEXP[byteValu]

        # return the division result
        return (byteValu)

    ## GALOIS POLYNOMIAL OPERATIONS
    # -----
    # Polynomial addition
    # polyA, polyB: polynomial addends
    # polySum: polynomial sum
    def _gfPolyAdd(self, polyA, polyB):
        # initialise the polynomial sum
        polySum = [0] * max(len(polyA), len(polyB))

        # process the first addend
        for polyPos in range(0, len(polyA)):
            polySum[polyPos + len(polySum) - len(polyA)] = polyA[polyPos]

        # add the second addend
        for polyPos in range(0, len(polyB)):
            polySum[polyPos + len(polySum) - len(polyB)] ^= polyB[polyPos]

        # return the sum
        return (polySum)

    # Polynomial multiplication
    # polyA, polyB: polynomial factors
    # polyProd: polynomial product
    def _gfPolyMult(self, polyA, polyB):
        # initialise the product
        polyProd = len(polyA) + len(polyB) - 1
        polyProd = [0] * polyProd

        # start multiplying
        for posB in range(0, len(polyB)):
            for posA in range(0, len(polyA)):
                polyProd[posA + posB] ^= self.__gfMult(polyA[posA], polyB[posB])

        # return the product result
        return (polyProd)

    # Polynomial scaling
    # argPoly: polynomial argument
    # argX: scaling factor
    # polyVal: scaled polynomial
    def _gfPolyScale(self, argPoly, argX):
        # initialise the scaled polynomial
        polyVal = [0] * len(argPoly)

        # start scaling
        for polyPos in range(0, len(argPoly)):
            polyVal[polyPos] = self.__gfMult(argPoly[polyPos], argX)

        # return the scaled polynomial
        return (polyVal)

    # Polynomial evaluation
    # argPoly: polynomial argument
    # argX: independent variable
    # byteValu: dependent variable
    def _gfPolyEval(self, argPoly, argX):
        # initialise the polynomial result
        byteValu = argPoly[0]

        # evaluate the polynomial argument
        for polyPos in range(1, len(argPoly)):
            tempValu = self.__gfMult(byteValu, argX)
            tempValu = tempValu ^ argPoly[polyPos]
            byteValu = tempValu

        # return the evaluated result
        return (byteValu)

    ## REED-SOLOMON SUPPORT ROUTINES
    # -----
    # Prepare the generator polynomial
    # errSize: number of error symbols
    # polyValu: generator polynomial
    def _rsGenPoly(self, errSize):
        polyValu = [1]

        for polyPos in range(0, errSize):
            tempVal = [1, self.__GFEXP[polyPos]]
            polyValu = self._gfPolyMult(polyValu, tempVal)

        # return the polynomial result
        return (polyValu)

    ## REED-SOLOMON ENCODING
    # ------
    # argMesg: the message block
    # errSize: number of error symbols
    # outBuffer: the encoded output buffer
    def RSEncode(self):

        # prepare the generator polynomial
        polyGen = self._rsGenPoly(self.EC_codewords_per_block)

        # prepare the output buffer
        outBuffer = [0] * (len(self.numbers_temp_block) + self.EC_codewords_per_block)
        # initialise the output buffer
        for mesgPos in range(0, len(self.numbers_temp_block)):
            mesgChar = self.numbers_temp_block[mesgPos]
            outBuffer[mesgPos] = mesgChar

        for mesgPos in range(0, len(self.numbers_temp_block)):
            mesgChar = outBuffer[mesgPos]
            if (mesgChar != 0):
                for polyPos in range(0, len(polyGen)):
                    tempValu = self.__gfMult(polyGen[polyPos], mesgChar)
                    outBuffer[mesgPos + polyPos] ^= tempValu

        # finalise the output buffer
        for mesgPos in range(0, len(self.numbers_temp_block)):
            mesgChar = self.numbers_temp_block[mesgPos]
            outBuffer[mesgPos] = mesgChar

        # return the output buffer
        outBuffer = outBuffer[len(self.numbers_temp_block):]
        return (outBuffer)
