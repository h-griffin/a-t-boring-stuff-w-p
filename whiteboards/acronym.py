

def acronym(text):             # new york police department
    acronym = ''
    text.upper()               # NEW YORK POLICE DEPARTMENT
    words = text.split()       # [NEW, YORK, POLICE, DEPARTMENT]
    remove_words=['in', 'a', 'of', 'the', 'and']


    # first letter
    # append to acronym
    # join acronym

	for word in words:
		if word in remove_words:
			words.remove(word)
		    initials.append(words[word:0])

    return acronym


if __name__ == "__main__":
    acronym('new york police department')
