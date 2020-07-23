def add_to_dict(korean={}, key="", value=""):   
  if type(korean) == str:
      print(f"You need to send a dictionary. You sent: {type(korean)}")
  elif type(korean) == dict and type(value) == str:
      if not value:
          print(f"You need to send a word a definition")
  elif type(korean) == dict and len(key) != 0 and len(value):


my_english_dict = {}
    
print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")