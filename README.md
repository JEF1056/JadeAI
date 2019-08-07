Hey, what's this?! A chatbot?

Jade is really simple to get up and running. Just get some data, such as these [anime subtitles](https://www.kaggle.com/jef1056/anime-subtitles) (*ahem shameless plug*), rename it to `inputcln.txt`, move it to the same directory as the `.py` file, and start the program with the `-train` flag.

BAM, it'll eat all your RAM and CPU until suddenly you have a 2-3 gb model (`.p`) file. *Run without the `-train` flag for faster, more nyoom speeds.*

Add Jade at https://discordbots.org/bot/410253782828449802

# ***ALL BELOW IS OUTDATED, AND IS NO LONGER SUPPORTED***

# JadeV4 Usage
--------
Jade's Prefix is `JD`, and is used to trigger all possible commands through NLP.
Prefix is not required in DMs.

## Example syntax:
--------

### Contextual Generative Conversation

<details><summary>Chatting Instructions</summary>
<p>

Query:
```
Hi!
How old are you?
```
Response:
```
Hi, I don't know you!
I am 9 years old.
```
Jade can do basic math, with spaces as delimiters. Some basic hardcoded functions also exist.

</p>
</details>

####
--------

### Neural Style

<details><summary>Style Instructions</summary>
<p>
  
Query:
```
Can you style this using un? [Attach Image]
Use exp to style [Image Link]
```
*[Attach Image] and [Image Link] would reference [This image](https://github.com/JEF1056/JadeAI/blob/master/EXAMPLE/style_ex.jpg) in this demo.*
<br>
<br>
Response:
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/un_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/exp_ex.jpg' height = '200px' width="355"></a>
<br>
Jade can extract style types (flags) such as `exp` and `un` and links from within the command phrase.

</p>
</details>

<details><summary>Style Types (Flags)</summary>
<p>
  
Listed below are flags, in the format `FLAG ||| NAME OF STYLE IMAGE`. Left images are the original, Right images are styled by Jade.
<br>
<br>
```un ||| Udnie ```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/un_ex.jpg' height = '200px' width="355"></a>
<br>
```dk ||| Dark Paint```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/dk_ex.jpg' height = '200px' width="355"></a>
<br>
```en ||| Enviornment```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/env_ex.jpg' height = '200px' width="355"></a>
<br>
```rd||| Red```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/rd_ex.jpg' height = '200px' width="355"></a>
<br>
```lm ||| La Muse```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/lm_ex.jpg' height = '200px' width="355"></a>
<br>
```rp ||| Rainbow Princess```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/rp_ex.jpg' height = '200px' width="355"></a>
<br>
```sc ||| The Scream```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/sc_ex.jpg' height = '200px' width="355"></a>
<br>
```wr ||| Wreck (George Washington)```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/wr_ex.jpg' height = '200px' width="355"></a>
<br>
```wv ||| Wave```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/wv_ex.jpg' height = '200px' width="355"></a>
<br>
```ha1 ||| My artist's art ^-^```
```Works best with images that have a "focus"```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/ha_ex.jpg' height = '200px' width="355"></a>
<br>
```exp ||| Experimental```
```WARNING: Most models in this folder are really... uh... weird```
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/style_ex.jpg' height = '200px' width="355"></a>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/exp_ex.jpg' height = '200px' width="355"></a>
<br>

</p>
</details>

####
--------

### Object Recognition

<details><summary>Object Recognition Instructions</summary>
<p>
  
Query:
```
What objects are in this image? [Attach Image]
Can you find the dog in this picture? [Image Link]
```
*[Attach Image] would reference [This image](https://github.com/JEF1056/JadeAI/blob/master/EXAMPLE/obj_ex_d.jpg) in this demo.*
<br>
*[Image Link] would reference [This image](https://github.com/JEF1056/JadeAI/blob/master/EXAMPLE/obj_ex_fd.jpg) in this demo.*
<br>
<br>
Response:
<br>

<img src="https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/d_ex.jpg" height="200" width="355"/></a>
<img src="https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/fd_ex.jpg" height="200" width="355"/></a>

<br>

</p>
</details>

####
--------

### Optical Character Recognition

<details><summary>OCR Instructions</summary>
<p>
  
Query:
```
What text is in this image? [Attach Image]
Could read this for me? [Image Link]
```
*[Attach Image] would reference [This image](UPLOAD PENDING) in this demo.*
<br>
*[Image Link] would reference [This image](UPLOAD PENDING) in this demo.*
<br>
<br>
Response:
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/ocr_re_ex.jpg' width='380px' height = '64px'></a>
<br>

</p>
</details>

####
--------

### Face Recognition

<details><summary>Face Recognition Instructions</summary>
<p>
  
Query:
```
Who is this? [Attach Image]
Do know who the people in this image: [Image Link] are?
```
*[Attach Image] and [Image Link] would reference [This image](EXAMPLE/fr_ex.png) in this demo.*
<br>
<br>
Response:
<br>
<img src = 'https://raw.githubusercontent.com/JEF1056/JadeAI/master/EXAMPLE/fr_re_ex.jpg' height = '355' width='200px'>
<br>
```Justin Timberlake```
<br>
<br>
Note: This operation works with multiple faces in an image.

</p>
</details>

<details><summary>Adding Faces</summary>
<p>
  
```DO NOT ADD FACES IF NOT NESSISARY. ONLY ADD FACES IF THE ORIGINAL IMAGE RETURNS "Unknown"```
<br>
<br>
Query:
```
Add "Justin Timberlake" using this: [Image Link]
This is "Justin Timberlake" [Attach Image]
```
**The "" are REQUIRED around names to be added.**
<br>
*[Attach Image] and [Image Link] would reference [This image](EXAMPLE/fr_ex.png) in this demo.*
<br>
<br>
Response:
<br>
```Added face "Justin Timberlake" to my library in 22742ms```
<br>

</p>
</details>

####
--------
[![Discord Bots](https://discordbots.org/api/widget/410253782828449802.svg)](https://discordbots.org/bot/410253782828449802)
