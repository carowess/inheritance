import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow",12)

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())

## this one won't work bc you can't run a method from the subtype in the supertype
## print(primrose.get_petals())
