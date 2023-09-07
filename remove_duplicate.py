'''get a list and remove the duplicate
'''
def remove_duplicate(list_in):
  ordered_list = list(dict.fromkeys(list_in))
  return ordered_list
