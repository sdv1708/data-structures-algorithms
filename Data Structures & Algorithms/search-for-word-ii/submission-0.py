class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.word = None  # Stores the text of the word itself

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode() 
        for word in words: 
            root.insert(word)
        
        ROWS = len(board)
        COLS = len(board[0])
        result = [] 
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, node): 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in node.children: 
                return 
            
            char = board[r][c] 
            next_node = node.children[char]

            if next_node.word: 
                result.append(next_node.word)
                next_node.word = None

            # mark as visited 
            board[r][c] = '#'

            for dr, dc in dirs: 
                nr, nc = r + dr, c + dc
                dfs(nr, nc, next_node) 
            
            board[r][c] = char 
        
        for r in range(ROWS): 
            for c in range(COLS): 
                dfs(r, c, root)
        
        return result

            



        