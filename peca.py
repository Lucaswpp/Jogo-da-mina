class Piece():

    def __init__(self,is_bomb,bandeira):

        self.is_bomb = is_bomb
        self.is_bandeira = bandeira
        self.num_bomb = 0
        self.vizinhos = []
        self.is_click = False