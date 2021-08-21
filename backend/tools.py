from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsNERTagger,
    Doc
)

def get_ner_models():
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    ner_tagger = NewsNERTagger(emb)
    ner_models = {
        'segmenter': segmenter,
        'morph_vocab': morph_vocab,
        'morph_tagger': morph_tagger,
        'ner_tagger': ner_tagger
    }
    return ner_models


def get_entities(text, segmenter, morph_tagger, ner_tagger, morph_vocab):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)
    result = [doc.spans[i].normal.lower() for i in range(len(doc.spans))]
    if len(result) == 0:
        return None
    return tuple(result)


def get_pred(json_file):
    # inn, data = convert_json_to_dataset(json_file)
    # return {inn: model.predict(data)[0]}


if __name__ == '__main__':
    pass
