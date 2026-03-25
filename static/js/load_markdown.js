document.addEventListener("DOMContentLoaded", () => {
    const noMarkdownIds = ["google_maps_src", "description"]
    const notSelector = noMarkdownIds.map(id => `:not(#id_${id})`).join("")
    const textAreasSelector = `textarea${notSelector}`
    const textAreas = document.querySelectorAll(textAreasSelector)
  
    setTimeout(() => {
      textAreas.forEach(textArea => {
        // Prevent double initialization
        if (textArea.getAttribute('data-simplemde')) return;
        textArea.setAttribute('data-simplemde', 'true');

        new SimpleMDE({
          element: textArea,
          toolbar: [
            "bold", "italic", "heading", "|",
            "quote", "code", "link", "image", "|",
            "unordered-list", "ordered-list", "|",
            "undo", "redo", "|",
            "preview", "side-by-side", "fullscreen",
          ],
          spellChecker: false,
          forceSync: true,
          autoDownloadFontAwesome: false,
          previewRender: (plainText) => {
            return marked.parse(plainText);
          },
        })
      })
    }, 100)
})
