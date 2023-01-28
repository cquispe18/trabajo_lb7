import re

def split_and_join(string):
	# Divida la cadena usando una expresión regular para que coincida con cualquier secuencia de caracteres no alfabéticos como delimitador
	split_string = re.split(r'[^a-zA-Z]', string)

	# Unir la lista de cadenas con un carácter '-' entre ellas
	joined_string = ''
	for i, s in enumerate(split_string):
		if i > 0:
			joined_string += '-'
		joined_string += s
	
	return split_string, joined_string

# Probar la función
string = 'Geeks for Geeks'
split_string, joined_string = split_and_join(string)
print(split_string)
print(joined_string)
