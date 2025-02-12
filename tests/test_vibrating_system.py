import numpy as np
import pytest


import pyfmi


def test__pyfmi_fmi_has_FMU():
    assert hasattr(pyfmi.fmi, "FMU"), (
        "pyfmi.fmi should have an FMU class\n"
        f"dir(pyfmi.fmi): {dir(pyfmi.fmi)}"
    )


@pytest.fixture(scope="module")  # Load FMU only once per test session
def model():
    return pyfmi.fmi.FMU("VibratingSystem.fmu")  # Path to your FMU


def test_initial_conditions(model):
    assert model.get("position") == 1.0  # Check initial position
    assert model.get("der(position)") == 0.0  # Check initial velocity


def test_natural_frequency(model):
    # Simulate
    time = np.linspace(0, 10, 500)
    results = model.simulate(start_time=0, stop_time=10, time_points=time)
    position = results["position"]

    # Analyze results (find peaks to determine observed frequency)
    peaks_indices = (np.diff(np.sign(np.diff(position))) == -2).nonzero()[0] + 1
    peak_times = time[peaks_indices]
    periods = np.diff(peak_times)
    observed_period = np.mean(periods)  # Average over a few periods

    # Calculate theoretical frequency
    m = 1.0  # Replace with your actual mass value
    k = 1.0  # Replace with your actual stiffness value
    theoretical_frequency = np.sqrt(k / m)
    theoretical_period = 2 * np.pi / theoretical_frequency

    tolerance = 0.1 # Adjust tolerance as needed
    assert abs(observed_period - theoretical_period) < tolerance , f"Observed period: {observed_period}, Theoretical period: {theoretical_period}"


def test_energy_conservation(model):
    # Simulate
    time = np.linspace(0, 10, 500)
    results = model.simulate(start_time=0, stop_time=10, time_points=time)
    position = results["position"]
    velocity = results["der(position)"]

    m = 1.0  # Replace with your actual mass value
    k = 1.0  # Replace with your actual stiffness value

    initial_energy = 0.5 * k * position[0]**2 + 0.5 * m * velocity[0]**2
    final_energy = 0.5 * k * position[-1]**2 + 0.5 * m * velocity[-1]**2

    tolerance = 0.01  # Adjust tolerance
    assert abs(final_energy - initial_energy) < tolerance, f"Initial energy: {initial_energy}, Final energy: {final_energy}"


if "__main__" == __name__:
  pytest.main([__file__])
