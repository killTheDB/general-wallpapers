from os import listdir
from os.path import isfile, join
mypath = "D:\softwares\wallpapers"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

readmefile = open('README.md', 'a')

for image in onlyfiles:
    htmlcode = "<img src=\""+ image + "\"> <br>"
    readmefile.write(htmlcode)
    readmefile.write('\n')

readmefile.close()
