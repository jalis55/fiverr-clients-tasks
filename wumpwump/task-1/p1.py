def main():
    word1 = 'macaroni'
    word2 = 'scuba diving'
    word3 = 'soggy'
    word4 = 'flowery'
    ringo(word3, word4)
    george(word1, word2)
def george(alpha, bravo):
    print('%s is majoring in %s.' % (alpha, bravo))
def ringo(charlie, foxtrot):
    print("What doesn't kill you makes you %s" % foxtrot)
    print('Stand a little %s' % charlie)
main()