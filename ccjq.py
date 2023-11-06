import sys
import json
from pprint import pprint

class CCJQ:
    def __init__(self,json_str):
        self.comma = ','
        self.spl_char = ['{','}','[',']']
        self.open = ['{','[']
        self.close = ['}',']']
        self.quotes = ['\'','\"']
        self.level = 0
        self.json_str = json_str
        self.default_space = 2
    
    def custom_pprint(self):
        idx = 0
        curr = ''
        while idx < len(self.json_str):
            
            if  self.json_str[idx] in  self.quotes:
                text =  ''
                idx+=1
                while self.json_str[idx] not in self.quotes:
                    text+= self.json_str[idx]
                    idx+=1
                curr+='\''+text+'\''     
            elif self.json_str[idx] in self.open:

                curr+= self.json_str[idx]
                self.level+=self.default_space
                
                if idx+1 < len(self.json_str) and self.json_str[idx+1]!=self.comma:
                    curr += '\n'
                    curr+=self.leave_space()
            
            elif self.json_str[idx] in self.close:
                if self.json_str[idx-1] not in self.close:
                    curr += '\n'
                self.level-=self.default_space
                
                curr+=self.leave_space()
                
                curr+= self.json_str[idx]
                if idx+1 < len(self.json_str) and self.json_str[idx+1]!=self.comma:
                    curr += '\n'
                    curr+=self.leave_space()
                    
            
                
            else:
                curr+= self.json_str[idx]

            
            if self.json_str[idx] == self.comma:
                curr += '\n'
                if self.json_str[idx-1]!=self.close:
                    curr+=self.leave_space()
                
                
            idx+=1
        
        print(curr)
        return 0
    
    def leave_space(self):
        return " " * self.level
    
    def parse_argument(self,ccjq_arg):
        return_as_list = True if ccjq_arg.startswith('[') and ccjq_arg.endswith(']') else False
        ccjq_arg = ccjq_arg[1:-1] if return_as_list else ccjq_arg
        data = json.loads(self.json_str)
        for filter in ccjq_arg.split('|'):
            data = self.apply_filter(data,filter)
        return [data] if return_as_list else data

    def extract_data(self,data,criteria):
        if criteria.isdigit():
            criteria = int(criteria)
        
        if isinstance(criteria,int):
            data = data[criteria] if 0 <= criteria < len(data) else None
        else:
            if isinstance(data,list):
                data = [row.get(criteria,None) for row in data]
            else:
                data = data.get(criteria,None)
        return data


    def apply_filter(self,data,filter):
        
        if filter=='.':
            return data
        
        #second_filter = None
        for single_filter in filter.split('.')[1:]:
            single_filter = single_filter.strip()
            if single_filter.endswith('?'):
                single_filter = single_filter[:-1]
            
            if single_filter.startswith('[') and single_filter.endswith(']'):
                
                single_filter = single_filter[1:-1]
                data = self.extract_data(data,single_filter)
            
            elif str(single_filter).endswith(']'):
                filter1, filter2 = single_filter.strip(']').split('[')
                
                
                data = self.extract_data(data,filter1)
                if filter2:
                    
                    data = self.extract_data(data,filter2)
                
            else:
                data = self.extract_data(data,single_filter)
                
            #if second_filter is not None:
                #data = data[second_filter] if 0 <= second_filter < len(data) else None
        
        return data

def main():
    json_str = sys.argv[1]
    #json = json.loads(json_str)
    ccjq_arg = sys.argv[2]

    ccjq = CCJQ(json_str)
    ccjq.json_str = str(ccjq.parse_argument(ccjq_arg))
    ccjq.custom_pprint()
    
if __name__ == "__main__":
    main()