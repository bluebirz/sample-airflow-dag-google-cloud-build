import unittest
from airflow.models import DagBag


class TestDags(unittest.TestCase):
    def setUp(self) -> None:
        self.dagbag = DagBag(include_examples=False)

    def test_dags_syntax(self):
        dags = self.dagbag.dags
        errs = self.dagbag.import_errors
        for dag in dags:
            print(dag)
        self.assertTrue(len(dags) > 0, "No DAGs found")
        self.assertFalse(len(errs), f"DAGs import errors: {errs}")


if __name__ == "__main__":
    loader = unittest.TestLoader().loadTestFromTestCase(TestDags)
    unittest.TextTestRunner(verbosity=2).run(loader)
