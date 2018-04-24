from django.test import TestCase
from .models import Todo
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
class ModelTestCast(TestCase):
    """This class defines the test suite for the todo model"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.todo_name = "Write World class code"
        self.todo = Todo(name=self.todo_name)

    def test_model_can_create_a_todo(self):
        """Test the todo model can create a new todo."""
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.todo_data = {'name': 'Prepare food'}
        self.response = self.client.post(
            reverse('create'),
            self.todo_data,
            format="json"
        )

    def test_api_can_create_a_todo(self):
        """Test the api has todo creation capability"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given todo"""
        todo = Todo.objects.get(id="1")
        response = self.client.get(
            reverse('details',
            kwargs={'pk': todo.id}), format="json"
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo)

    def test_api_can_update_todo(self):
        """Test the api can update a given todo"""
        change_todo = {'name': 'Something different'}
        res = self.client.put(
            reverse('details', kwargs={'pk': todo.id}),
            change_todo,
            format="json"
        )
        self.assertEqual(res.status_coee, status.HTTP_200_OK)

    def test_api_can_delete_todo(self):
        """Test the api can delete a todo"""
        todo = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': todo.id}),
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
