PeachPy
=======

A minimalist CLI framework for Python, uses the same interface as CherryPy

PeachPy should be as easy as :
<pre><code>
import peachpy
class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

# Interactive mode
peachpy.quickstart(HelloWorld())
# Or on-time mode
peachpy.run(HelloWorld())
</code></pre>

__License__

(c) Copyright 2011 Simone Masiero. Some Rights Reserved. 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">
    <img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/au/88x31.png" />
</a>

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-Noncommercial-Share Alike 3.0 License</a>.
