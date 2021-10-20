class QRplacement():
    def __init__(self, version, correction_type, size, message):
        self.version = version
        self.correction_type = correction_type
        self.size = size
        self.final_message = message

        self.none_mark = '%'
        self.white_mark = '░'
        self.black_mark = '█'
        self.reserved_mark = '╳'

        self.alignment_pattern_location_table = [[2, 6, 18, None, None, None, None, None],
                                                 [3, 6, 22, None, None, None, None, None],
                                                 [4, 6, 26, None, None, None, None, None],
                                                 [5, 6, 30, None, None, None, None, None],
                                                 [6, 6, 34, None, None, None, None, None],
                                                 [7, 6, 22, 38, None, None, None, None],
                                                 [8, 6, 24, 42, None, None, None, None],
                                                 [9, 6, 26, 46, None, None, None, None],
                                                 [10, 6, 28, 50, None, None, None, None],
                                                 [11, 6, 30, 54, None, None, None, None],
                                                 [12, 6, 32, 58, None, None, None, None],
                                                 [13, 6, 34, 62, None, None, None, None],
                                                 [14, 6, 26, 46, 66, None, None, None],
                                                 [15, 6, 26, 48, 70, None, None, None],
                                                 [16, 6, 26, 50, 74, None, None, None],
                                                 [17, 6, 30, 54, 78, None, None, None],
                                                 [18, 6, 30, 56, 82, None, None, None],
                                                 [19, 6, 30, 58, 86, None, None, None],
                                                 [20, 6, 34, 62, 90, None, None, None],
                                                 [21, 6, 28, 50, 72, 94, None, None],
                                                 [22, 6, 26, 50, 74, 98, None, None],
                                                 [23, 6, 30, 54, 78, 102, None, None],
                                                 [24, 6, 28, 54, 80, 106, None, None],
                                                 [25, 6, 32, 58, 84, 110, None, None],
                                                 [26, 6, 30, 58, 86, 114, None, None],
                                                 [27, 6, 34, 62, 90, 118, None, None],
                                                 [28, 6, 26, 50, 74, 98, 122, None],
                                                 [29, 6, 30, 54, 78, 102, 126, None],
                                                 [30, 6, 26, 52, 78, 104, 130, None],
                                                 [31, 6, 30, 56, 82, 108, 134, None],
                                                 [31, 6, 30, 56, 82, 108, 134, None],
                                                 [32, 6, 34, 60, 86, 112, 138, None],
                                                 [33, 6, 30, 58, 86, 114, 142, None],
                                                 [34, 6, 34, 62, 90, 118, 146, None],
                                                 [35, 6, 30, 54, 78, 102, 126, 150],
                                                 [36, 6, 24, 50, 76, 102, 128, 154],
                                                 [37, 6, 28, 54, 80, 106, 132, 158],
                                                 [38, 6, 32, 58, 84, 110, 136, 162],
                                                 [39, 6, 26, 54, 82, 110, 138, 166],
                                                 [40, 6, 30, 58, 86, 114, 142, 170]]

        self.matrix = [[self.none_mark for i in range(self.size)] for j in range(self.size)]

        self.reserved_matrix = None

    def add_finder_pattern(self, local_matrix, position):
        for y in range(7):
            for x in range(7):
                if y == 0 or y == 6:
                    local_matrix[position[1] + y][position[0] + x] = self.black_mark
                else:
                    if x == 0 or x == 6:
                        local_matrix[position[1] + y][position[0] + x] = self.black_mark
                    else:
                        local_matrix[position[1] + y][position[0] + x] = self.white_mark
                if y in range(2, 5) and x in range(2, 5):
                    local_matrix[position[1] + y][position[0] + x] = self.black_mark
        return local_matrix

    def add_separators(self, local_matrix):
        for y in range(self.size):
            for x in range(self.size):
                if (x == 7 or x == self.size - 8) and y in range(0, 7):
                    local_matrix[y][x] = self.white_mark
                if x == 7 and y in range(self.size - 7, self.size):
                    local_matrix[y][x] = self.white_mark
                if y == 7 and (x in range(0, 8) or x in range(self.size - 8, self.size)):
                    local_matrix[y][x] = self.white_mark
                if y == self.size - 8 and x in range(0, 8):
                    local_matrix[y][x] = self.white_mark
        return local_matrix

    def add_alignment_pattern(self, local_matrix):
        if self.version == 1:
            return local_matrix
        for entry in self.alignment_pattern_location_table:
            if int(self.version) == int(entry[0]):
                pos_log = entry[1:]
                all_poses = []
                for point_a in pos_log:
                    for point_b in pos_log:
                        if point_a is not None and point_b is not None:
                            all_poses.append([point_a, point_b])
                for pos in all_poses:
                    temp_matrix = list(map(list, local_matrix))
                    pos_offset = [pos[0] - 2, pos[1] - 2]
                    override = False
                    for y in range(5):
                        for x in range(5):
                            if temp_matrix[pos_offset[1] + y][pos_offset[0] + x] != self.none_mark:
                                override = True
                            if y == 0 or y == 4:
                                temp_matrix[pos_offset[1] + y][pos_offset[0] + x] = self.black_mark
                            else:
                                if x == 0 or x == 4:
                                    temp_matrix[pos_offset[1] + y][pos_offset[0] + x] = self.black_mark
                                else:
                                    temp_matrix[pos_offset[1] + y][pos_offset[0] + x] = self.white_mark
                            if y == 2 and x == 2:
                                temp_matrix[pos_offset[1] + y][pos_offset[0] + x] = self.black_mark
                    if not override:
                        local_matrix = temp_matrix
        return local_matrix

    def add_timing_pattern(self, local_matrix):
        for y in range(self.size):
            for x in range(self.size):
                if x == 6 and local_matrix[y][x] == self.none_mark:
                    if y % 2 == 0:
                        local_matrix[y][x] = self.black_mark
                    else:
                        local_matrix[y][x] = self.white_mark

                if y == 6 and local_matrix[y][x] == self.none_mark:
                    if x % 2 == 0:
                        local_matrix[y][x] = self.black_mark
                    else:
                        local_matrix[y][x] = self.white_mark

        return local_matrix

    def add_reserved_area(self, local_matrix):
        for y in range(self.size):
            for x in range(self.size):
                if local_matrix[y][x] == self.none_mark:
                    if x == 8 and (y in range(0, 9) or y in range(self.size - 8, self.size)):
                        local_matrix[y][x] = self.reserved_mark
                    if y == 8 and (x in range(0, 8) or x in range(self.size - 8, self.size)):
                        local_matrix[y][x] = self.reserved_mark
                    if int(self.version) >= 7:
                        if x in range(self.size - 8 - 3, self.size - 8) and y in range(0, 6):
                            local_matrix[y][x] = self.reserved_mark
                        if y in range(self.size - 8 - 3, self.size - 8) and x in range(0, 6):
                            local_matrix[y][x] = self.reserved_mark

        return local_matrix

    def add_data_bits(self, local_matrix):
        # white pixels for zero, black pixels for ones
        converted_chars = []
        for character in self.final_message:
            if character == '1':
                converted_chars.append(self.black_mark)
            elif character == '0':
                converted_chars.append(self.white_mark)

        free_matrix = []

        for x in range(self.size - 1, -1, -1):
            local_line = []
            for y in range(self.size - 1, -1, -1):
                if local_matrix[y][x] == self.none_mark:
                    local_line.append([y, x])
            if len(local_line) > 0:
                free_matrix.append(local_line)

        free_matrix_inverted = []

        for x in range(int(len(free_matrix) / 2)):
            first_line = list(free_matrix[x * 2])
            second_line = list(free_matrix[(x * 2) + 1])
            if x % 2 == 0:
                free_matrix_inverted.append(first_line)
                free_matrix_inverted.append(second_line)
            else:
                free_matrix_inverted.append(list(reversed(first_line)))
                free_matrix_inverted.append(list(reversed(second_line)))

        message_coords = []

        for x in range(int(len(free_matrix) / 2)):
            line_len = [len(free_matrix[x * 2]), len(free_matrix[(x * 2) + 1])]
            line_len_full = len(free_matrix[x * 2]) + len(free_matrix[(x * 2) + 1])

            first_line = list(free_matrix_inverted[x * 2])
            second_line = list(free_matrix_inverted[(x * 2) + 1])

            zig_zag = []

            '''for cell in range(max(line_len)):
                try:
                    print(f'{second_line[cell]}   {first_line[cell]}')
                    if first_line[cell][0] == second_line[cell][0]:
                        zig_zag.append(first_line[cell])
                        zig_zag.append(second_line[cell])
                    elif first_line[cell][0] < second_line[cell][0]:
                        pass
                except:
                    pass'''

            second_addition = 0
            first_addition = 0

            for cell in range(max(line_len)):
                try:
                    # print(f'{second_line[cell]}   {first_line[cell]}')
                    if first_line[cell + first_addition][0] == second_line[cell + second_addition][0]:
                        zig_zag.append(first_line[cell - second_addition])
                        zig_zag.append(second_line[cell - first_addition])
                    elif second_line[cell + second_addition][0] > first_line[cell + first_addition][0]:
                        zig_zag.append(second_line[cell])
                        second_addition += 1
                    elif second_line[cell + second_addition][0] < first_line[cell + first_addition][0]:
                        zig_zag.append(first_line[cell])
                        first_addition += 1
                except:
                    if len(first_line) > len(second_line):
                        try:
                            zig_zag.append(second_line[cell - first_addition])
                        except Exception:
                            pass

                        zig_zag.append(first_line[cell])
                    else:
                        try:
                            zig_zag.append(first_line[cell - second_addition])
                        except Exception:
                            pass

                        zig_zag.append(second_line[cell])

            message_coords.append(zig_zag)
        message_coords = list([j for sub in message_coords for j in sub])
        for coord in range(len(message_coords)):
            try:  # DONT WORK
                if self.final_message[coord] == '1':
                    character = self.black_mark
                else:
                    character = self.white_mark

                local_matrix[message_coords[coord][0]][message_coords[coord][1]] = character
            except:
                pass
        return local_matrix

    def choose_mask(self, local_matrix, reserved_matrix):
        penalty = []
        for mask in range(8):
            ############# EVALUATION 1 ################
            local_matrix = self.add_mask([row[:] for row in local_matrix], reserved_matrix, mask)
            score_1 = 0
            for y in range(self.size):
                y_penalty = 0
                last_bit = local_matrix[y][0]
                current_in_row = 1
                for x in range(1, self.size):
                    current_bit = local_matrix[y][x]
                    if last_bit == current_bit:
                        current_in_row += 1
                    else:
                        current_in_row = 1
                    if current_in_row == 5:
                        y_penalty += 3
                    if current_in_row > 5:
                        y_penalty += 1
                    last_bit = current_bit
                score_1 += y_penalty

            for x in range(self.size):
                x_penalty = 0
                last_bit = local_matrix[x][0]
                current_in_col = 1
                for y in range(1, self.size):
                    current_bit = local_matrix[y][x]
                    if last_bit == current_bit:
                        current_in_col += 1
                    else:
                        current_in_col = 1
                    if current_in_col == 5:
                        x_penalty += 3
                    if current_in_col > 5:
                        x_penalty += 1
                    last_bit = current_bit
                score_1 += x_penalty
            ##########################################
            ############# EVALUATION 2 ################
            score_2 = 0
            for y in range(self.size - 2):
                for x in range(self.size - 2):
                    current_mark = local_matrix[y][x]
                    width = []
                    for y_loc in range(y, self.size - 1):
                        for x_loc in range(x, self.size - 1):
                            if local_matrix[y_loc][x_loc] == current_mark or local_matrix[y_loc][
                                x_loc] == self.reserved_mark:
                                pass
                            else:
                                width.append(x_loc - x)
                                break
                        if len(width) == 0:
                            break
                        if width[-1] <= 1:
                            width.pop()
                            break
                        if len(width) > 1:
                            # print(f"{x,y} {x_loc,y_loc} {min(width)}x{len(width)} rectangle")
                            # print((min(width) - 1) * (len(width) - 1))
                            score_2 += 3
            ##########################################
            ############# EVALUATION 3 ################
            score_3 = 0
            search_pattern = [self.black_mark,
                              self.white_mark,
                              self.black_mark,
                              self.black_mark,
                              self.black_mark,
                              self.white_mark,
                              self.black_mark,
                              self.white_mark,
                              self.white_mark,
                              self.white_mark,
                              self.white_mark]

            for y in range(self.size - len(search_pattern) + 1):
                for x in range(self.size - len(search_pattern) + 1):

                    # x-forward
                    broken = False
                    for x_loc in range(len(search_pattern)):
                        if local_matrix[y][x + x_loc] != search_pattern[x_loc] and local_matrix[y][
                            x + x_loc] != self.reserved_matrix:
                            broken = True
                            break
                    if not broken:
                        # print(f"x-forward: {x,y}")
                        score_3 += 40
                    #############

                    # x-backward
                    broken = False
                    for x_loc in range(len(search_pattern)):
                        if local_matrix[y][x + x_loc] != search_pattern[len(search_pattern) - 1 - x_loc] and \
                                local_matrix[y][x + x_loc] != self.reserved_matrix:
                            broken = True
                            break
                    if not broken:
                        # print(f"x-backward: {x,y}")
                        score_3 += 40
                    #############

                    # y-forward
                    broken = False
                    for y_loc in range(len(search_pattern)):
                        if local_matrix[y + y_loc][x] != search_pattern[y_loc] and local_matrix[y + y_loc][
                            x] != self.reserved_matrix:
                            broken = True
                            break
                    if not broken:
                        # print(f"y-forward: {x,y}")
                        score_3 += 40
                    #############

                    # y-backward
                    broken = False
                    for y_loc in range(len(search_pattern)):
                        if local_matrix[y + y_loc][x] != search_pattern[len(search_pattern) - 1 - y_loc] and \
                                local_matrix[y + y_loc][x] != self.reserved_matrix:
                            broken = True
                            break
                    if not broken:
                        # print(f"y-backward: {x,y}")
                        score_3 += 40
                    #############

            ###########################################
            ############# EVALUATION 4 ################
            score_4 = 0
            total_modules = self.size * self.size
            dark_modules = 0
            for x in range(self.size):
                for y in range(1, self.size):
                    if local_matrix[y][x] == self.black_mark:
                        dark_modules += 1
            percent = (dark_modules / total_modules) * 100
            percent_round = [int((percent // 5) * 5), -int((-percent // 5) * 5)]
            absolute = [abs(percent_round[0] - 50), abs(percent_round[1] - 50)]
            divide = [int(val / 5) for val in absolute]
            score_4 = min(divide) * 10
            ###########################################
            loc_pen = score_1 + score_2 + score_3 + score_4
            penalty.append(loc_pen)
        val, idx = min((val, idx) for (idx, val) in enumerate(penalty))
        return idx

    def add_mask(self, local_matrix, reserved_matrix, mask_id):
        masks = [lambda _x, _y: (_x + _y) % 2 == 0,
                 lambda _x, _y: _y % 2 == 0,
                 lambda _x, _y: _x % 3 == 0,
                 lambda _x, _y: (_x + _y) % 3 == 0,
                 lambda _x, _y: ((_y // 2) + (_x // 3)) % 2 == 0,
                 lambda _x, _y: ((_x * _y) % 2) + ((x * _y) % 3) == 0,
                 lambda _x, _y: (((_x * _y) % 2) + ((_x * _y) % 3)) % 2 == 0,
                 lambda _x, _y: (((_x + _y) % 2) + ((_x * _y) % 3)) % 2 == 0]

        for y in range(self.size):
            for x in range(self.size):
                if masks[mask_id](x, y):
                    if reserved_matrix[y][x] == self.none_mark:
                        if local_matrix[y][x] == self.black_mark:
                            local_matrix[y][x] = self.white_mark
                        else:
                            local_matrix[y][x] = self.black_mark
        return local_matrix

    def add_format_string(self, local_matrix, mask_id):
        # list of coords for placing format string bits
        message_coords = [[[8, 0], [-1, 8]],
                          [[8, 1], [-2, 8]],
                          [[8, 2], [-3, 8]],
                          [[8, 3], [-4, 8]],
                          [[8, 4], [-5, 8]],
                          [[8, 5], [-6, 8]],
                          [[8, 7], [-7, 8]],
                          [[8, 8], [8, -8]],
                          [[7, 8], [8, -7]],
                          [[5, 8], [8, -6]],
                          [[4, 8], [8, -5]],
                          [[3, 8], [8, -4]],
                          [[2, 8], [8, -3]],
                          [[1, 8], [8, -2]],
                          [[0, 8], [8, -1]]]

        encoded_str = [0] * 15

        ##### ['ECC Level', 'Mask Pattern', 'Type Information Bits']
        format_str_table = [['L', '0', '111011111000100'],
                            ['L', '1', '111001011110011'],
                            ['L', '2', '111110110101010'],
                            ['L', '3', '111100010011101'],
                            ['L', '4', '110011000101111'],
                            ['L', '5', '110001100011000'],
                            ['L', '6', '110110001000001'],
                            ['L', '7', '110100101110110'],
                            ['M', '0', '101010000010010'],
                            ['M', '1', '101000100100101'],
                            ['M', '2', '101111001111100'],
                            ['M', '3', '101101101001011'],
                            ['M', '4', '100010111111001'],
                            ['M', '5', '100000011001110'],
                            ['M', '6', '100111110010111'],
                            ['M', '7', '100101010100000'],
                            ['Q', '0', '011010101011111'],
                            ['Q', '1', '011000001101000'],
                            ['Q', '2', '011111100110001'],
                            ['Q', '3', '011101000000110'],
                            ['Q', '4', '010010010110100'],
                            ['Q', '5', '010000110000011'],
                            ['Q', '6', '010111011011010'],
                            ['Q', '7', '010101111101101'],
                            ['H', '0', '001011010001001'],
                            ['H', '1', '001001110111110'],
                            ['H', '2', '001110011100111'],
                            ['H', '3', '001100111010000'],
                            ['H', '4', '000011101100010'],
                            ['H', '5', '000001001010101'],
                            ['H', '6', '000110100001100'],
                            ['H', '7', '000100000111011']]

        for entry in format_str_table:
            if entry[0] == self.correction_type and str(entry[1]) == str(mask_id):
                for c in range(len(entry[2])):
                    encoded_str[c] = int(entry[2][c])
                break

        # bits placement in matrix
        for i in range(len(encoded_str)):
            for cell in message_coords[i]:
                if encoded_str[i] == 0:
                    local_matrix[cell[0]][cell[1]] = self.white_mark
                elif encoded_str[i] == 1:
                    local_matrix[cell[0]][cell[1]] = self.black_mark
        return local_matrix

    def add_version_format(self, local_matrix):
        # ['Version', 'Version Information String']
        format_data = [['7', '000111110010010100'],
                       ['8', '001000010110111100'],
                       ['9', '001001101010011001'],
                       ['10', '001010010011010011'],
                       ['11', '001011101111110110'],
                       ['12', '001100011101100010'],
                       ['13', '001101100001000111'],
                       ['14', '001110011000001101'],
                       ['15', '001111100100101000'],
                       ['16', '010000101101111000'],
                       ['17', '010001010001011101'],
                       ['18', '010010101000010111'],
                       ['19', '010011010100110010'],
                       ['20', '010100100110100110'],
                       ['21', '010101011010000011'],
                       ['22', '010110100011001001'],
                       ['23', '010111011111101100'],
                       ['24', '011000111011000100'],
                       ['25', '011001000111100001'],
                       ['26', '011010111110101011'],
                       ['27', '011011000010001110'],
                       ['28', '011100110000011010'],
                       ['29', '011101001100111111'],
                       ['30', '011110110101110101'],
                       ['31', '011111001001010000'],
                       ['32', '100000100111010101'],
                       ['33', '100001011011110000'],
                       ['34', '100010100010111010'],
                       ['35', '100011011110011111'],
                       ['36', '100100101100001011'],
                       ['37', '100101010000101110'],
                       ['38', '100110101001100100'],
                       ['39', '100111010101000001'],
                       ['40', '101000110001101001']]

        message_coords = [[[0, -11], [-11, 0]],
                          [[0, -10], [-10, 0]],
                          [[0, -9], [-9, 0]],
                          [[1, -11], [-11, 1]],
                          [[1, -10], [-10, 1]],
                          [[1, -9], [-9, 1]],
                          [[2, -11], [-11, 2]],
                          [[2, -10], [-10, 2]],
                          [[2, -9], [-9, 2]],
                          [[3, -11], [-11, 3]],
                          [[3, -10], [-10, 3]],
                          [[3, -9], [-9, 3]],
                          [[4, -11], [-11, 4]],
                          [[4, -10], [-10, 4]],
                          [[4, -9], [-9, 4]],
                          [[5, -11], [-11, 5]],
                          [[5, -10], [-10, 5]],
                          [[5, -9], [-9, 5]]]
        encoded_str = [0] * 18
        for entry in format_data:
            if int(entry[0]) == int(self.version):
                encoded_str = list(entry[1])
                break
        # bits placement in matrix
        for i in range(len(encoded_str)):
            for cell in message_coords[i]:
                if int(encoded_str[i]) == 0:
                    local_matrix[cell[0]][cell[1]] = self.white_mark
                elif int(encoded_str[i]) == 1:
                    local_matrix[cell[0]][cell[1]] = self.black_mark
        return local_matrix

    def generateVisualMatrix(self):
        self.matrix = self.add_finder_pattern(self.matrix, [0, 0])
        self.matrix = self.add_finder_pattern(self.matrix, [(((int(self.version) - 1) * 4) + 21) - 7, 0])
        self.matrix = self.add_finder_pattern(self.matrix, [0, (((int(self.version) - 1) * 4) + 21) - 7])
        self.matrix = self.add_separators(self.matrix)
        self.matrix = self.add_alignment_pattern(self.matrix)
        self.matrix = self.add_timing_pattern(self.matrix)
        self.matrix[self.size - 8][8] = self.black_mark  # dark module
        self.matrix = self.add_reserved_area(self.matrix)
        self.reserved_matrix = list(map(list, self.matrix))
        self.matrix = self.add_data_bits(self.matrix)  # !!!!!!!!!!! not working correctly
        mask_id = self.choose_mask(self.matrix, self.reserved_matrix)
        self.matrix = self.add_mask(self.matrix, self.reserved_matrix, mask_id)
        self.matrix = self.add_format_string(self.matrix, mask_id)
        if int(self.version) >= 7:
            self.matrix = self.add_version_format(self.matrix)
        return self.matrix, mask_id

    def generateBinaryMatrix(self):
        bin_matrix = [[0 for col in range(self.size + 8)] for row in range(self.size + 8)]

        for y in range(self.size):
            for x in range(self.size):
                if self.matrix[y][x] == self.none_mark or self.matrix[y][x] == self.white_mark or \
                        self.matrix[y][
                            x] == self.reserved_mark:
                    bin_matrix[y + 4][x + 4] = 0
                elif self.matrix[y][x] == self.black_mark:
                    bin_matrix[y + 4][x + 4] = 1

        return bin_matrix
