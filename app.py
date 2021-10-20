from QR import QR_code
input_str = ["ABCD", "$%*+-,./:1234test", "test", "^()$%*+-,./:1234TEST", "$%*+-./:1234TEST", "1234", "-1234", "12.34",
             "1234567890123456789012345678901234567890", "0670059", "茗荷", "8675309", "HELLO WORLD", "Hello, world!"]
#input_str = ["Hello, world! this is test message encoded in QR code"]
#input_str = ['ALPHANUMERIC']
#input_str = ["another test for input string"]
#input_str = ["another test for input string"]
#input_str = ["12345.1"]
input_str = ["2137"]
if __name__ == "__main__":
    #qr = QR_code(input_str[0], 'A')
    for data in input_str:
        try:
            #                                7%   15%  25%  30%
            # input string, error_correction['L', 'M', 'Q', 'H']
            qr = QR_code(data, 'H')
            qr.show_complex_info()
            # qr.show_basic_info()
            # simple_json = qr.simple_info
            # complex_json = qr.complex_info

            '''
            SaveToFile(@filename, @resolution, @dpi, @block color, @background color):
            @filename                        <str>
            @resolution (px)                 <int>
            @dpi (inches per meter)          <int>  
            @block color (r, g, b, a)        <tuple>
            @background color (r, g, b, a)   <tuple>
            '''
            qr.SaveToFile(f"output{input_str.index(data)}.bmp", 300, 2835, (200, 40, 40, 255), (255, 255, 255, 255))
        except Exception as e:
            print(e)


'''
detected bugs:
number encoding sometimes dont work
version >= 7 dont works
data placement is not correct
'''