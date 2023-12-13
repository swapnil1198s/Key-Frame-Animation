import pygame
class Animation:
    def __init__(self, keyframes, duration_per_frame):
        self.keyframes = keyframes
        self.duration_per_frame = duration_per_frame
        self.current_frame = 0
        self.current_time = 0
        self.tween_factor = 0  # Represents the interpolation factor between 0 and 1
        self.is_last_frame_reached = False  # Flag to indicate last frame is reached

    def interpolate(self, start, end, factor):
        # Linear interpolation
        return start + (end - start) * factor

    def update(self, dt):
        if len(self.keyframes) < 2:  # Need at least two frames to interpolate
            return

        self.current_time += dt
        self.tween_factor = self.current_time / self.duration_per_frame

        if self.current_time >= self.duration_per_frame:
            self.current_time = 0
            self.current_frame += 1
            self.tween_factor = 0  # Reset tween factor for the next frame

            if self.current_frame >= len(self.keyframes) - 1:
                self.current_frame = 0  # Loop back to the first frame
                self.is_last_frame_reached = True  # Set flag when last frame is reached

    def get_current_keyframe(self):
        next_frame = (self.current_frame + 1) % len(self.keyframes)
        current_keyframe = self.keyframes[self.current_frame]
        next_keyframe = self.keyframes[next_frame]

        # Interpolate each property
        position = tuple(self.interpolate(s, e, self.tween_factor) for s, e in zip(current_keyframe['position'], next_keyframe['position']))
        arm_angles = {k: self.interpolate(current_keyframe['arm_angles'][k], next_keyframe['arm_angles'][k], self.tween_factor) for k in current_keyframe['arm_angles']}
        leg_angles = {k: self.interpolate(current_keyframe['leg_angles'][k], next_keyframe['leg_angles'][k], self.tween_factor) for k in current_keyframe['leg_angles']}

        return {'position': position, 'arm_angles': arm_angles, 'leg_angles': leg_angles}

    def pause_at_last_frame(self):
        if self.is_last_frame_reached:
            pygame.time.wait(3000)  # Wait for 5000 milliseconds (5 seconds)
            self.is_last_frame_reached = False  # Reset the flag
