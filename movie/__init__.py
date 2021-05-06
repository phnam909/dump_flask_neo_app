from .views import app
from .models import graph

#Create schema
# graph.run("CREATE CONSTRAINT ON (n:User) ASSERT n.username IS UNIQUE")
# graph.run("CREATE CONSTRAINT ON (n:Movie) ASSERT n.id IS UNIQUE")
# graph.run("CREATE CONSTRAINT ON (n:Gender) ASSERT n.id IS UNIQUE")

def create_uniqueness_constraint(label, property):
    query = "CREATE CONSTRAINT ON (n:{label}) ASSERT n.{property} IS UNIQUE"
    query = query.format(label=label, property = property)
    graph.run(query)

# chạy xog 1 lần thì cmt nó lại, vẫn chưa tìm dc hàm thay thế
create_uniqueness_constraint('User','username')
create_uniqueness_constraint('Movie','id')
create_uniqueness_constraint('Gender','id')