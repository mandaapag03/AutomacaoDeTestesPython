from unittest.mock import Mock
import pytest

@pytest.fixture
def posts():
    return [{'userId' : 1,
            'Id' : 1,
            'title' : 'Titulo teste 1',
            'body' : 'Conteudo do blog 1'},
            {'userId' : 2,
            'Id' : 2,
            'title' : 'Titulo teste 2',
            'body' : 'Teste de conteudo do blog 2'}]

def test_posts_retorna_2_posts(posts):
    blog = Mock()
    blog.posts.return_value = posts
    assert blog.posts() == posts

def test_post_by_user_1_retorna_1_post(posts):
    blog = Mock()
    blog.post_by_user_id.return_value = posts[0]
    assert blog.post_by_user_id(1) == posts[0]

def test_post_by_user_2_retorna_1_post(posts):
    blog = Mock()
    blog.post_by_user_id.return_value = posts[1]
    assert blog.post_by_user_id(1) == posts[1]