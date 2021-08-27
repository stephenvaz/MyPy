#luhns algo

card = '4417123456789113'
n = 0
while n <= 16:
    dub = 2*int(card[n])
    if dub >= 10:
        dub = str(dub)
        dub = int(dub[0]) + int(dub[1])
    n = n + 2
    print(dub)
#s1 = 2*int(card[n]) 



#Using Luhn algorithms and MOD 10 checksums
#https://www.groundlabs.com/blog/anatomy-of-a-credit-card-luhn-checks-bin-ranges-data-discovery/

#BREAKING DOWN Luhn Algorithm
#The credit card validation process requires businesses and credit card companies to be able to encrypt and decrypt sensitive financial information about the card, the issuer, and the cardholder nearly instantaneously. The volume of credit card transactions complicates this process and the companies party to these transactions look for ways to limit the amount of resources required to verify the transactions as much as they can. One way that they can speed up the verification process is to use the Luhn algorithm. The Luhn algorithm is especially helpful as more transactions are done online, where data breaches can be easier to make.

#The Luhn algorithm is not designed to protect the security of the parties involved in a credit card transaction as much as it is designed to check for errors made in the transmission of card numbers. For example, a cardholder may type in the wrong digit while making a purchase online. Rather than go through the entire verification process only to determine that the number was mistyped, the algorithm checks the digits earlier in the process and returns an error message if something is amiss.

#To determine whether a credit card number is valid, the sum of all of the digits, but not the check digit, is first calculated to find the units digit. The difference between the units digit of the resulting sum and the number ten is the estimated check digit. If the estimated check digit and the actual check digit are the same then the card has been validated.

# last digit of card is check digit