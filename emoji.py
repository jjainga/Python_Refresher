emojis ={
    ":)" : "😁",
    ":(" : "😢"
}


#emoji converter
def emoji_converter():
    user_input = input(">")
    words = user_input.split(" ")
    output = ""
    for i in words:
        output += emojis.get(i, f"{i} ")
    print(output)
emoji_converter()