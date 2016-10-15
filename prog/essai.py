
class Arbre:
	def __init__(self,noeud,liste=[]):
		self.fils=liste
		self.noeud=noeud
	
	def fairestring(self):	#pas au point
		if self.isSheet():
			return str(self.noeud)
		else :
			for x in self.fils:
				return str(x.noeud)+x.fairestring()
			
	def isSheet(self):
		return (len(self.fils)==0)

	def parcourir(self):		#pas au point
		for arbre in self.fils:
			if arbre.isSheet():
				for fils in arbre.fils:
					print()
					parcourir(arbre.fils)
#			else:
				

if __name__=='__main__' :					
	a7=Arbre('A7')
	a6=Arbre('A6')
	a5=Arbre('A5')
	a4=Arbre('A4')
	a3=Arbre('A3',[a7])
	a2=Arbre('A2',[a5,a7])
	a1=Arbre('A1',[a2,a3,a4])
	a=Arbre('c,d,f',
			[Arbre('b,c,f',
					[Arbre('a,b,c'),Arbre('b,e,f')]),Arbre('')])

	print(a.fils[0].noeud)	
#	print(a1.fils[0].fils[0].noeud)
#	print(a5.isSheet()) 
	
	