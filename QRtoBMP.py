class GenerateBMP():
    def __init__(self, matrix, filepath, scale, dpi, block_color, background_color):
        self.checkInput(matrix, filepath, scale, dpi, block_color, background_color)
        scale = scale // len(matrix)
        size = len(matrix) * scale

        ######################  HEADER  ##########################
        self._bfType = 19778  # the header field used to identify the BMP                           size: 2 bytes
        self._bfSize = 32 + size * size * 4  # The size of the BMP file in bytes                    size: 4 bytes
        self._bfReserved1 = 0  # reserved                                                           size: 2 bytes
        self._bfReserved2 = 0  # reserved                                                           size: 2 bytes
        self._bfOffBits = 26  # offset, starting address where the pixel array can be found         size: 4 bytes
        ##########################################################

        ##################  BITMAPCOREHEADER #####################
        self._bcSize = 108  # constant size of this BITMAPCOREHEADER  (40 bytes)                     size: 4 bytes
        self._bcWidth = size  # The bitmap width in pixels (unsigned 16-bit)                        size: 2 bytes
        self._bcHeight = size  # The bitmap height in pixels (unsigned 16-bit)                      size: 2 bytes
        self._bcPlanes = 1  # The number of color planes, must be 1                                 size: 2 bytes
        self._bcBitCount = 32  # The number of bits per pixel                                       size: 2 bytes
        self._compression = 3  # the compression method being used                                  size: 4 bytes
        self._imgSize = 32  # the image size. this is the size of the raw bitmap data               size: 4 bytes
        self._hRes = dpi  # the horizontal resolution of the image                                  size: 4 bytes
        self._vRes = dpi  # the vertical resolution of the image                                    size: 4 bytes
        self._nColor = 0  # number of colors in the color palette, or 0 to default to 2n            size: 4 bytes
        self._iColors = 0  # number of important colors used, 0 when every color is important       size: 4 bytes
        self._rMask = 16711680  # Red channel bit mask                                                   size: 4 bytes
        self._gMask = 65280  # Green channel bit mask                                               size: 4 bytes
        self._bMask = 255  # Blue channel bit mask                                             size: 4 bytes
        self._aMask = 4278190080  # Alpha channel bit mask                                          size: 4 bytes
        self._lcs = 1934772034  # LCS_WINDOWS_COLOR_SPACE                                           size: 4 bytes
        self._end = 0  # size: 4 bytes
        self._rGamma = 0  # unused                                                                  size: 4 bytes
        self._gGamma = 0  # unused                                                                  size: 4 bytes
        self._bGamma = 0  # unused                                                                  size: 4 bytes
        ##########################################################

        self.matrix_size = len(matrix)
        self._graphics = [(0, 0, 0, 0)] * self._bcWidth * self._bcHeight

        self.writeData(matrix, scale, block_color, background_color)
        self.saveFile(filepath)

    @staticmethod
    def checkInput(matrix, filepath, resolution, dpi, block_color, background_color):
        """
        this function returns an error if any of the parameters are invalid
        :param matrix:             <2d list>  list with matrix
        :param filepath:           <str>      path to file output
        :param resolution:         <int>  >=  qr code matrix size
        :param dpi:                <int>      (inches per meter)
        :param block_color:        <tuple>    (r, g, b, a) <0-255>
        :param background_color:   <tuple>    (r, g, b, a) <0-255>
        :return: nothing
        """
        if filepath[-4:] != '.bmp':
            raise Exception("file extension need to be .bmp")
        if type(resolution) != int or resolution < 1:
            raise Exception("scale need to be positive integer")
        if resolution < len(matrix):
            raise Exception("resolution need to be higher or equal to qr code size")
        if type(dpi) != int or dpi < 1:
            raise Exception("dpi need to be positive integer")
        if type(block_color) != tuple or type(background_color) != tuple:
            raise Exception("color must be (0,255,0-255,0-255,0-255) tuple")
        if len(block_color) != 4 or len(background_color) != 4:
            raise Exception("color must be (0,255, 0-255,0-255,0-255) tuple")
        if (not 0 <= block_color[0] <= 255) or (not 0 <= block_color[1] <= 255) or (not 0 <= block_color[2] <= 255):
            raise Exception("color must be (0,255,0-255,0-255,0-255) tuple")
        if (not 0 <= background_color[0] <= 255) or (not 0 <= background_color[1] <= 255) or (
                not 0 <= background_color[2] <= 255):
            raise Exception("color must be (0,255,0-255,0-255,0-255) tuple")

    def draw_pixel(self, x, y, color):
        """
        this function collects the corresponding pixel in the array
        :param x: x coord of color array
        :param y: y coord of color array
        :param color: color of pixel in rgba format
        :return: nothing
        """
        self._graphics[(self._bcHeight - 1 - y) * self._bcHeight + x] = (color[2], color[1], color[0], color[3])

    def writeData(self, matrix, scale, block_color, background_color):
        """
        this function writes color data array for bmp file
        :param matrix:             <2d list>  list with matrix
        :param filepath:           <str>      path to file output
        :param resolution:         <int>  >=  qr code matrix size
        :param block_color:        <tuple>    (r, g, b, a) <0-255>
        :param background_color:   <tuple>    (r, g, b, a) <0-255>
        :return: nothing
        """
        for y in range(len(matrix)):
            for x in range(len(matrix)):
                if matrix[y][x] == 1:
                    color = block_color
                else:
                    color = background_color
                for x_offset in range(scale):
                    for y_offset in range(scale):
                        self.draw_pixel(x * scale + x_offset, y * scale + y_offset, color)
                self.draw_pixel(x * scale, y * scale, color)

    def saveFile(self, filepath):
        """
        this function saves the collected data to a file specified in filepath parameter
        :param filepath: path to file
        :return: nothing
        """
        with open(filepath, 'wb') as f:
            header = self._bfType.to_bytes(2, byteorder='little') + \
                     self._bfSize.to_bytes(4, byteorder='little') + \
                     self._bfReserved1.to_bytes(2, byteorder='little') + \
                     self._bfReserved2.to_bytes(2, byteorder='little') + \
                     self._bfOffBits.to_bytes(4, byteorder='little')

            bitmapcoreheader = self._bcSize.to_bytes(4, byteorder='little') + \
                               self._bcWidth.to_bytes(4, byteorder='little') + \
                               self._bcHeight.to_bytes(4, byteorder='little') + \
                               self._bcPlanes.to_bytes(2, byteorder='little') + \
                               self._bcBitCount.to_bytes(2, byteorder='little') + \
                               self._compression.to_bytes(4, byteorder='little') + \
                               self._imgSize.to_bytes(4, byteorder='little') + \
                               self._hRes.to_bytes(4, byteorder='little') + \
                               self._vRes.to_bytes(4, byteorder='little') + \
                               self._nColor.to_bytes(4, byteorder='little') + \
                               self._iColors.to_bytes(4, byteorder='little') + \
                               self._rMask.to_bytes(4, byteorder='little') + \
                               self._gMask.to_bytes(4, byteorder='little') + \
                               self._bMask.to_bytes(4, byteorder='little') + \
                               self._aMask.to_bytes(4, byteorder='little') + \
                               self._lcs.to_bytes(4, byteorder='little') + \
                               self._end.to_bytes(36, byteorder='little') + \
                               self._rGamma.to_bytes(4, byteorder='little') + \
                               self._gGamma.to_bytes(4, byteorder='little') + \
                               self._bGamma.to_bytes(4, byteorder='little')

            f.write(header)
            f.write(bitmapcoreheader)
            for px in self._graphics:
                pixel_data = (px[0]).to_bytes(1, byteorder='little') + \
                             (px[1]).to_bytes(1, byteorder='little') + \
                             (px[2]).to_bytes(1, byteorder='little') + \
                             (px[3]).to_bytes(1, byteorder='little')
                f.write(pixel_data)
            for i in range((4 - ((self._bcWidth * 4) % 4)) % 4):
                f.write((0).to_bytes(1, byteorder='little'))
