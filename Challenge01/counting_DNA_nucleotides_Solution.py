def dna(s):
  s = s.strip()
  
  a = s.count("A")
  c = s.count("C")
  g = s.count("G")
  t = s.count("T")
return f"{a} {c} {g} {t}"

def main():
  dna_string = input()
  print(dna(dna_string))

main()
