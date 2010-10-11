import re

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim=u'-'):
    result = []
    for word in _punct_re.split(text.lower()):
        if word:
            result.append(word)
    return unicode(delim.join(result))
