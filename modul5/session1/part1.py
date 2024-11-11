# import

import random

print(random.choice('abcd'))
print(random.choice([1, 2, 3, 4, 5]))
print(random.randint(10000, 20000))

import random as r

print(r.choice('abcd'))

print('Name of this script is: ', __name__)

from modul4.session1.app1 import check_password

password = "test"
check_password(password)

from modul4 import session2

print(session2.VAR1)
print('Calcul varsta medie: ', session2.age_average())
print('Media este: ', session2.medie([1, 2]))
