import speech_recognition as sr
from GoogleNews import GoogleNews
import pyttsx3
import datetime
import webbrowser
import pywhatkit

# Intialization
googlenews = GoogleNews()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


# Commands
def cmd():
    with sr.Microphone() as source:
        print("Activating Ding...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        engine.say("Welcome back sir")
        engine.runAndWait()
        print('Sup?')
        recordedaudio = recognizer.listen(source, timeout=5)
        print("Alrighty!")
    try:
        command = recognizer.recognize_google(recordedaudio, language='en_US')
        command = command.lower()
        print('Your message:', format(command))

    except Exception as ex:
        print(ex)


    if 'Test' in command:
        cap = cv2.VideoCapture(0)

        hand_detector = mp.solutions.hands.Hands()
        drawing_utils = mp.solutions.drawing_utils
        screen_width, screen_height = pyautogui.size()

        index_y = 0

        while True:
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame_height, frame_width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = hand_detector.process(rgb_frame)
            hands = output.multi_hand_landmarks

            if hands:
                for hand in hands:
                    drawing_utils.draw_landmarks(frame, hand)

                    landmarks = hand.landmark
                    for ID, landmark in enumerate(landmarks):
                        x = int(landmark.x * frame_width)
                        y = int(landmark.y * frame_height)

                        if ID == 8:
                            cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                            index_x = screen_width / frame_width * x
                            index_y = screen_height / frame_height * y
                            pyautogui.moveTo(index_x, index_y)

                        if ID == 4:
                            cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                            thumb_x = screen_width / frame_width * x
                            thumb_y = screen_height / frame_height * y
                            print('On ', abs(index_y - thumb_y))
                            if abs(index_y - thumb_y) < 20:
                                # pyautogui.alert("Hello Aditya!")
                                pyautogui.click()
                                pyautogui.sleep(1)
                                print(hands)

            cv2.imshow('Hands', frame)
            key = cv2.waitKey(3)
            if key == 27:
                print('Exiting..')
                break
            engine.runAndWait()






   # hello
    if 'hello' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 250)
        engine.say('Hello Aditya Sir, How are you today?')
        engine.runAndWait()

    # news
    if "today's news" in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 250)
        a = googlenews.get_news('Todays news')
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')
        engine.say(a)
        engine.runAndWait()

    # time
    if 'what is time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say("Time right now is")
        engine.say(time)
        engine.runAndWait()

    # gm
    if 'good morning' in command:
        engine.say("Good morning Aditya Ji, Have a great day today!")
        engine.runAndWait()

    # youtube
    if 'open youtube' in command:
        b = 'opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')

    # ram
    if 'hare ram' in command:
        engine.say("Jay Shree Ram")
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=vVgz3Pg-EMs&t=107s')

    # creator
    if 'who is your creator' in command:
        engine.say("My Creator is Addy Sir, He lives in India and he made me using Python")
        engine.runAndWait()

    # weather
    if 'how is the weather today' in command:
        a = googlenews.get_news("Indore city Temprature")
        googlenews.result()
        a = googlenews.gettext()
        print(*a[1:5], sep=',')
        engine.say(a)
        engine.runAndWait()

    # jarvis
    if 'hey didi' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 200)
        a = 'Ji Aditya Sir?'
        engine.say(a)
        engine.runAndWait()

    if 'how smart are you' in command:
        a = 'I can do anything for you Aditya ji, like'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('www.youtube.com/watch?v=dQw4w9WgXcQ')

    if 'aur batao' in command:
        rate = engine.getProperty("rate")
        engine.setProperty("rate", 200)
        engine.say("sabh badiya, aap bataye")

        engine.runAndWait()

    if 'bye' in command:
        engine.say("Bye bye Aditya ji")
        engine.runAndWait()

    if 'open mail' in command:
        engine.say("opening mails sir")
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
        engine.runAndWait()

    if 'open linkedin' in command:
        engine.say("Opening Linkedin")
        webbrowser.open("www.linkedin.com/in/addy007")
        engine.runAndWait()

    if 'jay shri ram' in command:
        engine.say("JAY SHREE RAM!")
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com/watch?v=dZxrpr_yS5g&t=6s')

    if 'play a song' in command:
        engine.say("Here's a song for you, ")
        webbrowser.open("https://www.youtube.com/watch?v=LMeZAyPaRsU")
        engine.runAndWait()

    if 'open engine' in command:
        engine.say("Opening the engine")
        engine.open
        engine.runAndWait()


cmd()