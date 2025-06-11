from trie import Trie

# Create a Trie object
trie = Trie()

# Test cases
trie.insert("apple")
print(trie.search("apple"))    # Expected: True
print(trie.search("app"))      # Expected: False
print(trie.startsWith("app"))  # Expected: True
trie.insert("app")
print(trie.search("app"))      # Expected: True
