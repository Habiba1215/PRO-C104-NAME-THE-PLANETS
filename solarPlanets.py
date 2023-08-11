import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (20,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (225,225,225))
cv2.putText(img,
            "Mercury",
            (110,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Venus",
            (190,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Earth",
            (290,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Mars",
            (385,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Jupiter",
            (590,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Saturn",
            (800,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Uranus",
            (970,310),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.putText(img,
            "Neptune",
            (1110,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (230,490,225))
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("Output",img)
cv2.waitKey(0)