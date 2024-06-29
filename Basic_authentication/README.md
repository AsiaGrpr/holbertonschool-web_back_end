div align="center">

# Basic authentication

![image](../asset/Basic%20authentication.png)

</div>

<h2>Background Context</h2>

<p>In this project, you will learn what the authentication process means and implement a <strong>Basic Authentication</strong> on a simple API.</p>

<p>In the industry, you should <strong>not</strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-httpauth.readthedocs.io/en/latest/" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.youtube.com/watch?v=501dpx2IjGY" title="REST API Authentication Mechanisms" target="_blank">REST API Authentication Mechanisms</a> </li>
<li><a href="https://docs.python.org/3.7/library/base64.html" title="Base64 in Python" target="_blank">Base64 in Python</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization" title="HTTP header Authorization" target="_blank">HTTP header Authorization</a> </li>
<li><a href="https://palletsprojects.com/p/flask/" title="Flask" target="_blank">Flask</a> </li>
<li><a href="https://en.wikipedia.org/wiki/Base64" title="Base64 - concept" target="_blank">Base64 - concept</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What Base64 is</li>
<li>How to encode a string in Base64</li>
<li>What Basic authentication means</li>
<li>How to send the Authorization header</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

  </div>
</div>
    <h3 class="panel-title">
      0. Simple-basic-API
    </h3>

<p>Download and start your project from this <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/11/ec2f874b061bd3a2915949f081f4f5f055104f20.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240622%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240622T164102Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=376bef6f65925e1ce4733a5db98f79485da26be6908272c454df62f8145ed1b4" title="archive.zip" target="_blank">archive.zip</a></p>

<p>In this archive, you will find a simple API with one model: <code>User</code>. Storage of these users is done via a serialization/deserialization in files.</p>

<h4>Setup and start server</h4>

<pre><code>bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app &quot;app&quot; (lazy loading)
...
bob@dylan:~$
</code></pre>

<h4>Use the API <em>(in another tab or in your browser)</em></h4>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/status HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Content-Length: 16
&lt; Access-Control-Allow-Origin: *
&lt; Server: Werkzeug/1.0.1 Python/3.7.5
&lt; Date: Mon, 18 May 2020 20:29:21 GMT
&lt; 
{&quot;status&quot;:&quot;OK&quot;}
* Closing connection 0
bob@dylan:~$
</code></pre>
<h3 class="panel-title">
    1. Error handler: Unauthorized
</h3>
    <p>What the HTTP status code for a request unauthorized? <code>401</code> of course!</p>

<p>Edit <code>api/v1/app.py</code>:</p>

<ul>
<li>Add a new error handler for this status code, the response must be:

<ul>
<li>a JSON: <code>{&quot;error&quot;: &quot;Unauthorized&quot;}</code></li>
<li>status code <code>401</code></li>
<li>you must use <code>jsonify</code> from Flask</li>
</ul></li>
</ul>

<p>For testing this new error handler, add a new endpoint in <code>api/v1/views/index.py</code>:</p>

<ul>
<li>Route: <code>GET /api/v1/unauthorized</code></li>
<li>This endpoint must raise a 401 error by using <code>abort</code> - <a href="https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/" title="Custom Error Pages" target="_blank">Custom Error Pages</a></li>
</ul>

<p>By calling <code>abort(401)</code>, the error handler for 401 will be executed.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/unauthorized&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/unauthorized&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/unauthorized HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 401 UNAUTHORIZED
&lt; Content-Type: application/json
&lt; Content-Length: 30
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:50:40 GMT
&lt; 
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
* Closing connection 0
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    2. Error handler: Forbidden
</h3>
    <p>What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? <code>403</code> of course!</p>

<p>Edit <code>api/v1/app.py</code>:</p>

<ul>
<li>Add a new error handler for this status code, the response must be:

<ul>
<li>a JSON: <code>{&quot;error&quot;: &quot;Forbidden&quot;}</code></li>
<li>status code <code>403</code></li>
<li>you must use <code>jsonify</code> from Flask</li>
</ul></li>
</ul>

<p>For testing this new error handler, add a new endpoint in <code>api/v1/views/index.py</code>:</p>

<ul>
<li>Route: <code>GET /api/v1/forbidden</code></li>
<li>This endpoint must raise a 403 error by using <code>abort</code> - <a href="https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/" title="Custom Error Pages" target="_blank">Custom Error Pages</a></li>
</ul>

<p>By calling <code>abort(403)</code>, the error handler for 403 will be executed.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/forbidden&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/forbidden&quot; -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; GET /api/v1/forbidden HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; 
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 403 FORBIDDEN
&lt; Content-Type: application/json
&lt; Content-Length: 27
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Sun, 24 Sep 2017 22:54:22 GMT
&lt; 
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
* Closing connection 0
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    3. Auth class
</h3>
    <p>Now you will create a class to manage the API authentication.</p>

<ul>
<li>Create a folder <code>api/v1/auth</code></li>
<li>Create an empty file <code>api/v1/auth/__init__.py</code></li>
<li>Create the class <code>Auth</code>:

<ul>
<li>in the file <code>api/v1/auth/auth.py</code></li>
<li>import <code>request</code> from <code>flask</code></li>
<li>class name <code>Auth</code></li>
<li>public method <code>def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> that returns <code>False</code> - <code>path</code> and <code>excluded_paths</code> will be used later, now, you don&rsquo;t need to take care of them</li>
<li>public method <code>def authorization_header(self, request=None) -&gt; str:</code> that returns <code>None</code> - <code>request</code> will be the Flask request object</li>
<li>public method <code>def current_user(self, request=None) -&gt; TypeVar(&#39;User&#39;):</code> that returns <code>None</code> - <code>request</code> will be the Flask request object</li>
</ul></li>
</ul>

<p>This class is the template for all authentication system you will implement.</p>

<pre><code>bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 0
&quot;&quot;&quot;
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(&quot;/api/v1/status/&quot;, [&quot;/api/v1/status/&quot;]))
print(a.authorization_header())
print(a.current_user())

bob@dylan:~$ 
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    4. Define which routes don&#39;t need authentication
</h3>
    <p>Update the method <code>def require_auth(self, path: str, excluded_paths: List[str]) -&gt; bool:</code> in <code>Auth</code> that returns <code>True</code> if the <code>path</code> is not in the list of strings <code>excluded_paths</code>:</p>

<ul>
<li>Returns <code>True</code> if <code>path</code> is <code>None</code></li>
<li>Returns <code>True</code> if <code>excluded_paths</code> is <code>None</code> or empty</li>
<li>Returns <code>False</code> if <code>path</code> is in <code>excluded_paths</code></li>
<li>You can assume <code>excluded_paths</code> contains string path always ending by a <code>/</code></li>
<li>This method must be slash tolerant: <code>path=/api/v1/status</code> and <code>path=/api/v1/status/</code> must be returned <code>False</code> if <code>excluded_paths</code> contains <code>/api/v1/status/</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_1.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 1
&quot;&quot;&quot;
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth(&quot;/api/v1/status/&quot;, []))
print(a.require_auth(&quot;/api/v1/status/&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/status&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/users&quot;, [&quot;/api/v1/status/&quot;]))
print(a.require_auth(&quot;/api/v1/users&quot;, [&quot;/api/v1/status/&quot;, &quot;/api/v1/stats&quot;]))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    5. Request validation!
</h3>
    <p>Now you will validate all requests to secure the API:</p>

<p>Update the method <code>def authorization_header(self, request=None) -&gt; str:</code> in <code>api/v1/auth/auth.py</code>:</p>

<ul>
<li>If <code>request</code> is <code>None</code>, returns <code>None</code> </li>
<li>If <code>request</code> doesn&rsquo;t contain the header key <code>Authorization</code>, returns <code>None</code></li>
<li>Otherwise, return the value of the header request <code>Authorization</code></li>
</ul>

<p>Update the file <code>api/v1/app.py</code>:</p>

<ul>
<li>Create a variable <code>auth</code> initialized to <code>None</code> after the <code>CORS</code> definition</li>
<li>Based on the environment variable <code>AUTH_TYPE</code>, load and assign the right instance of authentication to <code>auth</code>

<ul>
<li>if <code>auth</code>:

<ul>
<li>import <code>Auth</code> from <code>api.v1.auth.auth</code></li>
<li>create an instance of <code>Auth</code> and assign it to the variable <code>auth</code></li>
</ul></li>
</ul></li>
</ul>

<p>Now the biggest piece is the filtering of each request. For that you will use the Flask method <a href="https://flask.palletsprojects.com/en/1.1.x/api/#flask.Blueprint.before_request" title="before_request" target="_blank">before_request</a></p>

<ul>
<li>Add a method in <code>api/v1/app.py</code> to handler <code>before_request</code>

<ul>
<li>if <code>auth</code> is <code>None</code>, do nothing</li>
<li>if <code>request.path</code> is not part of this list <code>[&#39;/api/v1/status/&#39;, &#39;/api/v1/unauthorized/&#39;, &#39;/api/v1/forbidden/&#39;]</code>, do nothing - you must use the method <code>require_auth</code> from the <code>auth</code> instance</li>
<li>if <code>auth.authorization_header(request)</code> returns <code>None</code>, raise the error <code>401</code> - you must use <code>abort</code></li>
<li>if <code>auth.current_user(request)</code> returns <code>None</code>, raise the error <code>403</code> - you must use <code>abort</code></li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status/&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    6. Basic auth
</h3>
    <p>Create a class <code>BasicAuth</code> that inherits from <code>Auth</code>. For the moment this class will be empty.</p>

<p>Update <code>api/v1/app.py</code> for using <code>BasicAuth</code> class instead of <code>Auth</code> depending of the value of the environment variable <code>AUTH_TYPE</code>, If <code>AUTH_TYPE</code> is equal to <code>basic_auth</code>:</p>

<ul>
<li>import <code>BasicAuth</code> from <code>api.v1.auth.basic_auth</code></li>
<li>create an instance of <code>BasicAuth</code> and assign it to the variable <code>auth</code></li>
</ul>

<p>Otherwise, keep the previous mechanism with <code>auth</code> an instance of <code>Auth</code>.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status/&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    7. Basic - Base64 part
</h3>
    <p>Add the method <code>def extract_base64_authorization_header(self, authorization_header: str) -&gt; str:</code> in the class <code>BasicAuth</code> that returns the Base64 part of the <code>Authorization</code> header for a Basic Authentication:</p>

<ul>
<li>Return <code>None</code> if <code>authorization_header</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>authorization_header</code> is not a string</li>
<li>Return <code>None</code> if <code>authorization_header</code> doesn&rsquo;t start by <code>Basic</code> (with a space at the end)</li>
<li>Otherwise, return the value after <code>Basic</code> (after the space)</li>
<li>You can assume <code>authorization_header</code> contains only one <code>Basic</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_2.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 2
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header(&quot;Holberton School&quot;))
print(a.extract_base64_authorization_header(&quot;Basic Holberton&quot;))
print(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9u&quot;))
print(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9uIFNjaG9vbA==&quot;))
print(a.extract_base64_authorization_header(&quot;Basic1234&quot;))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      8. Basic - Base64 decode
    </h3>
    <p>Add the method <code>def decode_base64_authorization_header(self, base64_authorization_header: str) -&gt; str:</code> in the class <code>BasicAuth</code> that returns the decoded value of a Base64 string <code>base64_authorization_header</code>:</p>

<ul>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is not a string</li>
<li>Return <code>None</code> if <code>base64_authorization_header</code> is not a valid Base64 - you can use <code>try/except</code></li>
<li>Otherwise, return the decoded value as UTF8 string - you can use <code>decode(&#39;utf-8&#39;)</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 3
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.decode_base64_authorization_header(None))
print(a.decode_base64_authorization_header(89))
print(a.decode_base64_authorization_header(&quot;Holberton School&quot;))
print(a.decode_base64_authorization_header(&quot;SG9sYmVydG9u&quot;))
print(a.decode_base64_authorization_header(&quot;SG9sYmVydG9uIFNjaG9vbA==&quot;))
print(a.decode_base64_authorization_header(a.extract_base64_authorization_header(&quot;Basic SG9sYmVydG9uIFNjaG9vbA==&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_3.py
None
None
None
Holberton
Holberton School
Holberton School
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      9. Basic - User credentials
    </h3>
    <p>Add the method <code>def extract_user_credentials(self, decoded_base64_authorization_header: str) -&gt; (str, str)</code> in the class <code>BasicAuth</code> that returns the user email and password from the Base64 decoded value.</p>

<ul>
<li>This method must return 2 values</li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> is <code>None</code></li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> is not a string</li>
<li>Return <code>None, None</code> if <code>decoded_base64_authorization_header</code> doesn&rsquo;t contain <code>:</code></li>
<li>Otherwise, return the user email and the user password - these 2 values must be separated by a <code>:</code></li>
<li>You can assume <code>decoded_base64_authorization_header</code> will contain only one <code>:</code></li>
</ul>

<pre><code>bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 4
&quot;&quot;&quot;
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials(&quot;Holberton School&quot;))
print(a.extract_user_credentials(&quot;Holberton:School&quot;))
print(a.extract_user_credentials(&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="dcbeb3be9cbbb1bdb5b0f2bfb3b1">[email&#160;protected]</a>:toto1234&quot;))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_4.py
(None, None)
(None, None)
(None, None)
(&#39;Holberton&#39;, &#39;School&#39;)
(&#39;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82e0ede0c2e5efe3ebeeace1edef">[email&#160;protected]</a>&#39;, &#39;toto1234&#39;)
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      10.  Basic - User object
    </h3>
    <p>Add the method <code>def user_object_from_credentials(self, user_email: str, user_pwd: str) -&gt; TypeVar(&#39;User&#39;):</code> in the class <code>BasicAuth</code> that returns the <code>User</code> instance based on his email and password.</p>

<ul>
<li>Return <code>None</code> if <code>user_email</code> is <code>None</code> or not a string</li>
<li>Return <code>None</code> if <code>user_pwd</code> is <code>None</code> or not a string</li>
<li>Return <code>None</code> if your database (file) doesn&rsquo;t contain any <code>User</code> instance with email equal to <code>user_email</code> - you should use the class method <code>search</code> of the <code>User</code> to lookup the list of users based on their email. Don&rsquo;t forget to test all cases: &ldquo;what if there is no user in DB?&rdquo;, etc.</li>
<li>Return <code>None</code> if <code>user_pwd</code> is not the password of the <code>User</code> instance found - you must use the method <code>is_valid_password</code> of <code>User</code></li>
<li>Otherwise, return the <code>User</code> instance</li>
</ul>

<pre><code>bob@dylan:~$ cat main_5.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 5
&quot;&quot;&quot;
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = &quot;Bob&quot;
user.last_name = &quot;Dylan&quot;
user.password = user_clear_pwd
print(&quot;New user: {}&quot;.format(user.display_name()))
user.save()

&quot;&quot;&quot; Retreive this user via the class BasicAuth &quot;&quot;&quot;

a = BasicAuth()

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="640109050d08240a0b10020b110a004a070b09">[email&#160;protected]</a>&quot;, &quot;pwd&quot;)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(user_email, &quot;pwd&quot;)
print(u.display_name() if u is not None else &quot;None&quot;)

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else &quot;None&quot;)

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_5.py 
New user: Bob Dylan
None
None
None
None
Bob Dylan
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      11.  Basic - Overload current_user - and BOOM!
    </h3>
    <p>Now, you have all pieces for having a complete Basic authentication.</p>

<p>Add the method <code>def current_user(self, request=None) -&gt; TypeVar(&#39;User&#39;)</code> in the class <code>BasicAuth</code> that overloads <code>Auth</code> and retrieves the <code>User</code> instance for a request:</p>

<ul>
<li>You must use <code>authorization_header</code></li>
<li>You must use <code>extract_base64_authorization_header</code></li>
<li>You must use <code>decode_base64_authorization_header</code></li>
<li>You must use <code>extract_user_credentials</code></li>
<li>You must use <code>user_object_from_credentials</code></li>
</ul>

<p>With this update, now your API is fully protected by a Basic Authentication. Enjoy!</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_6.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 6
&quot;&quot;&quot;
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1b7974795b73796f75357274">[email&#160;protected]</a>&quot;
user_clear_pwd = &quot;H0lbertonSchool98!&quot;
user = User()
user.email = user_email
user.password = user_clear_pwd
print(&quot;New user: {} / {}&quot;.format(user.id, user.display_name()))
user.save()

basic_clear = &quot;{}:{}&quot;.format(user_email, user_clear_pwd)
print(&quot;Basic Base64: {}&quot;.format(base64.b64encode(basic_clear.encode(&#39;utf-8&#39;)).decode(&quot;utf-8&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_6.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495 / <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a9cbc6cbe9c1cbddc787c0c6">[email&#160;protected]</a>
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic test&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot;
[
  {
    &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
    &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="5e3c313c1e363c2a30703731">[email&#160;protected]</a>&quot;, 
    &quot;first_name&quot;: null, 
    &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
    &quot;last_name&quot;: null, 
    &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
  }
]
bob@dylan:~$ 
</code></pre>

  </div>
