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