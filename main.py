from copy import copy
LENGTH=3
GLOBAL_LEVEL=0
strn_tab=[]
class Tree:
    def __init__(self,val,strong_weak,purins_primidins,level,strn):
        self.val=val
        if level==1221:
            search_end=val[:2]
            
            temp_sw=""
            temp_pp=""
            for char in search_end:
                match char:
                    case "C":
                        temp_sw+="S"
                        temp_pp+="Y"
                    case "G":
                        temp_sw+="S"
                        temp_pp+="R"
                    case "A":
                        temp_sw+="W"
                        temp_pp+="R"
                    case "T":
                        temp_pp+="Y"
                        temp_sw+="W"
            temp_pp+=val[-1]
            temp_sw+=val[-1]
            purins_primidins.remove(temp_pp)
            strong_weak.remove(temp_sw)
                
        
        self.strn=strn+val
        print(val)
        self.children=[]
        self.strong_weak=strong_weak
        self.purins_pirimidins=purins_primidins
        self.level=level

        self.visited=False
        self.generate_children()
    def generate_children(self):
        if self.level==3:
            None
        search_end=self.val[-(LENGTH-1):]
        print(self.level)
        possibilities_sw=[]
        possibilities_pp=[]
        possibilities=[]
        temp_sw=""
        temp_pp=""
        for char in search_end:
          match char:
            case "C":
                temp_sw+="S"
                temp_pp+="Y"
            case "G":
                temp_sw+="S"
                temp_pp+="R"
            case "A":
                temp_sw+="W"
                temp_pp+="R"
            case "T":
                temp_pp+="Y"
                temp_sw+="W"
        
        for element in self.strong_weak:
            t_sw=element[:(LENGTH-1)]
            if t_sw==temp_sw:
                possibilities_sw.append(element)
        for element in self.purins_pirimidins:
            t_pp=element[:(LENGTH-1)]
            if t_pp==temp_pp:
                possibilities_pp.append(element)
                  
        for id_pp in range (len(possibilities_pp)):
            for id_sw  in range (len(possibilities_sw)):
                if possibilities_pp[id_pp][-1]==possibilities_sw[id_sw][-1]:
                    possibilities.append((search_end+possibilities_pp[id_pp][-1],id_pp,id_sw))
                    
                    

     
        if len(possibilities)<1:
                    strn_tab.append(self.strn)   
        for possibility in possibilities:
                purins_local=[x for x in self.purins_pirimidins]
                sw_local=[x for x in self.strong_weak]
                purins_local.remove(possibilities_pp[possibility[1]])
                
                sw_local.remove(possibilities_sw[possibility[2]])
                
                child=Tree(possibility[0],sw_local,purins_local,self.level+1,self.strn)
                
                self.children.append(child)
        
x=Tree("TCG",["SSA","SST","SWA","SWC","WSG","WWC"],["RRC","RYA","RYG","YRA","YRC","YRT","YYG"],0,"")

print(x)
print(strn_tab)