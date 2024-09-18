# c is text to be deciphered s is the cipher shift value
def decipher(c, s):
    original = ''
    for char in c:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Calculate the original ASCII value with wrap-around for uppercase letters
            char_num = ord(char) - s
            # Wrap-around if the new ASCII value is less than 'A'
            if char_num < 65:
                char_num = char_num + 26
            # Convert ASCII value back to character and add to result
            original = original + str(chr(char_num))
        else:
            # Non-uppercase letters (including lowercase and punctuation) are added as is
            original = original + char
    return original

# Initial shift value
s = 1
# Example cipher text
cipher = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'
# Loop through shift values until a sensible deciphered text is found
while True:
    # Decipher the text with the current shift value
    original = decipher(cipher, s)
    print(original)
    # Prompt the user to confirm if the deciphered text makes sense
    if input('Does the deciphered text make sense (Y/N): ').strip().upper() == 'Y':
        break
    # Increment the shift value for the next iteration
    s = s + 1
    # Loops s around incase the user missed it the first go through
    if s == 26:
        s = s - 26
print("Shift value was:", s)
print("The original quote was:", original)

'''
OUTPUT: Deciphered code makes sense at shift value 13

UY EQXRUET UYBMFUQZF MZP M XUFFXQ UZEQOGDQ U YMWQ YUEFMWQE U MY AGF AR OAZFDAX MZPMF FUYQE TMDP FA TMZPXQ NGF UR KAG OMZF TMZPXQ YQ MF YK IADEF FTQZ KAG EGDQ ME TQXXPAZF PQEQDHQ YQ MF YK NQEF YMDUXKZ YAZDAQ
Does the deciphered text make sense (Y/N): N
TX DPWQTDS TXALETPYE LYO L WTEEWP TYDPNFCP T XLVP XTDELVPD T LX ZFE ZQ NZYECZW LYOLE ETXPD SLCO EZ SLYOWP MFE TQ JZF NLYE SLYOWP XP LE XJ HZCDE ESPY JZF DFCP LD SPWWOZYE OPDPCGP XP LE XJ MPDE XLCTWJY XZYCZP
Does the deciphered text make sense (Y/N): N
SW COVPSCR SWZKDSOXD KXN K VSDDVO SXCOMEBO S WKUO WSCDKUOC S KW YED YP MYXDBYV KXNKD DSWOC RKBN DY RKXNVO LED SP IYE MKXD RKXNVO WO KD WI GYBCD DROX IYE CEBO KC ROVVNYXD NOCOBFO WO KD WI LOCD WKBSVIX WYXBYO
Does the deciphered text make sense (Y/N): N
RV BNUORBQ RVYJCRNWC JWM J URCCUN RWBNLDAN R VJTN VRBCJTNB R JV XDC XO LXWCAXU JWMJC CRVNB QJAM CX QJWMUN KDC RO HXD LJWC QJWMUN VN JC VH FXABC CQNW HXD BDAN JB QNUUMXWC MNBNAEN VN JC VH KNBC VJARUHW VXWAXN
Does the deciphered text make sense (Y/N): N
QU AMTNQAP QUXIBQMVB IVL I TQBBTM QVAMKCZM Q UISM UQABISMA Q IU WCB WN KWVBZWT IVLIB BQUMA PIZL BW PIVLTM JCB QN GWC KIVB PIVLTM UM IB UG EWZAB BPMV GWC ACZM IA PMTTLWVB LMAMZDM UM IB UG JMAB UIZQTGV UWVZWM
Does the deciphered text make sense (Y/N): N
PT ZLSMPZO PTWHAPLUA HUK H SPAASL PUZLJBYL P THRL TPZAHRLZ P HT VBA VM JVUAYVS HUKHA APTLZ OHYK AV OHUKSL IBA PM FVB JHUA OHUKSL TL HA TF DVYZA AOLU FVB ZBYL HZ OLSSKVUA KLZLYCL TL HA TF ILZA THYPSFU TVUYVL
Does the deciphered text make sense (Y/N): N
OS YKRLOYN OSVGZOKTZ GTJ G ROZZRK OTYKIAXK O SGQK SOYZGQKY O GS UAZ UL IUTZXUR GTJGZ ZOSKY NGXJ ZU NGTJRK HAZ OL EUA IGTZ NGTJRK SK GZ SE CUXYZ ZNKT EUA YAXK GY NKRRJUTZ JKYKXBK SK GZ SE HKYZ SGXORET SUTXUK
Does the deciphered text make sense (Y/N): N
NR XJQKNXM NRUFYNJSY FSI F QNYYQJ NSXJHZWJ N RFPJ RNXYFPJX N FR TZY TK HTSYWTQ FSIFY YNRJX MFWI YT MFSIQJ GZY NK DTZ HFSY MFSIQJ RJ FY RD BTWXY YMJS DTZ XZWJ FX MJQQITSY IJXJWAJ RJ FY RD GJXY RFWNQDS RTSWTJ
Does the deciphered text make sense (Y/N): N
MQ WIPJMWL MQTEXMIRX ERH E PMXXPI MRWIGYVI M QEOI QMWXEOIW M EQ SYX SJ GSRXVSP ERHEX XMQIW LEVH XS LERHPI FYX MJ CSY GERX LERHPI QI EX QC ASVWX XLIR CSY WYVI EW LIPPHSRX HIWIVZI QI EX QC FIWX QEVMPCR QSRVSI
Does the deciphered text make sense (Y/N): N
LP VHOILVK LPSDWLHQW DQG D OLWWOH LQVHFXUH L PDNH PLVWDNHV L DP RXW RI FRQWURO DQGDW WLPHV KDUG WR KDQGOH EXW LI BRX FDQW KDQGOH PH DW PB ZRUVW WKHQ BRX VXUH DV KHOOGRQW GHVHUYH PH DW PB EHVW PDULOBQ PRQURH
Does the deciphered text make sense (Y/N): N
KO UGNHKUJ KORCVKGPV CPF C NKVVNG KPUGEWTG K OCMG OKUVCMGU K CO QWV QH EQPVTQN CPFCV VKOGU JCTF VQ JCPFNG DWV KH AQW ECPV JCPFNG OG CV OA YQTUV VJGP AQW UWTG CU JGNNFQPV FGUGTXG OG CV OA DGUV OCTKNAP OQPTQG
Does the deciphered text make sense (Y/N): N
JN TFMGJTI JNQBUJFOU BOE B MJUUMF JOTFDVSF J NBLF NJTUBLFT J BN PVU PG DPOUSPM BOEBU UJNFT IBSE UP IBOEMF CVU JG ZPV DBOU IBOEMF NF BU NZ XPSTU UIFO ZPV TVSF BT IFMMEPOU EFTFSWF NF BU NZ CFTU NBSJMZO NPOSPF
Does the deciphered text make sense (Y/N): N
IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL ANDAT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS HELLDONT DESERVE ME AT MY BEST MARILYN MONROE
Does the deciphered text make sense (Y/N): Y
Shift value was: 13
'''
