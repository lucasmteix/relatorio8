from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.235.104.135:7687", "neo4j", "mechanisms-canister-frame")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando alguns players
game_db.create_player("Nogueira_12", "1")
game_db.create_player("LelepeModerada", "13")
game_db.create_player("Lutiaumm", "2")

# Criando algumas matches
game_db.create_match("1")
game_db.create_match("2")
game_db.create_match("3")

# Colocando jogadores em partidas
game_db.insert_pontuacao("1", "1", 15)
game_db.insert_pontuacao("1", "13", 60)
game_db.insert_pontuacao("1", "2", 90)
game_db.insert_pontuacao("2", "1", 20)
game_db.insert_pontuacao("2", "13", 25)
game_db.insert_pontuacao("2", "2", 95)
game_db.insert_pontuacao("3", "1", 40)
game_db.insert_pontuacao("3", "13", 90)

# Colocando os venderos das partidas
game_db.insert_vencedor("1", "2")
game_db.insert_vencedor("2", "2")
game_db.insert_vencedor("3", "13")

# Atualizando o nome de um player
game_db.update_player("2", "KHN Lutiaumm")

# Deletando um aluno e uma aula
game_db.delete_player("2")
game_db.delete_match("2")

# Print de todas as informações do banco de dados
print("Players:")
print(game_db.get_players())
print("Histórico de partidas do jogador 13:")
print(game_db.get_player_history("13"))
print("Matches:")
print(game_db.get_info_match("1"))

# Fechando a conexão
db.close()