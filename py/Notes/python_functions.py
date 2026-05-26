## exmaple of proper List syntax
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]

# Syntax of standard "Slicing": 
#my_list[ start : stop : step ]

# Syntax of Omitting "Step Slicng": 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# Syntax of Step selection
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

# Synatax of Reverse Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]

# List Deletion (Use Del) 
def trim_strongholds(strongholds):
    del strongholds[0] # Deletes the first item from the list
    del strongholds[-2:] # Deletes the last 2 items from the list


## length function that shows the highest list item record
def get_last_index(inventory):
    return len(inventory) - 1

## Replace indexed list item absed on whether it matches the trigger (this case if 'Inventory' list has 'Iron Ore' in the 2nd slot it will update Iron Ore to Iron Bar
def smelt_ore(inventory):
    if inventory[1] == 'Iron Ore':
        inventory[1] = 'Iron Bar'
    return inventory

## Adds id's based on the number
def generate_user_list(num_of_users):
    player_ids = []
    for i in range(0, num_of_users):
        player_ids.append(i)
    return player_ids

## Removes the last item from the list every loop
    for i in range(0, len(inventory)):
        item = inventory.pop()

## Adds counter for each item in list, this can be used to show duplicates

    for i in range(0, len(items)):

        
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1

## adds highest item on list to Max_so_far

def find_max(nums):
    max_so_far = float("-inf")
    pass

    for nums in nums:
        if nums >= max_so_far: 
            max_so_far = nums
    return max_so_far


## adds numbers from list to another list if they are odd. this uses the Modulo "%", can be re-written to return whether a number is odd or even.
    for i in range(0, num):
        if i % 2 == 1:
            odd_numbers.append(i)


## Concat lists
total = [1, 2, 3] + [4, 5, 6]
# OR 
combined_list = list_1 + list_2 + list_3


## List Operations - Contains
    return weapon in top_weapons #Returns True if "weapon" is within "top_weapons" (False if not True)
    return weapon not in top_weapons #Returns False  if "weapon" is within "top_weapons" (True if not False)
## Tuples (Static Lists within lists)
    heroes = [
        ("Glorfindel", 2093,True), #The Tuple is containted within round brackets within the square brackets
        ("Gandalf",1054,False),
        ("Gimli",389,False),
        ("Aragorn",87,False)
    ]

## Reverse List
# new_list = []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    return new_list

# Filter out censored word, in this case "Dang"
def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for message in messages:
        words = message.split()
        good_words = []
        dangs = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
        filtered_messages.append(" ".join(good_words))
        num_dangs = len(dangs)
        dang_counts.append(num_dangs)

    return filtered_messages, dang_counts

#----------------------------------------------------------------------------#
## checks if item from recipe is in inventory, returns the % of missing items & returns a list of missing items
#----------------------------------------------------------------------------#
def check_ingredient_match(recipe, inventory):
    missing_item = []
    acquired_item = []

    for item in recipe:
        if item not in inventory:
            missing_item.append(item)  
        else:
            acquired_item.append(item)
            
            
    acquired_length = len(acquired_item)
    needed_length = len(recipe)

    missing_percentage = (acquired_length / needed_length) * 100
    return missing_percentage, missing_item
#----------------------------------------------------------------------------#
## adds item to unique list & unique set
#----------------------------------------------------------------------------#
    def remove_duplicates(spells):
    used_potion_spells = set() 
    unique_spells = []

    for i in spells: 
        if i not in used_potion_spells:
            unique_spells.append(i)
            used_potion_spells.add(i)
    return(unique_spells)
            
#----------------------------------------------------------------------------#
#Count Vowels used & return vowels used
#----------------------------------------------------------------------------#
    def count_vowels(text):
    counter = 0
    vowels = set()
    used_vowels = set()
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    
    for i in text:
        if i in vowels:
            counter += 1
            used_vowels.add(i)
    
    return counter, used_vowels
#----------------------------------------------------------------------------#
#removes ID's listed in both the first and second Ids
#----------------------------------------------------------------------------#
def find_missing_ids(first_ids, second_ids):
    first_ids = set(first_ids)
    second_ids = set(second_ids)
    third_ids = set()

    for i in first_ids:
        if i not in second_ids:
            third_ids.add(i)

    return third_ids

#----------------------------------------------------------------------------#
# combines the square from a list.
#----------------------------------------------------------------------------#
def area_sum(rectangles):
    square_response = 0
    for rect in rectangles:
        h = rect["height"]
        w = rect["width"]
        square = h * w
        square_response += square
    return square_response

#----------------------------------------------------------------------------#
# Concat's strings within list.
#----------------------------------------------------------------------------#
def join_strings(strings):
    string_list = ""
    for i in strings:
        if len(string_list) == 0:
            string_list = i 
        else:
            string_list = string_list +","+ i 
    return string_list
#----------------------------------------------------------------------------#
## Convert Binary to Numbers 
#----------------------------------------------------------------------------#

def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers = int(num_servers, 2)
    num_players = int(num_players, 2)
    num_admins = int(num_admins, 2)
    return num_servers, num_players, num_admins

#----------------------------------------------------------------------------#
# simple dicationary decleration & return
#----------------------------------------------------------------------------#

def get_character_record(name, server, level, rank):
    
    account_information = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": name + "#" + server
    }

    return account_information 

#----------------------------------------------------------------------------#
# dicationary process that counts duplicate values and returns the count
#----------------------------------------------------------------------------#
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        
        if enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 1
        else: 
            enemies_dict[enemy_name] += 1
    return enemies_dict
#----------------------------------------------------------------------------#
# dicationary process that returns the highest score
#----------------------------------------------------------------------------#
def get_top_scorer(scores):
    top_name = None
    top_score = None

    for name in scores:
        score = scores[name]
        if top_score is None or score > top_score:
            top_name = name
            top_score = score

    return top_name

#----------------------------------------------------------------------------#
# dicationary process that returns the lowest distance & includes clause for no inputs.
#----------------------------------------------------------------------------#
def get_most_common_enemy(enemies_dict):
    
    lowest_distance = None

    if len(enemies_dict) == 0:
        return lowest_distance

    else:
        for name in enemies_dict:
            distance = enemies_dict[name]
            if lowest_distance is None or distance > lowest_distance:
                closest_enemy = name
                lowest_distance = distance

    return closest_enemy
    
#----------------------------------------------------------------------------#
# dicationary updates count per item in dictionary, if its not already in inventory it adds 1 to inventory
#----------------------------------------------------------------------------#
def build_gem_inventory(picked_up):
    inventory = {}
    for gem in picked_up:
        if gem in inventory:
            inventory[gem] += 1
        else:
            inventory[gem] = 1
    return inventory

## Error documentation for Py: https://docs.python.org/3/library/exceptions.html

#----------------------------------------------------------------------------#
# Calls function and checks for varios errors 
  # Index Error returns: Index is too high
  # custom error for negative integers
  # Catch all error
#----------------------------------------------------------------------------#
def process_player_record(player_id):
    try:
        get_player_record(player_id)
        return get_player_record(player_id)
    except IndexError: # Index Error returns: Index is too high
        return "index is too high"
    except Exception as e: # Catch all error
            return str(e) 

def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed") # custom error for negative integers
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]
#----------------------------------------------------------------------------#
# Raises error handling when 1 variable that is expected to be larger is not.
# Otherwise if no error, function returns the difference.
#----------------------------------------------------------------------------#

def purchase_item(price, gold_available):
    if gold_available < price:
        raise Exception("not enough gold")
    return gold_available - price