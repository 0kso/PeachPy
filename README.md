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

This work is licensed under 
<a rel="license" href="http://www.gnu.org/licenses/lgpl.html">Gnu Lesser General Public License</a>

<a href="http://www.gnu.org/licenses/lgpl.html">
    <img alt="LGPL Logo" src="http://www.gnu.org/graphics/lgplv3-88x31.png" />
</a>