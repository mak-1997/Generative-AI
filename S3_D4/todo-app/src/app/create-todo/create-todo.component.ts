import { Component } from '@angular/core';
import { Todo } from '../todo.interface';
import { TodoService } from '../todo.service';

@Component({
  selector: 'app-create-todo',
  templateUrl: './create-todo.component.html',
  styleUrls: ['./create-todo.component.css']
})
export class CreateTodoComponent {
  todo: Todo = {
    id: 0,
    title: '',
    description: '',
    completed: false
  };

  constructor(private todoService: TodoService) { }

  createTodo(): void {
    this.todoService.addTodo({
      ...this.todo,
      id: Date.now() // Generate a unique ID
    });
    this.todo = {
      id: 0,
      title: '',
      description: '',
      completed: false
    };
  }
}
