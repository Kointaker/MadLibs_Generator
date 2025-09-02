# MadLibs Generator
import time
from tqdm import tqdm

print("Welcome to DiddyLibs")

name = input("Whats your name pretty boy? ")

age = int(input("Whats your age little one? "))

if age < 18:
    print("A minor I see\n")
    for i in tqdm(range(250), desc="Booting", ascii=False, ncols=75):
        time.sleep(0.0029)



thing = f"""
Your name is 







"""