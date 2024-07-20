import command_ai as ca
from say_AI import say
import webbrowser
import datetime
from Gemini_ai import get_task
import save_file
from check_if import check_if_NULL
from open_app_function import open_app
import os

if __name__=="__main__":
    sites={"youtube":"https://youtube.com","instagram":"https://instagram.com","javatpoint":"https://www.javatpoint.com","google":"https://www.google.com","Wikipedia":"https://Wikipedia.com"}
    while True:
        
        query=ca.command()
        print(query)
        if check_if_NULL(query):
            continue        
            
        if "artificial intelligence".lower() in str(query).lower() or  "use gemini" in str(query).lower():
            say("What would you like to do.")
            task_for_gemini = ca.command()
            value_by_gemini=get_task(task_for_gemini)
            say("you would like to save it.")
            ans=ca.command()
            
            if "yes".lower() in str(ans).lower() or "like to save it".lower() in str(query).lower():
                say("ok, Sir i am saving it for you")
                save_file.save_file(task_for_gemini,value_by_gemini)
                say("File is save Successfully")
            else:
                say("Ok, Sir")
        elif "open".lower() in str(query).lower() and "vs code".lower() in str(query).lower():
            say("Opening vs code")
            os.system("code")

        elif "open".lower() in str(query).lower() and"app".lower() in str(query).lower():
            say("Which app you would like to open")
            app_name=ca.command()
            while app_name==None:
                say("I didn't here what you say? ")
                app_name=ca.command()
            say(f"Opening {app_name}")
            open_app(app_name)
        
        elif "open".lower() in str(query).lower():
            for name,site in sites.items():
                if "open".lower() in str(query).lower() and name.lower() in str(query).lower():
                    say(f"Opening {name} sir...")
                    webbrowser.open_new_tab(site)
        elif "search".lower() in str(query).lower() and "website".lower() in str(query).lower():
            say("Which website you will like to visit.")
            task=ca.command()
            webbrowser.open_new_tab(f"https://www.google.com/search?q={task.lower()}")
        elif "the".lower() in str(query).lower() and "time".lower() in str(query).lower():
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")
        elif "exit" in str(query).lower():
            say("exiting the program")
            exit()
        else:
            sentence=get_task(query)
            say(sentence)