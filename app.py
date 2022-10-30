#pip install pywebcopy

from pywebcopy import save_webpage
 
kwargs = {'project_name': 'register'}
 
save_webpage(
    
    # url pf the website
    url='https://trumelabs.com/app/login/register/',
    #https://trumelabs.com/app/login/
    #https://trumelabs.com/app/
    
    # folder where the copy will be saved
    project_folder='C:/xampp/htdocs/clonar_trumelabs',
    **kwargs
)
