
import pickle
import sqlite3


class Record:
    def __init__(self, name, time, date, temperature):
        self.city=name 
        self.time=time
        self.date=date
        if not isinstance(temperature, float):
            raise Exception("Wrong kind of temperature")
        self.__temperature=temperature
    
    # def __str__(self):
    #     return f"In {self.city} at {self.date} {self.time} temp is {self.temperature}"
    
    def __repr__(self):
        return f"{self.city} at {self.date} {self.time}: {self.temperature}"
    
    # Note: classmethod is equivalent to staticmethod the only difference is that a
    # classmethod get an implicit argument: the class the method belongs to
    
    @classmethod
    def parse(cls, text):
        c,t,d,temp=text.split(";")
        return Record(c, t, d, float(temp))
    
    def temperatureGet(self):
        return self.__temperature 
       
    def temperatureSet(self, val):
        if not isinstance(val, float):
            raise Exception("Wrong kind of temperature")
        self.__temperature=val
    
    temperature=property(fget=temperatureGet, fset=temperatureSet) 
    
    # NOTE: city, time and date could (and should) also be defined as properties ...       
           
class ListOfRecord:
        
    def __init__(self):
        self.data=[] 
        
    def __repr__(self):
        return str(self.data)
       
    def addRecord(self, record):
        self.data.append(record)
        
    @staticmethod
    def parseFile(fname):
        lr=ListOfRecord()
        with open(fname,"r") as fic:
            fic.readline()
            for line in fic:
                lr.addRecord(Record.parse(line))
        return lr  
          
    #parseFile=staticmethod(parseFile) 
       
    @staticmethod
    def readFromFile(fname):
        with open(fname,"rb") as fic:
            return pickle.load(fic)
        
    #readFromFile=staticmethod(readFromFile)
    
    def __iter__(self): # to make ListOfRecord be an "iterable" object
        return self.data.__iter__()
    
    def saveIntoFile(self, fname):
        with open(fname,"wb") as fic:
            pickle.dump(self, fic) 
            
    def __contains__(self, city): # associated with the "in" operator
        for r in self:
            if r.city == city:
                return True
        return False 
            
    def averageTemp(self, cityName):
        if not cityName in self:
            raise Exception (f"{cityName} is not in the list")
        total=0
        ix=0
        for r in self: # This is possible because ListOfRecord is an iterable object
            if r.city==cityName:
                ix += 1
                total += r.temperature 
        return total/ix   
    
    def minMax(self, cityName):
        if not cityName in self:
            raise Exception (f"{cityName} is not in the list")
        first=True
        for r in self:
            if r.city==cityName:
                if first:
                    mini=maxi=r.temperature
                    first=False
                else:
                    if r.temperature > maxi: maxi=r.temperature
                    if r.temperature < mini: mini=r.temperature
        return (mini, maxi)
        
    def minMaxAll(self):
        first=True
        for r in self:
            if first:
                mini=maxi=r.temperature
                first=False
            else:
                if r.temperature > maxi: maxi=r.temperature
                if r.temperature < mini: mini=r.temperature
        return (mini, maxi)  
    
    @staticmethod
    def read_sql(tableName):
        """
        Read the table (using a select statement)
        and make use of the corresponding data to construct a "listOfRecord"
        
        SQL statements to construct the table:
        drop table temperatures
        create table temperatures (city varchar(20), 
                                   time time,
                                   date date,
                                   temp float)
        """
        try:
            lr=ListOfRecord()
            conn=sqlite3.connect(r"epfl.db")
            cursor=conn.cursor()
            cursor.execute(f"select * from {tableName}")
            while True:
                row = cursor.fetchone()
                if row == None:
                    break
                print(f"{row[0]:12s} -> {row[1]}, {row[2]}, {row[3]:.2f}")
                lr.addRecord(Record(row[0], str(row[1]), str(row[2]), row[3]))
            return lr
            cursor.close()
            conn.close()
        except Exception as ex:
            print(ex)
    
    def to_sql(self, tableName):
        """
        Insert in the table tableName (using insert statements)
        the current "listOfRecord"
        """
        try:
            conn=sqlite3.connect(r"epfl.db")
            cursor=conn.cursor()
            for e in self:
                print (e.time, e.date.replace('/','-'))
                cursor.execute(f"insert into {tableName} values ('{e.city}', '{e.time}','{e.date.replace('/','-')}', {e.temperature})")
                cursor.execute("commit") 
            cursor.close()
            conn.close()
        except Exception as ex:
            print(ex)
            
if __name__ == "__main__":
    # lofr=ListOfRecord.read_sql("temperatures")
    # print(lofr)
      
    lofr=ListOfRecord.parseFile("measures.txt")
    print(lofr)
    
    for r in lofr:
        print(r)
        
    lofr.to_sql("temperatures")