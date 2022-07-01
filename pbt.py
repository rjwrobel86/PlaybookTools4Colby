
import pandas as pd

df = pd.read_csv("~/Code/Schmitt/PlaybookTools/Playbook_Manifest.csv", index_col=False)
df = df[['First Name', 'Last Name', 'Salutation', 'Address Line1', 'City', 'State', 'Zip Code', 'Home Phone', 'Cell Phone', 'Email', 'Targeted VIN', 'Year', 'Make', 'Model', 'Purchased During Promotion', 'Sales Person Name', 'Customer Type', ' Loyalty Points', ' My Rewards Member', ' Offer Amount',' Oil Life', ' Opt In for Dealer Maintenance Network']]

dfsmall = df[['First Name','Last Name','City','Zip Code','Cell Phone','Home Phone', 'Email']]
dfsmall.to_csv('~/Code/Schmitt/PlaybookTools/dfsmall.csv')

#Based on Rewards Membership
df_rewards = df[df[' My Rewards Member'] == " Y "]
df.sort_values(by=' Loyalty Points', ascending=False)
df_rewards.to_csv("~/Code/Schmitt/PlaybookTools/rewardsmembers.csv")

#Based on Oil Life
df_50pct = df[df[' Oil Life'] == " 40.1 Percent - 50 Percent " ]
df_50pct.to_csv("~/Code/Schmitt/PlaybookTools/50pct.csv")
df_40pct = df[df[' Oil Life'] == " 30.1 Percent - 40 Percent " ]
df_40pct.to_csv("~/Code/Schmitt/PlaybookTools/40pct.csv")
df_30pct = df[df[' Oil Life'] == " 20.1 Percent - 30 Percent " ]
df_30pct.to_csv('~/Code/Schmitt/PlaybookTools/30pct.csv')
df_20pct = df[df[' Oil Life'] == " 10.1 Percent - 20 Percent " ]
df_20pct.to_csv("~/Code/Schmitt/PlaybookTools/20pct.csv")
df_10pct = df[df[' Oil Life'] == " 10 Percent or Less "]
df_10pct.to_csv('~/Code/Schmitt/PlaybookTools/10pct.csv')

#Based on Risk of Losing Customer
df_atrisk = df[df['Customer Type']== " At Risk "] 
df_atrisk.to_csv("~/Code/Schmitt/PlaybookTools/atrisk.csv")

#Based on "labor op code"
df_laboropcode = df[df['Labor Op Code']] >= 1]
df_laboropcode.to_csv("~Code/Schmitt/PlaybookTools/laboropcode.csv")
