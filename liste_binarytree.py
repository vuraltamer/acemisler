import re, sys
from classBinarytree import *

def kok_yerlestir(liste,tree): #listede tek eleman olacak.
	if len(liste)>0 and liste[0]<tree.getRootVal():
		if tree.getLeftChild()!=None:
			kok_yerlestir(liste,tree.getLeftChild())
				
		else:
			tree.insertLeft(liste.pop(0))
			kok_yerlestir(liste,tree) 
	if len(liste)>0 and liste[0]>tree.getRootVal():
		if tree.getRightChild()!=None:
			kok_yerlestir(liste,tree.getRightChild())
		else:
			tree.insertRight(liste.pop(0))
			kok_yerlestir(liste,tree)
			
################################

def liste_binarytree_yap(liste,tree):
	if len(liste)>0:
		kok_yerlestir([liste.pop(0)],tree)
		liste_binarytree_yap(liste,tree)

################################

#a=BinaryTree(12)
#liste_binarytree_yap([19,15,20,7,2,9],a)


#print a.getRootVal()
#print a.getLeftChild().getRootVal(),"<>",a.getRightChild().getRootVal()
#print a.getLeftChild().getLeftChild().getRootVal(),":",a.getLeftChild().getRightChild().getRootVal(),"<>",a.getRightChild().getLeftChild().getRootVal(),":",a.getRightChild().getRightChild().getRootVal()
