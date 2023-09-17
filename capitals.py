##### 9.7 Challenge: Capital City Loop #####
import random
capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}
state_list = list()
for state in capitals_dict:
    state_list.append(state)
state_name = random.choice(state_list)
capital = input(f"Enter the capital of the state {state_name} or exit: ")
while capital.lower() != capitals_dict[state_name].lower() and capital.lower() != 'exit':
    capital = input(f"Enter the capital of the state {state_name}: ")
if capital.lower() == capitals_dict[state_name].lower() :
    print("Correct")
else :
    print("Goodbye")