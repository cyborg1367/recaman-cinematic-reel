"""Perspective model for the temporal-depth reveal."""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, radians, sin


@dataclass(frozen=True, slots=True)
class Camera:
    yaw: float = 0.0
    pitch: float = 0.0
    focal: float = 720.0


def temporal_depth(step: int, current_step: int, gap: float = 1.45) -> float:
    """Place earlier and later arcs on a temporal z-axis."""

    return (step - current_step) * gap


def project(point: tuple[float, float, float], camera: Camera) -> tuple[float, float]:
    """Project a 3D point after yaw and pitch rotations."""

    x, y, z = point
    yaw = radians(camera.yaw)
    pitch = radians(camera.pitch)

    rotated_x = x * cos(yaw) + z * sin(yaw)
    yaw_z = -x * sin(yaw) + z * cos(yaw)
    rotated_y = y * cos(pitch) - yaw_z * sin(pitch)
    rotated_z = y * sin(pitch) + yaw_z * cos(pitch)

    denominator = camera.focal - rotated_z
    if denominator <= 1e-9:
        raise ValueError("point lies on or behind the projection plane")
    scale = camera.focal / denominator
    return rotated_x * scale, rotated_y * scale


def camera_for_time(seconds: float) -> Camera:
    """Match the reel's front view, reveal, orbit, and final hold."""

    time = max(0.0, min(60.0, seconds))
    if time <= 12.0:
        return Camera()
    if time <= 19.8:
        progress = (time - 12.0) / 7.8
        eased = progress * progress * (3 - 2 * progress)
        return Camera(yaw=20.0 * eased, pitch=-8.0 * eased)
    if time <= 57.0:
        progress = (time - 19.8) / 37.2
        return Camera(yaw=20.0 + 8.0 * sin(progress * 3.141592653589793), pitch=-8.0)
    return Camera(yaw=20.0, pitch=-8.0)

