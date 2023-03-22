from django import template

register = template.Library()
censor_list = ["Байден", "редиска", "псина"]


@register.filter()
def censor(value):

    list_value = value.split()
    result = ""
    for word in list_value:
        if word in censor_list:
            word = f"{word[0]}{(len(word) - 1) * '*'}"
            result += f"{word} "
        else:
            result += f"{word} "

    return result
