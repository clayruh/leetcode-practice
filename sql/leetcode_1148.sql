SELECT DISTINCT(author_id) as id
FROM Views
WHERE author_id = viewer_id 
ORDER BY author_id ASC

-- also can be
# query table views for where author_id = viewer_id
SELECT DISTINCT author_id as id FROM views
WHERE author_id = viewer_id
# sort by id in ASC, so ORDER BY id
ORDER BY id