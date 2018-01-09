from sys import exit

def pay_others_to_do_for_you():
    print "You asked your friends to help you and offered them free chocolate for a month."
    print "But no one wants to help as they scare that Santa will find out."
    print "You have to try another way! "
    print "You choose to: 'take a break first'/'pretend to help'/'get the easiest job'"

    choose = raw_input('> ')

    if choose == "take a break first":
        caught("Santa found out you're not doing your work!No more roast beef!")

    elif choose == "pretend to help":
        pretend_to_help()

    else:
        caught("Santa found out you're not doing your work!No more roast beef!")

def pretend_to_help():
    print "You are thinking about working in which department that no one will find out."
    print "Santa's office: as the receptionist and Santa rarely comes out from his office."
    print "Post office: no one will notice you as they're too busy dealing with the Christmas mails."
    print "Gift station: you can hide inside the big gift box. "
    print "You choose to: 'Santa's office'/'Post office'/'Gift station'"
    choose = raw_input('> ')
    if choose == "Santa's office":
        caught("Santa found out you're not doing your work!No more roast beef!")

    elif choose == "Post office":
        Post_office()

    elif choose == "Gift station":
        Gift_station()

    else:
        caught("Santa found out you're not doing your work!No more roast beef!")


def get_the_easiest_job():
    print "You got the easiest job finally."

    print "It's the kitchen in the Christmas village."
    print "They're all preparing for the big Christmas dinner for tonight!"
    print "And you're in charge of cooking of roast beef and you even can taste a little piece of beef while cooking!"
    print "It tastes so good and juicy! You're thinking whether you should work hard for this job from now on."
    print "So you decided to:"
    print "You choose to: 'work hard'/'not work hard'"
    choose = raw_input('> ')
    if choose == "work hard":
        print "Congratulation!You're no longer the laziest elf! Santa appreciate your efforts.MERRY CHRISTMAS~"
    else:
        caught("Santa found out you're not doing your work!No more roast beef!")

def Post_office():
    print "You needed to take a handwritting test as only elves with good handwritting can do this job."
    print "You failed the test!"

    print "You have to find another job:"
    print "You choose to: 'Gift station'/'Santa's office'"
    choose = raw_input('> ')
    if choose == "Gift station":
        Gift_station()
    else:
        caught("Santa found out you're not doing your work!No more roast beef!")

def Gift_station():
    print "You started to wrap some gifts but then you pretended having a paper cut and need to rest. "
    print "The senior elf knew you were faking it but he still gave you a chance to work in other departments."
    print "He gave you three options."
    print "You choose to: 'feed the reindeer'/'get the easiest job'/'Santa's office'"

    choose = raw_input('> ')

    if choose == "feed the reindeer":
        caught("Santa saw you're playing with the reindeer but not working.No more roast beef!")

    elif choose == "get the easiest job":
        get_the_easiest_job()

    else:
        caught("Santa found out you're not doing your work!No more roast beef!")

def caught(words):
    print words, "You can't enjoy the delicious Christmas dinner with others. Lonely~Lonely~Christmas."

    exit(0)

def start():
    print """
Letter from Santa:
Dear Elves,

    It's finally time for Christmas!
    This year will be a very busy one so please be ready and don't be lazy
    or you can't have roast beef for Christmas dinner!

Love,Santa.


    However,YOU,as the laziest elf among all, thinking about how to avoid from work......
    but still want to eat roast beef.

    """
    print "You choose to: 'pay others to do for you'/'pretend to help'/'get the easiest job'/'take a break first'"

    choose = raw_input('> ')

    if choose == "pay others to do for you":
        pay_others_to_do_for_you()

    elif choose == "pretend to help":
        pretend_to_help()

    elif choose == "get the easiest job":
        get_the_easiest_job()

    else:
        caught("Santa found out you're not doing your work!No more roast beef!")

start()
