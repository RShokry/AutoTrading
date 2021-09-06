import pandas as pd
df1 = pd.read_csv("volum_profil_sefty.csv")

df2 = pd.read_csv("zscorvwap_sefty.csv")


frames = [df1, df2]

result = pd.concat(frames)
pd.set_option('chained',None)
SUM = sum(result["ALL_PROFITS"])

result["ALL_PROFITS"][0] = SUM
print(result)



