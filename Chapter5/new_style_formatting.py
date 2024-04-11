salutation = "Mr."
name = "Mark"
product = "Roomba"
verbed = "exploded"
room = "living room"
animals = "animals"
amount = "$50"
percent = 95
spokeman = "Matthew"
job_tittle = "Quality Representative"



letter = """
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it shoud never be used in a {room}, specially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests is {percent}'%' 
less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokeman}
{job_tittle}"""

print(letter.format(salutation = "Mr.",
name = "Mark",
product = "Roomba",
verbed = "exploded",
room = "living room",
animals = "animals",
amount = "$50",
percent = 95,
spokeman = "Matthew",
job_tittle = "Quality Representative"))