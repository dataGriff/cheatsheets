class CheatSheet:

    def __init__(self, my_name):
        self.my_name = my_name
        self.beer_list = ["tiny rebel","garabage","crafty deval","flowerhorn","mad dog"]
        self.reverse_beer_list = []
        self.working_brewer = ""
        self.process_beer_list()
        self.first_list = self.beer_list[0]
        self.last_list = self.beer_list[-1]
        self.second_third_slice = self.beer_list[1:3]
        self.last_two_slice = self.beer_list[-2:]
        self.list_length = len(self.beer_list)
        
        self.beer_dict = {"tiny rebel":"clwb tropicana","crafty devil":"mike rayer","flowerhorn":"sprinkles"}
        self.beer_tuple = ("tiny rebel","clwb tropicana")
        
    def hello_coder(self,coder_type='hungovercoder'):
        message = f"Hello {self.my_name}, you are now a {coder_type}"
        print(message)
        return message
    
    def process_beer_list(self):  
        self.beer_list.append("pipes")
        self.beer_list.append("mistake")
        self.beer_list.remove("mistake")
        self.beer_list[2]= "crafty devil"
        del self.beer_list[1]
        self.beer_list.sort()
        self.working_brewer = self.beer_list.pop(-1)
        self.reverse_beer_list  = self.beer_list[:]
        self.reverse_beer_list.reverse()



    
        
        

        

        





    
