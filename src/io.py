''' I/O utilties based on Fitsio
    MR: probably will shift to astropy.io.pyfits
'''


import numpy
import matplotlib.pyplot as plt

import fitsio

class array(numpy.ndarray):
    ''' Wrapper around numpy.ndarray to facilitate visualization of 2D images 
    using imshow
    '''
    def __new__(cls, a):
        obj = numpy.asarray(a).view(cls)
        return obj
    
    def imshow(self, ax=None, vmin=0, vmax=0.2, origin='lower', 
               cmap=plt.cm.binary, title='', hold=False, **kwargs):
        if ax is None:
            fig, ax = plt.subplots()
            
        map1 = ax.imshow(self, vmin=vmin, vmax=vmax, origin=origin, cmap=cmap, **kwargs)
        ax.set_title(title)
        
        if not hold:
            plt.show()

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
        return array(self.data[ext].read()) # this will add method 'imshow'
    
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
