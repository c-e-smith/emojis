#!/home/greg/miniconda3/envs/ga/bin/python

'''
Accepts n integer as argument and returns the tags
of n emojis pulled from the GH emoji webpage.

Be sure to set your python path accordingly (above)
as well as have any dependencies installed.

Example:
    $ emojis 3
        :church: :-1: :clock9:
'''

def main():

    import sys
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import random
    
    num_emojis = sys.argv
    if len(sys.argv) == 1:
        num_emojis = 5
    else:
        num_emojis = int(sys.argv[1])
    
    class EmoTime:
        '''
        get dem dank emojis
        '''
        
        def __init__(self):
            self.url = 'https://gist.github.com/rxaviers/7360908'
        
        def get(self, n=5):
            '''
            n: number of emoji to retrieve, default 5
            '''
            res = BeautifulSoup(requests.get(self.url).content, 'html.parser') 
            emoji_list = []
            emoji_output = ''
            
            for table in res.findAll('table'):
                for cell in table.findAll('td'):
                    for emoji in cell.findAll('code'):
                        emoji_list.append(emoji.text)
    
            for i in range(n):
                emoji_output  += random.choice(emoji_list) + ' '
                
            print(emoji_output[:-1])
    
    foo = EmoTime()
    
    foo.get(num_emojis)

if __name__ == '__main__':
    main()

