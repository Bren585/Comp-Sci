# -*- coding: utf-8 -*-
def returnM(mMit,mDmg,mit):
	if mit == 'mag':
		mit = 'res'
	else: 
		mit = 'def'
	print 'Glimmer deals more damage up until %d ' % mMit + str(mit) + '.'
	print 'After %d ' % mMit + str(mit) + ' Moonbow deals more damage.'

def GvMCalc(atk,mit):
	'''Gives statistical advice on whether to use Moonbow or Glimmer, given unit’s Attack and the type of attack (mag or phys)'''
	atk = int(atk)
	mMit = 5/8.*atk
	mDmg = 9/16.*atk
	returnM(mMit, mDmg,mit)
	print 'Given the average mitigation stat of all S Tier heroes:'
	if mit == 'mag':
	   if mMit >= 30.22:
	       print 'Use Glimmer.'
	   elif mMit >= 25.16:
	       print 'Use Glimmer, unless you need a tank killer.'
	   else:
	       print 'Use Moonbow.'
	if mit == 'phys':
	   if mMit >= 35:
	       print 'Use Glimmer.'
	   elif mMit >= 27.83:
	       print 'Use Glimmer, unless you need a tank killer.'
	   else:
	       print 'Use Moonbow.'
