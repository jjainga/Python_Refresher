emojis ={
    ":)" : "😁",
    ":(" : "😢"
}

#emoji converter
def emoji_converter(user):
    words = user.split(" ")
    output = ""
    for i in words:
        output += emojis.get(i, f"{i} ")
    return(output)


user_input = input(">")
print(emoji_converter(user_input))