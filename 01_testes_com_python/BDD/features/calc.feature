# language: pt

#Behave

Funcionalidade: Calc
	Cenario: da soma basica
		Quando somar "2" com "2"
		Entao o resultado deve ser "4"
		
	Cenario: adicao do ponto flutuante
		Quando somar "2.0" com "2.0"
		Entao o resultado deve ser "4.0"	
