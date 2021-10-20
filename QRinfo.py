import QRvars

class QRinfo:
    def __init__(self, data, correction_type):
        if data is None or data == '':
            raise Exception("input string for qr code is empty")

        self.data = data
        self.mode_type, self.mode_indicator = self.data_analysis()
        self.error_correction = self.error_correction_check(correction_type)
        self.version, self.size = self.version_check()
        self.character_count_indicator = self.character_count_indicator_check()
    def getINF0(self):
        return self.mode_type, self.mode_indicator, self.error_correction, self.version, self.size, self.character_count_indicator

    @staticmethod
    def literate_assign(input_type):
        """
        :param input_type: QR code mode as string
        :return: literate assign of QR code text mode as int
        """
        formats = ["Numeric", "Alphanumeric", "Byte", "Kanji"]
        return formats.index(input_type)

    def data_analysis(self):
        formats = [["Numeric", "0001"], ["Alphanumeric", "0010"], ["Byte", "0100"],["Kanji", "1000"]]
        chars_set = [QRvars.digit, QRvars.alpha, QRvars.byte, QRvars.kanji]
        data = [formats[chars_set.index(key)] for key in chars_set if all(c in key for c in self.data)]
        if len(data) == 0:
            raise Exception("the input string contains characters that are not supported by any type of QR code")
        return [data[0][0], data[0][1]]

    @staticmethod
    def error_correction_check(correction_type):
        corrections_types = ['L', 'M', 'Q', 'H']
        if not all(c in corrections_types for c in correction_type):
            raise Exception(f"specified error correction type '{correction_type}' is not valid. choose from: {corrections_types}")
        return correction_type

    def version_check(self):
        """
        :return: size of qr in 'pixels' and qr version as int
        """
        smallest_version = 21  # 21x21pixels
        version_increment = 4  # each next version is 4 pixels larger

        # version, error, numeric, alphanumeric, byte, kanji
        version_table = QRvars.version_table

        if len(self.data) > int(version_table[-1][2 + self.literate_assign(self.mode_type)]):
            raise Exception("input string is to large! there is no QR version that support such a long string")

        for line in version_table:
            if line[1] == self.error_correction:
                if len(self.data) <= int(line[2 + self.literate_assign(self.mode_type)]):
                    version_level = line[0]
                    version_size = int(smallest_version) + (int(version_level) - 1) * int(version_increment)
                    return version_level, version_size
        raise Exception(f"an unusual error was detected while selecting version for input: '{self.data}' and correction level: '{self.error_correction}'")

    def character_count_indicator_check(self):
        """
        :return: count indicator that will be placed at the beginning of encoded data
        """
        # numeric, alphanumeric, byte, kanji
        versions_table_1_9 = [10, 9, 8, 8]
        versions_table_10_26 = [12, 11, 16, 10]
        versions_table_27_40 = [14, 13, 16, 12]

        long = 0
        if 1 <= int(self.version) <= 9:
            long = versions_table_1_9[self.literate_assign(self.mode_type)]
        elif 10 <= int(self.version) <= 26:
            long = versions_table_10_26[self.literate_assign(self.mode_type)]
        elif 27 <= int(self.version) <= 40:
            long = versions_table_27_40[self.literate_assign(self.mode_type)]

        return '%0*d' % (long, int(bin(len(self.data))[2:]))

