# Linha 102
# Linha 103
# Linha 104
# Linha 105
# Linha 106
# Linha 107
# Linha 108
# Linha 109
# Linha 110

# Linha 111
# Linha 112
# Linha 113
# Linha 114
# Linha 115
# Linha 116
# Linha 117
# Linha 118
# Linha 119
# Linha 120

# Linha 121
# Linha 122
# Linha 123
# Linha 124
# Linha 125
# Linha 126
# Linha 127
# Linha 128
# Linha 129
# Linha 130

# Linha 131
# Linha 132
# Linha 133
# Linha 134
# Linha 135
# Linha 136
# Linha 137
# Linha 138
# Linha 139
# Linha 140

# Linha 141
# Linha 142
# Linha 143
# Linha 144
# Linha 145
# Linha 146
# Linha 147
# Linha 148
# Linha 149
# Linha 150

# Linha 151
# Linha 152
# Linha 153
# Linha 154
# Linha 155
# Linha 156
# Linha 157
# Linha 158
# Linha 159
# Linha 160

# Linha 161
# Linha 162
# Linha 163
# Linha 164
# Linha 165
# Linha 166
# Linha 167
# Linha 168
# Linha 169
# Linha 170

# Linha 171
# Linha 172
# Linha 173
# Linha 174
# Linha 175
# Linha 176
# Linha 177
# Linha 178
# Linha 179
# Linha 180

# Linha 181
# Linha 182
# Linha 183
# Linha 184
# Linha 185
# Linha 186
# Linha 187
# Linha 188
# Linha 189
# Linha 190

# Linha 191
# Linha 192
# Linha 193
# Linha 194
# Linha 195
# Linha 196
# Linha 197
# Linha 198
# Linha 199
# Linha 200



import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands



cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")

      continue

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()