#decrypt this cipher: _mdkgem(\g(\`m(PGZ(@mdd([mzam{&(Ngz(|`m(Fmp|(k`iddmfom(qg}(add(fmml(|g(lmkglm(|`a{(kax`mz( eiqjm(qg}(fmml(|g(lmkglm(a|(nzge(ji{m><(naz{|!2(ke=}iecoF\^#i@F{nrZ1lP^1lf08mP^;FPprlf09nb]zm;I}[Opn8{;Y8`]l_9?kPda]]F1De|IA;B8_PlY_Pk9j@F'j[^ylfEfC55(In|mz(lmkglm(a|$(Lg(PGZ(gf(a|&(J}|(|`a{(|aem(m(lgf|(`i~m(i({xmkanak(cmq$(|`m(cmq(kg}dl(jm(ifq(f}ejmz(jm|mmf(9(|g(<8(2!
def xor_operation(char, key):
    return chr( ord(char) ^ key )

def encrypt_message(input_string, key=22):
    
    xor_chars = [xor_operation(char, key) for char in input_string]
    
   
    cipher = ''.join(xor_chars)
    return cipher


input_string = "B~e6awe6byy6sweo6pyd6oyc6~c~)6Xsnb6b{s61zz6{w}s6cxtdsw}wtzs6uf~sd"


result = encrypt_message(input_string)  
print(result)

#hint: 
#message ^ key = cipher
#cipher ^ key = message






