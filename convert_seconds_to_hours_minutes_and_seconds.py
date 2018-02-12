# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#


def convert_seconds(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    s = round(s, 1)
    if h == 1:
        str_h = 'hour'
    else:
        str_h = 'hours'

    if m == 1:
        str_m = 'minute'
    else:
        str_m = 'minutes'

    if s == 1:
        str_s = 'second'
    else:
        str_s = 'seconds'

    converting = '%d %s, %d %s, %s %s' % (h, str_h, m, str_m, s, str_s)
    return converting


print(convert_seconds(3600))