import unittest



from Statistics.Statistics import Statistics
from CsvReader.CSVReader import CsvReader
from CSVReader.Data import Data


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

     def test_mean(self):
         test_data = CsvReader("Tests/datapoints.csv")
         answers = CsvReader("Tests/answers.csv").data
         values = Data(test_data, 'value')
         for column in answers:
             self.assertEqual(self.statistics.mean(values), float((column['mean'])))


    def test_median(self):
        test_data = CsvReader("Tests/datapoints.csv")
        answers = CsvReader("Tests/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.median(values), float((column['median'])))
    
    def test_mode(self):
        test_data = CsvReader("Tests/datapoints.csv")
        answers = CsvReader("Tests/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.mod(values), float((column['mode'])))

    def test_psd(self):
        test_data = CsvReader("Tests/datapoints.csv")
        answers = CsvReader("Tests/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(round(self.statistics.psd(values), 4), float((column['PSD'])))

     def test_variance_population_proportion(self):
         test_data = CsvReader("Tests/datapoints.csv")
         answers = CsvReader("Tests/answers.csv").data
         values = Data(test_data, 'value')
         for column in answers:
            self.assertEqual(self.statistics.var_pop_proportion(values), float((column['VPP'])))

    

    def test_zscore(self):
        test_data = CsvReader("Tests/datapoints.csv")
        answers = CsvReader("Tests/answers.csv").data
        values = Data(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.z_score(values), (column['zscore']))


        
if __name__ == '__main__':
    unittest.main()
