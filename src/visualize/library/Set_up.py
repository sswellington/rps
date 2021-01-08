import matplotlib.pyplot as plt


class Set_up(object):
    
    def __init__(self):
        self.xlabel = 'Período observado'
        self.subtitle = 'Rio Paraíba do Sul: '
    
    def set_up(self, header, unit):
        
        self.header = header
        self.title = (self.subtitle + header)
        self.ylabel = (header + ' - ' + unit)

        
    def plt(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid()
        
        
    def get_header(self):
        return self.header

        
    def save(self, path):
        plt.savefig(path + '.pdf', dpi = 300)
        plt.cla()   # Clear axis
        plt.clf()   # Clear figure
