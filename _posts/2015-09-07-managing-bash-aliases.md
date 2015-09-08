---
layout: post
title:  "Managing bash aliases"
date:   2015-09-07 21:05:00
categories: code
---

Bash aliases are great. Whether you use them to quickly connect to servers or just soup up the standard bash commands, they are a useful tool for eliminating repetitive tasks. I'm always adding new ones to optimize my workflow which, of course, lead to me create aliases to optimize _that_ workflow. While there are more complete CLI alternatives for alias management like [aka][AKA], I prefer two simple commands for managing my aliases, which I keep in `~/.bash_aliases`.

{% highlight sh %}

alias eal="subl ~/.bash_aliases"
alias sal='. ~/.bash_aliases; echo "Sourced ~/.bash_aliases";'

{% endhighlight %}

The aliases are `eal` for "Edit ALiases" and `sal` for "Source ALiases". The command `subl` is the OSX CLI for [Sublime Text][Sublime CLI]. For reference, `.` is the same as `source`. Enjoy.

[AKA]: https://github.com/ytbryan/aka
[Sublime CLI]: https://www.sublimetext.com/docs/2/osx_command_line.html