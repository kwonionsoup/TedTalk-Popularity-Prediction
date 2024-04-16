import numpy as np
from apyori import apriori

def split_tokens(processed_text):
    '''
    Args:
        processed_text: list of text in form of output of process_text in text_processing.py
    Return:
        text_tokens: 2D list of split text tokens
    '''
    text_tokens = []
    for line in processed_text:
        text_tokens.append(str(line).split(' '))
    return text_tokens

def extract_rules(tokened_text, sthresh, cthresh, exclude_singles=False):
    '''
    Args:
        tokened_text: 2D list of text tokens
        sthresh: support threshold for association rule mining
        cthresh: confidence threshold for association rule mining
    Return:
        rules: list of rules (sets of words)
        support: list of rule support
        confidence: list of rule confidence
    '''
    results = list(apriori(tokened_text, min_support = sthresh, min_confidence = cthresh, max_length = 2))
    rules = []
    support = []
    confidence = []
    lift = []

    for rule in results:
        if len(rule.items) == 1:
            if exclude_singles:
                continue
            rules.append(list(rule.items))
            support.append(rule.support)
            confidence.append(rule.ordered_statistics[0].confidence)
            lift.append(rule.ordered_statistics[0].lift)
        else:
            for orderedstat in rule.ordered_statistics:
                if len(orderedstat.items_base) > 0:
                    rules.append(list(orderedstat.items_base) + list(orderedstat.items_add))
                    support.append(rule.support)
                    confidence.append(orderedstat.confidence)
                    lift.append(orderedstat.lift)

    return rules, support, confidence, lift

def rule_metrics(rule, tokened_text, metrics):
    '''
    Args:
        rule: set of word cluster
        tokened_text: 2D list of text tokens
        metrics: 1D ndarray of TEDTalk metric
    Return:
        rule_metric: 1D ndarray of metrics of TEDTalks with titles that contain the rule
    '''
    rule_mask = np.empty(len(tokened_text), dtype=bool)
    for j, title in enumerate(tokened_text):
        rule_mask[j] = rule.issubset(set(title))
    rule_metric = metrics[rule_mask]
    return rule_metric