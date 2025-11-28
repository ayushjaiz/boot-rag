# Build command: 
```
uv run cli/keyword_search_cli.py build
```

# Search commaand
```
 uv run cli/keyword_search_cli.py search "great"
```

# Find term frequency of a token in a doc
```
uv run cli/keyword_search_cli.py tf 424 bear
```

# Find inverse document frequency (idf) in a datast
```
uv run cli/keyword_search_cli.py idf bear
```




# verify model
```
uv run cli/semantic_search_cli.py verify
```


# generate embedding
```
uv run cli/semantic_search_cli.py embed_text "hi this is ayush"
```









Things to learn

- file importing