import pickle, scraping, scipy, sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.special
import scipy.optimize

def not_word(text, conf, x, y):
    conditions = [text == '',
                  text == ' ',
                  conf < 0,
                  y < 170,
                  y > 1240] # headers
    return any(conditions)

def loss_fcn(vec, X, num_words, num_lines): # num_lines = 200
    """
    Minimize loss, minimize weighted dist
    """
    initial = vec[0]
    spacing = vec[1]
    pred = initial + spacing * np.arange(num_lines)
    # first axis = iterate through target, length = num_words
    X = np.transpose(np.tile(X, (num_lines,1)))
    pred = np.tile(pred, (num_words,1))
    # second axis = iterate through pred pos, length = num_lines
    all_dist = (X-pred)**2
    dist = scipy.special.softmax(-all_dist, axis=1)*all_dist
    # softmax alone does not work, sum always = 1
    return np.sum(dist) # sum over all pred pos, and sum over all words


if __name__ == "__main__":
    """
    Look for outliers, remove them through not_word
    
    Problems: initial not unique (offset by any integer multiples of spacing)
    Spacing not unique (integer multiples of frequency)
    
    Better seeding?
    Regulation? Largest spacing as possible?
    but, hyperparameter tuning?
    """
    bookname = 'pos'
    page_num = 9

    with open('dict/' + bookname + str(page_num) + '.pkl', 'rb') as f:
        results = pickle.load(f)

    X = []
    Y = []
    for i in range(0, len(results["text"])):
        text, conf, x, y = scraping.get_word_attributes(results=results, idx=i)
        if not_word(text, conf, x, y):
            continue
        print(repr(text), conf, x, y)
        X.append(y)
        Y.append(0)
    plt.plot(X,Y,'o', markersize=3)

    X = np.array(X) # this is shorter than len(results["text"]) due to screening
    num_lines = 100
    optim_results = scipy.optimize.minimize(loss_fcn, np.array([203,26]),
                                    args=(X, X.size, num_lines))
    print(optim_results)
    params = optim_results.x
    pred = params[0] + params[1] * np.arange(num_lines)
    num_words = X.size

    X = np.transpose(np.tile(X, (num_lines, 1)))
    PRED = np.tile(pred, (num_words, 1))

    all_dist = (X - PRED) ** 2
    dist = scipy.special.softmax(-all_dist, axis=1) * all_dist

    mask = np.sum(dist,axis=0) < 1e-3
    masked_pred = np.delete(pred,mask)

    plt.plot(masked_pred,np.repeat(0.5, masked_pred.size),'o', markersize=3)
    print(f"Recommended line_space = {params[1]/2}")
    plt.ylim(-9,9)
    plt.show()