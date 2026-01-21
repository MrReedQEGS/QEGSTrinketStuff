#Trace tables example...
weights = [270,250,300,120]
total = 0
heavy = 0
light = 0

HEAVY_LIMIT = 250
#250 or more is heavy

for w in weights:
  if(w >= HEAVY_LIMIT):
    heavy = heavy + 1
  else:
    light = light + 1
  
  total = total + w

print(total,heavy,light)
  
  
  
