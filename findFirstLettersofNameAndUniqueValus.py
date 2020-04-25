def find_letter(pair):
    if pair[1]%2==0:
        return chr(((pair[0]-96+pair[1])%26)+96)
    d = pair[0]-96-pair[1]
    if d<0:
        d=26+d
    return chr(96+d)

def main():
    t=int(input())
    for i in range(t):
        strchk=input()
        secretkey = input()
        taketogether = zip([ord(i) for i in strchk],[int(j) for j in secretkey])
        final_string = map(find_letter,taketogether)
        print(''.join(final_string))

main()
