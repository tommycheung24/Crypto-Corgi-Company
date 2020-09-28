from cisc108 import assert_equal

def main():
    """
    Main function that calls all the other functions and provides
    an crypto experience
    """
#Asks if the user wants to encrpyt text or decrypt text
    user_input = input("Do you want to encrypt or decrypt?")    
#if the user typed "encrypt"   
    if user_input == "encrypt":
        message = input("Please enter the message that you want to encrypt:")
        print(encrypt_text(message,2,2))
        print(hash_text(message,31,1000000000))
#if the user typed "decrypt"    
    elif user_input == "decrypt":
        message = input("Please enter the encrypted message that you want the decrypt:")
        decrypted_text = decrypt_text(message,2,2)
        expected_hash = (hash_text(decrypted_text,31,1000000000))
        input_hash = int(input("Please enter the hash number:"))
#Compares the input hash and the expected hash      
        if input_hash == expected_hash:
            print(decrypted_text)
        else:
            print("error")
    else:
        print("error")
        
def convert_str(message: str) -> [int]:
    """
    This function consumes a message and converts it
    into a list of integers using a for loop and ord.
    
    Args:
        message(str): the message that the user inputs
    Returns:
        [int]: a list of integers that comes from the ord command and the for loop

    """
    new_list = []
    for character in message:
        new_list.append(ord(character))
    return new_list

assert_equal(convert_str("ABC"), [65,66,67])
assert_equal(convert_str("EFABC"), [69,70,65,66,67])
assert_equal(convert_str("EFDABC"), [69,70,68,65,66,67])


def shift_list(number_list: [int], shift: int)-> [int]:
    """
    This function consumes a list of numbers and a
    shift number and shifts the list of number by that amount.
    
    Args:
        number_list([int]): consumes a list of numbers
        shift(int): consumes a number that represents the amount of shifting
    Returns:
        ([int]): returns a list of numbers that has been shifted
        
    """
    new_list = number_list[-shift:] + number_list[0:-shift]
    return new_list

assert_equal(shift_list([14,15,16,17], 1),[17,14,15,16])
assert_equal(shift_list([14,15,16,17], 2),[16,17,14,15])
assert_equal(shift_list([14,15,16,17], 7),[14,15,16,17])


def rotate_list(a_shift_list: [int], rotation: int)-> [int]:
    """
    This function consumes a list of numbers and a rotation amount
    and produce a rotated list of numbers by that amount.
    
    Args:
        shift_list([int]): a list of numbers that is about to be rotated
        rotation(int): a number that represent the amount of rotation
    Returns:
        ([int]): return a list of number that has been rotated

    """
    new_list = []
    for number in a_shift_list:
        new_list.append(((number+rotation-32) % 94 + 32))
    return new_list

assert_equal(rotate_list([67],1),[68])
assert_equal(rotate_list([67],2),[69])
assert_equal(rotate_list([67],3),[70])


def append_value(a_rotate_list: [int]) -> [int]:
    """
    This function consumes a list of numbers and produce a list of
    numbers with ASCII value 126 after every integer less than 48.
    
    Args:
        rotate_list([int]): a list of number that is about to be modified
    Returns:
        ([int]): a list of integers that adds 126 after every number lees than 48
    """
    new_list = []
    for number in a_rotate_list:
        if number < 48:
            new_list.append(number)
            new_list.append(126)
        else:
            new_list.append(number)
    return new_list

assert_equal(append_value([45,49,50]),[45,126,49,50])
assert_equal(append_value([45,49,0,50]),[45,126,49,0,126,50])
assert_equal(append_value([]),[])


def convert_int(an_append_list:[int]) -> str:
    """
    This function consumes a list of numbers and produces a string
    that is converted from the list of numbers
    
    Args:
        append_list([int]): a list of numbers that is about to change to a string
    Returns:
        (str): a string that comes from the chr function
        
    """
    new_string = ""
    for number in an_append_list:
        new_string = new_string + chr(number)
    return new_string

assert_equal(convert_int([65,66,67]),"ABC")
assert_equal(convert_int([65,66,67,61]),"ABC=")
assert_equal(convert_int([65,66,67,61,69]),"ABC=E")


def remove_tilde(a_number_list:[int])->[int]:
    """
    This function consumes a list of numbers and produces a new
    list of numbers without the value 126
    
    Args:
        number_list([int]): a list of numbers that is about to change
    Returns:
        ([int]): a list of numbers without 126
    """
    new_list = []
    for number in a_number_list:
        if number != 126:
            new_list.append(number)
    return new_list

assert_equal(remove_tilde([124,125,126,127]), [124,125,127])
assert_equal(remove_tilde([126]), [])
assert_equal(remove_tilde([]), [])

def encrypt_text(message: str, shift: int, rotation: int) -> str:
    """
    This function consumes a string and two integers(shift and rotation),
    converts the string into list of numbers,
    encrypts them, and produces a string of encrypted text. 
    
    Args:
        message(str): the message that the user inputs
        shift(int): the number of spaces that a string is going to shift over
        rotation(int): the amount of rotation that a character is going to rotate
    Returns:
        (str): the encrypted text
    
    """
    number_list = convert_str(message)
    a_shift_list = shift_list(number_list, shift)
    a_rotate_list = rotate_list(a_shift_list , rotation)
    an_append_list = append_value(a_rotate_list)
    encrypted_message = convert_int(an_append_list)
    return encrypted_message

assert_equal(encrypt_text("A",1,1),"B")
assert_equal(encrypt_text("B",2,1),"C")
assert_equal(encrypt_text("A",1,2),"C")

def decrypt_text(message:str, shift: int, rotation: int) -> str:
    """
    This function consumes a encrypted text and and two integers(shift and rotation),
    
    decrypts them. and produces a string of decrypted text
    
    Args:
        message(str): the encrypted text
        shift(int): the number of spaces that a strings is going to shift
        rotation(int): the amount of rotation that a character is going to rotate
    Returns:
        (str): the decrypted text
        
    """
    a_number_list = convert_str(message)
    a_shift_list = remove_tilde(a_number_list)
    number_list = rotate_list(a_shift_list, -1*(rotation))
    an_append_list = shift_list(number_list, -1*(shift))
    decrypted_message = convert_int(an_append_list)
    return decrypted_message

assert_equal(decrypt_text("B",1,1),"A")
assert_equal(decrypt_text("C",1,2),"A")
assert_equal(decrypt_text("C",1,1),"B")

def hash_text(any_text: str, base: int, hash_size: int) -> int:
    """
    This function consumes any text and the base and hash size and
    produces an integer that attempts to represent the text
    
    Args:
        any_text(str): a string that is given by the user
        base(int): a number representing the base
        hash_size(int): a number representing the size of the hash
    Returns:
        (int): an integer that attempts to represent the text
    
    """
    new_list = convert_str(any_text)
#A for loop to get the index
#A for loop to tranform the original integer to the new integer
    transform_list = []
    count = -1
    for number in new_list:
        count = count + 1
        transform_list.append(((count + base) ** (number)))
#A for loop to sum up the transform list
    total = 0
    for number in transform_list:
        total = total + number
    return (total % hash_size)


assert_equal(hash_text("ABC",1,1), 0)
assert_equal(hash_text("I like",30, 100000), 82549)
assert_equal(hash_text("I like",30, 100), 49)


if __name__ == '__main__':
    main()