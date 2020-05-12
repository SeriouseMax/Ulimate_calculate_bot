from math import sin, cos


def function(update, context):
    try:
        state = context.user_data['state']
    except:
        state = 1
    if state == 1:
        update.message.reply_text('Enter ctg(n), where n - number')
        context.user_data['state'] = 2
        return 0
    elif state == 2:
        try:
            text = update.message.text
            n = int(text.split('(')[1][:-1])
            update.message.reply_text(cos(n) / sin(n))
            return -1
        except:
            update.message.reply_text('error. try again')
            return 0