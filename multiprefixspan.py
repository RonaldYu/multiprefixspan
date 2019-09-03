import itertools
import collections
import re
import operator
import ast

# prefixspan algorithm for one item within one event
class prefixspan_one_item_one_event:
    
    def __init__(self, sdb, min_support):
        
        self.found_patterns = {}
        self.sdb = sdb
        self.min_support = min_support
        
    def find_following_pattern(self, item, db):
        mdb = []
        for sequence in db:

            if item not in sequence:
                pass
            else:
                i_item = sequence.index(item)

                mdb.append(sequence[(i_item+1):])
        return mdb
    
    def item_candidate(self, db, min_support):
    
        item_supports = collections.Counter(itertools.chain(*map(lambda x: set(x), db)))
        return [i for i, j in item_supports.items() if j >=min_support]
    
    def prefixspan(self, patt, db, min_support):
    
        if len(db) == 0:
            return None
        else:

            item_candidates = self.item_candidate(db, min_support)
            if len(item_candidates) == 0:
                return None

            for item in item_candidates:
                mdb = self.find_following_pattern(item, db)
                if len(mdb) >= min_support:
                    new_patt = patt + [item]

                    self.found_patterns[str(new_patt)] = self.found_patterns.get(str(new_patt), 0) + len(mdb)

                    self.prefixspan(new_patt, mdb, min_support)
                    
    def exect(self):
        self.prefixspan([], self.sdb, self.min_support)
        
        



# prefixspan algorithm for multiple items in one event
        
class prefixspan_multiple_items_one_event:
    
    def __init__(self, sdb, min_support):
      
      # initialize a prefixspan object
      # sdb: the whole data whice is a list, a seqeunce of events
      # each list/seqence is also a list whose elements are sets/events. 
      # there may be more than one items within a set/event.
      # min_support: a pattern with times of appearing in sdb/the whole data greater than min_support will be returned 
      
      
      
        self.found_patterns = {}
        self.sdb = sdb
        self.min_support = min_support
    
    def find_combinations(self, x):
          
        #result_list = []
        add_x = x.intersection({'_'})
        x = x.difference({'_'})
        
        return list(map(lambda ii: str(set({ii}).union(add_x)), x))
        
        #xx = itertools.combinations(x, 1)
        #xx = list(map(lambda ii: str(set(ii).union(add_x)), xx))
        #result_list.extend(xx)
        
        #return result_list   
        
        
    def find_items_from_one_sequence(self, x):
        
        
        return list(set(itertools.chain(*map(self.find_combinations, x))))
        
       
    def find_items(self, db):
    
        return list(itertools.chain(*map(self.find_items_from_one_sequence, db)))
        
    
    def item_candidate(self, db, min_support):
      
        item_supports = collections.Counter(self.find_items(db))
        return [ast.literal_eval(i) for i, j in item_supports.items() if j >=min_support]
        
        
    def find_following_pattern(self, item, db):
        mdb = []
        for sequence in db:
    
            first_hit = 0
            is_hit = False
            for event_index, event in enumerate(sequence):
                
                
                if '_' not in item:
                
                    if (item.issubset(event)) and ('_' not in event):
                        first_hit = event_index
                        is_hit = True
                        break
                    else:
                        pass
                
                else:
                  
                    if item.issubset(event):
                        first_hit = event_index
                        is_hit = True
                        break
                    else:
                        pass  
                  
    
            if is_hit:
                new_event = sequence[first_hit].difference(item)
    
                if len(new_event) > 0:
                    new_event = new_event.union({'_'})
                    mdb.append([new_event] + sequence[(first_hit+1):])
                else:
                    append_list = sequence[(first_hit+1):]
                    
                    mdb.append(append_list)
            else:
                pass
    
        return mdb
        
    def prefixspan(self, patt, db, min_support):
      
        if len(db) == 0:
            return None
        else:
            item_candidates = self.item_candidate(db, min_support)
            
            if len(item_candidates) == 0:
                return None
            
            for item in item_candidates:
                mdb = self.find_following_pattern(item, db)
                if len(mdb) >= min_support:
                
                    new_patt = patt + [item]
                    self.found_patterns[str(new_patt)] = self.found_patterns.get(str(new_patt), 0) + len(mdb)
    
                    self.prefixspan(new_patt, mdb, min_support)
                    
    def merge_multiple_events(self, x):
    
        selected_index = [i for i, j in enumerate(x) if '_' in j]
    
        if len(selected_index) > 0:
            
            
            x[selected_index[0]-1] = x[selected_index[0]-1].union(x[selected_index[0]]).difference({'_'})
            x = x[:selected_index[0]] + x[(selected_index[0]+1):]
            
            return [] + self.merge_multiple_events(x)
            
        else:
            return x
             
    def exect(self):
      
        self.found_patterns = {}
        self.prefixspan([], self.sdb, self.min_support)
        self.found_patterns = [(self.merge_multiple_events(ast.literal_eval(i)), j) for i, j in self.found_patterns.items()]
        
        
