# created by kvbvs 2020
import random
import string
from colorama import init, Fore, Back, Style
import colorama
init(convert=True)
print(Fore.BLUE + 'created by kvbvs')
print(Fore.RED + 'created by kvbvs')
print(Fore.GREEN + 'created by kvbvs')
print(Fore.YELLOW + 'created by kvbvs')
print(Fore.WHITE + 'created by kvbvs')
f = open('pscgen.txt', 'a')
print()
print(Fore.WHITE + 'how many codes do you want?: ')
amount = int(input())
fix = 1
while fix <= amount:
    nitro = ('').join(random.choices(string.digits, k=16))
    url = "[KVGEN] PSC: "
    kvgen = "Generated by KVGEN: "
    f.write(url + nitro + '\n')
    discord_code = url + nitro
    print(Fore.WHITE + url + nitro)
    fix += 1
    fix += 1
# end of script
# donate me: https://www.paypal.me/plsdonatemehoooman
