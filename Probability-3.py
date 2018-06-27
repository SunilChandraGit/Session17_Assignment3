#possible combnations are RR, RB, BR, BB

#probability of getting RR
P_RR = (4/10)*(3/9)

#probability of getting RB
P_RB = (4/10)*(6/9)

#probability of getting BR
P_BR = (6/10)*(4/9)

#probability of getting BB
P_BB = (6/10)*(5/9)

print('Probability of getting 2 Red balls is {0:.2f}'.format(P_RR))
print('Probability of getting Black after Red ball is {0:.2f}'.format(P_RB))
print('Probability of getting Red after Black ball is {0:.2f}'.format(P_BR))
print('Probability of getting 2 Black balls is {0:.2f}'.format(P_BB))