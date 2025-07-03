# Balyos-Marvee-Final

This project explores how to navigate environments where movement costs change over time—like traffic or wind patterns that affect drones or autonomous vehicles. Traditional pathfinding algorithms like A* assume that costs are static, which doesn't work well when the environment changes dynamically. That's where the Predictive Friction Pathfinding (PFP) algorithm comes in.
The PFP algorithm predicts future movement costs and plans routes accordingly. It's like a GPS that not only knows where traffic is *now*, but also anticipates where it *will be*. This makes navigation smoother and more efficient, especially in real-time robotics or transport applications.

Project Components
```
main.py              # Runs the PFP search algorithm
pfp_algorithm.py     # Core logic and search mechanics
predictor.py         # Time-aware cost predictions
map_loader.py        # Map structure and neighbor definitions
test_pfp.py          # Test cases for validation

Make sure you have Python 3.9 or later installed. Then simply run:
```bash
python main.py

To make sure everything works as expected:
```bash
python -m unittest test_pfp.py
