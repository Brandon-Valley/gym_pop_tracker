


class Log_Event:
    def __init__(self, row_d):
        self.num_ppl = int(row_d['num_ppl'])
        
    def print_me(self):
        print('{{')
        print('  num_ppl: ', self.num_ppl)
        print('}}')
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    import main
    main.main()