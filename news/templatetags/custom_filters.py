from django import template


register = template.Library()

censored_list = ['yuioefjhg', 'uigdh', 'iuhjgcxtrdyuy']

@register.filter()
def censor(s):
    words = s.split(' ')
    for word_num in range(len(words)):
        if words[word_num].lower() in censored_list:
            if type(words[word_num]) is not str:
                raise TypeError('Censored word must be a string')
            for sym_num in range(1, len(words[word_num])):
                words[word_num] = words[word_num].replace(words[word_num][sym_num], "*")
    s = ' '.join(words)
    return s
