def designerPdfViewer(h: list[int], word: str):
    return len(word) * max(h[ord(i) - ord('a')] for i in word)

designerPdfViewer([1, 3, 1, ], 'torn')