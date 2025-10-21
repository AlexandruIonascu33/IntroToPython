# GitHub Copilot in Codespaces — Student Guide

## What is GitHub Copilot?

GitHub Copilot is an AI-powered “pair programmer” that automatically suggests lines of code and code snippets based on context (comments, existing code, etc.).  
It is integrated as an extension in Visual Studio Code (including the browser editor via Codespaces).

Copilot can:

- Suggest code completions as you type
- Transform comments into code (e.g., write a comment `# TODO: …` and it can automatically generate code)
- Help you write boilerplate code quickly

---

## 🧑‍💻 How to use Copilot in Codespaces

1. **Open the repository in Codespaces** (on GitHub → click the *“Code”* button → *“Open with Codespaces”*).  
2. Codespaces will launch a VS Code instance in the browser (or locally if connected to VS Code).  
3. In the Extensions menu, search for and activate **GitHub Copilot** (if not already enabled).  
4. While editing `.py` files (or other supported languages), Copilot will suggest completions as “ghost text,” which you can accept with the `Tab` key or the right arrow `→`.  
5. You can write “intent comments” to guide it. Example:

   ```python
   # Write a print statement that displays a friendly message
