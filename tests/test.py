from mc_package import materials_counter


def test_time_counter():
    assert materials_counter.count_time(100, 50) == 2.0, 'incorrect time'
