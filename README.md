** Read Me **

If your supervisor is as much as sadist as mine (to be clear, i'm not talking about Lata or Paulo here!), they'll ask you to change your citations from alphabetical to chronological every even week, and then back every odd week. Here's a script to do it for you. 

- If you can python, download the .py file (this is the cleanest way to do it).  
- If you can't python, open up overleaf, create a new project, load "compile_me.tex" and "python_overleaf.py". Input your .tex file that you want to manipulate, change the name to "main.tex", and then compile "compile_me.tex". Finally, click "logs and output files", click "other logs and files" and then download "corrected_citations.tex". 

In either case, choose whether you want to have alphabetical or chronological order (toggle the alpha_chrono variable), choose the patterns you want to search for (by default, it searches for \cite{}, \citep{} and \citet{}).