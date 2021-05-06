from py2neo import Graph,Node, Relationship, NodeMatcher
from passlib.hash import bcrypt
from datetime import datetime
import uuid
HOST = "localhost"
PORT = 7687
USER = "neo4j"
PASS = "123456" 

graph = Graph("bolt://" + HOST + ":7687/movie", auth=(USER, PASS))


# def db_auth():
#     HOST="localhost"
#     user = 'neo4j'
#     pword = '123456'
#     graph = Graph("bolt://" + HOST + ":7687", username=user, password=pword)
#     return graph


class User:
    def __init__(self,username):
        self.username = username
    
    # method allow to find user in the database
    def find(self):
        # print(username)
        # print('============')
        # print(self.username)
        user = graph.nodes.match('User', username = self.username).first()
       
        print(self.username)
       # print(username)
        return user
        #else return NONE
    
    def register(self, password):
        # find = NONE
        if not self.find():
            user = Node('User', username=self.username, password=bcrypt.encrypt(password))
            graph.create(user)
            #print(user)
            return True
        else:
            return False

    def verify_password(self,password):
        user = self.find()
        # print(user)
        # print(password)
        if user:
            return bcrypt.verify(password, user['password'])
            print('correct password')
        else:
            print('wrong password')
            return False

    def timestamp():
        epoch = datetime.utcfromtimestamp(0)
        now = datetime.now()
        delta = now - epoch
        return delta.total_seconds()

    def date():
        return datetime.now().strftime('%Y-%m-%d')

    def add_movie(self,title,tags,text):
        user = self.find()
        movie= Node('Movie',id=str(uuid.uuid4()),title=title,text=text)
        rel = Relationship(user,"ADD",movie)
        graph.create(rel)
        # separated by commas
        tags = [x.strip() for x in tags.lower().split(',')]
        print(movie)
        print(tags)
        print(rel)
        
        for tag in tags:
            t = Node("Gender", name=tag)
            t.__primarylabel__ = "Gender"
            t.__primarykey__ = "name"
            graph.merge(t)
            rel=Relationship(t, "TAGGED", movie)
            graph.create(rel)

    def get_all_movie():
        query=" MATCH (n:Movie) RETURN n "
        return graph.run(query)
   