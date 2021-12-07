char_dict = {';' : 'title',
    'n' : ['nrow_ncol'],
    '#' : ['walls'],
    '$' : ['boxes'],
    '.' : ['storage'],
    '@' : ['player'], 
    '+' : ['player','storage'], 
    '*' : ['boxes', 'storage'],
    ' ' : ['empty']
    }

class Level:
    def __init__(self):
        self.title = ''
        self.nrow_ncol = ''
        self.walls = ''
        self.boxes = ''
        self.storage = ''
        self.player = ''
        self.empty = ''

    def make_txt(self,path):
        char = ['nrow_ncol','walls','boxes','storage','player']
        write_path = os.path.join(path, self.title + '.txt')
        file = open(write_path, "w+")
        for key in char:
            file.write(self.__dict__[key] + '\n')
        file.close()

    def add_xy(self, char, y, x):
        for att in char_dict[char]:
            self.__dict__[att] += str(y) + ' ' + str(x) + ' '
    
    def add_n(self):
        char = ['walls', 'boxes', 'storage']
        for key in char:
            n = int(len(self.__dict__[key].split(' '))/2)
            self.__dict__[key] = str(n) + '. ' + self.__dict__[key]




def raw_lvl_list(path) -> list:
    levels_list = []
    for item in os.listdir(path):
        if not item.startswith('.') and os.path.isfile(os.path.join(dir, item)):
            file = open(item)
            try:
                lines = file.readlines()
            except UnicodeDecodeError:
                print('Cannot decode file: ', item)
            i_level = []
            for line in lines:
                if line == '':
                    continue
                elif not line[0] == ';':
                    i_level.append(line.replace('\n',''))
                elif line[0] == ';':
                    i_level.append(line.replace('\n',''))
                    levels_list.append(i_level)
                    i_level = []
            file.close()
        else:
            continue
    return(levels_list)



def create_lvl(lvl) -> Level:
    rv = Level()
    rv.__setattr__('nrow_ncol', str(len(lvl) - 1) + ' ' + str(len(lvl[0]) ))
    for y, line in enumerate(lvl, 1):
        if not line[0] == ';':
            for x, char in enumerate(line, 1):
                rv.add_xy(char, y, x)
        elif line[0] == ';':
            rv.__setattr__('title',line.replace(';','').replace(' ',''))
    rv.add_n()
    rv.empty= ''
    return(rv)


import os 
path = os.path.realpath(__file__)
dir = os.path.dirname(path)
dir = os.path.join(dir,'original_txt')
os.chdir(dir)

levels_list = raw_lvl_list(os.getcwd())
test_lvl = create_lvl(levels_list[0])


dir2 = os.path.dirname(path)
dir2 = os.path.join(dir2,'new_txt')
os.chdir(dir2)

lvl_list = []

for lvl in levels_list:
    try:
        temp_lvl = create_lvl(lvl)
        temp_lvl.make_txt(os.getcwd())
    except IndexError:
        pass

