class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, unique_id):
        query = "CREATE (:Player {name: $name, unique_id: $unique_id})"
        parameters = {"name": name, "unique_id": unique_id}
        self.db.execute_query(query, parameters)

    def create_match(self, unique_id):
        query = "CREATE (:Match {unique_id: $unique_id})"
        parameters = {"unique_id": unique_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_info_match(self, unique_id):
        query = "MATCH (p:Player)-[pnt:PONTUOU]->(m:Match) WHERE m.unique_id = $unique_id RETURN p.name, " \
                "pnt.pontuacao"
        parameters = {"unique_id": unique_id}
        results = self.db.execute_query(query, parameters)
        return [(result["p.name"], result["pnt.pontuacao"]) for result in results]

    def get_player_history(self, unique_id):
        query = "MATCH (p:Player)-[pnt:PONTUOU]->(m:Match) WHERE p.unique_id = $unique_id RETURN m.unique_id, " \
                "pnt.pontuacao"
        parameters = {"unique_id": unique_id}
        results = self.db.execute_query(query, parameters)
        return [(result["m.unique_id"], result["pnt.pontuacao"]) for result in results]

    def update_player(self, unique_id, new_name):
        query = "MATCH (p:Player {unique_id: $unique_id}) SET p.name = $new_name"
        parameters = {"unique_id": unique_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_pontuacao(self, unique_id, player_unique_id, pontuacao):
        query = "MATCH (m:Match{unique_id:$unique_id}), (p:Player{unique_id: $player_unique_id}) " \
                "CREATE(p)-[:PONTUOU{pontuacao: $pontuacao}]->(m)"
        parameters = {"unique_id": unique_id, "player_unique_id": player_unique_id, "pontuacao": pontuacao}
        self.db.execute_query(query, parameters)

    def insert_vencedor(self, unique_id, player_unique_id):
        query = "MATCH (m:Match{unique_id:$unique_id}), (p:Player{unique_id: $player_unique_id}) " \
                "CREATE(p)-[:VENCEU]->(m)"
        parameters = {"unique_id": unique_id, "player_unique_id": player_unique_id}
        self.db.execute_query(query, parameters)

    def delete_player(self, unique_id):
        query = "MATCH (p:Player {unique_id: $unique_id}) DETACH DELETE p"
        parameters = {"unique_id": unique_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, unique_id):
        query = "MATCH (m:Match {unique_id: $unique_id}) DETACH DELETE m"
        parameters = {"unique_id": unique_id}
        self.db.execute_query(query, parameters)