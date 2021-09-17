import pyknp
knp = pyknp.KNP(jumanpp=False)

def summarize(text, depth=-1):
    if depth < 0:
        return text

    output_sentences = []
    # parse
    text = text.replace(' ', '')
    text = text.replace('　', '')
    for sentence in text.strip().split('\n'):
        result = knp.parse(sentence)
        # search roots
        roots = [m for m in result if m.parent == None]


        def get_depth(bnst, d):
            if d <= 0:
                return bnst.midasi
            return ''.join([get_depth(child, d-1) for child in bnst.children]) + bnst.midasi

        for root in roots:
            output_sentences.append(get_depth(root, depth))
    return "\n".join(output_sentences)