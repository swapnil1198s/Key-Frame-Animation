class Keyframes:
    def __init__(self, motion):
        self.motion = motion
        self.keyframes = self.generate_keyframes()

    def generate_keyframes(self):
        if self.motion == 'j':
            return self.jump_keyframes()
        elif self.motion == 'w':
            return self.wave_keyframes() # Implement this
        else:
            raise ValueError("Invalid motion type")

    def jump_keyframes(self):
        # Define the keyframes for jumping motion
        # Replace the angle values with your specific data
        return [
            #Stand
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
             #Crouch intermediate
            {'position': (400, 310), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 135, 'left_lower': 90, 'right_upper': 45, 'right_lower': 90}},
             #Crouch
            {'position': (400, 340), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 165, 'left_lower': 90, 'right_upper': 15, 'right_lower': 90}},
             #Takeoff intermediate
            {'position': (400, 320), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 135, 'left_lower': 90, 'right_upper': 45, 'right_lower': 90}},
             #Takeoff intermediate 2
            {'position': (400, 310), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60},
              'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
              #Takeoff
            {'position': (400, 300), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
              #In air
            {'position': (400, 280), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
              #In air
            {'position': (400, 260), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
            {'position': (400, 240), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
              #Coming down
            {'position': (400, 260), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
            {'position': (400, 280), 'arm_angles': {'left_upper': 115, 'left_lower': 120, 'right_upper': 65, 'right_lower': 60},
              'leg_angles': {'left_upper': 110, 'left_lower': 90, 'right_upper': 70, 'right_lower': 90}},
             
              #Toch ground
            {'position': (400, 305), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
             #Brace impact
            {'position': (400, 310), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 135, 'left_lower': 90, 'right_upper': 45, 'right_lower': 90}},
             #Crouch
            {'position': (400, 320), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 165, 'left_lower': 90, 'right_upper': 15, 'right_lower': 90}},
             #Standing intermediate 2
            {'position': (400, 310), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 135, 'left_lower': 90, 'right_upper': 45, 'right_lower': 90}},
             #Stand
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': 45, 'right_lower': 60}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
        ]

  
    def wave_keyframes(self):
      return [
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -65, 'right_lower': -65}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -80, 'right_lower': -85}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -80, 'right_lower': -95}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -80, 'right_lower': -115}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -80, 'right_lower': -95}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -75, 'right_lower': -85}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -65, 'right_lower': -65}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -45, 'right_lower': -45}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -25, 'right_lower': -25}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -45, 'right_lower': -45}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
            {'position': (400, 300), 'arm_angles': {'left_upper': 135, 'left_lower': 120, 'right_upper': -65, 'right_lower': -65}, 
             'leg_angles': {'left_upper': 120, 'left_lower': 90, 'right_upper': 60, 'right_lower': 90}},
        ]

    def get_keyframes(self):
        return self.keyframes