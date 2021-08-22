import re
import jellyfish as jf
from data.samples import sample1, attr_sample1
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
    phone = re.findall(r'((\+7|7|8)+([0-9]){10})', text)
    if len(phone) == 0:
        phone = None
    else:
        phone = phone[0][0]
    email = re.findall(r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}', text)
    if len(email) == 0:
        email = None
    else:
        email = email[0]
    person, location, org = get_entities(text, **models)
    return {'email': email, 'phone': phone, 'location': location, 'person': person, 'org': org}


def hard_matching(user_attr, pred):
    for i in user_attr:
        if i['phone'] == pred['phone'] and i['email'] == pred['email'] \
                or i['phone'] == pred['phone']:
            return i
    return None


def fuzzy_matching(user_attr, pred):
    jaro_treshold = {'email': 0.9, 'phone': 0.9, 'person': 0.8, 'location': 0.8, 'org': 0.8}
    result = 0
    for i in user_attr:
        jaro_dict = {'email': 0, 'phone': 0, 'person': 0, 'location': 0, 'org': 0}
        if i['person'] is not None and pred['person'] is not None:
            jaro_dict['person'] = jf.jaro_similarity(i['person'][0], pred['person'][0])

        if i['phone'] is not None and pred['phone'] is not None:
            jaro_dict['phone'] = jf.jaro_similarity(i['phone'], pred['phone'])

        if i['location'] is not None and pred['location'] is not None:
            jaro_dict['location'] = jf.jaro_similarity(i['location'][0], pred['location'][0])

        if i['email'] is not None and pred['email'] is not None:
            jaro_dict['email'] = jf.jaro_similarity(i['email'], pred['email'])

        if i['org'] is not None and pred['org'] is not None:
            jaro_dict['org'] = jf.jaro_similarity(i['org'][0], pred['org'][0])

        if jaro_dict['email'] >= jaro_treshold['email'] and jaro_dict['phone'] >= jaro_treshold['phone']:
            result = 1
        elif jaro_dict['email'] >= jaro_treshold['email'] and jaro_dict['person'] >= jaro_treshold['person']:
            result = 1
        elif jaro_dict['person'] >= jaro_treshold['person'] and jaro_dict['ord'] >= jaro_treshold['org']:
            result = 1
        if result == 1:
            return i, jaro_dict, jaro_treshold, result
    return None, None, jaro_treshold, result


if __name__ == '__main__':
    # print(get_pred(sample1))
    print(fuzzy_matching(attr_sample1, get_pred(sample1)))
