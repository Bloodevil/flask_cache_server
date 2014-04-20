flask_cache_server
==================

simple cache server for save tumblr, blog backup or using cache.


1. request /a
2. if exist on flask_cache_server return /a content.
3. if not, ask target server
4. target server 200 <= status code < 300, save page to flask_cache_server and return content.
5. when save content, replace target_domain to flask_cache_server domain.
            
