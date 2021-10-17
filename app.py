from QRtoBMP import GenerateBMP
from QRinfo import QRinfo
from QRrs import ReedSolomon
from QRplacement import QRplacement

'''input_str = ["ABCD", "$%*+-,./:1234test", "test", "^()$%*+-,./:1234TEST", "$%*+-./:1234TEST", "1234", "-1234", "12.34",
             "1234567890123456789012345678901234567890", "0670059", "茗荷", "8675309", "HELLO WORLD", "Hello, world!"]'''
input_str = ["Hello, world!"]

class QR_code:
    def __init__(self, input_data, correction_type):

        # ['Version',
        # ' EC Level',
        # 'Total Number of Data Codewords for this Version and EC Level',
        # 'EC Codewords Per Block', 'Number of Blocks in Group 1',
        # "Number of Data Codewords in Each of Group 1's Blocks",
        # 'Number of Blocks in Group 2',
        # "Number of Data Codewords in Each of Group 2's Blocks",
        # 'Total Data Codewords']
        self.error_correction_table = [['1', 'L', '19', '7', '1', '19', '', '', '19'],
                                       ['1', 'M', '16', '10', '1', '16', '', '', '16'],
                                       ['1', 'Q', '13', '13', '1', '13', '', '', '13'],
                                       ['1', 'H', '9', '17', '1', '9', '', '', '9'],
                                       ['2', 'L', '34', '10', '1', '34', '', '', '34'],
                                       ['2', 'M', '28', '16', '1', '28', '', '', '28'],
                                       ['2', 'Q', '22', '22', '1', '22', '', '', '22'],
                                       ['2', 'H', '16', '28', '1', '16', '', '', '16'],
                                       ['3', 'L', '55', '15', '1', '55', '', '', '55'],
                                       ['3', 'M', '44', '26', '1', '44', '', '', '44'],
                                       ['3', 'Q', '34', '18', '2', '17', '', '', '34'],
                                       ['3', 'H', '26', '22', '2', '13', '', '', '26'],
                                       ['4', 'L', '80', '20', '1', '80', '', '', '80'],
                                       ['4', 'M', '64', '18', '2', '32', '', '', '64'],
                                       ['4', 'Q', '48', '26', '2', '24', '', '', '48'],
                                       ['4', 'H', '36', '16', '4', '9', '', '', '36'],
                                       ['5', 'L', '108', '26', '1', '108', '', '', '108'],
                                       ['5', 'M', '86', '24', '2', '43', '', '', '86'],
                                       ['5', 'Q', '62', '18', '2', '15', '2', '16', '62'],
                                       ['5', 'H', '46', '22', '2', '11', '2', '12', '46'],
                                       ['6', 'L', '136', '18', '2', '68', '', '', '136'],
                                       ['6', 'M', '108', '16', '4', '27', '', '', '108'],
                                       ['6', 'Q', '76', '24', '4', '19', '', '', '76'],
                                       ['6', 'H', '60', '28', '4', '15', '', '', '60'],
                                       ['7', 'L', '156', '20', '2', '78', '', '', '156'],
                                       ['7', 'M', '124', '18', '4', '31', '', '', '124'],
                                       ['7', 'Q', '88', '18', '2', '14', '4', '15', '88'],
                                       ['7', 'H', '66', '26', '4', '13', '1', '14', '66'],
                                       ['8', 'L', '194', '24', '2', '97', '', '', '194'],
                                       ['8', 'M', '154', '22', '2', '38', '2', '39', '154'],
                                       ['8', 'Q', '110', '22', '4', '18', '2', '19', '110'],
                                       ['8', 'H', '86', '26', '4', '14', '2', '15', '86'],
                                       ['9', 'L', '232', '30', '2', '116', '', '', '232'],
                                       ['9', 'M', '182', '22', '3', '36', '2', '37', '182'],
                                       ['9', 'Q', '132', '20', '4', '16', '4', '17', '132'],
                                       ['9', 'H', '100', '24', '4', '12', '4', '13', '100'],
                                       ['10', 'L', '274', '18', '2', '68', '2', '69', '274'],
                                       ['10', 'M', '216', '26', '4', '43', '1', '44', '216'],
                                       ['10', 'Q', '154', '24', '6', '19', '2', '20', '154'],
                                       ['10', 'H', '122', '28', '6', '15', '2', '16', '122'],
                                       ['11', 'L', '324', '20', '4', '81', '', '', '324'],
                                       ['11', 'M', '254', '30', '1', '50', '4', '51', '254'],
                                       ['11', 'Q', '180', '28', '4', '22', '4', '23', '180'],
                                       ['11', 'H', '140', '24', '3', '12', '8', '13', '140'],
                                       ['12', 'L', '370', '24', '2', '92', '2', '93', '370'],
                                       ['12', 'M', '290', '22', '6', '36', '2', '37', '290'],
                                       ['12', 'Q', '206', '26', '4', '20', '6', '21', '206'],
                                       ['12', 'H', '158', '28', '7', '14', '4', '15', '158'],
                                       ['13', 'L', '428', '26', '4', '107', '', '', '428'],
                                       ['13', 'M', '334', '22', '8', '37', '1', '38', '334'],
                                       ['13', 'Q', '244', '24', '8', '20', '4', '21', '244'],
                                       ['13', 'H', '180', '22', '12', '11', '4', '12', '180'],
                                       ['14', 'L', '461', '30', '3', '115', '1', '116', '461'],
                                       ['14', 'M', '365', '24', '4', '40', '5', '41', '365'],
                                       ['14', 'Q', '261', '20', '11', '16', '5', '17', '261'],
                                       ['14', 'H', '197', '24', '11', '12', '5', '13', '197'],
                                       ['15', 'L', '523', '22', '5', '87', '1', '88', '523'],
                                       ['15', 'M', '415', '24', '5', '41', '5', '42', '415'],
                                       ['15', 'Q', '295', '30', '5', '24', '7', '25', '295'],
                                       ['15', 'H', '223', '24', '11', '12', '7', '13', '223'],
                                       ['16', 'L', '589', '24', '5', '98', '1', '99', '589'],
                                       ['16', 'M', '453', '28', '7', '45', '3', '46', '453'],
                                       ['16', 'Q', '325', '24', '15', '19', '2', '20', '325'],
                                       ['16', 'H', '253', '30', '3', '15', '13', '16', '253'],
                                       ['17', 'L', '647', '28', '1', '107', '5', '108', '647'],
                                       ['17', 'M', '507', '28', '10', '46', '1', '47', '507'],
                                       ['17', 'Q', '367', '28', '1', '22', '15', '23', '367'],
                                       ['17', 'H', '283', '28', '2', '14', '17', '15', '283'],
                                       ['18', 'L', '721', '30', '5', '120', '1', '121', '721'],
                                       ['18', 'M', '563', '26', '9', '43', '4', '44', '563'],
                                       ['18', 'Q', '397', '28', '17', '22', '1', '23', '397'],
                                       ['18', 'H', '313', '28', '2', '14', '19', '15', '313'],
                                       ['19', 'L', '795', '28', '3', '113', '4', '114', '795'],
                                       ['19', 'M', '627', '26', '3', '44', '11', '45', '627'],
                                       ['19', 'Q', '445', '26', '17', '21', '4', '22', '445'],
                                       ['19', 'H', '341', '26', '9', '13', '16', '14', '341'],
                                       ['20', 'L', '861', '28', '3', '107', '5', '108', '861'],
                                       ['20', 'M', '669', '26', '3', '41', '13', '42', '669'],
                                       ['20', 'Q', '485', '30', '15', '24', '5', '25', '485'],
                                       ['20', 'H', '385', '28', '15', '15', '10', '16', '385'],
                                       ['21', 'L', '932', '28', '4', '116', '4', '117', '932'],
                                       ['21', 'M', '714', '26', '17', '42', '', '', '714'],
                                       ['21', 'Q', '512', '28', '17', '22', '6', '23', '512'],
                                       ['21', 'H', '406', '30', '19', '16', '6', '17', '406'],
                                       ['22', 'L', '1006', '28', '2', '111', '7', '112', '1006'],
                                       ['22', 'M', '782', '28', '17', '46', '', '', '782'],
                                       ['22', 'Q', '568', '30', '7', '24', '16', '25', '568'],
                                       ['22', 'H', '442', '24', '34', '13', '', '', '442'],
                                       ['23', 'L', '1094', '30', '4', '121', '5', '122', '1094'],
                                       ['23', 'M', '860', '28', '4', '47', '14', '48', '860'],
                                       ['23', 'Q', '614', '30', '11', '24', '14', '25', '614'],
                                       ['23', 'H', '464', '30', '16', '15', '14', '16', '464'],
                                       ['24', 'L', '1174', '30', '6', '117', '4', '118', '1174'],
                                       ['24', 'M', '914', '28', '6', '45', '14', '46', '914'],
                                       ['24', 'Q', '664', '30', '11', '24', '16', '25', '664'],
                                       ['24', 'H', '514', '30', '30', '16', '2', '17', '514'],
                                       ['25', 'L', '1276', '26', '8', '106', '4', '107', '1276'],
                                       ['25', 'M', '1000', '28', '8', '47', '13', '48', '1000'],
                                       ['25', 'Q', '718', '30', '7', '24', '22', '25', '718'],
                                       ['25', 'H', '538', '30', '22', '15', '13', '16', '538'],
                                       ['26', 'L', '1370', '28', '10', '114', '2', '115', '1370'],
                                       ['26', 'M', '1062', '28', '19', '46', '4', '47', '1062'],
                                       ['26', 'Q', '754', '28', '28', '22', '6', '23', '754'],
                                       ['26', 'H', '596', '30', '33', '16', '4', '17', '596'],
                                       ['27', 'L', '1468', '30', '8', '122', '4', '123', '1468'],
                                       ['27', 'M', '1128', '28', '22', '45', '3', '46', '1128'],
                                       ['27', 'Q', '808', '30', '8', '23', '26', '24', '808'],
                                       ['27', 'H', '628', '30', '12', '15', '28', '16', '628'],
                                       ['28', 'L', '1531', '30', '3', '117', '10', '118', '1531'],
                                       ['28', 'M', '1193', '28', '3', '45', '23', '46', '1193'],
                                       ['28', 'Q', '871', '30', '4', '24', '31', '25', '871'],
                                       ['28', 'H', '661', '30', '11', '15', '31', '16', '661'],
                                       ['29', 'L', '1631', '30', '7', '116', '7', '117', '1631'],
                                       ['29', 'M', '1267', '28', '21', '45', '7', '46', '1267'],
                                       ['29', 'Q', '911', '30', '1', '23', '37', '24', '911'],
                                       ['29', 'H', '701', '30', '19', '15', '26', '16', '701'],
                                       ['30', 'L', '1735', '30', '5', '115', '10', '116', '1735'],
                                       ['30', 'M', '1373', '28', '19', '47', '10', '48', '1373'],
                                       ['30', 'Q', '985', '30', '15', '24', '25', '25', '985'],
                                       ['30', 'H', '745', '30', '23', '15', '25', '16', '745'],
                                       ['31', 'L', '1843', '30', '13', '115', '3', '116', '1843'],
                                       ['31', 'M', '1455', '28', '2', '46', '29', '47', '1455'],
                                       ['31', 'Q', '1033', '30', '42', '24', '1', '25', '1033'],
                                       ['31', 'H', '793', '30', '23', '15', '28', '16', '793'],
                                       ['32', 'L', '1955', '30', '17', '115', '', '', '1955'],
                                       ['32', 'M', '1541', '28', '10', '46', '23', '47', '1541'],
                                       ['32', 'Q', '1115', '30', '10', '24', '35', '25', '1115'],
                                       ['32', 'H', '845', '30', '19', '15', '35', '16', '845'],
                                       ['33', 'L', '2071', '30', '17', '115', '1', '116', '2071'],
                                       ['33', 'M', '1631', '28', '14', '46', '21', '47', '1631'],
                                       ['33', 'Q', '1171', '30', '29', '24', '19', '25', '1171'],
                                       ['33', 'H', '901', '30', '11', '15', '46', '16', '901'],
                                       ['34', 'L', '2191', '30', '13', '115', '6', '116', '2191'],
                                       ['34', 'M', '1725', '28', '14', '46', '23', '47', '1725'],
                                       ['34', 'Q', '1231', '30', '44', '24', '7', '25', '1231'],
                                       ['34', 'H', '961', '30', '59', '16', '1', '17', '961'],
                                       ['35', 'L', '2306', '30', '12', '121', '7', '122', '2306'],
                                       ['35', 'M', '1812', '28', '12', '47', '26', '48', '1812'],
                                       ['35', 'Q', '1286', '30', '39', '24', '14', '25', '1286'],
                                       ['35', 'H', '986', '30', '22', '15', '41', '16', '986'],
                                       ['36', 'L', '2434', '30', '6', '121', '14', '122', '2434'],
                                       ['36', 'M', '1914', '28', '6', '47', '34', '48', '1914'],
                                       ['36', 'Q', '1354', '30', '46', '24', '10', '25', '1354'],
                                       ['36', 'H', '1054', '30', '2', '15', '64', '16', '1054'],
                                       ['37', 'L', '2566', '30', '17', '122', '4', '123', '2566'],
                                       ['37', 'M', '1992', '28', '29', '46', '14', '47', '1992'],
                                       ['37', 'Q', '1426', '30', '49', '24', '10', '25', '1426'],
                                       ['37', 'H', '1096', '30', '24', '15', '46', '16', '1096'],
                                       ['38', 'L', '2702', '30', '4', '122', '18', '123', '2702'],
                                       ['38', 'M', '2102', '28', '13', '46', '32', '47', '2102'],
                                       ['38', 'Q', '1502', '30', '48', '24', '14', '25', '1502'],
                                       ['38', 'H', '1142', '30', '42', '15', '32', '16', '1142'],
                                       ['39', 'L', '2812', '30', '20', '117', '4', '118', '2812'],
                                       ['39', 'M', '2216', '28', '40', '47', '7', '48', '2216'],
                                       ['39', 'Q', '1582', '30', '43', '24', '22', '25', '1582'],
                                       ['39', 'H', '1222', '30', '10', '15', '67', '16', '1222'],
                                       ['40', 'L', '2956', '30', '19', '118', '6', '119', '2956'],
                                       ['40', 'M', '2334', '28', '18', '47', '31', '48', '2334'],
                                       ['40', 'Q', '1666', '30', '34', '24', '34', '25', '1666'],
                                       ['40', 'H', '1276', '30', '20', '15', '61', '16', '1276']]

        self.raw_data = input_data

        ##################  QR CODE TYPE  ####################
        self.mode_type, \
        self.mode_indicator, \
        self.error_correction, \
        self.version, \
        self.size, \
        self.character_count_indicator = QRinfo(input_data, correction_type).getINF0()
        #######################################################

        ################ QR MESSAGE ENCODING ##################
        self.encoded_data = self.encode_raw_data()
        self.terminator, self.maximum_size = self.find_terminator()
        self.padded_data = self.pad_data()
        self.broken_codewords, self.error_numbers, self.EC_codewords = self.codewords()
        self.final_message = self.interleave()
        #######################################################

        ################ QR MATRIX GENERATION #################
        QRgenerator = QRplacement(self.version, correction_type, self.size, self.final_message)
        self.module_matrix = QRgenerator.generateVisualMatrix()
        self.output_matrix = QRgenerator.generateBinaryMatrix()
        ########################################################

    def show_complex_info(self):
        print('')
        print(f'version: {self.version}')
        print(f'error correction: {self.error_correction}')
        print(f'mode: {self.mode_type}')
        print(f'size: {self.size}x{self.size} matrix')
        print(f'mode indicator : {self.mode_indicator}')
        print(f'character count indicator: {self.character_count_indicator}')
        print(f'terminator: {self.terminator}')
        print(f'data : {self.raw_data}')
        print(f'encoded data: {self.encoded_data}')
        print(f'padded_data: {self.padded_data}')
        print(f'codewords groups: {self.broken_codewords}')
        print(f'error correction numbers: {self.error_numbers}')
        print(f'error correction codewords: {self.EC_codewords}')
        print(f'final message: {self.final_message}')
        print(f'module matrix:')
        print('')
        for column in self.module_matrix:
            buffer = ' '
            for element in column:
                buffer += str(str(element) + '  ')
            print(buffer)
        print('')

    def show_basic_info(self):
        print('')
        print(f'data: {self.raw_data}')
        print(f'version: {self.version}')
        print(f'error correction: {self.error_correction}')
        print(f'mode: {self.mode_type}')
        print(f'size : {self.size}x{self.size} matrix')
        print('')

    def encode_raw_data(self):
        encoded_data = None
        if self.mode_type is not None and self.raw_data is not None:
            if self.mode_type == "Numeric":
                splitted_input = [self.raw_data[i:i + 3] for i in range(0, len(self.raw_data), 3)]
                converted_splitted_input = []
                binary_raw_data = None
                for part in splitted_input:
                    int_part = int(part)
                    if int_part < 10:  # convert into 4 binary bits
                        binary_raw_data = '%0*d' % (4, int(bin(int_part)[2:]))
                    elif int_part > 9:  # convert into 7 binary bits
                        binary_raw_data = '%0*d' % (7, int(bin(int_part)[2:]))
                    elif int_part > 99:  # convert into 10 binary bits
                        binary_raw_data = '%0*d' % (10, int(bin(int_part)[2:]))
                    converted_splitted_input.append(binary_raw_data)
                encoded_data = converted_splitted_input
            elif self.mode_type == "Alphanumeric":
                alphanumeric_table = [[0, '0'],
                                      [1, '1'],
                                      [2, '2'],
                                      [3, '3'],
                                      [4, '4'],
                                      [5, '5'],
                                      [6, '6'],
                                      [7, '7'],
                                      [8, '8'],
                                      [9, '9'],
                                      [10, 'A'],
                                      [11, 'B'],
                                      [12, 'C'],
                                      [13, 'D'],
                                      [14, 'E'],
                                      [15, 'F'],
                                      [16, 'G'],
                                      [17, 'H'],
                                      [18, 'I'],
                                      [19, 'J'],
                                      [20, 'K'],
                                      [21, 'L'],
                                      [22, 'M'],
                                      [23, 'N'],
                                      [24, 'O'],
                                      [25, 'P'],
                                      [26, 'Q'],
                                      [27, 'R'],
                                      [28, 'S'],
                                      [29, 'T'],
                                      [30, 'U'],
                                      [31, 'V'],
                                      [32, 'W'],
                                      [33, 'X'],
                                      [34, 'Y'],
                                      [35, 'Z'],
                                      [36, ' '],
                                      [37, '$'],
                                      [38, '%'],
                                      [39, '*'],
                                      [40, '+'],
                                      [41, '-'],
                                      [42, '.'],
                                      [43, '/'],
                                      [44, ':']]
                converted_chars = []
                for char in self.raw_data:
                    for alpha_char in alphanumeric_table:
                        if alpha_char[1] == char:
                            converted_chars.append(alpha_char[0])
                            break

                splitted_input = [converted_chars[i:i + 2] for i in range(0, len(converted_chars), 2)]

                converted_alphanumeric_binary = []
                for part in splitted_input:
                    if len(part) == 2:
                        decimal_number = int((int(part[0]) * 45) + int(part[1]))  # multiplying first part by 45
                        binary_raw_data = '%0*d' % (11, int(bin(decimal_number)[2:]))  # 11 bit binary
                        converted_alphanumeric_binary.append(binary_raw_data)
                    else:
                        binary_raw_data = '%0*d' % (6, int(bin(part[0])[2:]))  # 6 bit binary
                        converted_alphanumeric_binary.append(binary_raw_data)
                encoded_data = converted_alphanumeric_binary
            elif self.mode_type == "Byte":
                byte_table = [['0x00', '^@'],
                              ['0x01', '^A'],
                              ['0x02', '^B'],
                              ['0x03', '^C'],
                              ['0x04', '^D'],
                              ['0x05', '^E'],
                              ['0x06', '^F'],
                              ['0x07', '^G'],
                              ['0x08', '^H'],
                              ['0x09', '^I'],
                              ['0x0a', '^J'],
                              ['0x0b', '^K'],
                              ['0x0c', '^L'],
                              ['0x0d', '^M'],
                              ['0x0e', '^N'],
                              ['0x0f', '^O'],
                              ['0x10', '^P'],
                              ['0x11', '^Q'],
                              ['0x12', '^R'],
                              ['0x13', '^S'],
                              ['0x14', '^T'],
                              ['0x15', '^U'],
                              ['0x16', '^V'],
                              ['0x17', '^W'],
                              ['0x18', '^X'],
                              ['0x19', '^Y'],
                              ['0x1a', '^Z'],
                              ['0x1b', '^['],
                              ['0x1c', '^\\'],
                              ['0x1d', '^]'],
                              ['0x1e', '^^'],
                              ['0x1f', '^_'],
                              ['0x20', ''],
                              ['0x21', '!'],
                              ['0x22', '"'],
                              ['0x23', '#'],
                              ['0x24', '$'],
                              ['0x25', '%'],
                              ['0x26', '&'],
                              ['0x27', "'"],
                              ['0x28', '('],
                              ['0x29', ')'],
                              ['0x2a', '*'],
                              ['0x2b', '+'],
                              ['0x2c', ','],
                              ['0x2d', '-'],
                              ['0x2e', '.'],
                              ['0x2f', '/'],
                              ['0x30', '0'],
                              ['0x31', '1'],
                              ['0x32', '2'],
                              ['0x33', '3'],
                              ['0x34', '4'],
                              ['0x35', '5'],
                              ['0x36', '6'],
                              ['0x37', '7'],
                              ['0x38', '8'],
                              ['0x39', '9'],
                              ['0x3a', ':'],
                              ['0x3b', ';'],
                              ['0x3c', '<'],
                              ['0x3d', '='],
                              ['0x3e', '>'],
                              ['0x3f', '?'],
                              ['0x40', '@'],
                              ['0x41', 'A'],
                              ['0x42', 'B'],
                              ['0x43', 'C'],
                              ['0x44', 'D'],
                              ['0x45', 'E'],
                              ['0x46', 'F'],
                              ['0x47', 'G'],
                              ['0x48', 'H'],
                              ['0x49', 'I'],
                              ['0x4a', 'J'],
                              ['0x4b', 'K'],
                              ['0x4c', 'L'],
                              ['0x4d', 'M'],
                              ['0x4e', 'N'],
                              ['0x4f', 'O'],
                              ['0x50', 'P'],
                              ['0x51', 'Q'],
                              ['0x52', 'R'],
                              ['0x53', 'S'],
                              ['0x54', 'T'],
                              ['0x55', 'U'],
                              ['0x56', 'V'],
                              ['0x57', 'W'],
                              ['0x58', 'X'],
                              ['0x59', 'Y'],
                              ['0x5a', 'Z'],
                              ['0x5b', '['],
                              ['0x5c', '\\'],
                              ['0x5d', ']'],
                              ['0x5e', '^'],
                              ['0x5f', '_'],
                              ['0x60', '`'],
                              ['0x61', 'a'],
                              ['0x62', 'b'],
                              ['0x63', 'c'],
                              ['0x64', 'd'],
                              ['0x65', 'e'],
                              ['0x66', 'f'],
                              ['0x67', 'g'],
                              ['0x68', 'h'],
                              ['0x69', 'i'],
                              ['0x6a', 'j'],
                              ['0x6b', 'k'],
                              ['0x6c', 'l'],
                              ['0x6d', 'm'],
                              ['0x6e', 'n'],
                              ['0x6f', 'o'],
                              ['0x70', 'p'],
                              ['0x71', 'q'],
                              ['0x72', 'r'],
                              ['0x73', 's'],
                              ['0x74', 't'],
                              ['0x75', 'u'],
                              ['0x76', 'v'],
                              ['0x77', 'w'],
                              ['0x78', 'x'],
                              ['0x79', 'y'],
                              ['0x7a', 'z'],
                              ['0x7b', '{'],
                              ['0x7c', '|'],
                              ['0x7d', '}'],
                              ['0x7e', '~'],
                              ['0x7f', '^?'],
                              ['0x80', ''],
                              ['0x81', ''],
                              ['0x82', ''],
                              ['0x83', ''],
                              ['0x84', ''],
                              ['0x85', ''],
                              ['0x86', ''],
                              ['0x87', ''],
                              ['0x88', ''],
                              ['0x89', ''],
                              ['0x8a', ''],
                              ['0x8b', ''],
                              ['0x8c', ''],
                              ['0x8d', ''],
                              ['0x8e', ''],
                              ['0x8f', ''],
                              ['0x90', ''],
                              ['0x91', ''],
                              ['0x92', ''],
                              ['0x93', ''],
                              ['0x94', ''],
                              ['0x95', ''],
                              ['0x96', ''],
                              ['0x97', ''],
                              ['0x98', ''],
                              ['0x99', ''],
                              ['0x9a', ''],
                              ['0x9b', ''],
                              ['0x9c', ''],
                              ['0x9d', ''],
                              ['0x9e', ''],
                              ['0x9f', ''],
                              ['0xa0', ''],
                              ['0xa1', '¡'],
                              ['0xa2', '¢'],
                              ['0xa3', '£'],
                              ['0xa4', '¤'],
                              ['0xa5', '¥'],
                              ['0xa6', '¦'],
                              ['0xa7', '§'],
                              ['0xa8', '¨'],
                              ['0xa9', '©'],
                              ['0xaa', 'ª'],
                              ['0xab', '«'],
                              ['0xac', '¬'],
                              ['0xad', '\xad'],
                              ['0xae', '®'],
                              ['0xaf', '¯'],
                              ['0xb0', '°'],
                              ['0xb1', '±'],
                              ['0xb2', '²'],
                              ['0xb3', '³'],
                              ['0xb4', '´'],
                              ['0xb5', 'µ'],
                              ['0xb6', '¶'],
                              ['0xb7', '·'],
                              ['0xb8', '¸'],
                              ['0xb9', '¹'],
                              ['0xba', 'º'],
                              ['0xbb', '»'],
                              ['0xbc', '¼'],
                              ['0xbd', '½'],
                              ['0xbe', '¾'],
                              ['0xbf', '¿'],
                              ['0xc0', 'À'],
                              ['0xc1', 'Á'],
                              ['0xc2', 'Â'],
                              ['0xc3', 'Ã'],
                              ['0xc4', 'Ä'],
                              ['0xc5', 'Å'],
                              ['0xc6', 'Æ'],
                              ['0xc7', 'Ç'],
                              ['0xc8', 'È'],
                              ['0xc9', 'É'],
                              ['0xca', 'Ê'],
                              ['0xcb', 'Ë'],
                              ['0xcc', 'Ì'],
                              ['0xcd', 'Í'],
                              ['0xce', 'Î'],
                              ['0xcf', 'Ï'],
                              ['0xd0', 'Ð'],
                              ['0xd1', 'Ñ'],
                              ['0xd2', 'Ò'],
                              ['0xd3', 'Ó'],
                              ['0xd4', 'Ô'],
                              ['0xd5', 'Õ'],
                              ['0xd6', 'Ö'],
                              ['0xd7', '×'],
                              ['0xd8', 'Ø'],
                              ['0xd9', 'Ù'],
                              ['0xda', 'Ú'],
                              ['0xdb', 'Û'],
                              ['0xdc', 'Ü'],
                              ['0xdd', 'Ý'],
                              ['0xde', 'Þ'],
                              ['0xdf', 'ß'],
                              ['0xe0', 'à'],
                              ['0xe1', 'á'],
                              ['0xe2', 'â'],
                              ['0xe3', 'ã'],
                              ['0xe4', 'ä'],
                              ['0xe5', 'å'],
                              ['0xe6', 'æ'],
                              ['0xe7', 'ç'],
                              ['0xe8', 'è'],
                              ['0xe9', 'é'],
                              ['0xea', 'ê'],
                              ['0xeb', 'ë'],
                              ['0xec', 'ì'],
                              ['0xed', 'í'],
                              ['0xee', 'î'],
                              ['0xef', 'ï'],
                              ['0xf0', 'ð'],
                              ['0xf1', 'ñ'],
                              ['0xf2', 'ò'],
                              ['0xf3', 'ó'],
                              ['0xf4', 'ô'],
                              ['0xf5', 'õ'],
                              ['0xf6', 'ö'],
                              ['0xf7', '÷'],
                              ['0xf8', 'ø'],
                              ['0xf9', 'ù'],
                              ['0xfa', 'ú'],
                              ['0xfb', 'û'],
                              ['0xfc', 'ü'],
                              ['0xfd', 'ý'],
                              ['0xfe', 'þ'],
                              ['0xff', 'ÿ'],
                              ['0x20', ' ']]
                converted_chars = []
                for char in self.raw_data:
                    for byte_char in byte_table:
                        if byte_char[1] == char:
                            converted_chars.append(byte_char[0])
                            break
                converted_bytes_binary = []
                for part in converted_chars:
                    hex_as_int = int(part, 16)
                    hex_as_binary = bin(hex_as_int)[2:]
                    binary_raw_data = '%0*d' % (8, int(hex_as_binary))  # 8 bit binary
                    converted_bytes_binary.append(binary_raw_data)
                encoded_data = converted_bytes_binary
            elif self.mode_type == "Kanji":
                converted_kanji = []
                for char in self.raw_data:
                    raw_byte = str(bytes(char, 'shift-jis'))
                    converted_byte = '0x' + str(raw_byte[4:-1]).upper().replace('\\', '').replace('X', '')
                    converted_byte_dec = int(converted_byte, 16)
                    converted_byte_new = ""
                    if 33088 < converted_byte_dec < 40956:  # from 0x8140 to 0x9FFC
                        converted_byte_new = "{0:#0{1}x}".format(converted_byte_dec - 33088,
                                                                 6)  # subtracting 0x8140 from char
                    elif 57408 < converted_byte_dec < 60351:  # from 0xE040 to 0xEBBF
                        converted_byte_new = "{0:#0{1}x}".format(converted_byte_dec - 49472,
                                                                 6)  # subtracting 0xC140 from char
                    else:
                        print(f'this kanji character "{char}" is not supported')
                        return None
                    most_significant = "0x" + converted_byte_new[2:4]
                    least_significant = "0x" + converted_byte_new[4:]
                    converted_multiplied = "{0:#0{1}x}".format(
                        (int(most_significant, 16) * 192) + int(least_significant, 16), 6)  # 0xC0 192
                    bin_kanji = (bin(int(converted_multiplied, 16))[2:].zfill(13))
                    converted_kanji.append(bin_kanji)
                encoded_data = ''.join(converted_kanji)
        return encoded_data

    def find_terminator(self):
        if self.version is not None and self.error_correction is not None and self.mode_indicator is not None and self.character_count_indicator is not None and self.encoded_data is not None:

            for entry in self.error_correction_table:
                if str(entry[0]) == str(self.version) and str(entry[1]) == str(self.error_correction):
                    total_number_multiply = int(entry[2]) * 8
                    chars_left = total_number_multiply - int(
                        len(self.mode_indicator) + len(self.character_count_indicator) + sum(
                            len(s) for s in self.encoded_data))
                    if chars_left == 0:
                        terminator = ''
                    elif chars_left == 1:
                        terminator = "0"
                    elif chars_left == 2:
                        terminator = "00"
                    elif chars_left == 3:
                        terminator = "000"
                    elif chars_left == 4:
                        terminator = "0000"
                    else:
                        terminator = "0000"
                    return terminator, total_number_multiply
        return None, None

    def pad_data(self):
        codewords_data = None
        if self.maximum_size is not None and self.version is not None and self.error_correction is not None and self.mode_indicator is not None and self.character_count_indicator is not None and self.encoded_data is not None and self.terminator is not None:
            unpadded_string = self.mode_indicator + self.character_count_indicator + ''.join(
                self.encoded_data) + self.terminator
            bytes_left = 8 - (len(unpadded_string) % 8)
            padded_string = unpadded_string + '0' * bytes_left  # adding additional 0 if string length is not multiply of 8
            padded_length = len(padded_string)
            if padded_length != self.maximum_size:
                endbyte_0 = "11101100"  # 11101100 -> if string is still not max size, add following bytes till the end. (236)
                endbyte_1 = "00010001"  # 00010001 -> if string is still not max size, add following bytes till the end. (17)
                space_left = int((self.maximum_size - padded_length) / 8)
                for x in range(space_left):
                    if x % 2 == 0:
                        padded_string = padded_string + endbyte_0
                    else:
                        padded_string = padded_string + endbyte_1
            codewords_data = [padded_string[i:i + 8] for i in
                              range(0, len(padded_string), 8)]  # splitting string into 8bits codewrods
        return codewords_data

    def codewords(self):
        self.size = 37
        self.version = 5
        self.error_correction = "Q"
        self.padded_data = ['01000011',
                            '01010101',
                            '01000110',
                            '10000110',
                            '01010111',
                            '00100110',
                            '01010101',
                            '11000010',
                            '01110111',
                            '00110010',
                            '00000110',
                            '00010010',
                            '00000110',
                            '01100111',
                            '00100110',
                            '11110110',
                            '11110110',
                            '01000010',
                            '00000111',
                            '01110110',
                            '10000110',
                            '11110010',
                            '00000111',
                            '00100110',
                            '01010110',
                            '00010110',
                            '11000110',
                            '11000111',
                            '10010010',
                            '00000110',
                            '10110110',
                            '11100110',
                            '11110111',
                            '01110111',
                            '00110010',
                            '00000111',
                            '01110110',
                            '10000110',
                            '01010111',
                            '00100110',
                            '01010010',
                            '00000110',
                            '10000110',
                            '10010111',
                            '00110010',
                            '00000111',
                            '01000110',
                            '11110111',
                            '01110110',
                            '01010110',
                            '11000010',
                            '00000110',
                            '10010111',
                            '00110010',
                            '00010000',
                            '11101100',
                            '00010001',
                            '11101100',
                            '00010001',
                            '11101100',
                            '00010001',
                            '11101100']

        for entry in self.error_correction_table:
            if self.version is not None and self.error_correction is not None and self.padded_data is not None:
                if int(entry[0]) == int(self.version) and entry[1] == self.error_correction:
                    total_codewords = int(entry[2])
                    EC_codewords_per_block = int(entry[3])
                    blocks_in_group_1 = int(entry[4])
                    data_codewords_in_group_1 = int(entry[5])
                    try:
                        blocks_in_group_2 = int(entry[6])
                        data_codewords_in_group_2 = int(entry[7])
                    except Exception:
                        blocks_in_group_2 = 0
                        data_codewords_in_group_2 = 0
                    if blocks_in_group_2 == 0:
                        codeword_groups_count = 1
                    else:
                        codeword_groups_count = 2
                    if len(self.padded_data) == total_codewords:
                        codeword_groups = []
                        numbers_groups = []
                        EC_groups = []

                        current_codesword = 0
                        for group in range(codeword_groups_count):
                            codeword_blocks = []
                            numbers_blocks = []
                            EC_blocks = []
                            if group == 0:
                                max_blocks = blocks_in_group_1
                                max_codewords = data_codewords_in_group_1
                            else:
                                max_blocks = blocks_in_group_2
                                max_codewords = data_codewords_in_group_2
                            for block in range(max_blocks):
                                codeword_temp_block = []
                                numbers_temp_block = []
                                for block_entry in range(max_codewords):
                                    codeword_temp_block.append(self.padded_data[current_codesword])
                                    numbers_temp_block.append(int(self.padded_data[current_codesword], 2))
                                    current_codesword += 1

                                EC_values = ReedSolomon(numbers_temp_block, EC_codewords_per_block).RSEncode()

                                codeword_blocks.append(codeword_temp_block)
                                numbers_blocks.append(numbers_temp_block)
                                EC_blocks.append(EC_values)
                            codeword_groups.append(codeword_blocks)
                            numbers_groups.append(numbers_blocks)
                            EC_groups.append(EC_blocks)
                        return codeword_groups, numbers_groups, EC_groups
        return None, None, None

    def interleave(self):
        remainder_bits_table = [[1, 0],
                                [2, 7],
                                [3, 7],
                                [4, 7],
                                [5, 7],
                                [6, 7],
                                [7, 0],
                                [8, 0],
                                [9, 0],
                                [10, 0],
                                [11, 0],
                                [12, 0],
                                [13, 0],
                                [14, 3],
                                [15, 3],
                                [16, 3],
                                [17, 3],
                                [18, 3],
                                [19, 3],
                                [20, 3],
                                [21, 4],
                                [22, 4],
                                [23, 4],
                                [24, 4],
                                [25, 4],
                                [26, 4],
                                [27, 4],
                                [28, 3],
                                [29, 3],
                                [30, 3],
                                [31, 3],
                                [32, 3],
                                [33, 3],
                                [34, 3],
                                [35, 0],
                                [36, 0],
                                [37, 0],
                                [38, 0],
                                [39, 0],
                                [40, 0]]

        if self.version is not None and self.error_numbers is not None and self.EC_codewords is not None:
            remainder_bits = 0
            for entry in remainder_bits_table:
                if int(entry[0]) == self.version:
                    remainder_bits = int(entry[1])
            interleaved_numbers = self.block_interleave(self.error_numbers)
            interleaved_codewords = self.block_interleave(self.EC_codewords)
            combined_messages = interleaved_numbers + interleaved_codewords
            binary_str = ''
            for value in combined_messages:
                binary_str += f'{value:08b}'
            for x in range(remainder_bits):
                binary_str += '0'
            return binary_str
        else:
            return None

    @staticmethod
    def block_interleave(data):
        matrix = []
        highest_length = 0
        for group in data:
            for block in group:
                if len(block) > highest_length:
                    highest_length = len(block)
                matrix.append(block)
        rows = len(matrix)
        columns = highest_length
        matrix_T = []
        for j in range(columns):
            row = []
            for i in range(rows):
                try:
                    row.append(matrix[i][j])
                except Exception:
                    pass
            matrix_T.append(row)
        interleaved_data = [j for sub in matrix_T for j in sub]
        return interleaved_data

    def SaveToFile(self, filepath, scale, dpi, block_color, background_color):
        GenerateBMP(self.output_matrix, filepath, scale, dpi, block_color, background_color)


if __name__ == "__main__":
    for data in input_str:
        #                                7%   15%  25%  30%
        # input string, error_correction['L', 'M', 'Q', 'H']
        qr = QR_code(data, 'M')
        qr.show_complex_info()
        #qr.show_basic_info()
        # <str>   ,<int> ,<int>                  ,<tuple>                  ,<tuple>
        # filename, scale, dpi (inches per meter), block color (r, g, b, a), background color (r, g, b, a)
        qr.SaveToFile("output.bmp", 5, 2835, (200, 40, 40, 255), (255, 255, 255, 255))


