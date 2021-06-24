text='https://drive.google.com/file/d/1eBzSHyZwc-IL4rTNDztrCMu-v9fotyzC/view?usp=sharing'
header=text.count('https://drive.google.com/file/d/')
textsub=text.replace('https://drive.google.com/file/d/','')
textsub=textsub.replace('/view?usp=sharing','')
print(textsub)
