print("Papagaiļa instrukcija")
print("Cik daudz ir jādod papagailim graudus atkarīgi no laika")
print("Cik ir pulkstiens?")
pulkstiens = int(input())
if (pulkstiens >= 0 ) and (pulkstiens <= 9):
  pulkstiens = 10
  print(str(pulkstiens) + "g")
if (pulkstiens > 10 ) and (pulkstiens <= 13):
  pulkstiens1 = 30
  print(str(pulkstiens1) + "g")
if (pulkstiens > 13 ) and (pulkstiens <= 23):
  pulkstiens2 = 50
  print(str(pulkstiens2) + "g")
print("Kāda ir jūsu istabas temperatūra?")
temperatura = int(input())
if (temperatura >= 18 ) and (temperatura <= 25):
  print(str(temperatura) + " ir komforta temperatura ")
if (temperatura > -10 ) and (temperatura < 18):
  print(str(temperatura) + " ir auksta tempeatura ")
if (temperatura > 25 ) and (temperatura <= 35):
  print(str(temperatura) + " ir karsta temperatura ")
print("Cik bieži jūs nedeļa tīrat papgaiļu buri?")
reizes = int(input())
if (reizes >= 2 ) and (reizes <= 3):
  print(str(reizes) + " ir labi")
if (reizes >= 4 ) and (reizes <= 10):
  print(str(reizes) + " ir padaudz")
if (reizes >= 0 ) and (reizes <= 1):
  print(str(reizes) + " ir pamaz")