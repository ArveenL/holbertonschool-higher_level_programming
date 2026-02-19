# 1. Differentiate between HTTP and HTTPS.

ok, so HTTP vs HTTPS 

- What's HTTP, anyway? Sounds like a very dangerous virus or something

- Well it stands for HyperText Transfer Protocol ( HTTP )

Let's break it down : 

HYPERTEXT | TRANSFER | PROTOCOL 

'Transfer Protol' meaning some Rules we(or the computers) follow while transfering WEB DATA between CLIENT AND SERVER ( client = e.g web browser, apps, etc &&& SERVER = a computer that stores data and allows the client to fetch those data)

Soooooooooooo, then, why not WEB DATA TRANSFER PROTOCOL (WDTP) ?

That's because when the internet was invented, mostly HyperText only, were being transfered between computers(clients and servers)

And the name remained, HyperText Transfer Protocol(HTTP)

***By the way Hypertext is a click-able(link) to a HTML document. The latter contains texts and other clickable links that send us to files, webpages, locations

---------------------------------
#### Moving on to the S in HTTPS now

The 's' in HTTPS is for 'secure' (wow, shocker !!)

HTTPS is HTTP with encryption and verification. The only difference between the two protocols is that HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses, and to digitally sign those requests and responses. As a result, HTTPS is far more secure than HTTP. A website that uses HTTP has http:// in its URL, while a website that uses HTTPS has https://.

# 2. Understand the basic working and structure of HTTP requests and responses.

HTTP works when the client send a __STRUCTURED REQUEST__ to the server

-> Structured Request = The request must follow a specific format and order { REQUEST LINE --> HEADERS --> BODY(optional) }

- _Example of REQUEST LINE_ = 

  GET /products HTTP/1.1

- _Example of HTTP HEADERS_ = 

  **Host:** example.com <br>
  **User-Agent:** Chrome <br>
  **Accept:** text/html <br>

- _Example of Body_ = 

  {<br>

    username = "John"<br>
    password = "1234"<br>

  }

**Note**: HTTPS use the same type of request line / headers / body, as HTTP but it's encrypted during the transmission(So, others can't read or modify them. Hereby, "others" = any 3rd party human or machine trying to intercept the data)

-------

# 3. Recognize and explain the common HTTP methods and status codes.

**Common HTTP methods**: GET (retrieve data), POST (send data), PUT (update/replace data), DELETE (remove data), PATCH (partially update data).

For example, GET is an HTTP command (method) that tells the server “send me this resource.”

**Common status codes**: 200 (OK), 201 (Created), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Internal Server Error).

We can see status codes in the browser’s Developer Tools (Network tab) or in server/API responses.

