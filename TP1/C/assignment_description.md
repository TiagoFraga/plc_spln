Write a Python function which receives a Python dictionary and outputs
its representation in XML:

* dictionary keys become XML tags
* if a key starts with an underscore, it becomes an attribute
* if a key is `__CONTENT` , it becomes the parent's tag text content

Take into account nested dictionaries!
