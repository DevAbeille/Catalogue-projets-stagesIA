import os

script_to_inject = """  <!-- Auto-Theme Script -->
  <script>
    if (localStorage.getItem('theme') === 'light') {
      document.documentElement.classList.add('light-theme');
    }
  </script>
</head>"""

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Si le script n'est pas déjà présent, on l'injecte avant la fermeture de </head>
            if "localStorage.getItem('theme')" not in content and "</head>" in content:
                new_content = content.replace("</head>", script_to_inject)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Modifié : {path}")

print("Terminé ! Toutes tes pages HTML sont à jour.")
