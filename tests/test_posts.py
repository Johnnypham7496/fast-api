# testing posts
from typing import List
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    post_map = map(validate, res.json())
    posts_list = list(post_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    res.status_code == 401