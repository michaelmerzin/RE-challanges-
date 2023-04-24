
def find_key():
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                for l in range(97, 123):
                    for m in range(97, 123):
                        for n in range(97, 123):
                            s = chr(i) + 'a' + 'a' + chr(j) + 'a' + chr(k) + chr(l) + 'a' + 'a' + chr(m) + chr(n)
                            if algorthm_for_key(s) == 0x660:
                                return s
    return None


def algorthm_for_key(name):
    var1 = ord(name[9]) - ord(name[10])
    var2 = ord(name[5]) - ord(name[3])
    var3 = ord(name[6]) - ord(name[0])
    help = (var1 * var1) + (var2 * var3 * 0x88)
    return help


if __name__ == '__main__':
    print(find_key())


