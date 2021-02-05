import subprocess
import pkg_resources
import sys
import re


required = {"wikipedia"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("=================================================================================\nDownloading Dependencies\n=================================================================================")
    python = sys.executable
    try:
        subprocess.check_call([python, '-m', 'pip', 'install', *missing])
        print("=================================================================================\nDependencies installed\n=================================================================================")
    except:
        print("=================================================================================\nDependencies could not be installed.\nCheck your system is connected to Internet and pip is installed on your system.\n=================================================================================")
        sys.exit()

import wikipedia
    
def wikiSearch(terms):
    print("Searching wikipedia for", terms)
    p=progressBar(3)

    searchResults = wikipedia.search(terms,results=20,suggestion=True)
    p.addOne()

    if searchResults is None or len(searchResults[0])<1:
        p.updateComplete()
        print("Ambiguous search text.\nRetry with a more specific terms.")
        sys.exit()
    p.addOne()
    #print(searchResults)
    ptr=0
    p.addOne()

    if len(searchResults[0])>1:
        print("Please choose your topic from the list below:\n")
        for r in searchResults[0]:
            print(ptr+1,". ",r)
            ptr=ptr+1
        ptr=int(input("\nEnter your choice: "))-1

    searchUrl=re.sub(' ','_',"https://en.wikipedia.org/wiki/"+searchResults[0][ptr])
    print(searchUrl)

    with open("wiki_search_log.txt", 'a') as logfile:
        logfile.write(searchUrl + "\n")
        logfile.close()
    sys.exit(0)

class progressBar:
    def __init__(self,total, prefix = 'Progress:', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
        self.total=total
        self.prefix=prefix
        self.suffix=suffix
        self.decimals=decimals
        self.length=length
        self.fill=fill
        self.printEnd=printEnd
        self.iteration=0

    def update (self,iteration):
        self.iteration=iteration
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (iteration / float(self.total)))
        filledLength = int(self.length * iteration // self.total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end = self.printEnd)
        if iteration == self.total: 
            print()
    def addOne(self):
        self.update(self.iteration+1)
    def updateComplete(self):
        self.update(self.total)


if __name__ == '__main__':
    search_key = ' '

    if len(sys.argv) == 1:
        search_keyword = input("Enter your search terms: \n")
    else:
        search_keyword = search_key.join(sys.argv[1:])

    wikiSearch(search_keyword)
