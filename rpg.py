
import random

character={}
character['name'] = input("What is the character's name? ")
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']
character['class'] = random.choice(classes)
races = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling']
character['race'] = random.choice(races)
abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

def generateAbilityScores():
    for n in abilities:
        ability = n
        abilityScore = random.randrange(3, 18)
        character[ability] = abilityScore
        print("pack" .format(ability) .format(abilityScore))
        if abilityScore < 13:
            abilityIncrease = input("Este valor de habilidade está abaixo de 13, então você pode aumentar seu valor se desejar. Insira um número de 0 a 5 para aumentar esta habilidade nessa quantidade:" )
            if abilityIncrease not in ['0', '1', '2', '3', '4', '5']:
                abilityIncrease = 0
                print("Você não selecionou um aumento entre 0 e 5. Nenhuma alteração feita.")
            abilityIncrease = int(abilityIncrease)
            if abilityIncrease < 0:
                abilityIncrease = 0
                print("Vamos mantê-lo entre 0 e 5, certo? Limite inferior de 0 selecionado.")
            elif abilityIncrease > 5:
                abilityIncrease = 5
                print("Vamos mantê-lo entre 0 e 5, certo? Limite superior de 5 selecionado.")
            abilityScore = abilityScore + abilityIncrease
            character[ability] = abilityScore
            print(ability, abilityScore)

generateAbilityScores()

print(character.items())
availableSkills = ['Alchemy', 'Animal empathy', 'Appraise', 'Balance', 'Bluff', 'Climb', 'Concentration', 'Craft', 'Decipher Script', 'Diplomacy', 'Disable Device', 'Disguise', 'Escape Artist', 'Forgery']
skillRanks = 4
