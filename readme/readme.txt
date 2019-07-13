Formatter "CSS AutoPrefixer".
It allows to insert needed vendor prefixes in lexers CSS, SCSS, Sass.
Uses Node.js library "Autoprefixer". 

Example: such CSS code:

    #wrapper {
        border-radius: 1em;
        transform: rotate(45deg)
    }

will be changed to:

    #wrapper {
        border-radius: 1em;
        -webkit-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
                transform: rotate(45deg)
    }

Uses portions from Sublime Text plugin:
https://github.com/sindresorhus/sublime-autoprefixer

Author: Alexey Torgashin (CudaText)
License: MIT
