model VibratingSystem
  extends Modelica.Mechanics.Translational.Components.Mass;

  parameter Real m = 1 "Mass";
  parameter Real k = 1 "Stiffness";

  Modelica.Mechanics.Translational.Components.Spring spring(k=k);
  Modelica.Mechanics.Translational.Components.Fixed fixed;

  Modelica.Mechanics.Translational.Interfaces.Flange_b flange_b;

equation
  // Connect the mass to the spring
  flange_b = spring.flange_a;

  // Connect the other end of the spring to a fixed point
  spring.flange_b = fixed.flange;

  // Set the mass value
  this.m = m;

  // Initial conditions (optional - you can change these)
  der(position) = 0; // Initial velocity
  position = 1;      // Initial displacement

end VibratingSystem;


// Test model to simulate and visualize the system
model VibratingSystemTest
  extends Modelica.Mechanics.Translational.Examples.Utilities.Plot;

  VibratingSystem vibratingSystem(m=1, k=1); // Instantiate the system with m=1 kg, k=1 N/m

  // Connect the vibrating system
  vibratingSystem.flange_b = plot.flange;

  // Simulation settings
  final simulationOptions = Modelica.Simulation.Options(startTime=0, stopTime=10, numberOfIntervals=500);

end VibratingSystemTest;
