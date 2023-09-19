
# object: any
# - this is to indicate that the param can accept any type of object

def all_thing_is_obj(object: any) -> int:
    if isinstance(type(object), list):
        print("List : " + str(type(object)))
    elif isinstance(type(object), tuple):
        print("Tuple : " + str(type(object)))
    elif isinstance(type(object), set):
        print("Set : " + str(type(object)))
    elif isinstance(type(object), dict):
        print("Dict : " + str(type(object)))
    elif isinstance(type(object), str):
        print(str(object) + " is in the kitchen : " + str(type(object)))
    else:
        print("Type not found")
    return (42)
