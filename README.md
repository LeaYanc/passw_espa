# Password Complexity Españolizer

:![Spanish ñ](/images/laenie.jpg)

Remembering randomly generated passwords is too complex for most people, unless you use a password manager. 
Most people like to use passwords that are easy to remember. 
But brute force attacks tend to use traditional ASCII characters first. 
To slow down this type of attack, I created a small Python script that replaces some letters and symbols of traditional passwords with characters commonly found on Spanish keyboards.
The results gives a new possible password that will be far more secure than the unhardened ones.
In this way, users can use passwords they can easily remember, but hardened with Spanish special characters.


## Spanish special characters
![Spanish characters](/images/SpaChar.png)


## Proof of concept
With the Bitwarden password strenght testing tool (https://bitwarden.com/password-strength/)

I tested some weak passwords that have been hardened with the script:
![Spanish ñ](/images/Prompt.png)

And it added an extra layer of complexity to the given password.

### Original Password - 1 minute to crack
![Spanish ñ](/images/Kamala.png)

### Spanish Hardened Password - 3 years to crack
![Spanish ñ](/images/Kabuena.png)

### Original Password - 5 seconds to crack
![Spanish ñ](/images/canad.png)

### Spanish Hardened Password - 3 hours to crack
![Spanish ñ](/images/canadOK.png)

### Original Password - Less than one second to crack
![Spanish ñ](/images/BCN.png)

### Spanish Hardened Password - 1 day to crack
![Spanish ñ](/images/BCNOK.png)




