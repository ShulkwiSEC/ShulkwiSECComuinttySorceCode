from ai import AI
import time
class Gold:
    def __init__(self, word):
        result = self.detect_gold_word(word)
        if result:
            gold, statement = result
            self.result = self.act(gold, statement)

    def detect_gold_word(self, word):
        word = str(word)
        if word.find("(") > 0:
            start = word.find("(") + 1
            end = word.find(")")
            gold = word[:(start - 1)]
            statement = word[start:end]
            if len(statement) > 0 and len(gold) > 0:
                return gold, statement
            elif len(gold) > 0:
                return gold, ''
            else:
                return None
        else:
            return None
    
    def act(self, gold, statement=''):
        if gold == 'time':
            statement = str(statement) or None
            if(statement == 'start'):
                start_time = time.time()
                return f'Timer Start at {start_time}'
            elif (statement == 'end' or 'stop'):
                end_time = time.time
                try:
                    timer = end_time - start_time
                    return timer
                except NameError:
                    return str('Pls: Start The Timer First Using time(start) Then Close It Using time(stop)')
            elif(statement == 'time' or 'now' or ''):
                return str(time.time()) 
            else:
                return ''
        
        elif gold == 'askai':
            ai = AI(statement)
            response = f'ai: {ai.result}'
            return response
        elif gold == 'file':
            if len(statement) > 0:
                try:
                    response = open(statement, 'r').read()
                except FileNotFoundError:
                    return 'File Not Found'
                except Exception as error:
                    return error
                else:
                    return response
            elif len(statement) <= 0:
                return 'Type: file(/path/to/your/file)'
        elif gold == 'send':
            return 'Comming Soon'