import re
from data.samples import sample1
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
    person = [doc.spans[i].normal for i in range(len(doc.spans)) if doc.spans[i].type == 'PER']
    location = [doc.spans[i].normal for i in range(len(doc.spans)) if doc.spans[i].type == 'LOC']
    org = [doc.spans[i].normal for i in range(len(doc.spans)) if doc.spans[i].type == 'ORG']
    if len(person) == 0:
        person = None
    if len(location) == 0:
        location = None
    if len(org) == 0:
        org = None
    return person, location, org


def get_pred(text):
    models = get_ner_models()
    phone = re.findall(r'((\+7|7|8)+([0-9]){10})', text)[0][0]
    if len(phone) == 0:
        phone = None
    email = re.findall(r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}', text)[0]
    if len(email) == 0:
        email = None
    person, location, org = get_entities(text, **models)
    return {'email': email, 'phone': phone, 'location': location, 'person': person, 'org': org}


def matching(pred):
    ...


if __name__ == '__main__':
    print(get_pred(sample1))
