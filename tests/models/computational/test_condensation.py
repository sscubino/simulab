import pytest

from simulab.models.computational.condensation.model import Condensation
from simulab.simulation.core.equilibrium_criterion import WithoutCriterion
from simulab.simulation.core.experiment import ExperimentParametersSet
from simulab.simulation.core.neighborhood import Moore
from simulab.simulation.core.runner import Runner

experiment_parameters_set = ExperimentParametersSet(
    length=[50],
    probability=[0.15, 0.20, 0.25],
    neighborhood=[Moore],
)
runner = Runner(
    Condensation,
    experiment_parameters_set,
    WithoutCriterion(),
    max_steps=5,
)


def test_real_state_market() -> None:
    assert len(runner.experiments) == 3
    with pytest.raises(AttributeError):
        runner.experiments[0].series

    runner.start()
    for series in runner.experiments[0].series.values():
        assert len(series) == 5 + 1
