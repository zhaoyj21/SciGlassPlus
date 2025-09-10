from SciGlassPlus.load import SGP, available_columns


print("start")

df_all = SGP()
columnNames = available_columns()
elements_cfg = {
    "drop": ["Ca"],
    "keep": ["Si", "O"]
}
compounds_cfg = {
    "drop": ["CaO"],
    "keep": ["SiO2", "Al2O3"]
}
properties_cfg = {
    "drop": ["T1"],
    "keep": ["T2", "T3"]
}
metadata_cfg = {
    "drop": ["Emails"],
    "keep": ["Authors", "Doi"]
}
df_filtered = SGP(elements_cfg=elements_cfg,
                  compounds_cfg=compounds_cfg,
                  properties_cfg=None,
                  metadata_cfg=None)

print("end")
