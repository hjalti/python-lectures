import re

text = '''
John enjoyed listening to singers while hiking or walking in his lingerie
'''

config = '''
cuteness: 1200
timeout: 400
sofa_tearing: 990
description: Extremely playful and fun
breed: Sphynx
'''


string = 'i am    a very     interesting      string                 indeed'

more_text = '''
Python was conceived in the late 1980s,[29] and its implementation began in December 1989[30] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[31] capable of exception handling and interfacing with the Amoeba operating system.[6] Van Rossum remains Python's principal author. His continuing central role in Python's development is reflected in the title given him by the Python community: Benevolent Dictator For Life (BDFL).

On the origins of Python, Van Rossum wrote in 1996:[32]
“ 	...In December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. My office ... would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus). 	”

Python 2.0 was released on 16 October 2000 and had many major new features, including a cycle-detecting garbage collector and support for Unicode. With this release, the development process became more transparent and community-backed.[33]

Python 3.0 (initially called Python 3000 or py3k) was released on 3 December 2008 after a long testing period. It is a major revision of the language that is not backward-compatible with previous versions.[34] However, many of its major features have been backported to the backward-compatible Python 2.6.x[35] and 2.7.x version series.

Python 2.7's end-of-life date (a.k.a. EOL, sunset date) was initially set at 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[36][37] In January 2017, Google announced work on a Python 2.7 to Go transcompiler. The Register speculated that this was in response to Python 2.7's planned end-of-life[38], but Google cited performance under concurrent workloads as their only motivation.[39]
'''


digits = [9, 2, 3, 4, 1]
