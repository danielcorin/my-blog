---
layout: post
title:  "Elixir binary search"
date:   2015-09-06 19:08:00
categories: code
---


<link rel="stylesheet" href="{{ "/css/katex.min.css" | prepend: site.baseurl }}">
<script type="text/javascript" src="{{ "/js/katex.min.js" | prepend: site.baseurl }}"></script>
<style type="text/css">
.equation {
    margin-bottom: 15px;
}
</style>

A few days ago, I saw the [Guess my word][GuessMyWord] game on the front page of Hacker News. Before spoiling the fun for myself by checking out the comments, I decided to try my hand at writing a solution in Elixir. Afterwards, I generalized the code to choose its own word from the UNIX dictionary and then "guess" it, applying a binary search base on the feedback of whether each guess was alphabetically greater or less than the word itself.

{% gist ab458ec544178fb86076 %}

Example output:

    $ iex words.exs 

    Word is: barruly
    Less than: modificatory
    Less than: eagerness
    Less than: canari
    Greater than: asthenosphere
    Less than: bifoliolate
    Greater than: barad
    Less than: beguilement
    Less than: batzen
    Less than: basaltic
    Greater than: barmbrack
    Greater than: barreler
    Less than: bartholomew
    Greater than: barrio
    Found word: barruly

Something I encountered worth mentioning is how Elixir compares strings that have different capitalization. Capital letters are "less than" their lower case versions:

{% highlight elixir %}

    iex> "B" < "b"
    true

{% endhighlight %}

Knowing this, we use `String.downcase` in our implementation to avoid comparison issues in the binary search. Binary search has a time complexity of:

<div class="equation" id="eq"></div>

Given that the UNIX dictionary has 235,886 words

    $ cat /usr/share/dict/words | wc -l
      235886

the fact the our algorithm took 14 steps to "guess" the word is plausible given

<div class="equation" id="eq2"></div>

which is the number of steps we would expect it to take to guess our word.

<script type="text/javascript">
    katex.render("O(log_{2}n)", document.getElementById("eq"));
    katex.render("O(log_{2}235886) \\approx 17.85", document.getElementById("eq2"));
</script>

[GuessMyWord]: http://simbase.org/gmw/gmw.html

