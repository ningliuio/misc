"""Count words."""

import operator


def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    # TODO: Count the number of occurences of each word in s
    # TODO: Sort the occurences in descending order (alphabetically in case of
    # ties)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    sli = s.split()
    cnt = {}
    for wd in sli:
        cnt.setdefault(wd, 0)
        cnt[wd] += 1

    cnt_absorted = sorted(cnt.items())
    cnt_sorted = sorted(cnt_absorted, key=operator.itemgetter(1), reverse=True)
    top_n = cnt_sorted[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter",
                      3))


if __name__ == '__main__':
    test_run()
