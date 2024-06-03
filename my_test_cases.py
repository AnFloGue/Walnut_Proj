def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def my_sum(a):
    sum, x = 0, type
    if x(a) != list: return a
    if x(a) == list and len(a) <= 1: return 0
    if x(a[0]) == str: sum = ""
    for num in a: sum += num
    return sum


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_uni,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def get_knowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_uni(s): return s.years_uni
