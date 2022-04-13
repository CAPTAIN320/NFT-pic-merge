from PIL import Image

group1 = [
  "./assets/sky/sky1.png",
  "./assets/sky/sky2.png",
  "./assets/sky/sky3.png",
  "./assets/sky/sky4.png",
  "./assets/sky/sky5.png",
]
group2 = [
  "./assets/sun/sun1.png",
  "./assets/sun/sun2.png",
  "./assets/sun/sun3.png",
  "./assets/sun/sun4.png",
  "./assets/sun/sun5.png",
]
group3 = [
  "./assets/mountains/mountains1.png",
  "./assets/mountains/mountains2.png",
  "./assets/mountains/mountains3.png",
  "./assets/mountains/mountains4.png",
  "./assets/mountains/mountains5.png",
  "./assets/mountains/mountains6.png",
  "./assets/mountains/mountains7.png",
  "./assets/mountains/mountains8.png",
  "./assets/mountains/mountains9.png",
  "./assets/mountains/mountains10.png",
]
group4 = [
  "./assets/clouds/clouds1.png",
]

group5 = [
  "./assets/castle roof/castle roof1.png",
  "./assets/castle roof/castle roof2.png",
  "./assets/castle roof/castle roof3.png",
  "./assets/castle roof/castle roof4.png",
  "./assets/castle roof/castle roof5.png",
]

group6 = [
  "./assets/castle wall/castle wall1.png",
  "./assets/castle wall/castle wall2.png",
  "./assets/castle wall/castle wall3.png",
  "./assets/castle wall/castle wall4.png",
  "./assets/castle wall/castle wall5.png",
]

group7 = [
  "./assets/castle base + arch/castle base + arch1.png",
  "./assets/castle base + arch/castle base + arch2.png",
  "./assets/castle base + arch/castle base + arch3.png",
  "./assets/castle base + arch/castle base + arch4.png",
  "./assets/castle base + arch/castle base + arch5.png",
]

group8 = [
  "./assets/trees/trees1.png",
  "./assets/trees/trees2.png",
  "./assets/trees/trees3.png",
  "./assets/trees/trees4.png",
  "./assets/trees/trees5.png",
  "./assets/trees/trees6.png",
]

group9 = [
  "./assets/birds/birds1.png",
]

counter = 0

def createImage(a,b,c,d,e,f,g,h,i,counter):
  first = group1[a]
  second = group2[b]
  third = group3[c]
  fourth = group4[d]
  fifth = group5[e]
  sixth = group6[f]
  seventh = group7[g]
  eight = group8[h]
  ninth = group9[i]


  image01 = Image.open(first).convert("RGBA")
  image02 = Image.open(second).convert("RGBA")
  image03 = Image.open(third).convert("RGBA")
  image04 = Image.open(fourth).convert("RGBA")
  image05 = Image.open(fifth).convert("RGBA")
  image06 = Image.open(sixth).convert("RGBA")
  image07 = Image.open(seventh).convert("RGBA")
  image08 = Image.open(eight).convert("RGBA")
  image09 = Image.open(ninth).convert("RGBA")


  intermediate = Image.alpha_composite(image01, image02)
  intermediate2 = Image.alpha_composite(intermediate,image03)
  intermediate3 = Image.alpha_composite(intermediate2,image04)
  intermediate4 = Image.alpha_composite(intermediate3,image05)
  intermediate5 = Image.alpha_composite(intermediate4,image06)
  intermediate6 = Image.alpha_composite(intermediate5,image07)
  intermediate7 = Image.alpha_composite(intermediate6,image08)
  intermediate8 = Image.alpha_composite(intermediate7,image09)




  name = "merged/" + str(counter) + ".png"
  intermediate8.save(name)


for a in range(5):
  for b in range(5):
    for c in range(10):
      for d in range(1):
        for e in range(5):
          for f in range(5):
            for g in range(5):
              for h in range(6):
                for i in range(1):
                  createImage(a,b,c,d,e,f,g,h,i,counter)
                  counter = counter + 1



