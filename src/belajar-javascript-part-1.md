Title: Belajar Javascript: Bhg 1
Date: 2012-11-28 22:47:00
Status: draft
Category: JavaScript

Memetik kata-kata [Douglas Crockford][1], JavaScript adalah bahasa 
pengaturcaraan yang sering disalahfahami walaupun ianya merupakan bahasa 
pengaturcaraan yang paling popular sekali dengan penggunaan yang paling meluas.  

JavaScript, sebelum penggunaannya yang begitu meluas seperti sekarang biasanya 
menjadi bahasa kelas kedua bagi kebanyakkan programmer. Saya katakan kelas 
kedua kerana ia jarang dipelajari secara formal sepertimana bahasa lain seperti 
PHP, Python, Ruby, Perl, Java, C dan sebagainya. Maksud 'formal' disini ialah 
kita mengambil masa untuk berkenalan dengan bahasa tersebut bermula daripada 
ciri-ciri asas seperti *data type*, *control structure* dan sebagainya.  
Seringkali apabila terpaksa menggunakan JavaScript, kita akan mendapatkan 
library ataupun *code snippet* di Internet, ubah beberapa baris dan sekiranya 
ia melakukan apa yang kita kehendaki, selesai ! Akhirnya JavaScript sering 
menjadi cercaan apabila beberapa masalahnya yang tidak dijangka kita temui 
dalam aplikasi yang kita bangunkan.

Saya bercadang untuk mula mempelajari JavaScript secara lebih tersusun dan 
berharap dapat berkongsi pengalaman yang tersebut melalui beberapa siri tulisan 
dalam blog ini. Untuk proses pembelajaran ini, saya akan cuba membina sebuah 
aplikasi JavaScript ringkas dan akan cuba meneroka ciri-ciri asas JavaScript.  
Ini bagi saya lebih menarik dan tidak menjemukan berbanding mencuba satu demi 
satu contoh kod bagi setiap *features* yang ada. Sebaliknya kita akan 
mengenalpasti masalah yang perlu diselesaikan dan cuba cari *features* 
JavaScript yang boleh digunakan untuk menyelesaikan masalah tersebut.

Aplikasi yang saya ingin bangunkan adalah fungsi *autocomplete* ringkas. Kita 
selalu temui *features* ini dalam banyak laman web, terutamanya yang melibatkan 
fungsi carian. Saya juga banyak menggunakan *autocomplete* dalam aplikasi yang 
saya bangunkan. Namun sehingga ke hari ini saya tidak pernah mengambil tahu 
bagaimana sebenarya fungsi autocomplete ini berfungsi dalam JavaScript.

Kita mulakan aplikasi ini dengan kod html ringkas seperti berikut:-

    <html>
    <head>
    <script src="app.js"></script>
    </head>
    <body>
    <input type="text" name="keyword" id="keyword" value="" size="20" />
    </body>
    </html>

`app.js` pula akan kelihatan seperti di bawah:-

    (function() {
        var keyword = document.getElementById('keyword');
        alert (keyword);
    }())

[1]:http://javascript.crockford.com/
[2]:http://stackoverflow.com/questions/1634268/explain-javascripts-encapsulated-anonymous-function-syntax
