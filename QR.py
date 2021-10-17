from QRtoBMP import GenerateBMP
from QRinfo import QRinfo
from QRplacement import QRplacement
from QRencoding import QRencoding


class QR_code:
    def __init__(self, input_data, correction_type):

        raw_data = input_data

        ##################  QR CODE TYPE  ####################
        mode_type, \
        mode_indicator, \
        error_correction, \
        version, \
        size, \
        character_count_indicator = QRinfo(input_data, correction_type).getINF0()
        #######################################################

        ################ QR MESSAGE ENCODING ##################
        encoded_data, \
        terminator, \
        maximum_size, \
        padded_data, \
        broken_codewords, \
        error_numbers, \
        ec_codewords, \
        final_message = QRencoding(raw_data,
                                   mode_type,
                                   mode_indicator,
                                   error_correction,
                                   version,
                                   size,
                                   character_count_indicator).getEncodedData()
        #######################################################

        ################ QR MATRIX GENERATION #################
        QRgenerator = QRplacement(version, correction_type, size, final_message)
        self.module_matrix = QRgenerator.generateVisualMatrix()
        self.output_matrix = QRgenerator.generateBinaryMatrix()
        ########################################################

        self.simple_info = {"input_data": raw_data,
                            "mode": mode_type,
                            "version": version,
                            "error_correction": error_correction,
                            "size": size}

        self.complex_info = {"input_data": raw_data,
                             "mode": mode_type,
                             "mode_indicator": mode_indicator,
                             "version": version,
                             "error_correction": error_correction,
                             "size": size,
                             "character_count_indicator": character_count_indicator,
                             "encoded_data": encoded_data,
                             "terminator": terminator,
                             "maximum_size": maximum_size,
                             "padded_data": padded_data,
                             "broken_codewords": broken_codewords,
                             "error_numbers": error_numbers,
                             "ec_codewords": ec_codewords,
                             "final_message": final_message
                             }

    def print_matrix(self, binary):
        if binary:
            printed_matrix = self.output_matrix
        else:
            printed_matrix = self.module_matrix
        for column in printed_matrix:
            buffer = ' '
            for element in column:
                buffer += str(str(element) + '  ')
            print(buffer)

    def show_complex_info(self):
        print('')
        print(f'version: {self.complex_info["version"]}')
        print(f'error correction: {self.complex_info["error_correction"]}')
        print(f'mode: {self.complex_info["mode"]}')
        print(f'size: {self.complex_info["size"]}x{self.complex_info["size"]} matrix')
        print(f'mode indicator : {self.complex_info["mode_indicator"]}')
        print(f'character count indicator: {self.complex_info["character_count_indicator"]}')
        print(f'terminator: {self.complex_info["terminator"]}')
        print(f'data : {self.complex_info["input_data"]}')
        print(f'encoded data: {self.complex_info["encoded_data"]}')
        print(f'padded_data: {self.complex_info["padded_data"]}')
        print(f'codewords groups: {self.complex_info["broken_codewords"]}')
        print(f'error correction numbers: {self.complex_info["error_numbers"]}')
        print(f'error correction codewords: {self.complex_info["ec_codewords"]}')
        print(f'final message: {self.complex_info["final_message"]}')
        print(f'module matrix:')
        print('')
        self.print_matrix(False)
        print('')

    def show_basic_info(self):
        print('')
        print(f'data: {self.simple_info["raw_data"]}')
        print(f'version: {self.simple_info["version"]}')
        print(f'error correction: {self.simple_info["error_correction"]}')
        print(f'mode: {self.simple_info["mode_type"]}')
        print(f'size : {self.simple_info["size"]}x{self.simple_info["size"]} matrix')
        print('')

    def SaveToFile(self, filepath, scale, dpi, block_color, background_color):
        GenerateBMP(self.output_matrix, filepath, scale, dpi, block_color, background_color)
