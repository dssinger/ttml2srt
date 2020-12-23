# ttml2srt

Convert [TTML subtitles][ttml] to [SRT subtitles][srt].

[ttml]: https://en.wikipedia.org/wiki/Timed_Text_Markup_Language
[srt]: https://www.matroska.org/technical/subtitles.html#srt-subtitles



## How to use

Clone this repo, then run the script by passing the name of the file:

```console
$ git clone https://github.com/alexwlchan/ttml2srt.git
$ cd ttml2srt
$ ./ttml2srt mysubtitle.ttml
mysubtitle.srt
```

The converted subtitles will be written to an SRT file with the same name, and the path printed to stdout.



## History

This is a fork of a script [written by Laura Klünder](https://github.com/codingcatgirl/ttml2srt).

I've tweaked it to automatically write the new subtitles to an SRT file rather than stdout, and tried to make it faster.
