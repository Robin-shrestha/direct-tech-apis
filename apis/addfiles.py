import glob
from PIL import Image
from apis.models import Gallery

mypath = 'C:\\Users\\Dell\\Downloads\\gallery'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles=[]
image_paths = glob.glob(mypath + '/*.png')

for path in image_paths: 
    im = Image.open(path)
    # Gallery.objects.create(image)

print(im)