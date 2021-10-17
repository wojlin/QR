from QR import QR_code
'''input_str = ["ABCD", "$%*+-,./:1234test", "test", "^()$%*+-,./:1234TEST", "$%*+-./:1234TEST", "1234", "-1234", "12.34",
             "1234567890123456789012345678901234567890", "0670059", "茗荷", "8675309", "HELLO WORLD", "Hello, world!"]'''
input_str = ["Hello, world! this is test message encoded in QR code"]


if __name__ == "__main__":
    for data in input_str:
        #                                7%   15%  25%  30%
        # input string, error_correction['L', 'M', 'Q', 'H']
        qr = QR_code(data, 'M')
        qr.show_complex_info()
        # qr.show_basic_info()
        # simple_json = qr.simple_info
        # complex_json = qr.complex_info
        # <str>   ,<int> ,<int>                  ,<tuple>                  ,<tuple>
        # filename, scale, dpi (inches per meter), block color (r, g, b, a), background color (r, g, b, a)
        qr.SaveToFile("output.bmp", 20, 2835, (200, 40, 40, 255), (255, 255, 255, 255))
