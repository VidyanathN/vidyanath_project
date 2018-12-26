import webbrowser
"""Google search using python script"""

class Abc():
    def set1(self):
        new=2
        taburl="https://www.google.com/search?source=hp&ei=hEQZXKrWO8TIvgSp0bS4BQ&q=python&btnK=Google+Search&oq=python&gs_l=psy-ab.3..0j0i131j0l8.5195.6441..7752...0.0..0.154.487.5j1......0....1..gws-wiz.....0..0i10.ljPE1n4KEio"
        term=""
        webbrowser.open(taburl+term,new=new)
        
        
        
        
        
        
c=Abc()
c.set1()
