# -*- coding: utf-8 -*-

class DialogManager(dict):

    def __init__(self):

        #load dialog

        fdia = open('txt/dialog.csv')
        sdia = fdia.read()

        sdia = sdia.split('\n')

        #on exclut les lignes vides et les lignes commentée
        sdia = [s for s in sdia if len(s)>0]
        sdia = [s for s in sdia if s[0]!='#']


        for line in sdia:

            data = line.split(';')
            code = data[0]
            name = data[1] 
            txt = data[2]

            if code != '' :
                if not self.has_key(code):
                    self[code] = []

                ddia = self[code]

                ddia.append((name,txt))

        # for k,v in self.items():
        #     print k.upper()
        #     for l in v:
        #         print l


if __name__ == "__main__":
    dia =  DialogManager()