import argparse,requests
#argparse function
parser=argparse.ArgumentParser(description='Web-Directory Bruteforcing')
parser.add_argument('-u','--url',required=True,help='http://example.com')
parser.add_argument('-w','--wordlist',required=True,help='Wordlist file location')
args=parser.parse_args()
wordlist=args.wordlist

#wordlist to list for bruteforcing
fd=open(wordlist,'r')
directory_list=fd.read()
directory_list=list(directory_list.split('\n'))
fd.close()

 #bruteforcing and result
for i in directory_list: 
    url2=f"{args.url}/{i}"
    try:
        r=requests.get(url2)
        if r.status_code!=404 and len(r.text)>0:
            print(url2)
    except:
        pass

