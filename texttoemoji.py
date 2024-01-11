#create variables
unallowed = "ęóąśłżźćń"
translator = dict()

# define special characters #
translator["?"] = ":grey_question:"
translator[" "] = ":blue_square:"
translator["!"] = ":grey_exclamation:"
translator["."] = ":record_button:"
translator["#"] = ":hash:"
translator["@"] = ":monkey:"
translator["-"] = ":no_entry:"
# characters that is not converted to emoji #
translator["\n"] = "\n"
translator["\t"] = "      "

# define polish characters #
translator["ę"] = ":regional_indicator_e:"
translator["ó"] = ":regional_indicator_o:"
translator["ą"] = ":regional_indicator_a:"
translator["ś"] = ":regional_indicator_s:"
translator["ł"] = ":regional_indicator_l:"
translator["ż"] = ":regional_indicator_z:"
translator["ź"] = ":regional_indicator_z:"
translator["ć"] = ":regional_indicator_c:"
translator["ń"] = ":regional_indicator_n:"

# define numbers #
translator["0"] = ":zero:"
translator["1"] = ":one:"
translator["2"] = ":two:"
translator["3"] = ":three:"
translator["4"] = ":four:"
translator["5"] = ":five:"
translator["6"] = ":six:"
translator["7"] = ":seven:"
translator["8"] = ":eight:"
translator["9"] = ":nine:"

# convert #
def ConvertToEmoji(value):
    def get_longest_line_length(value):
        lines = value.split('\n')
        longest_line_length = max(len(line) for line in lines)
        return longest_line_length
    length = get_longest_line_length(value)
    message = []
    lines = value.split('\n')
    for line in lines:
        line = line.lower()
        for i in range(len(line)):
            if line[i].isalpha() and unallowed.find(line[i]) == -1:
                message.append(":regional_indicator_" + line[i] + ":")
            else:
                if translator.keys().__contains__(line[i]):
                    message.append(translator[line[i]])
                else:
                    message.append(":blue_square:")
        # Dodajemy :blue_square: na końcu każdej linii
        message.extend([":blue_square:"] * (length - len(line)))
        message.append("\n")
    return ' '.join(message)
