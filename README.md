# Frontendmentor.io Color Helper
Python script to extract colors from frontendmentor.io into css variables
there're 2 modes available: `sass` and `css`
to run it:
```lang=bash
python main.py path_to_style-guide.md [mode('css' | 'sass')]
```
example running it aginst the [style-guide.md](https://raw.githubusercontent.com/nicksenap/frontendmentor.io.color.helper/master/style-guide.md) file in this repo will output the following with `css` mode:
```lang=css
:root {
    --moderateBlue: hsl(238, 40%, 52%);
    --softRed: hsl(358, 79%, 66%);
    --lightGrayishBlue: hsl(239, 57%, 85%);
    --paleRed: hsl(357, 100%, 86%);
    --darkBlue: hsl(212, 24%, 26%);
    --grayishBlue: hsl(211, 10%, 45%);
    --lightGray: hsl(223, 19%, 93%);
    --veryLightGray: hsl(228, 33%, 97%);
    --white: hsl(0, 0%, 100%);
}
```
and following with `sass` mode:
```lang=sass
$moderate-blue: hsl(238, 40%, 52%);
$soft-red: hsl(358, 79%, 66%);
$light-grayish-blue: hsl(239, 57%, 85%);
$pale-red: hsl(357, 100%, 86%);
$dark-blue: hsl(212, 24%, 26%);
$grayish-blue: hsl(211, 10%, 45%);
$light-gray: hsl(223, 19%, 93%);
$very-light-gray: hsl(228, 33%, 97%);
$white: hsl(0, 0%, 100%);
```
