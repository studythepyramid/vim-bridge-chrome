
## shell script to run the code

```bash
#!/bin/bash
# Route stdin to the bridge project
cd ~/dev/vim-bridge-chrome && uv run python main.py
```

chmod +x ~/local/bin/gemi-paste  # Adjust path if needed


## vim side

```vimscript
" Highlight text, press <leader>g, and send to Gemini
vnoremap <leader>g :w !gemi-paste<CR>
```



