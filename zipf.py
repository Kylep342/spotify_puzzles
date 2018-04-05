#!/usr/bin/env python
import sys


def zipf(_list, _to_return):
    _quality_dict = {}
    _base_quality = int(_list[0][0])
    for _num in range(len(_list)):
        _quality = int(_list[_num][0]) / ((1 / (_num + 1)) * _base_quality)
        if _quality not in _quality_dict.keys():
            _quality_dict[_quality] = {_num: _list[_num][1]}
        else:
            _quality_dict[_quality][_num] = _list[_num][1]
    _song_titles = []
    for _score in sorted(_quality_dict.keys(), reverse=True):
        for _n_track in sorted(_quality_dict[_score].keys()):
            _song_titles.append(_quality_dict[_score][_n_track])
    return _song_titles[:_to_return]


def main():
    _instructions = sys.stdin.readline().strip().split(' ')
    _n_songs, _to_return = int(_instructions[0]), int(_instructions[1])
    _master_list = []
    for _num in range(_n_songs):
        _song = sys.stdin.readline().strip().split(' ')
        _master_list.append(_song)
    _to_print = zipf(_master_list, _to_return)
    print('\n'.join(_to_print))


if __name__ == '__main__':
    main()
