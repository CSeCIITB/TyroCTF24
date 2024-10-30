from PIL import Image

input_potato_plant =  'my_potato.png'
output_potato_plant = 'output_potato.png' 

potato = Image.open(input_potato_plant)

potato = potato.convert('RGB')

buds, sprouts = potato.size

chips = potato.load()

for bud in range(buds // 2):
    for sprout in range(sprouts // 2):

        new_bud = buds - 1 - bud
        new_sprout = sprouts - 1 - sprout

        temp_chip = chips[bud, sprout]

        chips[bud, sprout] = chips[new_bud, new_sprout]
        chips[new_bud, new_sprout] = temp_chip

potato.save(output_potato_plant)

print(f"potato saved successfullsprout as {output_potato_plant}!")
