div align="center">

# Personal data

![image](../asset/personal%20data.png)

</div>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="https://piwik.pro/blog/what-is-pii-personal-data/" title="What Is PII, non-PII, and Personal Data?" target="_blank">What Is PII, non-PII, and Personal Data?</a></li>
<li><a href="https://docs.python.org/3/library/logging.html" title="logging documentation" target="_blank">logging documentation</a></li>
<li><a href="https://github.com/pyca/bcrypt/" title="bcrypt package" target="_blank">bcrypt package</a></li>
<li><a href="https://www.youtube.com/watch?v=-ARI4Cz-awo" title="Logging to Files, Setting Levels, and Formatting" target="_blank">Logging to Files, Setting Levels, and Formatting</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>Examples of Personally Identifiable Information (PII)</li>
<li>How to implement a log filter that will obfuscate PII fields</li>
<li>How to encrypt a password and check the validity of an input password</li>
<li>How to authenticate to a database using environment variables</li>
</ul>

<h2>Requirements</h2>

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
<li>All your functions should be type annotated</li>
</ul>

  </div>
</div>

 <h2 class="gap">Tasks</h2>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Regex-ing
    </h3>
  </div>
<p>Write a function called filter_datum that returns the log message obfuscated:</p>
<ul>
<li>Arguments:

<ul>
<li><code>fields</code>: a list of strings representing all fields to obfuscate</li>
<li><code>redaction</code>: a string representing by what the field will be obfuscated</li>
<li><code>message</code>: a string representing the log line</li>
<li><code>separator</code>: a string representing by which character is separating all fields in the log line (<code>message</code>)</li>
</ul></li>
<li>The function should use a regex to replace occurrences of certain field values.</li>
<li><code>filter_datum</code> should be less than 5 lines long and use <code>re.sub</code> to perform the substitution with a single regex.</li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

filter_datum = __import__(&#39;filtered_logger&#39;).filter_datum

fields = [&quot;password&quot;, &quot;date_of_birth&quot;]
messages = [&quot;name=egg;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="543139353d3869313333393d3a143133332735392438317a373b39">[email&#160;protected]</a>;password=eggcellent;date_of_birth=12/12/1986;&quot;, &quot;name=bob;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="30555d51595c0d525f527054495c515e1e535f5d">[email&#160;protected]</a>;password=bobbycool;date_of_birth=03/04/1993;&quot;]

for message in messages:
    print(filter_datum(fields, &#39;xxx&#39;, message, &#39;;&#39;))

bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c1a4aca0a8adfca4a6a6aca8af81a4a6a6b2a0acb1ada4efa2aeac">[email&#160;protected]</a>;password=xxx;date_of_birth=xxx;
name=bob;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="89ece4e8e0e5b4ebe6ebc9edf0e5e8e7a7eae6e4">[email&#160;protected]</a>;password=xxx;date_of_birth=xxx;
bob@dylan:~$
</code></pre>

  </div>

<h3 class="panel-title">
    1. Log formatter
</h3>

  </div>

<p>Copy the following code into <code>filtered_logger.py</code>.</p>

<pre><code class="python">import logging


class RedactingFormatter(logging.Formatter):
    &quot;&quot;&quot; Redacting Formatter class
        &quot;&quot;&quot;

    REDACTION = &quot;***&quot;
    FORMAT = &quot;[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s&quot;
    SEPARATOR = &quot;;&quot;

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -&gt; str:
        NotImplementedError
</code></pre>

<p>Update the class to accept a list of strings <code>fields</code> constructor argument.</p>

<p>Implement the <code>format</code> method to filter values in incoming log records using <code>filter_datum</code>. Values for fields in <code>fields</code> should be filtered.</p>

<p>DO NOT extrapolate <code>FORMAT</code> manually. The <code>format</code> method should be less than 5 lines long.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

import logging
import re

RedactingFormatter = __import__(&#39;filtered_logger&#39;).RedactingFormatter

message = &quot;name=Bob;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a6c3cbc7cfca9bc4c9c4e6c2dfcac7c888c5c9cb">[email&#160;protected]</a>;ssn=000-123-0000;password=bobby2019;&quot;
log_record = logging.LogRecord(&quot;my_logger&quot;, logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=(&quot;email&quot;, &quot;ssn&quot;, &quot;password&quot;))
print(formatter.format(log_record))

bob@dylan:~$
bob@dylan:~$ ./main.py
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
bob@dylan:~$
</code></pre>

  </div>

<h3>
    2. Create logger
</h3>

<p>Use <a href="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2019/11/a2e00974ce6b41460425.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240622%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240622T171212Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29bcf059b8d924e1ddddd16f83a6b044a96fc96f8a0edeb1d0182e1df5f81693" title="user_data.csv" target="_blank">user_data.csv</a> for this task</p>

<p>Implement a <code>get_logger</code> function that takes no arguments and returns a <code>logging.Logger</code> object.</p>

<p>The logger should be named <code>&quot;user_data&quot;</code> and only log up to <code>logging.INFO</code> level. It should not propagate messages to other loggers.
It should have a <code>StreamHandler</code> with <code>RedactingFormatter</code> as formatter.</p>

<p>Create a tuple <code>PII_FIELDS</code> constant at the root of the module containing the fields from <code>user_data.csv</code> that are considered PII. 
<code>PII_FIELDS</code> can contain only 5 fields - choose the right list of fields that can are considered as &ldquo;important&rdquo; PIIs or information that you <strong>must hide</strong> in your logs.
Use it to parameterize the formatter.</p>

<p><strong>Tips:</strong></p>

<ul>
<li><a href="https://piwik.pro/blog/what-is-pii-personal-data/" title="What Is PII, non-PII, and personal data?" target="_blank">What Is PII, non-PII, and personal data?</a></li>
<li><a href="https://www.digitalguardian.com/blog/uncovering-password-habits-are-users%E2%80%99-password-security-habits-improving-infographic" title="Uncovering Password Habits" target="_blank">Uncovering Password Habits</a></li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

import logging

get_logger = __import__(&#39;filtered_logger&#39;).get_logger
PII_FIELDS = __import__(&#39;filtered_logger&#39;).PII_FIELDS

print(get_logger.__annotations__.get(&#39;return&#39;))
print(&quot;PII_FIELDS: {}&quot;.format(len(PII_FIELDS)))

bob@dylan:~$
bob@dylan:~$ ./main.py
&lt;class &#39;logging.Logger&#39;&gt;
PII_FIELDS: 5
bob@dylan:~$
</code></pre>

  </div>

<h3 class="panel-title">
    3. Connect to secure database
</h3>

<p>Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.</p>

<p>In this task, you will connect to a secure <code>holberton</code> database to read a <code>users</code> table. 
The database is protected by a username and password that are set as environment variables on the server named <code>PERSONAL_DATA_DB_USERNAME</code> (set the default as &ldquo;root&rdquo;), <code>PERSONAL_DATA_DB_PASSWORD</code> (set the default as an empty string) and <code>PERSONAL_DATA_DB_HOST</code> (set the default as &ldquo;localhost&rdquo;). </p>

<p>The database name is stored in <code>PERSONAL_DATA_DB_NAME</code>. </p>

<p>Implement a <code>get_db</code> function that returns a connector to the database (<code>mysql.connector.connection.MySQLConnection</code> object). </p>

<ul>
<li>Use the <code>os</code> module to obtain credentials from the environment</li>
<li>Use the module <code>mysql-connector-python</code> to connect to the MySQL database (<code>pip3 install mysql-connector-python</code>)</li>
</ul>

<pre><code>bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY &#39;root&#39;;
GRANT ALL PRIVILEGES ON my_db.* TO &#39;root&#39;@&#39;localhost&#39;;

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email VARCHAR(256)
);

INSERT INTO users(email) VALUES (&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4b2924290b2f32272a2565282426">[email&#160;protected]</a>&quot;);
INSERT INTO users(email) VALUES (&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1a7873785a7e63767b7434797577">[email&#160;protected]</a>&quot;);

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT COUNT(*) FROM users;&quot; | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

get_db = __import__(&#39;filtered_logger&#39;).get_db

db = get_db()
cursor = db.cursor()
cursor.execute(&quot;SELECT COUNT(*) FROM users;&quot;)
for row in cursor:
    print(row[0])
cursor.close()
db.close()

bob@dylan:~$
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
2
bob@dylan:~$
</code></pre>

  </div>

<h3 class="panel-title">
    4. Read and filter data
</h3>

<p>Implement a <code>main</code> function that takes no arguments and returns nothing.</p>

<p>The function will obtain a database connection using <code>get_db</code> and retrieve all rows in the <code>users</code> table and display each row under a filtered format like this:</p>

<pre><code class="python">[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
</code></pre>

<p>Filtered fields:</p>

<ul>
<li>name</li>
<li>email</li>
<li>phone</li>
<li>ssn</li>
<li>password</li>
</ul>

<p>Only your <code>main</code> function should run when the module is executed.</p>

<pre><code>bob@dylan:~$ cat main.sql
-- setup mysql server
-- configure permissions
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY &#39;root&#39;;
GRANT ALL PRIVILEGES ON my_db.* TO root@localhost;

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    name VARCHAR(256), 
        email VARCHAR(256), 
        phone VARCHAR(16),
    ssn VARCHAR(16), 
        password VARCHAR(256),
    ip VARCHAR(64), 
        last_login TIMESTAMP,
    user_agent VARCHAR(512)
);

INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES (&quot;Marlene Wood&quot;,&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9af2edffe9eef3f3f3dafbeeeeb4f4ffee">[email&#160;protected]</a>&quot;,&quot;(473) 401-4253&quot;,&quot;261-72-6780&quot;,&quot;K5?BMNv&quot;,&quot;60ed:c396:2ff:244:bbd0:9208:26f2:93ea&quot;,&quot;2019-11-14 06:14:24&quot;,&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36&quot;);
INSERT INTO users(name, email, phone, ssn, password, ip, last_login, user_agent) VALUES (&quot;Belen Bailey&quot;,&quot;<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f59796908396b58c949d9a9adb969a98">[email&#160;protected]</a>&quot;,&quot;(539) 233-4942&quot;,&quot;203-38-5395&quot;,&quot;^3EZ~TkX&quot;,&quot;f724:c5d1:a14d:c4c5:bae2:9457:3769:1969&quot;,&quot;2019-11-14 06:16:19&quot;,&quot;Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30&quot;);

bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo &quot;SELECT COUNT(*) FROM users;&quot; | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,621: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
bob@dylan:~$
</code></pre>

  </div>
    <h3 class="panel-title">
      5. Encrypting passwords
    </h3>

<p>User passwords should NEVER be stored in plain text in a database.</p>

<p>Implement a <code>hash_password</code> function that expects one string argument name <code>password</code> and returns a salted, hashed password, which is a byte string.</p>

<p>Use the <code>bcrypt</code> package to perform the hashing (with <code>hashpw</code>).</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

hash_password = __import__(&#39;encrypt_password&#39;).hash_password

password = &quot;MyAmazingPassw0rd&quot;
print(hash_password(password))
print(hash_password(password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b&#39;$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO&#39;
b&#39;$2b$12$xSAw.bxfSTAlIBglPMXeL.SJnzme3Gm0E7eOEKOVV2OhqOakyUN5m&#39;
bob@dylan:~$
</code></pre>

<h3 class="panel-title">
    6. Check valid password
</h3>
    <p>Implement an <code>is_valid</code> function that expects 2 arguments and returns a boolean.</p>

<p>Arguments:</p>

<ul>
<li><code>hashed_password</code>:  <code>bytes</code> type</li>
<li><code>password</code>: string type</li>
</ul>

<p>Use <code>bcrypt</code> to validate that the provided password matches the hashed password.</p>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;

hash_password = __import__(&#39;encrypt_password&#39;).hash_password
is_valid = __import__(&#39;encrypt_password&#39;).is_valid

password = &quot;MyAmazingPassw0rd&quot;
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))

bob@dylan:~$
bob@dylan:~$ ./main.py
b&#39;$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO&#39;
True
bob@dylan:~$
</code></pre>

