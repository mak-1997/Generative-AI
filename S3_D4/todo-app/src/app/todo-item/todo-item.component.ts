import { Component, Input } from '@angular/core';
import { Todo } from '../todo.interface';
import { TodoService } from '../todo.service';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})
export class TodoItemComponent {
  @Input() todo: Todo = { id: 0, title: '', description: '', completed: false };

  constructor(private todoService: TodoService) { }

  toggleCompleted(): void {
    if (this.todo.completed) {
      this.todoService.markIncomplete(this.todo);
    } else {
      this.todoService.markCompleted(this.todo);
    }
  }

  deleteTodo(): void {
    this.todoService.deleteTodo(this.todo);
  }
}
