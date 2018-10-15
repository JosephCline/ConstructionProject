Material = ["wood","stone","brick","gravel","sand","plywood\n"]
Material2 = 4
Material.append("aluminum sheet")
Material.insert(Material2,"ironsheet")
print(len(Material))
print(Material.index("wood"))
print(not"stonebrick" in Material)
if "stonebrick" in Material:
    print(len(Material2))
if "garage door" in str(Material2):
    print("We have a garage door")
else:
    print("We don't have a garage door")
print(Material)
