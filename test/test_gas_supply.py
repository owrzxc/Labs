import unittest

from src.gas_supply import find_gas_route, find_unreachable_cities


class TestGasSupply(unittest.TestCase):
    def test_all_cities_reachable(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
        ]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            []
        )

    def test_some_cities_unreachable(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
        ]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [["Сховище_1", ["Долина"]]]
        )

    def test_multiple_storages(self):
        cities = ["Львів", "Стрий", "Долина", "Самбір"]
        storages = ["Сховище_1", "Сховище_2"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Сховище_2", "Долина"],
        ]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [
                ["Сховище_1", ["Долина", "Самбір"]],
                ["Сховище_2", ["Львів", "Стрий", "Самбір"]],
            ]
        )

    def test_storage_to_storage_transit(self):
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_1", "Сховище_2"]
        pipelines = [
            ["Сховище_1", "Сховище_2"],
            ["Сховище_2", "Львів"],
            ["Львів", "Стрий"],
        ]

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            []
        )

    def test_no_pipelines(self):
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_1"]
        pipelines = []

        self.assertEqual(
            find_unreachable_cities(cities, storages, pipelines),
            [["Сховище_1", ["Львів", "Стрий"]]]
        )

    def test_find_route_exists(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
        ]

        self.assertEqual(
            find_gas_route(
                cities,
                storages,
                pipelines,
                "Сховище_1",
                "Долина",
            ),
            ["Сховище_1", "Львів", "Стрий", "Долина"],
        )

    def test_find_route_not_exists(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
        ]

        self.assertEqual(
            find_gas_route(
                cities,
                storages,
                pipelines,
                "Сховище_1",
                "Долина",
            ),
            [],
        )

    def test_find_route_invalid_nodes(self):
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_1"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
        ]

        self.assertEqual(
            find_gas_route(
                cities,
                storages,
                pipelines,
                "Сховище_3",
                "Стрий",
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()