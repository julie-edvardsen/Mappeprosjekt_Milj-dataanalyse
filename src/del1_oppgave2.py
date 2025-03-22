import kagglehub

# Laster ned nyeste versjonen til datasettet fra Tyskland 
pathGermany = kagglehub.dataset_download("l3llff/wind-power")
# Laster ned nyeste versjonen til datasettet fra Tyrkia 
pathTurkey = kagglehub.dataset_download("berkerisen/wind-turbine-scada-dataset")

print("Path to dataset files:", pathGermany)

print("Path to dataset files:", pathTurkey)