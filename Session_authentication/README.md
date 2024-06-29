div align="center">

# Session authentication

</div>

<h2>Background Context</h2>

<p>In this project, you will implement a <strong>Session Authentication</strong>. You are not allowed to install any other module.</p>

<p>In the industry, you should <strong>not</strong> implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="https://flask-httpauth.readthedocs.io/en/latest/" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.youtube.com/watch?v=501dpx2IjGY" title="REST API Authentication Mechanisms - Only the session auth part" target="_blank">REST API Authentication Mechanisms - Only the session auth part</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie" title="HTTP Cookie" target="_blank">HTTP Cookie</a> </li>
<li><a href="https://palletsprojects.com/p/flask/" title="Flask" target="_blank">Flask</a> </li>
<li><a href="[/rltoken/sfyvsYn5YM2MDBUqyqnK-A](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)" title="Flask Cookie" target="_blank">Flask Cookie</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What session authentication means</li>
<li>What Cookies are</li>
<li>How to send Cookies</li>
<li>How to parse Cookies </li>
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
<h2 class="gap">Tasks</h2>
    <h3 class="panel-title">
      1. Et moi et moi et moi!
    </h3>
    <p>Copy all your work of the <a href="https://github.com/AsiaGrpr/holbertonschool-web_back_end/tree/main/Basic_authentication" title="Basic authentication" target="_blank">Basic authentication</a> project in this new folder.</p>

<p>In this version, you implemented a <strong>Basic authentication</strong> for giving you access to all User endpoints:</p>

<ul>
<li><code>GET /api/v1/users</code></li>
<li><code>POST /api/v1/users</code></li>
<li><code>GET /api/v1/users/&lt;user_id&gt;</code></li>
<li><code>PUT /api/v1/users/&lt;user_id&gt;</code></li>
<li><code>DELETE /api/v1/users/&lt;user_id&gt;</code></li>
</ul>

<p>Now, you will add a new endpoint: <code>GET /users/me</code> to retrieve the authenticated <code>User</code> object.</p>

<ul>
<li>Copy folders <code>models</code> and <code>api</code> from the previous project <code>0x06. Basic authentication</code></li>
<li>Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.</li>
<li>Update <code>@app.before_request</code> in <code>api/v1/app.py</code>:

<ul>
<li>Assign the result of <code>auth.current_user(request)</code> to <code>request.current_user</code></li>
</ul></li>
<li>Update method for the route <code>GET /api/v1/users/&lt;user_id&gt;</code> in <code>api/v1/views/users.py</code>:

<ul>
<li>If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is <code>None</code>: <code>abort(404)</code></li>
<li>If <code>&lt;user_id&gt;</code> is equal to <code>me</code> and <code>request.current_user</code> is not <code>None</code>: return the authenticated <code>User</code> in a JSON response (like a normal case of <code>GET /api/v1/users/&lt;user_id&gt;</code> where <code>&lt;user_id&gt;</code> is a valid <code>User</code> ID)</li>
<li>Otherwise, keep the same behavior</li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 0
&quot;&quot;&quot;
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ddbfb2bf9db5bfa9b3f3b4b2">[email&#160;protected]</a>&quot;
user_clear_pwd = &quot;H0lbertonSchool98!&quot;

user = User()
user.email = user_email
user.password = user_clear_pwd
print(&quot;New user: {}&quot;.format(user.id))
user.save()

basic_clear = &quot;{}:{}&quot;.format(user_email, user_clear_pwd)
print(&quot;Basic Base64: {}&quot;.format(base64.b64encode(basic_clear.encode(&#39;utf-8&#39;)).decode(&quot;utf-8&quot;)))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495
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
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot;
[
  {
    &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
    &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="791b161b39111b0d17571016">[email&#160;protected]</a>&quot;, 
    &quot;first_name&quot;: null, 
    &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
    &quot;last_name&quot;: null, 
    &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
  }
]
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot;
{
  &quot;created_at&quot;: &quot;2017-09-25 01:55:17&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3e5c515c7e565c4a50105751">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;9375973a-68c7-46aa-b135-29f79e837495&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-09-25 01:55:17&quot;
}
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      1. Empty session
    </h3>
    <p>Create a class <code>SessionAuth</code> that inherits from <code>Auth</code>. For the moment this class will be empty. It&rsquo;s the first step for creating a new authentication mechanism:</p>

<ul>
<li>validate if everything inherits correctly without any overloading</li>
<li>validate the &ldquo;switch&rdquo; by using environment variables</li>
</ul>

<p>Update <code>api/v1/app.py</code> for using <code>SessionAuth</code> instance for the variable <code>auth</code> depending of the value of the environment variable <code>AUTH_TYPE</code>, If <code>AUTH_TYPE</code> is equal to <code>session_auth</code>:</p>

<ul>
<li>import <code>SessionAuth</code> from <code>api.v1.auth.session_auth</code></li>
<li>create an instance of <code>SessionAuth</code> and assign it to the variable <code>auth</code></li>
</ul>

<p>Otherwise, keep the previous mechanism.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
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

  </div>
    <h3 class="panel-title">
      2. Create a session
    </h3>
    <p>Update <code>SessionAuth</code> class:</p>

<ul>
<li>Create a class attribute <code>user_id_by_session_id</code> initialized by an empty dictionary</li>
<li>Create an instance method <code>def create_session(self, user_id: str = None) -&gt; str:</code> that creates a Session ID for a <code>user_id</code>:

<ul>
<li>Return <code>None</code> if <code>user_id</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>user_id</code> is not a string</li>
<li>Otherwise:

<ul>
<li>Generate a Session ID using <code>uuid</code> module and <code>uuid4()</code> like <code>id</code> in <code>Base</code></li>
<li>Use this Session ID as key of the dictionary <code>user_id_by_session_id</code> - the value for this key must be <code>user_id</code></li>
<li>Return the Session ID</li>
</ul></li>
<li>The same <code>user_id</code> can have multiple Session ID - indeed, the <code>user_id</code> is the value in the dictionary <code>user_id_by_session_id</code></li>
</ul></li>
</ul>

<p>Now you an &ldquo;in-memory&rdquo; Session ID storing. You will be able to retrieve an <code>User</code> id based on a Session ID.</p>

<pre><code>bob@dylan:~$ cat  main_1.py 
#!/usr/bin/env python3
&quot;&quot;&quot; Main 1
&quot;&quot;&quot;
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

print(&quot;{}: {}&quot;.format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))

user_id = None
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = 89
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;abcde&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;fghij&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

user_id = &quot;abcde&quot;
session = sa.create_session(user_id)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id, session, sa.user_id_by_session_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
&lt;class &#39;dict&#39;&gt;: {}
None =&gt; None: {}
89 =&gt; None: {}
abcde =&gt; 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {&#39;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&#39;: &#39;abcde&#39;}
fghij =&gt; 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {&#39;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&#39;: &#39;abcde&#39;, &#39;69e45c25-ec89-4563-86ab-bc192dcc3b4f&#39;: &#39;fghij&#39;}
abcde =&gt; 02079cb4-6847-48aa-924e-0514d82a43f4: {&#39;61997a1b-3f8a-4b0f-87f6-19d5cafee63f&#39;: &#39;abcde&#39;, &#39;02079cb4-6847-48aa-924e-0514d82a43f4&#39;: &#39;abcde&#39;, &#39;69e45c25-ec89-4563-86ab-bc192dcc3b4f&#39;: &#39;fghij&#39;}
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      3. User ID for Session ID
    </h3>
    <p>Update <code>SessionAuth</code> class:</p>

<p>Create an instance method <code>def user_id_for_session_id(self, session_id: str = None) -&gt; str:</code> that returns a <code>User</code> ID based on a Session ID:</p>

<ul>
<li>Return <code>None</code> if <code>session_id</code> is <code>None</code></li>
<li>Return <code>None</code> if <code>session_id</code> is not a string</li>
<li>Return the value (the User ID) for the key <code>session_id</code> in the dictionary <code>user_id_by_session_id</code>.</li>
<li>You must use <code>.get()</code> built-in for accessing in a dictionary a value based on key</li>
</ul>

<p>Now you have 2 methods (<code>create_session</code> and <code>user_id_for_session_id</code>) for storing and retrieving a link between a <code>User</code> ID and a Session ID.</p>

<pre><code>bob@dylan:~$ cat main_2.py 
#!/usr/bin/env python3
&quot;&quot;&quot; Main 2
&quot;&quot;&quot;
from api.v1.auth.session_auth import SessionAuth

sa = SessionAuth()

user_id_1 = &quot;abcde&quot;
session_1 = sa.create_session(user_id_1)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_1, session_1, sa.user_id_by_session_id))

user_id_2 = &quot;fghij&quot;
session_2 = sa.create_session(user_id_2)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_2, session_2, sa.user_id_by_session_id))

print(&quot;---&quot;)

tmp_session_id = None
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = 89
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = &quot;doesntexist&quot;
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

print(&quot;---&quot;)

tmp_session_id = session_1
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

tmp_session_id = session_2
tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
print(&quot;{} =&gt; {}&quot;.format(tmp_session_id, tmp_user_id))

print(&quot;---&quot;)

session_1_bis = sa.create_session(user_id_1)
print(&quot;{} =&gt; {}: {}&quot;.format(user_id_1, session_1_bis, sa.user_id_by_session_id))

tmp_user_id = sa.user_id_for_session_id(session_1_bis)
print(&quot;{} =&gt; {}&quot;.format(session_1_bis, tmp_user_id))

tmp_user_id = sa.user_id_for_session_id(session_1)
print(&quot;{} =&gt; {}&quot;.format(session_1, tmp_user_id))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
abcde =&gt; 8647f981-f503-4638-af23-7bb4a9e4b53f: {&#39;8647f981-f503-4638-af23-7bb4a9e4b53f&#39;: &#39;abcde&#39;}
fghij =&gt; a159ee3f-214e-4e91-9546-ca3ce873e975: {&#39;a159ee3f-214e-4e91-9546-ca3ce873e975&#39;: &#39;fghij&#39;, &#39;8647f981-f503-4638-af23-7bb4a9e4b53f&#39;: &#39;abcde&#39;}
---
None =&gt; None
89 =&gt; None
doesntexist =&gt; None
---
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
a159ee3f-214e-4e91-9546-ca3ce873e975 =&gt; fghij
---
abcde =&gt; 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {&#39;a159ee3f-214e-4e91-9546-ca3ce873e975&#39;: &#39;fghij&#39;, &#39;8647f981-f503-4638-af23-7bb4a9e4b53f&#39;: &#39;abcde&#39;, &#39;5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee&#39;: &#39;abcde&#39;}
5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee =&gt; abcde
8647f981-f503-4638-af23-7bb4a9e4b53f =&gt; abcde
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      4. Session cookie
    </h3>
    <p>Update <code>api/v1/auth/auth.py</code> by adding the method <code>def session_cookie(self, request=None):</code> that returns a cookie value from a request:</p>

<ul>
<li>Return <code>None</code> if <code>request</code> is <code>None</code></li>
<li>Return the value of the cookie named <code>_my_session_id</code> from <code>request</code> - the name of the cookie must be defined by the environment variable <code>SESSION_NAME</code></li>
<li>You must use <code>.get()</code> built-in for accessing the cookie in the request cookies dictionary</li>
<li>You must use the environment variable <code>SESSION_NAME</code> to define the name of the cookie used for the Session ID</li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_3.py
#!/usr/bin/env python3
&quot;&quot;&quot; Cookie server
&quot;&quot;&quot;
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route(&#39;/&#39;, methods=[&#39;GET&#39;], strict_slashes=False)
def root_path():
    &quot;&quot;&quot; Root path
    &quot;&quot;&quot;
    return &quot;Cookie value: {}\n&quot;.format(auth.session_cookie(request))

if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, port=&quot;5000&quot;)

bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot;
Cookie value: None
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id=Hello&quot;
Cookie value: Hello
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id=C is fun&quot;
Cookie value: C is fun
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000&quot; --cookie &quot;_my_session_id_fake&quot;
Cookie value: None
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      5. Before request
    </h3>
    <p>Update the <code>@app.before_request</code> method in <code>api/v1/app.py</code>:</p>

<ul>
<li>Add the URL path <code>/api/v1/auth_session/login/</code> in the list of excluded paths of the method <code>require_auth</code> - this route doesn&rsquo;t exist yet but it should be accessible outside authentication</li>
<li>If <code>auth.authorization_header(request)</code> and <code>auth.session_cookie(request)</code> return <code>None</code>, <code>abort(401)</code></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/status&quot;
{
  &quot;status&quot;: &quot;OK&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; # not found but not &quot;blocked&quot; by an authentication system
{
  &quot;error&quot;: &quot;Not found&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot;
{
  &quot;error&quot;: &quot;Unauthorized&quot;
}
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; -H &quot;Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh&quot; # Won&#39;t work because the environment variable AUTH_TYPE is equal to &quot;session_auth&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76&quot; # Won&#39;t work because no user is linked to this Session ID
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      6. Use Session ID for identifying a User
    </h3>
    <p>Update <code>SessionAuth</code> class:</p>

<p>Create an instance method <code>def current_user(self, request=None):</code> (overload) that returns a <code>User</code> instance based on a cookie value:</p>

<ul>
<li>You must use <code>self.session_cookie(...)</code> and <code>self.user_id_for_session_id(...)</code> to return the User ID based on the cookie <code>_my_session_id</code></li>
<li>By using this User ID, you will be able to retrieve a <code>User</code> instance from the database - you can use <code>User.get(...)</code> for retrieving a <code>User</code> from the database.</li>
</ul>

<p>Now, you will be able to get a User based on his session ID.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ cat main_4.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main 4
&quot;&quot;&quot;
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

&quot;&quot;&quot; Create a user test &quot;&quot;&quot;
user_email = &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82e0ede0f1e7f1f1ebedecc2eae0f6ecacebed">[email&#160;protected]</a>&quot;
user_clear_pwd = &quot;fake pwd&quot;

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

&quot;&quot;&quot; Create a session ID &quot;&quot;&quot;
sa = SessionAuth()
session_id = sa.create_session(user.id)
print(&quot;User with ID: {} has a Session ID: {}&quot;.format(user.id, session_id))

&quot;&quot;&quot; Create a Flask app &quot;&quot;&quot;
app = Flask(__name__)

@app.route(&#39;/&#39;, methods=[&#39;GET&#39;], strict_slashes=False)
def root_path():
    &quot;&quot;&quot; Root path
    &quot;&quot;&quot;
    request_user = sa.current_user(request)
    if request_user is None:
        return &quot;No user found\n&quot;
    return &quot;User found: {}\n&quot;.format(request_user.id)

if __name__ == &quot;__main__&quot;:
    app.run(host=&quot;0.0.0.0&quot;, port=&quot;5000&quot;)

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot;
No user found
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot; --cookie &quot;_my_session_id=Holberton&quot;
No user found
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/&quot; --cookie &quot;_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485&quot;
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      7. New view for Session Authentication
    </h3>
    <p>Create a new Flask view that handles all routes for the Session authentication.</p>

<p>In the file <code>api/v1/views/session_auth.py</code>, create a route <code>POST /auth_session/login</code> (= <code>POST /api/v1/auth_session/login</code>):</p>

<ul>
<li>Slash tolerant (<code>/auth_session/login</code> == <code>/auth_session/login/</code>)</li>
<li>You must use <code>request.form.get()</code> to retrieve <code>email</code> and <code>password</code> parameters</li>
<li>If <code>email</code> is missing or empty, return the JSON <code>{ &quot;error&quot;: &quot;email missing&quot; }</code> with the status code <code>400</code> </li>
<li>If <code>password</code> is missing or empty, return the JSON <code>{ &quot;error&quot;: &quot;password missing&quot; }</code> with the status code <code>400</code> </li>
<li>Retrieve the <code>User</code> instance based on the <code>email</code> - you must use the class method <code>search</code> of <code>User</code> (same as the one used for the <code>BasicAuth</code>)

<ul>
<li>If no <code>User</code> found, return the JSON <code>{ &quot;error&quot;: &quot;no user found for this email&quot; }</code> with the status code <code>404</code> </li>
<li>If the <code>password</code> is not the one of the <code>User</code> found, return the JSON <code>{ &quot;error&quot;: &quot;wrong password&quot; }</code> with the status code <code>401</code> - you must use <code>is_valid_password</code> from the <code>User</code> instance</li>
<li>Otherwise, create a Session ID for the <code>User</code> ID:

<ul>
<li>You must use <code>from api.v1.app import auth</code> - <strong>WARNING: please import it only where you need it</strong> - not on top of the file (can generate circular import - and break first tasks of this project)</li>
<li>You must use <code>auth.create_session(..)</code> for creating a Session ID</li>
<li>Return the dictionary representation of the <code>User</code> - you must use <code>to_json()</code> method from User </li>
<li>You must set the cookie to the response - you must use the value of the environment variable <code>SESSION_NAME</code> as cookie name - <a href="/rltoken/FCL4DJLbn05Cd3_G0-8i4g" title="tip" target="_blank">tip</a></li>
</ul></li>
</ul></li>
</ul>

<p>In the file <code>api/v1/views/__init__.py</code>, you must add this new view at the end of the file.</p>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XGET
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$  curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST
{
  &quot;error&quot;: &quot;email missing&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3f5a525e565302584a5653535e4a525a7f575d4b51115650">[email&#160;protected]</a>&quot;
{
  &quot;error&quot;: &quot;password missing&quot;
}
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="50353d31393c6d3725393c3c31253d35103832243e7e393f">[email&#160;protected]</a>&quot; -d &quot;password=test&quot;
{
  &quot;error&quot;: &quot;no user found for this email&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ee8b838f8782d38c818c9d8b9d9d878180ae868c9a80c08781">[email&#160;protected]</a>&quot; -d &quot;password=test&quot;
{
  &quot;error&quot;: &quot;wrong password&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="83e6eee2eaefbee1ece1f0e6f0f0eaecedc3ebe1f7edadeaec">[email&#160;protected]</a>&quot; -d &quot;password=fake pwd&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bfddd0ddccdaccccd6d0d1ffd7ddcbd191d6d0">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7e1b131f1712431c111c0d1b0d0d1711103e161c0a10501711">[email&#160;protected]</a>&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="492b262b3a2c3a3a20262709212b3d27672026">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$ 
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=df05b4e1-d117-444c-a0cc-ba0d167889c4&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="3f5d505d4c5a4c4c5650517f575d4b51115650">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
</code></pre>

<p>Now you have an authentication based on a Session ID stored in cookie, perfect for a website (browsers love cookies).</p>

  </div>
    <h3 class="panel-title">
      8. Logout
    </h3>
    <p>Update the class <code>SessionAuth</code> by adding a new method <code>def destroy_session(self, request=None):</code> that deletes the user session / logout:</p>

<ul>
<li>If the <code>request</code> is equal to <code>None</code>, return <code>False</code></li>
<li>If the <code>request</code> doesn&rsquo;t contain the Session ID cookie, return <code>False</code> - you must use <code>self.session_cookie(request)</code></li>
<li>If the Session ID of the request is not linked to any User ID, return <code>False</code> - you must use <code>self.user_id_for_session_id(...)</code></li>
<li>Otherwise, delete in <code>self.user_id_by_session_id</code> the Session ID (as key of this dictionary) and return <code>True</code></li>
</ul>

<p>Update the file <code>api/v1/views/session_auth.py</code>, by adding a new route <code>DELETE /api/v1/auth_session/logout</code>:</p>

<ul>
<li>Slash tolerant</li>
<li>You must use <code>from api.v1.app import auth</code></li>
<li>You must use <code>auth.destroy_session(request)</code> for deleting the Session ID contains in the request as cookie:

<ul>
<li>If <code>destroy_session</code> returns <code>False</code>, <code>abort(404)</code></li>
<li>Otherwise, return an empty JSON dictionary with the status code 200</li>
</ul></li>
</ul>

<p>In the first terminal:</p>

<pre><code>bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In a second terminal:</p>

<pre><code>bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/login&quot; -XPOST -d &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="50353d31393c6d323f3223352323393f3e103832243e7e393f">[email&#160;protected]</a>&quot; -d &quot;password=fake pwd&quot; -vvv
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
&gt; POST /api/v1/auth_session/login HTTP/1.1
&gt; Host: 0.0.0.0:5000
&gt; User-Agent: curl/7.54.0
&gt; Accept: */*
&gt; Content-Length: 42
&gt; Content-Type: application/x-www-form-urlencoded
&gt; 
* upload completely sent off: 42 out of 42 bytes
* HTTP 1.0, assume close after body
&lt; HTTP/1.0 200 OK
&lt; Content-Type: application/json
&lt; Set-Cookie: _my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721; Path=/
&lt; Access-Control-Allow-Origin: *
&lt; Content-Length: 210
&lt; Server: Werkzeug/0.12.1 Python/3.4.3
&lt; Date: Mon, 16 Oct 2017 04:57:08 GMT
&lt; 
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="8defe2effee8fefee4e2e3cde5eff9e3a3e4e2">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
* Closing connection 0
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
{
  &quot;created_at&quot;: &quot;2017-10-16 04:23:04&quot;, 
  &quot;email&quot;: &quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82e0ede0f1e7f1f1ebedecc2eae0f6ecacebed">[email&#160;protected]</a>&quot;, 
  &quot;first_name&quot;: null, 
  &quot;id&quot;: &quot;cf3ddee1-ff24-49e4-a40b-2540333fe992&quot;, 
  &quot;last_name&quot;: null, 
  &quot;updated_at&quot;: &quot;2017-10-16 04:23:04&quot;
}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/logout&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;405 Method Not Allowed&lt;/title&gt;
&lt;h1&gt;Method Not Allowed&lt;/h1&gt;
&lt;p&gt;The method is not allowed for the requested URL.&lt;/p&gt;
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/auth_session/logout&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot; -XDELETE
{}
bob@dylan:~$
bob@dylan:~$ curl &quot;http://0.0.0.0:5000/api/v1/users/me&quot; --cookie &quot;_my_session_id=e173cb79-d3fc-4e3a-9e6f-bcd345b24721&quot;
{
  &quot;error&quot;: &quot;Forbidden&quot;
}
bob@dylan:~$
</code></pre>

<p>Login, logout&hellip; what&rsquo;s else?</p>

<p>Now, after getting a Session ID, you can request all protected API routes by using this Session ID, no need anymore to send User email and password every time.</p>

  </div>
