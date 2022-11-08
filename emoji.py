emojis ={
    ":)" : "😁",
    ":(" : "😢"
}


user_input = input(">")
#emoji converter
def emoji_converter(user):
    words = user.split(" ")
    output = ""
    for i in words:
        output += emojis.get(i, f"{i} ")
    return(output)


print(emoji_converter(user_input))