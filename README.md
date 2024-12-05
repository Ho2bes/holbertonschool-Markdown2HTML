# **Markdown2HTML**

## **Description**

**Markdown2HTML** est un script Python qui convertit des fichiers au format Markdown (.md) en fichiers HTML. Il prend en charge plusieurs fonctionnalités courantes du Markdown, notamment les titres, les listes, les textes enrichis (gras, italique) et certaines transformations spécifiques, tout en respectant les exigences d'un projet Python standard.

Ce projet explore la manière dont GitHub et d'autres plateformes rendent les fichiers Markdown en HTML.

---

## **Fonctionnalités**

1. **Conversion de titres** : Supporte les niveaux de titre de `#` à `######`.
   - Markdown : `# Heading level 1`
   - HTML : `<h1>Heading level 1</h1>`

2. **Listes non ordonnées** :
   - Markdown :
     ```markdown
     - Élément 1
     - Élément 2
     ```
   - HTML :
     ```html
     <ul>
       <li>Élément 1</li>
       <li>Élément 2</li>
     </ul>
     ```

3. **Listes ordonnées** :
   - Markdown :
     ```markdown
     * Élément 1
     * Élément 2
     ```
   - HTML :
     ```html
     <ol>
       <li>Élément 1</li>
       <li>Élément 2</li>
     </ol>
     ```

4. **Paragraphes** : Chaque bloc de texte devient un paragraphe HTML.
   - Markdown :
     ```
     Ceci est un paragraphe.
     ```
   - HTML :
     ```html
     <p>Ceci est un paragraphe.</p>
     ```

5. **Texte enrichi** :
   - Gras (`**texte**`) : Converti en `<b>texte</b>`.
   - Italique (`__texte__`) : Converti en `<em>texte</em>`.

6. **Transformations spéciales** :
   - Texte entre `[[...]]` : Converti en son hash MD5.
   - Texte entre `((...))` : Suppression de toutes les lettres "c" (insensible à la casse).

---

## **Installation et exécution**

### **Prérequis**
- Python 3.7 ou supérieur.
- Système d'exploitation : Ubuntu 18.04 LTS.
- Le script doit être rendu exécutable :
  ```bash
  chmod +x markdown2html.py
