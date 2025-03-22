import kagglehub

# Laster ned nyeste versjonen til datasettet fra Tyskland 
pathGermany = kagglehub.dataset_download("l3llff/wind-power")

print("Path to dataset files:", pathGermany)