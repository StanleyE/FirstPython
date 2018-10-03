# First Python Test!

print ("Hello World!")

def hal9000(name):
    creepyGreeting = 'Good morning... {}'.format(name)
    print (creepyGreeting)

def monsterMash(*name):
    invited = '{} have all been invited to the Monster Mash. '.format(name)
    total = 'In total {} have been invited'.format(len(name))
    print (invited + total)

hal9000('Dave')
hal9000('Cathy')
monsterMash('Dave', 'Stan', 'Micheal')