"""Generate Recamán's sequence and expose every algorithmic decision."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Jump:
    """One transition in Recamán's sequence."""

    step: int
    origin: int
    backward_candidate: int
    destination: int
    direction: str

    @property
    def used_backward_move(self) -> bool:
        return self.direction == "backward"


def trace(steps: int = 180) -> list[Jump]:
    """Return a decision trace containing exactly ``steps`` transitions."""

    if steps < 0:
        raise ValueError("steps must be non-negative")

    seen = {0}
    current = 0
    jumps: list[Jump] = []

    for step in range(1, steps + 1):
        origin = current
        candidate = current - step
        can_move_backward = candidate > 0 and candidate not in seen
        current = candidate if can_move_backward else current + step
        seen.add(current)
        jumps.append(
            Jump(
                step=step,
                origin=origin,
                backward_candidate=candidate,
                destination=current,
                direction="backward" if can_move_backward else "forward",
            )
        )

    return jumps


def generate(steps: int = 180) -> list[int]:
    """Return the initial zero followed by ``steps`` Recamán values."""

    return [0, *(jump.destination for jump in trace(steps))]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=180)
    args = parser.parse_args()

    values = generate(args.steps)
    print(f"values: {len(values)}")
    print(f"maximum: {max(values, default=0)}")
    print("sequence:", ", ".join(map(str, values)))


if __name__ == "__main__":
    main()

