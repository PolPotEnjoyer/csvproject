import pandas as pd

df = pd.read_csv("students.csv")

def search():

    print(df.loc[df[input("input column: ")] == input("input desired content: ")])

def menu():
    print("s to search.")
    choice = input("")
    if choice == "s":
        search()

menu()