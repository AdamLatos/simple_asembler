source = open("program.txt","r")
mcode = open('program.mc','w')

current_line = source.readline()
current_line = current_line.replace(',','')
current_line = current_line.replace(';','')
current_line = current_line.replace('\n','')
current_line = current_line.split(' ')
print(current_line)

def parse_line(line):
  parsed = {
    #'mov'  : mov
    'movi'  : movi(line)
    #'nop'   : nop
    #'jump'  : jump
    #'jumpi' : jumpi(line)
    #'jz'    : jz(line)
    #'jnz'   :
    #'add'   :
    #'addi'  : addi
    #'and'   : andd
    #'andi'  :
    #'load'  :
    #'loadi' :
  }
  return switcher.get(argument, '00106700')

def movi(line):
  Rd = parse_reg(line[1])
  imm = parse_imm(line[2])
  return '00168'+Rx+imm

def parse_reg(reg):
  return reg.replace('R','')

def parse_imm(imm):
  if "0x" in imm:
    return imm.lstrip('0x')
  elif "0b" in imm:
    t = int(imm.lstrip('0b'), 16)
    return str(t)
  else:
    return str(int(imm, 16))

parse_line(current_line)
print(parsed)

source.close()
mcode.close()