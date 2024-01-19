import speech_recognition as sr
import pyttsx3
import openai
import winsound

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Hirantha"
bot_name = "Jarvis"

# New code to play a sound when the assistant is ready to listen
#winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#engine.say("I am ready to listen, say Jarvis to start")
#engine.runAndWait()

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source)
    print("Jarvis no longer listening.")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

 # New code to trigger the assistant only by the keyword "Jarvis"
    #if user_input.lower() != "jarvis":
        #continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()