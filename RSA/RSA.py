import math
import time
import binascii

def matrix_overview(BB, bound):
    for ii in range(BB.dimensions()[0]):
        a = ('%02d ' % ii)
        for jj in range(BB.dimensions()[1]):
            a += '0' if BB[ii,jj] == 0 else 'X'
            a += ' '
        if BB[ii, ii] >= bound:
            a += '~'
        print(a)

def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    if not 0 < beta <= 1:
        raise ValueError("beta should belongs in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    BB = BB.LLL()

    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    potential_roots = new_pol.roots()
    if debug:
        print("potential roots are : ", potential_roots)
        
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    return roots

e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 72280435426334165577906189315110628880055142007534628220204498542417850323439380695887128510826008333689415816181297256599643506547848427759484281941594887877927643024429257508583153927539192545668261754691203601209822683806409405203755032942453511813573393521853565080168506271518611097581393536125145348497

ZmodN = Zmod(N);

def break_RSA(M_str, max_length_x):
    global e, C, ZmodN

    M_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in M_str])

    for length_x in range(0, max_length_x+1, 4):

        P.<x> = PolynomialRing(ZmodN)
        pol = ((int(M_binary_str, 2)<<length_x) + x)^e - C
        dd = pol.degree()

        #########
        beta = 1                                # b = N
        epsilon = beta / 7                      # <= beta / 7
        mm = ceil(beta**2 / (dd * epsilon))     # optimized value
        tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
        XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

        if roots:
            print("Length of Root is : ", length_x)
            root = '{0:b}'.format(roots[0])
            print("Root without padding : ", root)
            print("\n")
            
            print("\nThe obtained codeword after padding with zero is : ")
            print(('0'*(8-len(root)%8) + root))
            print("\n")
            
            # pswd=0
            # i=0
            # for temp in root:
            #     pswd += (-('0'-temp))<<(len(root)-1-i)
            #     pswd << 1
            #     i=i+1
            # print("\nFinal password : ", binascii.b2a_uu(pswd))
            # print("\n")
            
            print("Convert the above codeword to ASCII to get the password!")
            return

    print('No solution found\n')

if __name__ == "__main__":
    break_RSA("Cicadas: This door has RSA encryption with exponent 5 and the password is ", 300)
    