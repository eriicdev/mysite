from django.test import TestCase
from django.contrib.auth.models import User
from blog.models.post import Post

class PostModelTest(TestCase):
    def setUp(self):
        # cria um usuário para ser o autor
        self.user = User.objects.create_user(username="testeuser", password="123")

    def test_criacao_post(self):
        post = Post.objects.create(
            title="Meu primeiro post",
            slug="meu-primeiro-post",
            author=self.user,
            content="Conteúdo de teste"
        )

        # Verifica se o título foi salvo
        self.assertEqual(post.title, "Meu primeiro post")

        # Verifica o __str__ (tem que ser o título)
        self.assertEqual(str(post), "Meu primeiro post")

        # Verifica se o status padrão é 0 (Draft)
        self.assertEqual(post.status, 0)
# Create your tests here.
