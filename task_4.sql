select column_name, column_type, is_nullable, column_key, extra
from information_schema.columns
where table_name = 'books' and table_schema = alx_book_store;

