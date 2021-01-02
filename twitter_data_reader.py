project_twitter_data_file = open("project_twitter_data.csv", "r")
resulting_data_file = open("resulting_data.csv","w")


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of positive words
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


#list of negative words

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(s):
    for c in punctuation_chars:
        s = s.replace(c,"")
    return s


def get_pos( s ):
    s = strip_punctuation(s)
    s = s.lower()
    st = s.split()
    count = 0
    for c in st:
        for word in positive_words:
            if c == word:
                 count = count + 1
    return count


def get_neg( strsentence ):
    strsentence = strip_punctuation(strsentence)
    strsentence = strsentence.lower()
    temp = strsentence.split()
    count = 0
    for word in temp:
        for tem in negative_words:
            if word == tem:
                count = count + 1
    return count

def write_in_file( resulting_data_file):
    resulting_data_file.write( "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score" )
    resulting_data_file.write("\n")

    lines = project_twitter_data_file.readlines()
    lines.pop(0)
    for line in lines:
        line = line.strip().split(',')

        resulting_data_file.write('{},{},{},{},{}'.format(line[1], line[2], get_pos(line[0]), get_neg(line[0]), ( get_pos(line[0])-get_neg(line[0]) )))
        resulting_data_file.write('\n')


write_in_file(resulting_data_file)
project_twitter_data_file.close()
resulting_data_file.close()
