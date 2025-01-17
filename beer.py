#function to calculate the time required to get sober if you drink just beer (0.5 litres) in Czech Republic
def sober_calc(sex, body_weight, drink_volume):
    beer_alcohol_content = 5
    if sex == "f":
        beta = 0.085
    if sex == "m":
        beta = 0.1

    alcohol_mass = (drink_volume * beer_alcohol_content * 0.8)/100
    degraded_alcohol_mass = body_weight * beta
    sober_time = round(alcohol_mass / degraded_alcohol_mass,2)
    
    print(f"You are supposed to be sober in {sober_time} hours. I am really sorry darling, but you just have to wait. Don't drink and drive!")

# Aaaaaand action"
sex = input("Hello darling, nice to see you! Are you a female or a male(f/m)?: ")
body_weight = float(input("Pardon my impertinence, but how much do you weight(in kilograms, please)?: "))
drink_volume = float(input("And how many large beers did you have?: "))*500

sober_calc(sex, body_weight, drink_volume)