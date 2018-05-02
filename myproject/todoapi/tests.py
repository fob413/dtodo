from django.test import TestCase
from .models import Todo
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the todo model"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.todo_name = "Write World class code"
        self.todo = Todo(name=self.todo_name)

    def test_should_create_a_todo(self):
        """Test the todo model can create a new todo."""
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)


class TodoView(TestCase):
    """This class defines the test suite for the todo view"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.todoData1 = {
            'name': 'new todo'
        }
        self.todoData2 = {
            'name': 'Finish writing tests'
        }
        self.editTodo = {
            'name': 'Update the todo'
        }
        self.client.post('/todo/', self.todoData1, format="json")
        self.existingTodo = Todo.objects.get()

    def test_should_successfully_get_all_todos(self):
        """Test the todo get response"""
        oldTodoCount = Todo.objects.all().count()
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        newTodoCount = Todo.objects.all().count()
        self.assertEqual(oldTodoCount, newTodoCount)

    def test_should_successfully_create_a_todo(self):
        """Test the todo post request"""
        oldTodoCount = Todo.objects.all()
        response = self.client.post('/todo/', self.todoData2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_get_single_todo_successfully(self):
        """Test the todo gets a single todo"""
        response = self.client.get('/todo/%s/' % (self.existingTodo.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert(self.existingTodo, response.data)

    def test_should_successfully_update_a_todo(self):
        """Test updating a todo"""
        response = self.client.put('/todo/%s/' % (self.existingTodo.id), self.editTodo, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert(response.data['name'], self.editTodo['name'])

    def test_should_delete_an_existing_todo(self):
        """Tests deleting a todo"""
        response1 = self.client.post('/todo/', self.todoData1, format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.client.delete('/todo/%s/' % response1.data['id'])
        import pdb;pdb.set_trace()
        self.assertEqual(response2.status_code, 204)
