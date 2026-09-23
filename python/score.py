"""Build the 60-second musical event model used by the reel."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sin

try:
    from .recaman import generate
except ImportError:  # Allows: python python/score.py
    from recaman import generate


BPM = 60
BEAT_SECONDS = 60 / BPM
TRIPLET_SECONDS = BEAT_SECONDS / 3
FADE_SECONDS = 3.0

# bass, arpeggio, melody. ``None`` means no melody event in that slot.
SCORE_BARS = (
    (37, (56, 61, 64), (None, None, None, None, None, 68, None, None, None, None, None, 69)),
    (33, (56, 59, 64), (None, None, None, None, None, 68, None, None, None, None, None, 66)),
    (35, (54, 59, 63), (None, None, None, None, None, 66, None, None, None, None, None, 64)),
    (32, (56, 59, 63), (None, None, None, None, None, 64, None, None, None, None, None, 63)),
    (30, (54, 57, 61), (None, None, None, None, None, 61, None, None, None, None, None, 64)),
    (33, (56, 61, 64), (None, None, 64, None, None, 68, None, None, 69, None, None, 73)),
    (32, (56, 59, 64), (None, 71, None, None, 68, None, None, 66, None, None, 64, None)),
    (30, (54, 57, 61), (None, None, 66, None, None, 69, None, None, 73, None, None, 76)),
    (39, (54, 57, 60), (None, 75, None, None, 72, None, None, 69, None, None, 66, None)),
    (32, (56, 60, 63), (None, None, 68, None, None, 72, None, None, 75, None, None, 80)),
    (40, (56, 61, 64), (None, None, 76, None, None, 73, None, None, 71, None, None, 68)),
    (33, (56, 61, 64), (None, 69, None, None, 68, None, None, 64, None, None, 61, None)),
    (33, (54, 57, 61), (None, None, 66, None, None, 69, None, None, 68, None, None, 64)),
    (32, (56, 60, 63), (None, 63, None, None, 68, None, None, 72, None, None, 75, None)),
    (37, (56, 61, 64), (None, None, 73, None, None, 68, None, None, 64, None, None, 61)),
)


@dataclass(frozen=True, slots=True)
class NoteEvent:
    time: float
    midi: int
    velocity: float
    duration: float
    voice: str
    act: int


def duration_seconds() -> float:
    return len(SCORE_BARS) * 12 * TRIPLET_SECONDS


def master_gain(time: float) -> float:
    """Return the normalized master gain with a linear final fade."""

    total = duration_seconds()
    fade_start = total - FADE_SECONDS
    if time <= fade_start:
        return 1.0
    if time >= total:
        return 0.0
    return (total - time) / FADE_SECONDS


def build_score(values: list[int] | None = None) -> list[NoteEvent]:
    """Create bass, arpeggio, and melody events for all three acts."""

    values = generate(180) if values is None else values
    if len(values) < 181:
        raise ValueError("the score requires at least 181 Recamán values")

    peak = max(values) or 1
    events: list[NoteEvent] = []

    for bar_index, (bass, arpeggio, melody) in enumerate(SCORE_BARS):
        act = bar_index // 5
        bar_start = bar_index * 12 * TRIPLET_SECONDS
        coda = bar_index == len(SCORE_BARS) - 1
        bass_velocity = (0.074, 0.080, 0.068)[act]
        events.append(NoteEvent(bar_start, bass, bass_velocity, 4.4 if coda else 3.55, "bass", act))

        for slot in range(12):
            step = bar_index * 12 + slot + 1
            time = bar_start + slot * TRIPLET_SECONDS + (0.012 if slot % 3 == 2 else 0.0)
            order = (0, 1, 2, 1)[slot % 4]
            recaman_accent = values[step] / peak
            phrase_shape = 0.004 * sin((slot / 11) * pi)
            velocity = 0.050 + 0.013 * recaman_accent + (0.008 if slot % 3 == 0 else 0) + (0.006 if act == 1 else 0) + phrase_shape
            events.append(NoteEvent(time, arpeggio[order], velocity, 2.2 if coda else 2.0, "arpeggio", act))

            melody_note = melody[slot]
            if melody_note is not None:
                melody_velocity = 0.046 if coda else (0.064 if act == 1 else 0.057)
                events.append(NoteEvent(time + 0.008, melody_note, melody_velocity, 2.9 if coda else 2.35, "melody", act))

    return sorted(events, key=lambda event: (event.time, event.voice))


def main() -> None:
    events = build_score()
    voices = {voice: sum(event.voice == voice for event in events) for voice in ("bass", "arpeggio", "melody")}
    print(f"duration: {duration_seconds():.3f} s")
    print(f"events: {len(events)}")
    print("voices:", voices)
    print(f"fade: {duration_seconds() - FADE_SECONDS:.3f}–{duration_seconds():.3f} s")


if __name__ == "__main__":
    main()
