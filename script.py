import random

def generate_password(max_len: int = 18) -> str:

	""" 
		Функция генерирования пароля. Принимает опцианальный 
		параметр max_len - длина пароля, по умолчанию 18 символов. 
	"""

	symbols = '?&$#@!()*abcdefghijklmnopqrstuvwxyz' 

	symbols = tuple(symbols + symbols[9::].upper() + ''.join(map(str, [i for i in range(10)]))) 

	return ''.join(random.sample(symbols, max_len)) 



print(generate_password())