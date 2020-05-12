''' I/O utilties based on Fitsio
    MR: probably will shift to astropy.io.pyfits
'''

import fitsio

class DataLoader:
    '''
    DataLoader
    
    
    
    '''
    
    def __init__(self, science_img, header_ext=0):
        '''
        
        inputs
        -------
        science_img: str, path to the science image
        header_ext: int, extension number of the main header
        
        '''
        
        self.data = fitsio.FITS(science_img)
        self.header = self.data[header_ext].read_header() # read the header from the 0th ext
        
        self.header_keys = self.header.keys()
        self.num_ext = len(self.data)
        
        # MR: do we want to read all extensions?
        #self.extensions = {}
        #for d in self.data:
        #    self.extensions[d.get_extname()] = (d.read(), d.get_extname(), d.read_header())
        
    def read_ext(self, ext=1):
        ''' 
        
        inputs
        --------
        ext: int, extension number 
        
        '''
        assert ext < self.num_ext, f'ext={ext} does not exist'
        return self.data[ext].read()
    
    def get_keyword(self, keyword):
        '''
        inputs
        --------
        keyword: str
        '''
        assert keyword in self.header_keys, f'Sorry, {keyword} does not exist!'
        return self.header.get(keyword)
    
    def __repr__(self):
        ''' use the __repr__ method from fitsio.
        '''
        return self.data.__repr__()
