<!DOCTYPE html>
<html lang="en">
<body>

  <div class="panel-body">
<h1>Redis Basis</h1>
<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="/rltoken/VOYtf-O0J8IniAaofOwoNQ" title="Redis commands" target="_blank">Redis commands</a></li>
<li><a href="/rltoken/yqIvla14uyQ2pBRk2i-tBQ" title="Redis python client" target="_blank">Redis python client</a></li>
<li><a href="/rltoken/NxpS4PTyCpDK29oLyCBwHQ" title="How to Use Redis With Python" target="_blank">How to Use Redis With Python</a></li>
<li><a href="/rltoken/vk2Wan5dEYyoGNwCIvoFaQ" title="Redis Crash Course Tutorial" target="_blank">Redis Crash Course Tutorial</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Learn how to use redis for basic operations</li>
<li>Learn how to use redis as a simple cache</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)</li>
<li>All of your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions and methods should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions and coroutines must be type-annotated.</li>
</ul>

<h2>Install Redis on Ubuntu 18.04</h2>

<pre><code>$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i &quot;s/bind .*/bind 127.0.0.1/g&quot; /etc/redis/redis.conf
</code></pre>

<h2>Use Redis in a container</h2>

<p>Redis server is stopped by default - when you are starting a container, you should start it with: <code>service redis-server start</code></p>

  </div>
</div>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Writing strings to Redis
    </h3>

<!-- Task Body -->
<p>Create a <code>Cache</code> class. In the <code>__init__</code> method, store an instance of the Redis client as a private variable named <code>_redis</code> (using <code>redis.Redis()</code>) and flush the instance using <code>flushdb</code>.</p>

<p>Create a <code>store</code> method that takes a <code>data</code> argument and returns a string. The method should generate a random key (e.g. using <code>uuid</code>), store the input data in Redis using the random key and return the key.</p>

<p>Type-annotate <code>store</code> correctly. Remember that <code>data</code> can be a <code>str</code>, <code>bytes</code>, <code>int</code> or <code>float</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
import redis

Cache = __import__(&#39;exercise&#39;).Cache

cache = Cache()

data = b&quot;hello&quot;
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b&#39;hello&#39;
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
    <li>Directory: <code>0x0B_redis_basic</code></li>
    <li>File: <code>exercise.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->

  </div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Reading from Redis and recovering original type
    </h3>
<!-- Progress vs Score -->

<!-- Task Body -->
<p>Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store <code>&quot;a&quot;</code> as a UTF-8 string, it will be returned as <code>b&quot;a&quot;</code> when retrieved from the server.</p>

<p>In this exercise we will create a <code>get</code> method that take a <code>key</code> string argument and an optional <code>Callable</code> argument named <code>fn</code>. This callable will be used to convert the data back to the desired format.</p>

<p>Remember to conserve the original <code>Redis.get</code> behavior if the key does not exist.</p>

<p>Also, implement 2 new methods: <code>get_str</code> and <code>get_int</code> that will automatically parametrize <code>Cache.get</code> with the correct conversion function.</p>

<p>The following code should not raise:</p>

<pre><code class="python">cache = Cache()

TEST_CASES = {
    b&quot;foo&quot;: None,
    123: int,
    &quot;bar&quot;: lambda d: d.decode(&quot;utf-8&quot;)
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
    <li>Directory: <code>0x0B_redis_basic</code></li>
    <li>File: <code>exercise.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->

  </div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Incrementing values
    </h3>
<!-- Task Body -->
<p>Familiarize yourself with the <code>INCR</code> command and its python equivalent.</p>

<p>In this task, we will implement a system to count how many times methods of the <code>Cache</code> class are called.</p>

<p>Above <code>Cache</code> define a <code>count_calls</code> decorator that takes a single <code>method</code> <code>Callable</code> argument and returns a <code>Callable</code>.</p>

<p>As a key, use the qualified name of <code>method</code> using the <code>__qualname__</code> dunder method.</p>

<p>Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.</p>

<p>Remember that the first argument of the wrapped function will be <code>self</code> which is the instance itself, which lets you access the Redis instance.</p>

<p>Protip: when defining a decorator it is useful to use <code>functool.wraps</code> to conserve the original function&rsquo;s name, docstring, etc. Make sure you use it as described <a href="/rltoken/KzeKedfUQXfD6x6u2OmY-A" title="here" target="_blank">here</a>.</p>

<p>Decorate <code>Cache.store</code> with <code>count_calls</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main file &quot;&quot;&quot;

Cache = __import__(&#39;exercise&#39;).Cache

cache = Cache()

cache.store(b&quot;first&quot;)
print(cache.get(cache.store.__qualname__))

cache.store(b&quot;second&quot;)
cache.store(b&quot;third&quot;)
print(cache.get(cache.store.__qualname__))

bob@dylan:~$ ./main.py
b&#39;1&#39;
b&#39;3&#39;
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
    <li>Directory: <code>0x0B_redis_basic</code></li>
    <li>File: <code>exercise.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->

  </div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Storing lists
    </h3>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="5634"></span>

<!-- Progress vs Score -->

<!-- Task Body -->
<p>Familiarize yourself with redis commands <code>RPUSH</code>, <code>LPUSH</code>, <code>LRANGE</code>, etc.</p>

<p>In this task, we will define a <code>call_history</code> decorator to store the history of inputs and outputs for a particular function.</p>

<p>Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.</p>

<p>In <code>call_history</code>, use the decorated function&rsquo;s qualified name and append <code>&quot;:inputs&quot;</code> and <code>&quot;:outputs&quot;</code> to create input and output list keys, respectively.</p>

<p><code>call_history</code> has a single parameter named <code>method</code> that is a <code>Callable</code> and returns a <code>Callable</code>.</p>

<p>In the new function that the decorator will return, use <code>rpush</code> to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use <code>str(args)</code> to normalize. We can ignore potential <code>kwargs</code> for now.</p>

<p>Execute the wrapped function to retrieve the output. Store the output using <code>rpush</code> in the <code>&quot;...:outputs&quot;</code> list, then return the output.</p>

<p>Decorate <code>Cache.store</code> with <code>call_history</code>.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot; Main file &quot;&quot;&quot;

Cache = __import__(&#39;exercise&#39;).Cache

cache = Cache()

s1 = cache.store(&quot;first&quot;)
print(s1)
s2 = cache.store(&quot;secont&quot;)
print(s2)
s3 = cache.store(&quot;third&quot;)
print(s3)

inputs = cache._redis.lrange(&quot;{}:inputs&quot;.format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange(&quot;{}:outputs&quot;.format(cache.store.__qualname__), 0, -1)

print(&quot;inputs: {}&quot;.format(inputs))
print(&quot;outputs: {}&quot;.format(outputs))

bob@dylan:~$ ./main.py
04f8dcaa-d354-4221-87f3-4923393a25ad
a160a8a8-06dc-4934-8e95-df0cb839644b
15a8fd87-1f55-4059-86aa-9d1a0d4f2aea
inputs: [b&quot;(&#39;first&#39;,)&quot;, b&quot;(&#39;secont&#39;,)&quot;, b&quot;(&#39;third&#39;,)&quot;]
outputs: [b&#39;04f8dcaa-d354-4221-87f3-4923393a25ad&#39;, b&#39;a160a8a8-06dc-4934-8e95-df0cb839644b&#39;, b&#39;15a8fd87-1f55-4059-86aa-9d1a0d4f2aea&#39;]
bob@dylan:~$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Technical information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
    <li>Directory: <code>0x0B_redis_basic</code></li>
    <li>File: <code>exercise.py</code></li>
</ul>
</div>

<!-- Self-paced manual review -->

  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Retrieving lists
    </h3>

  </div>

  <div class="panel-body">
    <span id="user_id" data-id="5634"></span>

<p>In this tasks, we will implement a <code>replay</code> function to display the history of calls of a particular function.</p>

<p>Use keys generated in previous tasks to generate the following output:</p>

<pre><code>&gt;&gt;&gt; cache = Cache()
&gt;&gt;&gt; cache.store(&quot;foo&quot;)
&gt;&gt;&gt; cache.store(&quot;bar&quot;)
&gt;&gt;&gt; cache.store(42)
&gt;&gt;&gt; replay(cache.store)
Cache.store was called 3 times:
Cache.store(*(&#39;foo&#39;,)) -&gt; 13bf32a9-a249-4664-95fc-b1062db2038f
Cache.store(*(&#39;bar&#39;,)) -&gt; dcddd00c-4219-4dd7-8877-66afbe8e7df8
Cache.store(*(42,)) -&gt; 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
</code></pre>

<p>Tip: use <code>lrange</code> and <code>zip</code> to loop over inputs and outputs.</p>

  </div>

  <div class="list-group">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-web_back_end</code></li>
            <li>Directory: <code>0x0B_redis_basic</code></li>
            <li>File: <code>exercise.py</code></li>
        </ul>
    </div>

</body>
</html>
